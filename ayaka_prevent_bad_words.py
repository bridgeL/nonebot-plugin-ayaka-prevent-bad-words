import re
from asyncio import sleep
from typing import List
from loguru import logger
from pydantic import BaseModel
from nonebot.adapters.onebot.v11 import MessageSegment, Message
from nonebot.matcher import current_bot, current_event
from ayaka import AyakaCat, AyakaConfig

cat = AyakaCat("坏词撤回")
cat.help = '''自动撤回包含屏蔽词的消息'''


class WordPackage(BaseModel):
    name: str = ""
    words: List[str] = []
    groups: List[int] = []


default_word_packages = [
    WordPackage(name="示例词包1", words=["芝士雪豹", "雪豹闭嘴"], groups=["12311211"]),
    WordPackage(name="示例词包2", words=["wtf", "holy shit"], groups=[
                "12311211", "389019292"])
]


class Config(AyakaConfig):
    __config_name__ = cat.name
    delay: int = 0
    powerful: int = 0
    tip: str = "请谨言慎行"
    word_packages: List[WordPackage] = default_word_packages
    exclude_cq: list[str] = ["at", "image", "json", "xml"]


config = Config()


def get_words(group_id: int):
    words: List[str] = []
    for word_pack in config.word_packages:
        if group_id in word_pack.groups or 0 in word_pack.groups:
            words.extend(word_pack.words)
    return words


def check(msg: str, group_id: int):
    for cq in config.exclude_cq:
        msg = re.sub(f"\[CQ:{cq}.*?\]", "", msg)

    if config.powerful == 1:
        msg = re.sub(r'[\W]', '', msg)

    words = get_words(group_id)
    for word in words:
        if word in msg:
            return True


@cat.on_text(always=True)
async def bad_words():
    msg = cat.message
    mid = current_event.get().message_id
    gid = int(cat.group.id)

    if not check(msg, gid):
        return

    if config.powerful >= 0:
        await sleep(config.delay)
        try:
            await current_bot.get().delete_msg(message_id=mid)
        except:
            logger.warning("撤回失败，可能是bot权限不够导致")

    if config.tip:
        await cat.send(Message([MessageSegment.reply(mid), config.tip]))
