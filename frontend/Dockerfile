FROM node:14

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
RUN npm init -y
RUN npm i -s express
RUN mkdir build
COPY ./server.js .
COPY ./build ./build

EXPOSE 3000
CMD [ "node", "server.js" ]

# docker build -t dinesh .
# docker run -it -p 3000:3000 dinesh

# dineshsonachalam@macbook frontend % docker run -it dinesh /bin/bash
# root@e037ce51848f:/usr/src/app# 