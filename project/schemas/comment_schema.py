"""Schema for comment"""
from project.schemas.schema import Schema
from project.schemas.post_schema import PostSchema

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
                post_id,
                feeling
            )
            VALUES(
                '{data[0]}',
                {data[1]},
                '{data[2]}',
                '{data[3]}',
                '{data[4]}',
                '{data[5]}',
                {data[6]},
                {data[7]},
                {data[8]}
            )
        """
        self.exec_query(query)

    def multi_insert(self, data):
        """Insert multiple lines into comment"""
        post_schema = PostSchema()
        post_ids = post_schema.get_field_list("post_id")
        query = f"""INSERT INTO {self.table_name}(
                comment_id,
                profile_id,
                from_name,
                gender,
                created_date,
                created_time,
                reactions,
                post_id
            )
            VALUES
        """
        for i in range(len(data)):
            if str(data[i][7]) in post_ids:
                post_id = post_schema.show({"post_id":data[i][7]})
                query += f"""(
                    '{data[i][0]}',
                    {data[i][1]},
                    '{data[i][2]}',
                    '{data[i][3]}',
                    '{data[i][4]}',
                    '{data[i][5]}',
                    {data[i][6]},
                    {post_id["id"]}
                )"""
                if i == len(data)-1:
                    query += ";"
                else:
                    query += ","
        self.exec_query(query)
