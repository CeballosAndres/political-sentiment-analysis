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

    def show(self, data):
        """Returns row in db, only works with varchar data for now

        Args:
            data (dict): Contains name of field and value for search

        Returns:
            dict: Requested row from DB
        """
        field = list(data.keys())[0]
        query = f"""SELECT * FROM {self.table_name}
                    WHERE {field} = '{data[field]}'"""
        return self.exec_query(query)[0]

    def insert(self, data):
        """Insert data into page"""
        query = f""" INSERT INTO {self.table_name}(
                page_id,
                page_name,
                page_name_id,
                political_party,
                kind,
                region
            )
            VALUES(
                '{data[0]}',
                '{data[1]}',
                '{data[2]}',
                '{data[3]}',
                '{data[4]}',
                '{data[5]}'
            );
        """
        return self.exec_query(query)
