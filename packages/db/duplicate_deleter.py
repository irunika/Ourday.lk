import multiprocessing

from Mongo_Collection_Handler import Mongo_Collection_Handler
from random import randint
from time import localtime
from datetime import datetime

db_col_handler_tickets = Mongo_Collection_Handler('tickets')
db_col_handler_summaries = Mongo_Collection_Handler('summaries')
db_col_handler_keywords = Mongo_Collection_Handler('keywords')


issues = db_col_handler_summaries._get_data_({})

while issues.__len__() != 0:
    issue = issues.pop()
    issue_summary = issue['issue_summary']

    issues_matching_summary = db_col_handler_summaries._get_data_({'issue_summary':issue_summary})

    if issues_matching_summary.__len__() > 2:
        issues_matching_summary.pop()

        print 'found Duplicate : ', issues_matching_summary[0]['issue_summary'] + '  ---> ', issues_matching_summary.__len__()

        for matching_issue in issues_matching_summary:
            db_col_handler_summaries._remove_item_({'_id':matching_issue['_id']})
            db_col_handler_keywords._update_data_(
                    {},
                    {'$pull':{'id_list':{'$in':[matching_issue['_id']]}}},
                    multi=True)

        issues = db_col_handler_summaries._get_data_({})


