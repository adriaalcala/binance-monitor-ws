FROM python:3.8-slim

WORKDIR app
RUN pip install --no-cache-dir pipenv==2020.11.15

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy && rm -rf ~/.cache/


ENTRYPOINT [ "python",  "./main.py"]

COPY . ./
