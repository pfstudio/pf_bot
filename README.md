# pf_bot

全称：pf_bot

可能会超级无敌厉害的攀峰机器人，目前支持功能

- 定时消息任务 
  
    使用，定时任务计算工具 https://tool.lu/crontab/
  ```
  输入 crontab -e
  增加一行
  0 8 * * * cd /root/pf_bot/qq;python3 cron_manager.py qq_duty_notify_config
  ```
## 配置格式
```json5
{
    "base_url": "http://localhost:5700",
    "config": {
        "qq_duty_notify_config": {
            "config_name": "qq_duty_notify_config", // 配置名
            "request_url": "send_group_msg",        // 接口名
            "qq_group_ids": [],                     // qq群组id列表
            "template": "【机器人消息提示】：今日值班人是 %s ，快去 520 工作室开卷吧！ [CQ:at,qq=%s]", // 消息模板， 参照 https://github.com/botuniverse/onebot/blob/master/v11/specs/message/string.md
            "data": {
                // 其他自定义数据，以下为举例
                "duty_table": {

                },
                "start_week": "2021/6/6"
            },
            "job_type": 1 // const 中的任务类型
        },
        "some_config": {
            "request_url": "",
            "qq_group_id": []
        }
    }
}
```

## 更新历史

- 2021/6/12: 高度支持定制化 QQ 定时任务

## 使用开源项目

- [onebot](https://github.com/botuniverse/onebot) 一个聊天机器人应用接口标准
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) qq消息客户端