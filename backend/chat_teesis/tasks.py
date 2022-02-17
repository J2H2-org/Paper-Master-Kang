from __future__ import absolute_import, unicode_literals

import os
import sys

from celery import Celery, shared_task
from django.conf import settings
from elasticsearch import Elasticsearch

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

app = Celery('backend', broker='amqp://rabbitmq:5672//')


@shared_task
def delete_Q_DB_ES(Id, delete_type):  # delete_type(0:elastic, 1:db_q+elastic, 2:db_p+db_q+elastic)
    es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
    if delete_type == 0:
        mentee_question_Id = Id
        doc = {"query": {
            "match": {
                "mentee_question_Id": mentee_question_Id,
            }
        }
        }
        docs = es.delete_by_query(index='search_1', doc_type="_doc", body=doc)
        return
