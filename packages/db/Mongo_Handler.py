from pymongo import MongoClient

class Mongo_Handler(object):

    def __init__(self, ip, port, db_name):
        self.ip = ip; #IP for the database
        self.port = port #port for the databse

        self.mongo_client = MongoClient(ip, port) #Mongo Client for the databse

        self.db_name = db_name #Name of the database
        self.db = self.mongo_client.get_database(self.db_name) #This can be used after connecting to database


    def _delete_database_(self, db_name=''):
        if db_name.__len__()==0:
            self.mongo_client.drop_database(self.db_name)
            print "'", self.db_name, "' database deleted"
        else:
            self.mongo_client.drop_database(db_name)
            print "'", db_name, "' database deleted"


    def _insert_data_(self, collection, data):
        '''
        :param collection: Name of the collection which data should be included
        :param data: Data in Json format which should be written to the given collection
        :return: None
        '''
        self.db.get_collection(collection).insert(data)
        print "Added data to ", self.db_name , " --> ", collection


    def _get_data_(self, collection, query={}):
        '''
        :param collection: Name of the collection whihc the data should be retrieved
        :param query: Query to get data from the database (Give it in JSON format)
        :return: list of data which was queried
        '''
        dataList = []
        if not query.__len__() == 0:
            for db in  self.mongo_client.get_database(self.db_name).get_collection(collection).find(query):
                dataList.append(db)
        else:
            for db in  self.mongo_client.get_database(self.db_name).get_collection(collection).find():
                dataList.append(db)
        return dataList


    def _get_count_(self, collection, query={}):
        '''
        :param collections: Collection which the item count should be taken
        :param query: If a specific item count should be taken it can be taken from here
        :return: Return the item count specified by
        '''
        if query.__len__() == 0:
            return self.mongo_client.get_database(self.db_name).get_collection(collection).count()
        else:
            return self.mongo_client.get_database(self.db_name).get_collection(collection).find(query).count()


    def _contains_item_(self, collection, query):
        '''
        :param collection: Collections where the data should be retrived
        :param query: query which you wanna chack whether the item set exist
        :return: True if item exist, False otherwise
        '''
        count = self.mongo_client.get_database(self.db_name).get_collection(collection).find(query).count()
        if count <= 0:
            return False
        else:
            return True


    def _update_data_(self, collection, query, update, multi=False):
        '''
        :param collection: Collection which should be updated
        :param query: query to find the items to be updated
        :param update: query to update
        :param multi : If multiple documents should get updated this must be true
        :return: None
        '''

        if multi==True:
            self.mongo_client.get_database(self.db_name).get_collection(collection).update_many(
                query,
                update
            )

        else:
            self.mongo_client.get_database(self.db_name).get_collection(collection).update_one(
                query,
                update
            )

    def _copy_collection_to(self, from_collection, to_collection):
        '''
        :param from_collection: From which collection to copy
        :param to_collection: To which collection to copy
        :return: None
        '''
        print 'Copying data from collectio:', from_collection, " to collection:", to_collection , '\n Please wait!'
        for item in self.mongo_client.get_database(self.db_name).get_collection(from_collection).find():
            self.mongo_client.get_database(self.db_name).get_collection(to_collection).insert(item)

        print 'Copying data from collectio:', from_collection, " to collection:", to_collection, " is complete!"


    def _remove_item_(self, collection, query):
        '''
        :param collection: Collection to remove item
        :param query: Query to remove item
        :return: None
        '''
        self.mongo_client.get_database(self.db_name).get_collection(collection).remove(query)