# 坏词撤回

基于ayaka开发的 坏词撤回 插件

任何问题请发issue

- 自动撤回包含屏蔽词的消息
- 只适用于群聊
- 管理员无法撤回其他管理员和群主的发言

<b>注意：由于更新pypi的readme.md需要占用版本号，因此其readme.md可能不是最新的，强烈建议读者前往[github仓库](https://github.com/bridgeL/nonebot-plugin-ayaka-prevent-bad-words)以获取最新版本的帮助</b>


# How to start

## 安装 ayaka

安装 [前置插件](https://github.com/bridgeL/nonebot-plugin-ayaka) 

`poetry add nonebot-plugin-ayaka`


## 安装 本插件

安装 本插件

`poetry add nonebot-plugin-ayaka-prevent-bad-words`

修改nonebot2  `bot.py` 

```python
nonebot.load_plugin("ayaka_prevent_bad_words")
```

## 修改屏蔽词列表
文件位置：`data/plugins/坏词撤回/words.txt`（该文件在第一次启动时会自动生成）

一行一个敏感词

```
芝士雪豹
雪豹闭嘴
```

之后群友发言包含这些词时会被撤回


## 其他配置
文件位置：`data/plugins/坏词撤回/config.json`（该文件在第一次启动时会自动生成）

`delay` 

延迟n秒后撤回，默认为0

可能会因为网络延迟而不准确

`powerful` 

检测力度，默认为0

| powerful | 效果                               |
| -------- | ---------------------------------- |
| -1       | 发出提示语，不撤回                 |
| 0        | 只有坏词完全匹配时，才会撤回       |
| 1        | 即使坏词中夹杂了标点符号，也会撤回 |

`tip` 

提示语，默认为 请谨言慎行

**注意：修改配置后，需要重启bot才能生效**

