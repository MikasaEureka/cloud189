import os
config = {
    "multi": [
        {
            "account": os.environ['tyyp_user'],
            "password": os.environ['tyyp_pwd'],
        },
    ],
    "push": {
        # 合并发送消息, 只合并未单独配置 push 的账号
        "type": "pushplus",
        "key": os.environ['PUSHPLUS_TOKEN'],
    },
}
