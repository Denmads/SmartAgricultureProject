FROM python

#docker run -it --rm -p 127.0.0.1:3000:3000 {tag}

COPY api.py ./work/
COPY db.py ./work/
COPY Drone.py ./work/
COPY Field.py ./work/
COPY hub.py ./work/
COPY job.py ./work/
COPY parth.py ./work/
COPY server.py ./work/
COPY requirements.txt ./work/requirements.txt
WORKDIR /work/
RUN pip install -r requirements.txt 
RUN pip install mysql-connector
CMD ["python", "/work/db.py"]