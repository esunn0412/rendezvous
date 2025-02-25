FROM python:3.11

WORKDIR /home/

RUN echo "testingggg"

RUN git clone https://github.com/esunn0412/rendezvous.git

WORKDIR /home/rendezvous/

RUN python -m pip install --upgrade pip

RUN pip install gunicorn

RUN pip install mysqlclient

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=myPinterest.settings.deploy && python manage.py migrate --settings=myPinterest.settings.deploy && gunicorn myPinterest.wsgi --env DJANGO_SETTINGS_MODULE=myPinterest.settings.deploy --bind 0.0.0.0:8080"]