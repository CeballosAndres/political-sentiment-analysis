"""Module of migration"""
import pandas as pd
import re
from project.schemas.page_schema import PageSchema
from project.schemas.post_schema import PostSchema
from project.schemas.comment_schema import CommentSchema

class Migrator():
    """Object for migrate data"""
    def __init__(self, path):
        self.file = pd.ExcelFile(path)
        self.is_right_file = False
        if self.__validate_sheet_file():
            self.is_right_file = True
            self.file_comments = self.file.parse("Comments").dropna()
            self.file_posts = self.file.parse("Posts").dropna()
            self.page_columns = self.__page_columns
            self.post_columns = self.__post_columns
            self.comment_columns = self.__comment_columns
        
    def __validate_sheet_file(self):
        return set(["Posts", "Comments"]).issubset(set(self.file.sheet_names))    

    def clean_dataframe(self):
        self.file_posts['message'] = self.file_posts['message'].apply(self.clean_text) 
        self.file_comments['message'] = self.file_comments['message'].apply(self.clean_text) 
        self.file_comments =  self.file_comments[self.file_comments['message'] != ''].reset_index(drop=True)
        
    
    def clean_text(self, text):
        text = str(text)
        text = re.sub(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", '', text)
        text = re.sub(r'@[A-Za-z0-9]+', '', text) # para menciones
        text = re.sub(r'#[A-Za-z0-9]+', '', text)
        text = re.sub(r'[\.\,\'\"]', ' ', text)
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'RT[\s]+', '', text)
        text = re.sub(r'\[PHOTO\]','', text)
        text = " ".join(text.split())
        return text

    def verify_file_structure(self):
        post_columns = [
            "created_date",
            "created_time",
            "message",
            "format",
            "classification",
            "page_id",
            "page_name",
            "page_name_id",
            "post_id",
            "react_angry",
            "react_haha",
            "react_like",
            "react_love",
            "react_sad",
            "react_wow",
            "react_care",
            "share",
            "political_party",
            "region",
            "kind"
        ]
        comment_columns = [
            "post_id",
            "comment_id",
            "profile_id",
            "created_date",
            "created_time",
            "from_name",
            "message",
            "gender",
            "reactions",
            "feeling"
        ]
        if not (set(post_columns).issubset(set(self.file_posts.columns))
                and
                set(comment_columns).issubset(set(self.file_comments.columns))):
            return {
                "post": post_columns,
                "comments": comment_columns
            }

    def convert_page(self):
        """Recieves file as an argument and returns DataFrame"""
        df_page = pd.DataFrame(
            list(
                zip(
                    self.file_posts[self.page_columns[0]],
                    self.file_posts[self.page_columns[1]],
                    self.file_posts[self.page_columns[2]],
                    self.file_posts[self.page_columns[3]],
                    self.file_posts[self.page_columns[4]],
                    self.file_posts[self.page_columns[5]],
                )
            ),
            columns=self.page_columns
        )
        return df_page

    def convert_post(self):
        """Recieves file as an argument and returns DataFrame"""
        df_post = pd.DataFrame(
            list(
                zip(
                    self.file_posts[self.post_columns[0]],
                    self.file_posts[self.post_columns[1]],
                    self.file_posts[self.post_columns[2]],
                    self.file_posts[self.post_columns[3]],
                    self.file_posts[self.post_columns[4]],
                    self.file_posts[self.post_columns[5]],
                    self.file_posts[self.post_columns[6]],
                    self.file_posts[self.post_columns[7]],
                    self.file_posts[self.post_columns[8]],
                    self.file_posts[self.post_columns[9]],
                    self.file_posts[self.post_columns[10]],
                    self.file_posts[self.post_columns[11]],
                    self.file_posts[self.post_columns[12]],
                )
            ),
            columns=self.post_columns
        )
        if df_post["created_date"].dtypes == "object":
            df_post['created_date'] = df_post['created_date'].astype('datetime64')
        return df_post

    def convert_comment(self):
        """Recieves file and returns DataFrame"""
        df_comment = pd.DataFrame(
            list(
                zip(
                    self.file_comments[self.comment_columns[0]],
                    self.file_comments[self.comment_columns[1]],
                    self.file_comments[self.comment_columns[2]],
                    self.file_comments[self.comment_columns[3]],
                    self.file_comments[self.comment_columns[4]],
                    self.file_comments[self.comment_columns[5]],
                    self.file_comments[self.comment_columns[6]],
                    self.file_comments[self.comment_columns[7]],
                    self.file_comments[self.comment_columns[8]],
                    self.file_comments[self.comment_columns[9]],
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
        page = page_schema.show({
            "page_name": data[1]
        })
        if page:
            page_schema.exec_query(f"CALL delete_all_page_data('{page[0]['page_name']}')")
        page_schema.insert(data)
        return data[1]

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
            "message",
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
            "message",
            "gender",
            "created_date",
            "created_time",
            "reactions",
            "post_id",
            "feeling"
        ]
