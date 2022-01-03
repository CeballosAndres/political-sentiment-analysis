"""Controller module"""

import pandas as pd
from project.db.migrator import Migrator
from project.schemas.post_schema import PostSchema
from project.schemas.page_schema import PageSchema
from project.schemas.comment_schema import CommentSchema
from project.datamining.mywordcloud import MyWordCloud
from project.datamining.clustering import Cluster

class AppController():
    """Basic controller for backend app"""
    def __init__(self):
        self.__post_schema = PostSchema()
        self.__page_schema = PageSchema()
        self.__comment_schema = CommentSchema()

    def get_pages(self):
        """Returns all resources in page table"""
        return self.__page_schema.get_all()

    def get_filters_fields(self):
        """Returns filter fields for data

        Returns:
            dict: Contains the name of filter as key, and filter data as a list
                Example:
                {
                    "page_name": [
                        "Irene Herrera",
                        "Virgilio Mendoza"
                    ],
                    "political_party": [
                        "Partido Revolucionario Institucional",
                        "Partido Verde Ecologista de México"
                    ],
                    "kind": [
                        "Presidencia Municipal",
                        "Gubernatura"
                    ],
                    "region": [
                        "Colima",
                        "Manzanillo"
                    ]
                }
        """

        filters = {
            "page_name": [],
            "political_party": [],
            "kind": [],
            "region": []
        }
        for field in filters:
            result = self.__page_schema.get_distinct(field)
            for data in result:
                filters[field].append(data[field])
        return filters

    def insert_data_from_file(self, path):
        """Read an uploaded file and insert data form it into DB
        Args:
            path (string): complete path where file is stored with filename too
        """
        migrator = Migrator(path)
        if not migrator.is_right_file:
            return Exception()
        error = migrator.verify_file_structure()
        if error:
            return Exception()
        migrator.clean_dataframe()
        page_name = migrator.insert_page()
        migrator.insert_posts()
        migrator.insert_comments()
        return page_name

    def get_algorithm_info(self, filters):
        """
        Recieves filter info and make a query to DB with it

        Args:
            filters (dict): Contains the name of filter as key, and filter data as a list
                Example:
                {
                    "page_name": [
                        "Irene Herrera",
                        "Virgilio Mendoza"
                    ],
                    "political_party": [
                        "Partido Revolucionario Institucional",
                        "Partido Verde Ecologista de México"
                    ],
                    "kind": [
                        "Presidencia Municipal",
                        "Gubernatura"
                    ],
                    "region": [
                        "Colima",
                        "Manzanillo"
                    ]
                }
        Returns:
            DataFrame: Contains filtered data
        """

        query = f"""SELECT 
                c.from_name,
                c.gender,
                c.message,
                c.created_date,
                c.created_time,
                c.reactions,
                c.feeling
                FROM {self.__comment_schema.table_name} c
                JOIN {self.__post_schema.table_name} p ON c.post_id = p.id
                JOIN {self.__page_schema.table_name} pa ON pa.id = p.page_id
                {self.__prepare_filters(filters, "")}
                """
        data = self.__comment_schema.exec_query(query)
        df = pd.DataFrame(data)
        wordcloud = MyWordCloud(df)
        wordcloud.generate_wordcloud()
        del df["message"]
        cluster = Cluster(df)
        return cluster.get_clustering(["gender", "feeling"], 4)

    def __prepare_filters(self, filters, query):
        """
        Recieves a dict with filter lists, and returns a query for filter data

        Args:
            filters (dict): Each key of dict contains a list with filter values
            query (string): should send an empty string
        Returns:
            Formatted query with multiple filters
        """
        w_where = "WHERE"
        w_and = "AND"
        if filters["page_name"]:
            filter_list = self.__format_filter_list(filters["page_name"])
            query += f"{w_where} page_name IN {filter_list} "
            filters["page_name"] = []
            return self.__prepare_filters(filters, query)
        elif filters["political_party"]:
            filter_list = self.__format_filter_list(filters["political_party"])
            if query:
                query += f"""
                    {w_and} political_party IN {filter_list} 
                """
            else:
                query += f"""
                    {w_where} political_party IN {filter_list} 
                """
            filters["political_party"] = []
            return self.__prepare_filters(filters, query)
        elif filters["kind"]:
            filter_list = self.__format_filter_list(filters["kind"])
            if query:
                query += f"{w_and} kind IN {filter_list} "
            else:
                query += f"{w_where} kind IN {filter_list} "
            filters["kind"] = []
            return self.__prepare_filters(filters, query)
        elif filters["region"]:
            filter_list = self.__format_filter_list(filters["region"])
            if query:
                query += f"{w_and} region IN {filter_list} "
            else:
                query += f"{w_where} region IN {filter_list} "
            filters["region"] = []
            return self.__prepare_filters(filters, query)
        return query

    @staticmethod
    def __format_filter_list(filter_list):
        """Recieves the list of filters and format them according the length"""
        if len(filter_list)>1:
            return repr(tuple(filter_list))
        return f"('{filter_list[0]}')"
