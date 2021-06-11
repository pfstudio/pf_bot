# coding: utf-8
import requests


class QQAction(object):
    @classmethod
    def send_group_msg(cls, url, group_id, message, auto_escape=False):
        resp = requests.get(url,
                            params={'group_id': group_id, 'message': message, 'auto_escape': auto_escape}, timeout=3)
