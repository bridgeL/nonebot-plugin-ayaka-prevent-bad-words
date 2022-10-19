# 坏词撤回

基于ayaka开发的 坏词撤回 插件

任何问题请发issue

注意：只适用于群聊！

<b>注意：由于更新pypi的readme.md需要占用版本号，因此其readme.md可能不是最新的，强烈建议读者前往[github仓库](https://github.com/bridgeL/nonebot-plugin-ayaka-prevent-bad-words)以获取最新版本的帮助</b>

自动撤回包含屏蔽词的消息

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

## 配置

推荐配置（非强制要求）
```
COMMAND_START=["#"]
COMMAND_SEP=[" "]
```


## 修改屏蔽词列表
打开nonebot下的`data/plugins/坏词撤回/words.txt`（该文件在第一次启动时会自动生成），一行一个敏感词

例如
```
芝士雪豹
雪豹闭嘴
```

之后群友发言包含这些敏感词时会被撤回


## 其他配置
`data/plugins/坏词撤回/config.json`

delay 延迟n秒后撤回，默认为0

powerful 检测力度，默认为0

powerful | 效果
-|-
0|只有坏词完全匹配时，才会撤回
1|即使坏词中夹杂了标点符号，也会撤回
