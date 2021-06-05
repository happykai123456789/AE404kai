from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
line_bot_api = LineBotApi('dWJjWqsOTsYdsSegOq3/8vXEKJOBf7KNGvKL+NaWP69sR5NrC9I0pW5LL/tvekwH901g7sXqF1jVvuqaFf98fT4g46bqHEUwL5lduZhldjt2dVBY7J7alXcwJQj/MH3EBRzm4d5zrtgGd6c/6yLTRwdB04t89/1O/w1cDnyilFU=')
UserID = 'Uc60911a4c7289ecd49f81f2bf344af13'

text_message = TextSendMessage(text = 'hello world!')
line_bot_api.push_message(UserID, text_message)

Sticker_message = StickerSendMessage(package_id = "789", sticker_id = '10855')
line_bot_api.push_message(UserID, Sticker_message)

image_message = ImageSendMessage(
    original_content_url='https://i.imgur.com/xyPtn4m.jpeg',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg')
line_bot_api.push_message(UserID,image_message)

location_message = LocationSendMessage(
    title='CodingAPE猿創力程式設計學校',
    address='台北市信義區基隆路一段180號',
    latitude=25.042408,
    longitude=121.564839)
line_bot_api.push_message(UserID,location_message)

video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)
