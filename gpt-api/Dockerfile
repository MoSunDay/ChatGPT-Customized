FROM python:3.10
WORKDIR /workflow-controlloer
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 8080
CMD ["python", "start.py"]
COPY app /workflow-controlloer/app
COPY requirements.txt /workflow-controlloer/requirements.txt
COPY start.py /workflow-controlloer/start.py