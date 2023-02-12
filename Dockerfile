FROM python:3.8

WORKDIR /Django_stripe_test

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "./stripe_ecommerce/manage.py", "runserver", "0.0.0.0:8000"]