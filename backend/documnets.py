from elasticsearch import Elasticsearch

import json
import csv

es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))


def create_index(search):
    if not es.indices.exists(index='search_2'):
        return es.indices.create(
            index='search_2',
            body={
                "settings": {
                    "index": {
                        "analysis": {
                            "analyzer": {
                                "nori": {
                                    "tokenizer": "nori_tokenizer"
                                }
                            }
                        }
                    }},
                "mappings": {
                    "properties": {
                        "mentee_question_Id": {
                            "type": "long"
                        },
                        "major": {
                            "type": "text",
                            "analyzer": "nori"
                        },
                        "subject": {
                            "type": "text",
                            "analyzer": "nori"
                        }
                    }
                }
            }
        )


search_path = "C:\\Users\\dr0jo\\J2H2\\backend\\chat_teesis\\"
with open(search_path + "bulk.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())
body = ""

for i in json_data:
    body = body + json.dumps({"index": {"_index": "search_2"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

    f = open(search_path + 'input3.json', 'w')
    f.write(body)
    f.close()

    es.bulk(body)
