"""Module of migration"""
import pandas as pd
from project.schemas.page_schema import PageSchema
from project.schemas.post_schema import PostSchema
from project.schemas.comment_schema import CommentSchema

class Migrator():
    """Object for migrate data"""
    def __init__(self, path):
        self.file = pd.ExcelFile(path)
        self.page_columns = self.__page_columns
        self.post_columns = self.__post_columns
        self.comment_columns = self.__comment_columns

    def convert_page(self):
        """Recieves file as an argument and returns DataFrame"""
        posts = self.file.parse("Posts")
        df_page = pd.DataFrame(
            list(
                zip(
                    posts[self.page_columns[0]],
                    posts[self.page_columns[1]],
                    posts[self.page_columns[2]],
                    posts[self.page_columns[3]],
                    posts[self.page_columns[4]],
                    posts[self.page_columns[5]],
                )
            ),
            columns=self.page_columns
        )
        return df_page

    def convert_post(self):
        """Recieves file as an argument and returns DataFrame"""
        posts = self.file.parse("Posts")
        df_post = pd.DataFrame(
            list(
                zip(
                    posts[self.post_columns[0]],
                    posts[self.post_columns[1]],
                    posts[self.post_columns[2]],
                    posts[self.post_columns[3]],
                    posts[self.post_columns[4]],
                    posts[self.post_columns[5]],
                    posts[self.post_columns[6]],
                    posts[self.post_columns[7]],
                    posts[self.post_columns[8]],
                    posts[self.post_columns[9]],
                    posts[self.post_columns[10]],
                    posts[self.post_columns[11]],
                )
            ),
            columns=self.post_columns
        )
        if df_post["created_date"].dtypes == "object":
            df_post['created_date'] = df_post['created_date'].astype('datetime64')
        return df_post

    def convert_comment(self):
        """Recieves file and returns DataFrame"""
        comments = self.file.parse("Comments")
        df_comment = pd.DataFrame(
            list(
                zip(
                    comments[self.comment_columns[0]],
                    comments[self.comment_columns[1]],
                    comments[self.comment_columns[2]],
                    comments[self.comment_columns[3]],
                    comments[self.comment_columns[4]],
                    comments[self.comment_columns[5]],
                    comments[self.comment_columns[6]],
                    comments[self.comment_columns[7]],
                    comments[self.comment_columns[8]]
                )
            ),
            columns=self.comment_columns
        )
        df_comment["from_name"] = df_comment["from_name"].str.replace("'", '"')
        if df_comment["created_date"].dtypes == "object":
            df_comment["created_date"] = df_comment["created_date"].astype("datetime64")
        return df_comment

    def insert_page(self):
        """Insert page data from file"""
        df_page = self.convert_page()
        data = df_page.iloc[0].values.tolist()
        page_schema = PageSchema()
        page_schema.insert(data)

    def insert_posts(self):
        """Insert post data from file"""
        df_post = self.convert_post()
        post_schema = PostSchema()
        data = []
        for i in range(len(df_post)):
            row = df_post.iloc[i].values.tolist()
            data.append(row)
        post_schema.multi_insert(data)

    def insert_comments(self):
        """Insert comment data from file"""
        df_comment = self.convert_comment()
        comment_schema = CommentSchema()
        data = []
        for i in range(len(df_comment)):
            row = df_comment.iloc[i].values.tolist()
            data.append(row)
        comment_schema.multi_insert(data)

    
    def file_to_dataframe(self):
        return self.file.parse("Comments")


    @property
    def __page_columns(self):
        """Returns columns for page"""
        return [
            "page_id",
            "page_name",
            "page_name_id",
            "political_party",
            "kind",
            "region"
        ]
    @property
    def __post_columns(self):
        """Returns columns for post"""
        return [
            "post_id",
            "created_date",
            "created_time",
            "react_angry",
            "react_haha",
            "react_like",
            "react_love",
            "react_sad",
            "react_wow",
            "react_care",
            "share",
            "page_id",
        ]
    @property
    def __comment_columns(self):
        """Returns columns for comment"""
        return [
            "comment_id",
            "profile_id",
            "from_name",
            "gender",
            "created_date",
            "created_time",
            "reactions",
            "post_id",
            "feeling"
        ]
