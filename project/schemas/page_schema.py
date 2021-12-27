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

    def insert(self, data):
        """Insert data into page"""
        query = f""" INSERT INTO {self.table_name}(
                page_name,
                page_name_id,
                political_party,
                kind,
                region
            )
            VALUES(
                '{data[1]}',
                '{data[2]}',
                '{data[3]}',
                '{data[4]}',
                '{data[5]}'
            )
        """
        return self.exec_query(query)
