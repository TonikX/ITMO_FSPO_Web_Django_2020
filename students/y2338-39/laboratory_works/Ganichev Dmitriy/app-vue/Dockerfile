FROM node:14.13.1

ENV CI=trueq
ENV PORT=8021
ENV HOST=::

WORKDIR /app-vue
COPY package.json .
RUN npm i

COPY . .

EXPOSE 8021
