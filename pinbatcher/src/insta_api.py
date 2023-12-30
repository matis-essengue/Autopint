from instagrapi import Client
from instagrapi.types import Usertag, UserShort, User
import os


class InstaClient:
    def __init__(self, gui=False):
        self.username = os.getenv('INSTA_USERNAME')
        self.password = os.getenv('INSTA_PASSWORD')

    def post(self, image, caption, usertag):
        cl = Client()
        cl.login(self.username, self.password)
        user_long = cl.user_info_by_username(usertag)
        user_short = self._shorten_user(user_long)
        cl.photo_upload(
            image,
            caption,
            usertags=[
                Usertag(user=user_short, x=0.5, y=0.5)
            ]
        )
        print("Posted")

    def _shorten_user(self, user: User) -> UserShort:
        user_short = UserShort(
            pk=user.pk,
            username=user.username,
            full_name=user.full_name,
            profile_pic_url=user.profile_pic_url,
            profile_pic_url_hd=user.profile_pic_url_hd,
            is_private=user.is_private
        )
        return user_short
