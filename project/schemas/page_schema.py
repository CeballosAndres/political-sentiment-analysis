"""Schema for page"""
from project.schemas.schema import Schema

class PageSchema(Schema):
    """Schema for page"""
    def __init__(self):
        super().__init__()
        self.table_name = "page"
