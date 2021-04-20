FROM python:3

WORKDIR /app/

ADD requirments.txt requirments.txt
RUN pip install -r requirments.txt

ADD . .

CMD python main.py