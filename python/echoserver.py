from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/LpvO9eD68kXp+5HCnn34zqoQBks8PCZ0bLsx7UMLuSAWyMkc47FixZ3XrbSkG6aPbAsmDiknQjWG5KWJ99/XupRxBOavhUMra6Iquh69mfq76cfif+k1YjZcGJUBFwCJUYQZ/3Tw//lgRr5hjPvbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7705ffaaac029b082794f323850d0d03')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()