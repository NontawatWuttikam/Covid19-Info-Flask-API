from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
from covid19uncle import ThaiCovid19
from covid19uncle import covid19
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage,TextSendMessage

appBlueprint = Blueprint("webhook",__name__)
line_bot_api = LineBotApi('FMo5EGRDYJ2gg74JRPmR/G0QeaOaIg+DPEXWtz4bspWt7dvzwK61w7G+x4EkVLPdT0Lpvi4pNStIcvg3P//+9ujUoEO5uqurzm5kBVO6XUFHPQOEo0DH6MQr+Kux8odZwexl3GGJFXGv6zegH1j8DAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9000b5a93374236a05ffa5683505f0ee')

@appBlueprint.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        handler.handle(body,signature)
        return 'OK'

    
@handler.add(MessageEvent, message=TextMessage)
def handler_message(evt):
    line_bot_api.reply_message(
        evt.reply_token,
        TextSendMessage(text=evt.message.text)
    )