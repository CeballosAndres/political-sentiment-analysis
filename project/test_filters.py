class Try():
    def __init__(self):
        self.query = {
            "page_name": [

            ],
            "political_party": [
            ],
            "kind": [
            ],
            "region": [
            ]
        }

    def data(self):
        data = self.query
        print(self.__prepare_filters(data, ""))

    def __prepare_filters(self, filters, query):
        w_where = "WHERE"
        w_and = "AND"
        if filters["page_name"]:
            filter_list = self.__format_filter_list(filters["page_name"])
            query += f"{w_where} page_name IN {filter_list} "
            filters["page_name"] = []
            return self.__prepare_filters(filters, query)
        elif filters["political_party"]:
            filter_list = self.__format_filter_list(filters["political_party"])
            if query:
                query += f"""
                    {w_and} political_party IN {filter_list} 
                """
            else:
                query += f"""
                    {w_where} political_party IN {filter_list} 
                """
            filters["political_party"] = []
            return self.__prepare_filters(filters, query)
        elif filters["kind"]:
            filter_list = self.__format_filter_list(filters["kind"])
            if query:
                query += f"{w_and} kind IN {filter_list} "
            else:
                query += f"{w_where} kind IN {filter_list} "
            filters["kind"] = []
            return self.__prepare_filters(filters, query)
        elif filters["region"]:
            filter_list = self.__format_filter_list(filters["region"])
            if query:
                query += f"{w_and} region IN {filter_list} "
            else:
                query += f"{w_where} region IN {filter_list} "
            filters["region"] = []
            return self.__prepare_filters(filters, query)
        return query

    @staticmethod
    def __format_filter_list(filter_list):
        if len(filter_list)>1:
            return repr(tuple(filter_list))
        return f"('{filter_list[0]}')"

Try().data()