from flask.views import MethodView
from flask import jsonify, request
from mail_utils import Mail
from cred import user, password

class MailView(MethodView):
    def post(self):
        payload = request.json or {}
        post_kwargs = self.get_required(payload)
        print(post_kwargs)
        if self.is_valid(post_kwargs):
            mail = Mail(user, password)
            mail.init_message(to=post_kwargs["to"], subject=post_kwargs["subject"], body=post_kwargs["body"])
            mail.send()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "fail"})
    
    def get_required(self, payload):
        fields = ["to", "subject", "body"]
        return {field:payload.get(field) for field in fields}
    
    def is_valid(self, arguments):
        if None in arguments.values():
            return False
        return True