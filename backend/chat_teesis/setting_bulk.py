import json, requests

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='elasticsearch', port=9200)
search_path = '/Users/choisujeong/J2H2-project/J2H2/backend/chat_teesis/'

es.indices.create(
    index='search_data',
    body={
        "settings":{
            "index":{
                "analyzer":{
                    "nori":{
                        "tokenizer":"nori_tokenizer"
                    }
                }
            }
        },
        "mapping":{
            "properties":{
                "user_Id":{
                    "type":"long",
                },
                "major":{
                    "type":"text",
                    "analyzer": "nori"
                },
                "subject": {
                    "type": "text",
                    "analyzer": "nori"
                },
                "tag": {
                    "type": "text",
                    "analyzer": "nori"
                }
            }
        }
    }
)
with open(search_path+"search_data.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())
body = ""

j=1
for i in json_data:
    body = body + json.dumps({"index": {"_index": "search_data","_id":j}})+ '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'
    if j == 1:
        print(body)
    j += 1

f = open(search_path+'input.json', 'w')
f.write(body)
f.close()

es.bulk(body)

