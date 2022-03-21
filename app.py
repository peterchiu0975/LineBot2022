# -*- coding: utf-8 -*-
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)


# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('vfMoLhoxu4IMBxil/iZeTRUTsjgX21sQPuWKTjt9+0zik+nychozMwKyalCjNk6R6PvgHMPc/QW7vhaNIdlsYgSPnFmv5fwHkDntd/YRdXGElm8EJvXgjxbEUhok+L0hr+BDU0mpUa9G+euf6VfcXAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('58f13b495ee1ccf72ea6f99409a5a4d0')

line_bot_api.push_message('Ud9f868bfb17736f037645b7a8404c429', TextSendMessage(text='包裹到了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('幾點了?',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('自己看！'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)