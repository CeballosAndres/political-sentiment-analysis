"""Controller module"""
import pandas as pd
from project.db.migrator import Migrator
from project.schemas.post_schema import PostSchema
from project.schemas.page_schema import PageSchema
from project.schemas.comment_schema import CommentSchema

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

    def insert_data_from_file(self):
        """Read an uploaded file and insert data form it into DB"""
        migrator = Migrator("project/static/04 Datos Limpios.xlsx")
        migrator.clean_dataframe()
        migrator.insert_page()
        migrator.insert_posts()
        migrator.insert_comments()

    def get_algorithm_info(self):
        """FUNCTION IN DEVELOPMENT PROCESS. It will be finished when 
        filters could be received from frontend"""
        query = f"""SELECT 
                c.from_name,
                c.gender,
                c.created_date,
                c.created_time,
                c.reactions,
                c.feeling
                FROM {self.__comment_schema.table_name} c"""
        data = self.__comment_schema.exec_query(query)
        df = pd.DataFrame(columns=[
            "from_name",
            "gender",
            "created_date",
            "created_time",
            "reactions",
            "feeling"
        ])
        for resource in data:
            df = df.append(resource, ignore_index=True)
        return df

    def data_mining(self):
        """Call the clustering algorithm and returns result data
        """
        cluster = Cluster(self.get_algorithm_info())
        return cluster.get_clustering(['gender','feeling'], 4)