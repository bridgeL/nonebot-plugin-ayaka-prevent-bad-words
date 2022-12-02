import re
from asyncio import sleep
from typing import List
from ayaka import AyakaApp, MessageSegment, Message

app = AyakaApp("坏词撤回")
app.help = '''自动撤回包含屏蔽词的消息'''


class Config(app.BaseConfig):
    delay: int = 0
    powerful: int = 0
    tip: str = "请谨言慎行"
    words: List[str] = ["芝士雪豹", "雪豹闭嘴"]


config = Config()


def check(msg: str):
    for word in config.words:
        if word in msg:
            return True

    if config.powerful == 1:
        msg = re.sub(r'[\W]', '', msg)

        for word in config.words:
            if word in msg:
                return True


@app.on.idle()
@app.on.text()
async def bad_words():
    msg = app.event.get_plaintext()
    mid = app.event.message_id

    if not check(msg):
        return

    tip = Message([MessageSegment.reply(mid), config.tip])
    if config.powerful == -1:
        await app.send(tip)
        return

    await sleep(config.delay)
    try:
        await app.bot.delete_msg(message_id=mid)
    except:
        pass

    await app.send(tip)
