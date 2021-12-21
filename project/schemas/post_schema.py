"""Schema for post"""
from schemas.schema import Schema

class PostSchema(Schema):
    """Schema for post"""
    def __init__(self):
        super().__init__()
        self.table_name = "post"
