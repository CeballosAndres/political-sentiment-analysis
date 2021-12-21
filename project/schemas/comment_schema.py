"""Schema for comment"""
from project.schemas.schema import Schema

class CommentSchema(Schema):
    """Schema for comment"""
    def __init__(self):
        super().__init__()
        self.table_name = "comment"
