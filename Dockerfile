FROM python:3.12-bookworm

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]