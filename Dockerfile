FROM mongo
WORKDIR /data/mongo
COPY mongo/  /data/mongo/
RUN npm install


