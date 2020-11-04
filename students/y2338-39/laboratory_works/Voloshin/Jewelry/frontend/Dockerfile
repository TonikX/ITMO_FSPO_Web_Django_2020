FROM node:10-alpine

WORKDIR /frontend
COPY package.json .
RUN npm install
RUN npm rebuild node-sass
