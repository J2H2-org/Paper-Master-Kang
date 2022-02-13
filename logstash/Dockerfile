FROM docker.elastic.co/logstash/logstash:7.16.3

# install dependency
RUN bin/logstash-plugin install logstash-integration-jdbc

ADD https://jdbc.postgresql.org/download/postgresql-42.2.23.jar /usr/share/logstash/postgresql-42.2.23.jar
USER root
RUN chown -R logstash /usr/share/logstash/
CMD ["logstash", "-f", "/usr/share/logstash/pipeline/logstash.conf"]