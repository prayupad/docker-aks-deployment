#FROM nginx:1.22.0
FROM node:12-alpine
#COPY index.html /usr/share/nginx/html
#COPY linux.png /usr/share/nginx/html

EXPOSE 80 	

#CMD ["nginx", "-g", "daemon off;"]
