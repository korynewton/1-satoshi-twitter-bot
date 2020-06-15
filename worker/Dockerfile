FROM python:3

WORKDIR /usr/src/worker

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "run.py" ]