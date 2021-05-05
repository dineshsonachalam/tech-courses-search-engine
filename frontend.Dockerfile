FROM node:14

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN npm init -y
RUN npm i -s express


RUN mkdir /usr/src/app/build
COPY frontend/build /usr/src/app/build

COPY frontend/server.js .


EXPOSE 3000
CMD [ "node", "server.js" ]