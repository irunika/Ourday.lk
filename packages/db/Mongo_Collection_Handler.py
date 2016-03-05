from Mongo_Handler import Mongo_Handler


class Mongo_Collection_Handler(Mongo_Handler):

    def __init__(self,collection, mongo_handler = Mongo_Handler('localhost', 27017, 'ourday')):
        '''
        :param mongo_handler: Handles the connection for mongodb provided by super class
        :param collection: Collection which specific data are stored
        '''
        super(Mongo_Collection_Handler, self).__init__(mongo_handler.ip, mongo_handler.port, mongo_handler.db_name)
        self.collection = collection

    def _insert_data_(self, data):
        '''
        :param data: Data which need to be inserted (Json Format)
        :return: None
        '''
        return super(Mongo_Collection_Handler, self)._insert_data_(self.collection, data)

    def _get_data_(self, query={}):
        '''
        :param query: query to retrieve data from the database
        :return: List of data
        '''
        return super(Mongo_Collection_Handler, self)._get_data_(self.collection, query)

    def _get_count_(self, query={}):
        '''
        :param query: If you want you can give a query to identify the number of items in the database
        Otherwise it returns the numbre of items in the collection
        :return: count of the number of items
        '''
        return super(Mongo_Collection_Handler, self)._get_count_(self.collection, query)

    def _contains_item_(self, query):
        '''
        :param query: query which you wanna chack whether the item set exist
        :return: True if item exist, False otherwise
        '''
        return super(Mongo_Collection_Handler,self)._contains_item_(self.collection, query)

    def _update_data_(self, query, update, multi=False):
        '''
        :param query: query to find the items to be updated
        :param update: query to update
        :return: None
        '''
        super(Mongo_Collection_Handler, self)._update_data_(self.collection, query, update, multi)

    def _remove_item_(self, query):
        '''
        :param query: Query to remove item
        :return: None
        '''
        super(Mongo_Collection_Handler, self)._remove_item_(self.collection, query)

