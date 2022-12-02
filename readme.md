# 坏词撤回 0.1.1

基于[ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)开发的 坏词撤回 插件

任何问题请发issue

- 自动撤回包含屏蔽词的消息
- 只适用于群聊
- 管理员无法撤回其他管理员和群主的发言

## 安装插件

`nb plugin install nonebot-plugin-ayaka-prevent-bad-words`

## 配置

文件位置：`ayaka_setting.json`（该文件在第一次启动时会自动生成）

### word_packages

敏感词列表，可设置若干个词包，供各群组独立使用或交叉使用

```json
{
	"word_packages":[
		{
			"name": "违禁词包1",
			"words":  ["词1","词2"],
			"groups": [123455667, 102882912]
		},
		{
			"name": "违禁词包2",
			"words":  ["词3"],
			"groups": [102882912]
		}
	]
}
```

每个词包的`name`属性可以为空

**特殊情况**：若设置群号为0，则该词包会对所有群聊生效

```json
{
	"word_packages":[
		{
			"name": "违禁词包3",
			"words":  ["词5","词6"],
			"groups": [0]
		}
	]
}
```

### delay

延迟n秒后撤回，默认为0

可能会因为网络延迟而不准确

### powerful 

检测力度，默认为0

| powerful | 效果                               |
| -------- | ---------------------------------- |
| -1       | 发出提示语，不撤回                 |
| 0        | 只有坏词完全匹配时，才会撤回       |
| 1        | 即使坏词中夹杂了标点符号，也会撤回 |

### tip 

撤回消息后发送提示语，默认为 `请谨言慎行`

若设置为空，则撤回时不发送提示语

## 重启bot

注意：修改配置后，需要重启bot才能生效

## 关于警告

`[WARNING] ayaka | playwright未加载，win平台请关闭fastapi reload功能`

如果仅使用了本插件(`ayaka_prevent_bad_words`)，那么可以关闭`ayaka_setting.json`中的`use_playwright`设置

```json
{
    "__root__": {
        "use_playwright": true,
        ...
    },
    ...
}
```
