# coding: utf-8
import sys

from config_helper import ConfigHelper
from const import JobType
from cronjob import DailySendDutyMsg2GroupCronJob, BaseSendGroupMessageCronjob

# 配置任务参数 -> Job map，支持可拓展; dict value 均为 Cronjob 子类，执行 execute(conf) 即可
config_dict = {
    'qq_duty_notify_config': DailySendDutyMsg2GroupCronJob
}

base_config_dict = {
    JobType.SEND_GROUP_MSG: BaseSendGroupMessageCronjob
}


def main():
    if len(sys.argv) < 1:
        print("[error]: 请输入执行的任务名~")
    config_name = sys.argv[1]
    conf = ConfigHelper.get_config(config_name)

    job = config_dict.get(config_name)
    # 若不是走的自定义逻辑，直接让这个 job 类别的基类消费
    if not job:
        job = base_config_dict.get(conf.job_type)
    job.execute(conf)


if __name__ == '__main__':
    main()
