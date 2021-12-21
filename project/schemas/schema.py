from db.connection_adapter import ConnectionAdapter

class Schema():
    """Generic Schema"""
    def __init__(self):
        self.connection = ConnectionAdapter()
        self.table_name = None
        self.cursor = None
    
    def get_all(self):
        """Returns all registers from table"""
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f"SELECT * FROM {self.table_name}"
        )
        result = self.cursor.fetchall()
        self.connection.commit()
        return result

    def exec_query(self, query):
        """Function for make query"""
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.connection.commit()
        return result
