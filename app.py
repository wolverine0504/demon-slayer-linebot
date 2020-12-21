import tensorflow.keras
import time
import numpy as np
from PIL import Image, ImageOps

from flask import Flask, request, abort

from flask_ngrok import run_with_ngrok

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
# run_with_ngrok(app)
# Channel Access Token 填上你的 channel access token
line_bot_api = LineBotApi(
    'URtK3q5o/BTNQJGAeLTA1jrs7Y2aUKxboGpzpe72LFHUPfUq/KhxjsBD6uBLEEpjHLscnXkj4CugsKFKPB+vITKDRnfCnUVNIO6Ki2yJdzANRWgo8dyPN+FJ+21GxPz2+cpXGkUr7AH1q1TOWW1wngdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1f9c051bccbcaff271acf1633aaba6c4')

# 監聽所有來自 /callback 的 Post Request
# 連上我的heroku
# 1.line webhook URL 改成 https://demon-slayer.herokuapp.com/callback

# 本地端用ngrok測試
# 1.另開終端執行ngrok在有ngrok執行檔的地方 ./ngrok http 5000
# 2.line webhook URL 改成 https://ngrok的網址/callback
# 3.執行app.py python3 app.py


class_dict = {}
with open('converted_savedmodel/labels.txt') as f:
    for line in f:
        (key, val) = line.split()
        class_dict[int(key)] = val

reply_imgs_url = {
    0: "https://i.pinimg.com/564x/5b/27/8f/5b278fd455d2dd1eef8cfcfca9cea213.jpg",
    1: "https://i.pinimg.com/564x/73/e9/f1/73e9f103a2f2bf0c5941cada58d997d2.jpg",
    2: "https://i.pinimg.com/564x/ec/68/78/ec68785dbfbb1f715cf506b2d1f9fdd8.jpg",
    3: "https://i.pinimg.com/564x/47/f9/16/47f916be831f08ce48ecb1b1c584f1c8.jpg",
    4: "https://i.pinimg.com/564x/00/b2/ee/00b2eeb8386e662dd7059481bd9c5bee.jpg",
    5: "https://i.pinimg.com/564x/8a/c3/5e/8ac35e26c1c1a862ea5620d8ba9869cb.jpg"
}
print(reply_imgs_url)
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
    msgtext = event.message.text
    if msgtext == "文字":
        print("要文字")
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
    elif msgtext == "貼圖":
        print("要貼圖")
        message = StickerSendMessage(package_id=1, sticker_id=2)
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == "大哥沒有輸":
        print("大哥真的沒有輸")
        message = ImageSendMessage(original_content_url='https://i.pinimg.com/564x/8b/a1/9d/8ba19d2c866c852d73a3d7c28581de68.jpg',
                                   preview_image_url='https://i.pinimg.com/564x/8b/a1/9d/8ba19d2c866c852d73a3d7c28581de68.jpg')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='請傳一張圖片讓我看看你最像誰!')
        line_bot_api.reply_message(event.reply_token, message)


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model(
    'converted_savedmodel/model.savedmodel')


@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):

    # print(time.asctime(time.localtime(time.time())))

    message_content = line_bot_api.get_message_content(event.message.id)
    file_name = event.message.id+'.jpg'
    with open(file_name, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    # print(time.asctime(time.localtime(time.time())))

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(file_name)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # print(time.asctime(time.localtime(time.time())))

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0 - 1)

    # Load the image into the array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array[0:224, 0:224, 0:3]

    # run the inference
    prediction = model.predict(data)

    # print(time.asctime(time.localtime(time.time())))

    max_probability_item_index = np.argmax(prediction[0])

    reply_img = reply_imgs_url.get(max_probability_item_index)
    print(reply_img)

    result_text_message = TextSendMessage("最像你的鬼滅角色是%s!!!" % (
        class_dict.get(max_probability_item_index)))
    result_image_message = ImageSendMessage(
        original_content_url=reply_img, preview_image_url=reply_img)

    line_bot_api.reply_message(
        event.reply_token, [result_text_message, result_image_message])
    #line_bot_api.reply_message(event.reply_token, result_image_message)
    # if prediction.max() > 0.6:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(
    #             """這個物件極有可能是 %s ，其相似機率為 %s 。""" % (class_dict.get(
    #                 max_probability_item_index), prediction[0][max_probability_item_index])
    #         )
    #     )
    # else:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(
    #             """再給我清楚一點的圖！！"""
    #         )
    #     )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()
