"""Schema for page"""
from schemas.schema import Schema

class PageSchema(Schema):
    """Schema for page"""
    def __init__(self):
        super().__init__()
        self.table_name = "page"
