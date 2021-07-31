FROM node:16.6.0-slim

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN npm init -y
RUN npm i -s express

COPY frontend .

EXPOSE 3000
CMD [ "node", "server.js" ]