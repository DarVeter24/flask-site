FROM python:3.8
COPY . /flask-site
WORKDIR /flask-site
RUN python3 -m pip install flask gunicorn flask_autoindex flask_simplelogin 

EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]
