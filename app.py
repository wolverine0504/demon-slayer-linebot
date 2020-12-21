from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests
import os
app = Flask(__name__)
# Channel Access Token 填上你的 channel access token
line_bot_api = LineBotApi('URtK3q5o/BTNQJGAeLTA1jrs7Y2aUKxboGpzpe72LFHUPfUq/KhxjsBD6uBLEEpjHLscnXkj4CugsKFKPB+vITKDRnfCnUVNIO6Ki2yJdzANRWgo8dyPN+FJ+21GxPz2+cpXGkUr7AH1q1TOWW1wngdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1f9c051bccbcaff271acf1633aaba6c4')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header values
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
