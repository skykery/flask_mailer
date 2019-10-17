# flask_mailer
Flask api over Google SMTP account.

## Env vars
**API_MAIL_USER** - google mail user API_MAIL_PASS - google mail password

Run command: `docker run -p 9505:9505 -e API_MAIL_USER="test@gmail.com" -e API_MAIL_PASS="test" api_mail`

Example of POST to send an email: `curl -X POST http://127.0.0.1:9505/mail/ -d '{"to":"test@test.com", "subject": "Hello from flask", "body": "Hmm, seems its working, from docker mofo!"}' -H "Content-Type: application/json"`

[Image on Docker Hub](https://cloud.docker.com/u/skykery/repository/docker/skykery/api_mail)
