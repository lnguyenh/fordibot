FROM python:3.9-alpine3.14
RUN apk add --no-cache wkhtmltopdf ttf-dejavu bash
RUN mkdir /wkhtmltopdf-folder
RUN chmod 0700 /wkhtmltopdf-folder
ENV XDG_RUNTIME_DIR=/wkhtmltopdf-folder
WORKDIR /app
COPY ../requirements.txt .
RUN pip3 install -r requirements.txt
COPY .. .
CMD [ "python3", "-m" , "fordibot.bot"]
