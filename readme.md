# 坏词撤回

基于[ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)开发的 坏词撤回 插件

任何问题请发issue

- 自动撤回包含屏蔽词的消息
- 只适用于群聊
- 管理员无法撤回其他管理员和群主的发言

## 安装插件

`nb plugin install nonebot-plugin-ayaka-prevent-bad-words`

## 修改配置

文件位置：`ayaka_setting.json`（该文件在第一次启动时会自动生成）

`words` 

敏感词列表

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

