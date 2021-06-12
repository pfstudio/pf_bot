# coding: utf-8
from datetime import datetime

from config_helper import Config
from qq_actions import QQAction


# Cronjob 任务接口
class Cronjob(object):

    @classmethod
    def execute(cls, conf, *args):
        pass


# 基础发送群消息cronjob
class BaseSendGroupMessageCronjob(Cronjob):

    @classmethod
    def execute(cls, conf, *args):
        """
        :type conf: Config
        """
        message = conf.template
        if args:
            message = conf.template % args
        for group_id in conf.qq_group_ids:
            QQAction.send_group_msg(url=conf.request_url, group_id=group_id, message=message)


class DailySendDutyMsg2GroupCronJob(BaseSendGroupMessageCronjob):

    @classmethod
    def execute(cls, conf, *args):
        """
        :type conf: Config
        :param conf:
        :return:
        """
        name, qq = DailySendDutyMsg2GroupCronJob.calculate_who(conf.data)
        super(DailySendDutyMsg2GroupCronJob, cls).execute(conf, name, qq)

    @classmethod
    def calculate_who(cls, data):
        # 设置起始周
        li = data.get('start_week').split('/')
        li = [int(x) for x in li]
        start_date = datetime(li[0], li[1], li[2])
        now = datetime.now()
        time_diff = now - start_date
        # 计算单双周，even 为 1 为双周
        even = int((time_diff.days - 1) / 7) % 2
        idx = even * 7 + now.weekday() + 1
        people_msg = data.get('duty_table').get(str(idx))
        name = people_msg.get('name')
        qq_id = people_msg.get('qq')
        return name, qq_id
