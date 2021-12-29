"""Schema for post"""
from project.schemas.schema import Schema
from project.schemas.page_schema import PageSchema

class PostSchema(Schema):
    """Schema for post"""
    def __init__(self):
        super().__init__()
        self.table_name = "post"

    def show(self, data):
        """Returns row in db, only works with varchar data for now

        Args:
            data (dict): Contains name of field and value for search

        Returns:
            dict: Requested row from DB
        """
        field = list(data.keys())[0]
        query = f"""SELECT * FROM {self.table_name}
                    WHERE {field} = '{data[field]}'"""
        return self.exec_query(query)[0]

    def insert(self, data):
        """Insert data into post"""
        query = f""" INSERT INTO {self.table_name}(
                post_id,
                created_date,
                created_time,
                message,
                react_angry,
                react_haha,
                react_like,
                react_love,
                react_sad,
                react_wow,
                react_care,
                share,
                page_id
            )
            VALUES(
                '{data[0]}',
                '{data[1]}',
                '{data[2]}',
                '{data[3]}',
                {data[4]},
                {data[5]},
                {data[6]},
                {data[7]},
                {data[8]},
                {data[9]},
                {data[10]},
                {data[11]},
                {data[12]},
            )
        """
        self.exec_query(query)

    def multi_insert(self, data):
        """Insert multiple lines into post"""
        page_schema = PageSchema()
        page_ids = page_schema.get_field_list("page_id")
        pages = page_schema.exec_query("SELECT id, page_id FROM page")
        query = f"""INSERT INTO {self.table_name}(
                post_id,
                created_date,
                created_time,
                message,
                react_angry,
                react_haha,
                react_like,
                react_love,
                react_sad,
                react_wow,
                react_care,
                share,
                page_id
            )
            VALUES
        """
        for i in range(len(data)):
            page_facebook_id = str(data[i][12])
            if page_facebook_id in page_ids:
                page_id = None
                for page in pages:
                    if page["page_id"] == page_facebook_id:
                        page_id = page["id"]
                query += f"""(
                    '{data[i][0]}',
                    '{data[i][1]}',
                    '{data[i][2]}',
                    '{data[i][3]}',
                    {data[i][4]},
                    {data[i][5]},
                    {data[i][6]},
                    {data[i][7]},
                    {data[i][8]},
                    {data[i][9]},
                    {data[i][10]},
                    {data[i][11]},
                    {page_id}
                )"""
                if i == len(data)-1:
                    query += ";"
                else:
                    query += ","
        self.exec_query(query)
