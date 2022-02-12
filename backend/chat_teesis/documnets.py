from elasticsearch import Elasticsearch

import json

es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))


def create_index(search):
    if not es.indices.exists(index='search_1'):
        return es.indices.create(
            index='search_1',
            body={
                "settings": {
                    "index": {
                        "analysis": {
                            "analyzer": {
                                "my_analyzer": {
                                    "type": "custom",
                                    "tokenizer": "nori_tokenizer"
                                }
                            }
                        }
                    }
                },
                "mappings": {
                    "properties": {
                        "mentee_question_Id": {
                            "type": "long"
                        },
                        "major": {
                            "type": "text",
                            "analyzer": "my_analyzer"
                        },
                        "subject": {
                            "type": "text",
                            "analyzer": "my_analyzer"
                        }
                    }
                }
            }
        )

# es.index(index='search',
#                  body={
#                      "user_Id": "",
#                      "major": "경영학과",
#                      "subject": "기업의 경영~~~"
#         })

#
# search_path = ""
# with open(search_path+"search_data.json", encoding='utf-8') as json_file:
#     json_data = json.loads(json_file.read())
# body = ""
#
# j=1
# for i in json_data:
#     body = body + json.dumps({"index": {"_index": "search","_id":j}})+ '\n'
#     body = body + json.dumps(i, ensure_ascii=False) + '\n'
#     if j == 1:
#         print(body)
#
#         j += 1
#     f = open(search_path + 'input.json', 'w')
#     f.write(body)
#     f.close()
#
#     es.bulk(body)
