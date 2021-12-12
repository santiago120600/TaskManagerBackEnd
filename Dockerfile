FROM python:3.9.7

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# copy project
COPY . /code/

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "taskManagerApi", "taskManagerApi.wsgi:application"]
