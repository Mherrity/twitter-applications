from discord import Webhook, RequestsWebhookAdapter

class Discord:
    def __init__(self, webhook_url):
        self.webhook = Webhook.from_url(webhook_url, adapter = RequestsWebhookAdapter())
    
    def send_message(self,user):
        message = self.create_message(user)
        self.webhook.send(message)

    @staticmethod
    def create_message(user):
        return  f"🚨 NEW APPLICANT 🚨 \n Applicant Name : {user['name']} \n Profile : {user['profile']} \n Thread : {user['thread']}"




