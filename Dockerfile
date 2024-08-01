FROM python:3.10
ARG OPENAI_API_KEY
ENV API_KEY=$OPENAI_API_KEY

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME
CMD ["java", "-version"]

#RUN apt-get install -y poppler-utils

WORKDIR /app
RUN mkdir -p /data
COPY . /app
RUN cd /app && pip install -r requirements.txt
RUN pip install protobuf==3.20.0
ENV PYTHONPATH=/app
EXPOSE 8282
CMD ["/app/start_ui.sh"]
