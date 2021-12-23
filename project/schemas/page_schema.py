"""Schema for page"""
from project.schemas.schema import Schema

class PageSchema(Schema):
    """Schema for page"""
    def __init__(self):
        super().__init__()
        self.table_name = "page"

    def get_distinct(self, field):
        """Returns not repeated data

        Args:
            field (string): Name of the field for execute the SELECT DISTINCT

        Returns:
            dict: Requested field from DB without repeated values
        """
        query = f"SELECT DISTINCT {field} FROM {self.table_name}"
        return self.exec_query(query)
