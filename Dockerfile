FROM python:3.11-alpine3.18

WORKDIR /var/www/

ADD requirements.txt /var/www/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /var/www/

RUN chmod a+x /var/www/docker/app.sh

RUN pip3 install gunicorn

RUN addgroup -g 1000 www

RUN adduser -D -u 1000 -G www www -s /bin/sh

USER www

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8080", "app.main:app"]
