FROM node:10-alpine
RUN mkdir /front
WORKDIR /front
COPY ./package*.json ./
RUN npm install
RUN npm install -g http-server
COPY . ./
EXPOSE 8080
CMD ["npm","run","dev"]
