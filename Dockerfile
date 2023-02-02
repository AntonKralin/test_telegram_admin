FROM python:3.10.9-alpine3.17
MAINTAINER AntonKralin
RUN mkdir -p /opt/test_telegram_admin
COPY requirements.txt /opt/test_telegram_admin/requirements.txt
WORKDIR /opt/test_telegram_admin
RUN pip install --no-cache-dir -r requirements.txt
VOLUME /opt/test_telegram_admin
RUN chmod -R 777 /opt/test_telegram_admin
CMD [ "python", "./main.py" ]