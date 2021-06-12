# coding: utf-8
import json
from const import JobType


class Config(object):
    config_name = None
    request_url = None
    qq_group_ids = None
    template = None
    data = None
    job_type = None


class ConfigHelper(object):
    # 通用获取配置字段
    @classmethod
    def get_config(cls, config_type):
        """
        :param config_type:
        :return: Config
        """
        try:
            with open('config.json', 'r') as f:
                data = f.read()
        except Exception as e:
            # 兼容 python qq/qq_actions.py 场景
            with open('qq/config.json', 'r') as f:
                data = f.read()

        all_config = json.loads(data)
        base_url = all_config.get('base_url')
        # 兼容 base_url 后缀没写 / 场景
        if base_url[-1] != '/':
            base_url += '/'
        custom_config = {} if (isinstance(all_config, map)) else all_config.get('config').get(config_type)
        conf = Config()
        conf.request_url = base_url + custom_config.get('request_url', '')
        conf.qq_group_ids = custom_config.get('qq_group_ids', [])
        conf.template = custom_config.get('template', {})
        conf.data = custom_config.get('data', {})
        conf.job_type = custom_config.get('job_type', JobType.SEND_GROUP_MSG)
        return conf


if __name__ == '__main__':
    print(ConfigHelper.get_config('qq_duty_notify_config').__dict__)
