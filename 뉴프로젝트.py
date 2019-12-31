import discord

clinet = discord.Client()


@clinet.event
async def on_ready():
    print(clinet.user.id)
    print("ready")
    game = discord.Game("트와이스필정쏙")
    await clinet.change_presence(status=discord.Status.online, activity=game)



@clinet.event
async def on_message(message):
    if message.content.startswith("트하"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("죠악개"):
        await message.channel.send("올팬입니다 삐삑")
    if message.content.startswith("민비는?"):
        await message.channel.send("올팬이다")
    if message.content.startswith("트바"):
        await message.channel.send("안녕히가세요 ")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))













clinet.run("NjYwODIxNTE5OTkxMTc3MjM2.Xgql-A.BL9mMSt8736V_0b1WxmJ3DnOwhs")
