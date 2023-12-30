from pinbatcher.src.infoinputapp import InfoInputApp
from pinbatcher.src.insta_api import InstaClient


def run():
    # app = InfoInputApp()
    # title, description, link = app.run()
    # print(f"Title: {title}")
    # print(f"Description: {description}")
    # print(f"Link: {link}")
    image = 'pinbatcher/cjay1k__at__2022-11-16_19-00-01_UTC_10.jpg'
    caption = 'This is a caption'
    icl = InstaClient()
    icl.post(image, caption)
