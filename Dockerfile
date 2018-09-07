FROM python:3-alpine
ADD src /
RUN pip install -r requirements.txt
#RUN echo "${API_MAIL_PASS}"
#ENV API_MAIL_USER test@gmail.com
#ENV API_MAIL_PASS test
#RUN echo "user = ${API_MAIL_USER}\npassword = ${API_MAIL_PASS}" > cred.py
CMD [ "python", "./app.py" ]
