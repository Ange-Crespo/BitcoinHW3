from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group


def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("update").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    Group("update").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
