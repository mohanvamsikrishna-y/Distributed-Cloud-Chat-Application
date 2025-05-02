#using mongodb image
FROM mongo:6.0

#set the default working directory
WORKDIR /data/db

#mongodb public port
EXPOSE 27017

#run mongodb with necessary configurations
CMD ["mongod", "--bind_ip", "0.0.0.0"]
