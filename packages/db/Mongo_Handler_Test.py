from Mongo_Handler import Mongo_Handler
from random import randint
from time import localtime
import sys

'''
Note : This is to check Mongo_Handler No use for project
'''

if __name__ == '__main__':
    db_handler = Mongo_Handler('localhost', 27017, 'test')
    # db_handler._delete_database_()
    #
    # for id in range(100000):
    #     data = {
    #         "_id" : id,
    #         "rand" : randint(0,100),
    #         "time" : str(localtime())
    #     }
    #     db_handler._insert_data_('test1', data)
    #


    # query1 =  {
    #     "rand":{'$gt':98}
    # }
    #
    # query2 = {"$and" :
    #     [
    #         {"_id":{"$gt":9000}}, {"rand":50}
    #     ]
    # }
    #
    #
    # for data in db_handler._get_data_("test_col",query2):
    #     print data
    #
    # print db_handler._get_count_('test_col')
    # print db_handler._get_count_('test_col', query1)
    # print db_handler._get_count_('test_col', query2)
    # print db_handler._get_count_('test_col', {'_id':9000})
    # print db_handler._get_data_('test_col', {'_id':9000})
    # db_handler._update_data('test_col',
    #                         {'_id':9000},
    #                         {'$set': {'rand':20}}
    #                         )
    # print db_handler._get_data_('test_col', {'_id':9000})

    # db_handler._copy_collection_to('test1', 'test2')

    # print db_handler._get_count_()
    print db_handler._get_count_('keywords',
                                 {'key_list': 'password'}
                                 )
