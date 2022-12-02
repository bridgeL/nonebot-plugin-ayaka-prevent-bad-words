import re
from asyncio import sleep
from typing import List
from loguru import logger
from pydantic import BaseModel
from ayaka import AyakaApp, MessageSegment, Message

app = AyakaApp("坏词撤回")
app.help = '''自动撤回包含屏蔽词的消息'''


class WordPackage(BaseModel):
    name: str = ""
    words: List[str] = []
    groups: List[int] = []


class Config(app.BaseConfig):
    delay: int = 0
    powerful: int = 0
    tip: str = "请谨言慎行"
    word_packages: List[WordPackage] = [WordPackage(name="示例词包", words=["芝士雪豹", "雪豹闭嘴"])]


config = Config()


def get_words(group_id: int):
    words: List[str] = []
    for word_pack in config.word_packages:
        if group_id in word_pack.groups or 0 in word_pack.groups:
            words.extend(word_pack.words)
    return words


def check(msg: str, group_id: int):
    if config.powerful == 1:
        msg = re.sub(r'[\W]', '', msg)

    words = get_words(group_id)
    for word in words:
        if word in msg:
            return True


@app.on.idle()
@app.on.text()
async def bad_words():
    msg = app.event.get_plaintext()
    mid = app.event.message_id
    gid = app.group_id

    if not check(msg, gid):
        return

    if config.powerful >= 0:
        await sleep(config.delay)
        try:
            await app.bot.delete_msg(message_id=mid)
        except:
            logger.warning("撤回失败，可能是bot权限不够导致")

    if config.tip:
        await app.send(Message([MessageSegment.reply(mid), config.tip]))
