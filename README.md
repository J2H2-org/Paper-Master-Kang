# 논문 좀 써본 강조교 (by Team Teesis)
논문 기획부터 출판까지 도움을 주는 챗봇 '논문 좀 써본 강조교'입니다. 

<a href="https://drive.google.com/file/d/1IEZ7JGj7zjMwyBLuUjl5MO9-oFHlxFUR/view?usp=sharing">
발표 자료</a> 

## Demo
<p>
<img src="https://user-images.githubusercontent.com/73998876/155296655-8776899c-7e50-4c28-a183-cf47fccb9f84.gif" style="width: 60%">

<img src="https://user-images.githubusercontent.com/73998876/155300124-d4685237-76ab-408f-b5a1-37010d07b950.gif" style="width: 30%">
</p>
<p>
<img src="https://user-images.githubusercontent.com/73998876/155301925-b550034b-a5f4-4755-a930-50c0ee1c1b80.gif" style="width: 29%">
<img src="https://user-images.githubusercontent.com/73998876/155301929-15a0dde8-ab7a-4cc6-be15-0e0afa255b3b.gif" style="width: 30%">
<img src="https://user-images.githubusercontent.com/73998876/155301933-7467a8be-f4f0-4af4-9fd1-5fa960ba9bd5.gif" style="width: 30%">
</p>

## About Project
해당 프로젝트는 성남 청년 AI & Chatbot 실리콘벨리 프리인턴십 프로그램을 통해 만들어졌습니다.<br>
해당 레포지토리의 코드는 Mindwareworks의 CogInsight 챗봇 솔루션을 위한 API 서버이며, 챗봇에 대한 코드와 설정은 포함되어 있지 않습니다.<br>

자세한 API 사용 방법은 Swagger를 참고해 주시길 바랍니다.



## Service Detail
<p>
<img src="https://user-images.githubusercontent.com/73998876/155297275-f79d913a-945a-4676-8d31-b8af8c609dda.png" style="width: 40%">
<img src="https://user-images.githubusercontent.com/73998876/155297279-bdbb9fff-04a9-44b7-b70c-6dc1b16b0fd6.png" style="width: 40%">
</p>
<p>
<img src="https://user-images.githubusercontent.com/73998876/155297277-f85630db-0887-4011-82d0-fbdb63430bd1.png" style="width: 40%">
</p>

## Service Architecture
<img src="https://user-images.githubusercontent.com/73998876/155295777-e42a44bc-0411-48b4-956e-c36f5da7808a.png" alt="">

## Installation Process
### Initial Install
Git Clone
```shell
$ git clone https://github.com/J2H2-org/J2H2.git
```

Build (Build전 template 파일의 파일 이름에서 .template 부분을 지우고 비어있는 설정 값을 채워 주시길 바랍니다.)
```shell
$ docker-compose up --build
```

### Django Initial Setting
```shell
$ docker-compose -f docker-compose.yml exec backend python manage.py makemigrations
$ docker-compose -f docker-compose.yml exec backend python manage.py migrate
$ docker-compose -f docker-compose.yml exec backend python manage.py collectstatic
```

### Elasticsearch Initial Setting
1. 인덱스 생성
    ```shell
    $ curl -u id:pw -XPUT localhost:9200/index_name?pretty
    ```
2. 인덱스 확인
    ```shell
    $  curl -u id:pw -XGET localhost:9200/_cat/indices
    ```
3. 인덱스 닫기
    ```shell
    $  curl -u id:pw -XPOST localhost:9200/index_name/_close
    ```
4. 설정 변경
    ```shell
    $  curl -u id:pw -XPUT localhost:9200/index_name/_settings?
        pretty" -H 'Content-Type: application/json' -d'{
                         "index": {
                             "analysis": {
                                 "analyzer": {
                                     "nori": {
                                         "tokenizer": "nori_tokenizer"
                                     }
                                 }
                             }
                        }}'
    ```
5. 매핑 변경
    ```shell
    $  curl -u id:pw -XPUT localhost:9200/index_name/_mappings?
        pretty" -H 'Content-Type: application/json' -d'
    {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "nori"
            },
            "contents": {
                "type": "text",
                "analyzer": "nori"
            }
        }
    }'
    ```
6. 인덱스 오픈
    ```shell
    $ curl -u id:pw -XPOST localhost:9200/index_name/_open
    ```

### Grafana Prometheus Setting
1. localhost:8082 Grafana page 접속
2. 설정탭 클릭
3. Datasource 클릭
4. Prometheus 선택
5. 연결

### main path
- Swagger : localhost:8000/api/v1/swagger
- DRF : localhost:8000/api/v1
- Grafana : localhost:8082
- Prometheus : localhost:9090
- Kibana : localhost:5601

### Team Members
- 김영준 [@0BVer](https://github.com/0BVer)
  - Team Leader, Backend, DevOps
- 최수정 [@jadechoi](https://github.com/jadechoi)
  - Backend, Search Engine
- 강민혁 [@santa4246](https://github.com/santa4246)
  - Frontend
- 이혁 [@leehyeok97](https://github.com/leehyeok97)
  - ChatBot