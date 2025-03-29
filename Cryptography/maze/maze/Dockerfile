FROM nginx:alpine

WORKDIR /usr/share/nginx/html/
RUN rm -rf /usr/share/nginx/html/*
COPY src/* .

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
