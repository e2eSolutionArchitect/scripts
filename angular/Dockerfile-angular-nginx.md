```
FROM nginx:latest

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY /dist/datahub .

ENTRYPOINT ["nginx","-g","daemon off;"]

EXPOSE 80

# sudo docker run -d -p 80:80 obliqueo:latest
# curl http://localhost:80

```
