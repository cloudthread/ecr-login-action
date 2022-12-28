FROM python:3.10
RUN pip install requests
COPY main.py /opt/main.py
ENTRYPOINT ["python", "/opt/main.py"]
