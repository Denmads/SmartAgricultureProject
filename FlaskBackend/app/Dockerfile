FROM tensorflow/tensorflow

#docker run -it --rm -p 127.0.0.1:5000:5000 {tag}

COPY app.py ./work/
COPY ModelHandler.py ./work/
COPY requirements2.txt ./work/requirements.txt
COPY Models ./work/Models/
WORKDIR /work/
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]