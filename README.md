# 논문 좀 써본 강조교 (by Team Teesis)
## Demo
<img src="">
논문 기획부터 출판까지 도움을 주는 챗봇 '논문 좀 써본 강조교'입니다.

## About Project
해당 프로젝트는 성남 청년 AI & Chatbot 실리콘벨리 프리인턴십 프로그램을 통해 만들어졌습니다.<br>
해당 레포지토리의 코드는 Mindwareworks의 CogInsight 챗봇 솔루션을 위한 API 서버이며, 챗봇에 대한 코드와 설정은 포함되어 있지 않습니다.<br>

자세한 API 사용 방법은 Swagger를 참고해 주시길 바랍니다.

## Service Detail
<img src="">

## Service Architecture
<img src="">

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
$ docker-compose -f docker-compose.prod.yml exec backend python manage.py makemigrations
$ docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate
$ docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic
```

### Elasticsearch Initial Setting


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