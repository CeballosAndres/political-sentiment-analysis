"""Schema for comment"""
from project.schemas.schema import Schema

class CommentSchema(Schema):
    """Schema for comment"""
    def __init__(self):
        super().__init__()
        self.table_name = "comment"

    def insert(self, data):
        """Insert data into comment"""
        query = f""" INSERT INTO {self.table_name}(
                comment_id,
                profile_id,
                from_name,
                gender,
                created_date,
                created_time,
                reactions,
                post_id
            )
            VALUES(
                {data[0]},
                {data[1]},
                '{data[2]}',
                '{data[3]}',
                '{data[4]}',
                '{data[5]}',
                {data[6]},
                {data[7]}
            )
        """
        self.exec_query(query)
