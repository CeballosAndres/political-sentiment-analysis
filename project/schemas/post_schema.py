"""Schema for post"""
from project.schemas.schema import Schema

class PostSchema(Schema):
    """Schema for post"""
    def __init__(self):
        super().__init__()
        self.table_name = "post"

    def insert(self, data):
        """Insert data into post"""
        query = f""" INSERT INTO {self.table_name}(
                post_id,
                created_date,
                created_time,
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
                {data[0]},
                '{data[1]}',
                '{data[2]}',
                {data[3]},
                {data[4]},
                {data[5]},
                {data[6]},
                {data[7]},
                {data[8]},
                {data[9]},
                {data[10]},
                {data[11]}
            )
        """
        self.exec_query(query)
