import multiprocessing

from Mongo_Collection_Handler import Mongo_Collection_Handler
from random import randint
from time import localtime
from datetime import datetime


if __name__ == '__main__':

    db_col_handler_tickets = Mongo_Collection_Handler('tickets')
    db_col_handler_summaries = Mongo_Collection_Handler('summaries')

    # db_handler._delete_database_()

    # for id in range(100000):
    #     data = {
    #         "_id" : id,
    #         "rand" : randint(0,100),
    #         "time" : str(localtime())
    #     }
    #     db_col_handler._insert_data_(data)

    # query1 =  {
    #     "rand":{'$gt':98}
    # }
    #
    # query2 = {"$and" :
    #     [
    #         {"_id":{"$gt":99000}}, {"rand":50}
    #     ]
    # }
    #
    # for data in db_col_handler._get_data_(query2):
    #     print data
    #
    #
    #
    # print db_col_handler._contains_item_({"_id":9000 })
    #
    #
    # for item in db_col_handler_tickets._get_data_({"_id":"SKYTVNZDEV"})[0]["issues"]:
    #     if item["issue_id"] == "SKYTVNZDEV-33":
    #         print item
    # db_col_handler._update_data_(
    #     {'_id':9000},
    #     {'$set' : {'rand' : 45}}
    # )
    # print('---------')
    #
    # db_col_handler._remove_item_(query2)
    # for data in db_col_handler._get_data_(query2):
    #     print data


    # db_col_handler._remove_item_({"issue_summary":"Critical Security Update for Identity Server 5.0.0"})

    # db_col_handler._update_data_(
    #     {},
    #     {
    #         "$set":{"modified_answer":[], "modified_by":"Not Modified"}
    #      },
    #     multi=True
    # )

    # print  db_col_handler._get_data_({"id_list":"150b93a5b6251270"})
    #     for i in item["issues"]:
    #         print i["_id"]
    # print db_col_handler._contains_item_({"_id":"MBRND-2"})

    # count = 0;
    # for item in db_col_handler._get_data_({"id_list":"BCDTRAVELDEVSPRT-1"}):
    #     print item["key_list"]
    #     count  = count + 1
    #
    # print count

    # print db_col_handler._get_data_({"key_list":"rest"})

    # for ticket in db_col_handler_tickets._get_data_({"_id":"STRAATSBOSBEHEERPROD"})[0]["issues"]:
    #     if ticket["issue_id"] == "STRAATSBOSBEHEERPROD-1":
    #         print ticket["project_category"]

    # print db_col_handler_summaries._remove_item_({"issue_summary": "Security Patch for Apache Rampart Issue: RAMPART-269"})
    print db_col_handler_summaries._get_count_()
    # print db_col_handler_summaries._get_data_({"_id":"SKYTVNZDEV-33"})[0]["issue_summary"]
    # print db_col_handler_summaries._get_data_({"_id":"SKYTVNZDEV-33"})[0]["description"]


    x = [1,2,3]
    z = [1,2,3]
    y = [2,4,5,6]

    d = {}
    d["a"] = []
    d["a"] = d["a"].__add__(x);
    print d["a"]

    g = list(set(x).intersection(set(y)))
    print g
    # g.append(y)
    x = x.__add__(y)
    print x

    x.pop()
    print x

    print 'this , do s '.strip(',')
