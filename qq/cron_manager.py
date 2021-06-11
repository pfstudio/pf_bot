# coding: utf-8
import sys
from cronjob import DailySendDutyMsg2GroupCronJob
from config_helper import ConfigHelper

# 配置任务参数 -> Job map，支持可拓展; dict value 均为 Cronjob 子类，执行 execute(conf) 即可
config_dict = {
    'qq_duty_notify_config': DailySendDutyMsg2GroupCronJob
}


def main():
    config_name = sys.argv[1]
    conf = ConfigHelper.get_config(config_name)
    config_dict.get(config_name).execute(conf)


if __name__ == '__main__':
    main()
