from elasticsearch import Elasticsearch
import json,os

es = Elasticsearch(hosts='localhost', port=9200)

search_path = '/Users/choisujeong/J2H2-project/J2H2/backend/chat_teesis/'
with open(search_path+"search_data.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())
body = ""

j=1
for i in json_data:
    body = body + json.dumps({"index": {"_index": "search_info","_id":j}})+ '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'
    if j == 1:
        print(body)
    j += 1

f = open(search_path+'input.json', 'w')
f.write(body)
f.close()

es.bulk(body)

