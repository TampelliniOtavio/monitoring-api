FROM python:3.9-bookworm as production

COPY . .

RUN pip install virtualenv

RUN python -m virtualenv venv

RUN . venv/bin/activate

RUN venv/bin/pip install -r requirements.txt

EXPOSE 8000

CMD venv/bin/python main.py
