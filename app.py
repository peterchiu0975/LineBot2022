from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import  MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('vfMoLhoxu4IMBxil/iZeTRUTsjgX21sQPuWKTjt9+0zik+nychozMwKyalCjNk6R6PvgHMPc/QW7vhaNIdlsYgSPnFmv5fwHkDntd/YRdXGElm8EJvXgjxbEUhok+L0hr+BDU0mpUa9G+euf6VfcXAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58f13b495ee1ccf72ea6f99409a5a4d0')
line_bot_api.push_message('Ud9f868bfb17736f037645b7a8404c429', TextSendMessage(text='包裹到了'))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
