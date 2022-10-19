import re
from asyncio import sleep
from ayaka import AyakaApp

app = AyakaApp("坏词撤回")
app.help = '''自动撤回包含屏蔽词的消息'''

data = app.plugin_storage(
    "words", suffix=".txt",
    default="芝士雪豹\n1!5!\n"
).load()
words = []
if data:
    data = data.rstrip("\n")
    words = data.split("\n")

config = app.plugin_storage(
    "config",
    default={
        "delay": 0,
        "powerful": 0
    }
).load()


@app.on_text()
async def _():
    msg = app.event.get_plaintext()
    if config["powerful"] == 1:
        msg = re.sub(r'[\W]', '', msg)
    for word in words:
        if word in msg:
            await sleep(config["delay"])
            await app.bot.delete_msg(message_id=app.event.message_id)
