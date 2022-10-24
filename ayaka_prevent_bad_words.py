import re
from asyncio import sleep
from ayaka import AyakaApp, MessageSegment, Message

app = AyakaApp("坏词撤回")
app.help = '''自动撤回包含屏蔽词的消息'''


def get_words():
    data = app.plugin_storage("words.txt", default="芝士雪豹\n雪豹闭嘴\n").load()
    words = []
    if data:
        data = data.rstrip("\n")
        words = data.split("\n")
    words = [w for w in words if w]
    return words


def get_config():
    config = app.plugin_storage(
        "config.json",
        default={
            "delay": 0,
            "powerful": 0,
            "tip": "请谨言慎行"
        }
    ).load()
    return config


words = get_words()
config = get_config()


def check(msg: str):
    for word in words:
        if word in msg:
            return True

    if config["powerful"] == 1:
        msg = re.sub(r'[\W]', '', msg)

        for word in words:
            if word in msg:
                return True


@app.on_text()
async def bad_words():
    msg = app.event.get_plaintext()
    mid = app.event.message_id

    if not check(msg):
        return

    tip = Message([MessageSegment.reply(mid), config["tip"]])
    if config["powerful"] == -1:
        await app.send(tip)
        return

    await sleep(config["delay"])
    try:
        await app.bot.delete_msg(message_id=mid)
    except:
        await app.send(tip)
