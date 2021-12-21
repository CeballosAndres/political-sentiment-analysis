from project.db.connection_adapter import ConnectionAdapter

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


    def parse_sql(self, filename):
        data = open(filename, 'r').readlines()
        stmts = []
        DELIMITER = ';'
        stmt = ''

        for lineno, line in enumerate(data):
            if not line.strip():
                continue

            if line.startswith('--') or line.startswith('/*'):
                continue

            if 'DELIMITER' in line:
                DELIMITER = line.split()[1]
                continue

            if (DELIMITER not in line):
                stmt += line.replace(DELIMITER, ';')
                continue

            if stmt:
                stmt += line
                stmts.append(stmt.strip())
                stmt = ''
            else:
                stmts.append(line.strip())
        return stmts
