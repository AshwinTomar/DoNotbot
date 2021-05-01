import random
from random import shuffle
import discord
from discord import channel
from discord.ext import commands, tasks
from itertools import cycle
import calendar
import TenGiphPy
from googletrans import Translator
from keep_alive import keep_alive
client = commands.Bot(command_prefix='&')

# definition column
translator = Translator()
t = TenGiphPy.Tenor(token='41QVLZGFS5MZ')

status = cycle(['Kids hunter 6969', 'flamethrower420'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')


 



@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_leave(member):
    print(f'{member} has left the server.')


@client.command(aliases=["mc"])
async def member_count(ctx):

    a = ctx.guild.member_count
    b = discord.Embed(
        title=f"members in {ctx.guild.name}", description=a, color=discord.Color((0xffff00)))
    await ctx.send(embed=b)



@client.command(aliases=['trans'])
async def translate(ctx,*, words):
    result = translator.translate(words,dest='en')
    await ctx.send(result.text)
       


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    await ctx.send(t.random("anime cute"))


@client.command()
async def trap(ctx):
    await ctx.send(t.random("anime traps"))


@client.command()
async def thighs(ctx):
    await ctx.send(t.random("anime thighs"))


@client.command(aliases=['s'])
async def search(ctx, *, word):
    await ctx.send(t.random(word))


@client.command(aliases=["i"])
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=745997490163023912&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D745997490163023912%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscord.com%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D745997&scope=bot")
    await ctx.send(t.random("white cat"))


@client.command(aliases=['hey', 'hello', 'sup'])
async def hi(ctx):
    responses = [
        "Everyone’s entitled to act stupid once in a while but you’re abusing the privilege.",
        "do something productive for once rather than chatting to a bot...",
        "Umm...pardon me, I wasn’t listening. Can you repeat what you just said?",
        "Ok.",
        "That sounds weird coming from you.",
        "Whatever you said",
        "I’m not a cactus expert but I do know a prick when I see one."
        "Sorry, I don’t understand what you’re saying. I don’t speak bullshit.",
        "Did it hurt when you fell from heaven? \nCause it looks like you landed on your face",
        "Thank you very much for thinking about me! Bye.",
        "Goodbye!",
        "How is that supposed to make me feel?",
        "There are some incredibly dumb people in this world. Thanks for helping me understand that. I am a bot y'know",
        "Look, if I wanted to hear from an asshole, all I had to do was fart.",
        "Huh",
        "You know you really should buy some breath mints? ",
        "Stupidity’s not a crime, so you’re free to go.",
        "You always bring me so much joy, the minute you leave the room.",
        "Sorry buddy but I don’t have the energy to pretend to like you today.",
        "Everyone said you were unpleasant but I didn’t believe them ……. until now.",
        "Sorry but you’re confusing me with someone who actually cares about what you think.",
        "I don’t know what your problem is but I’m guessing it’s hard to pronounce.",
        "Why don’t you check eBay and see if they have a life for sale.",
        "You only annoy me when you’re breathing, really.",
        "I was going to give you a nasty look but I can see you already got one."
        "Mirrors don’t lie, and lucky for you, they don’t laugh either.",
        "I believed in evolution until I met you.",
        "I accept I’m not perfect but at least I’m not you."]
    await ctx.send(f'\n {random.choice(responses)}')
    await ctx.send(t.random("anime laugh"))


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, user: discord.Member, *, reason):
    await user.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def hams(ctx):
    await ctx.channel.send("https://tenor.com/view/hamster-drinking-pets-gif-11796328")


@client.command()
async def iloveyou(ctx):
    await ctx.channel.send("i love you too boss")
    await ctx.send(t.random("anime heart"))


@client.command()
async def cal(ctx):
    await ctx.channel.send(calendar.month(2020, 11))


@client.command()
async def power(ctx):
    await ctx.channel.send("https://www.youtube.com/channel/UCPYyI4KDMRXIVCO_UNXd9sw\n Go subscribe!! i know you haven't yet :eye:")
    await ctx.send(t.random("anime pouting"))


@client.command()
async def beebom(message):
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f'{mention} want to see the big wholesome bee'
    await message.channel.send(response)
    await message.send(t.random("bee"))


@client.command(aliases=["tyler", 'trump'])
async def nick(ctx):
    await ctx.channel.send("what a fucking whiny bitch he is")
    await ctx.send(t.random("anime smirk"))


@client.command()
async def intro(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/767278948815470594/771291330328264704/unknown.png')


@client.command()
async def chun(ctx):
    await ctx.channel.send("https://media1.tenor.com/images/c5b2cdbe3815555653dacafacb035dfe/tenor.gif?itemid=12702077")


@client.command()
async def ava(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/772816194004582410/772816301172719666/image0.jpg?width=311&height=587")


@client.command()
async def bye(ctx):
    await ctx.channel.send("https://cdn.discordapp.com/emojis/760673279442026537.png?v=1")
    await ctx.send(t.random("bye"))


@client.command(aliases=["uwu", "UwU", "OwO"])
async def owo(ctx):
    await ctx.channel.send('UwU')
    await ctx.send(t.random("owo cute"))


@client.command(aliases=["bd"])
async def birthday(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} wishes {user.mention} a very happy birthday!!!"
    await message.channel.send(response)
    await message.send(t.random("anime birthday dance"))


@client.command()
async def slap(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} have just slapped {user.mention} real hard"
    await message.channel.send(response)
    await message.send(t.random("anime slap"))


@client.command()
async def cloud(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} want to see the omegalul pogchamp pedophile and only real anime girl waifu......here you go"
    await message.channel.send(response)
    await message.send(t.random("cute anime girl"))


@client.command()
async def meeza(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f'{mention} want to see the slav artist....here goes nothing'
    await message.channel.send(response)
    await message.send('https://media.discordapp.net/attachments/746003623036583960/837052379353317476/PicsArt_03-08-07.png?width=670&height=670')

@client.command()
async def clay(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f'{mention} sandeich sandeich sandeich sandeich moment'
    await message.channel.send(response)
    await message.send(t.random("Linkin Park"))


@client.command()
async def punch(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} have just punched {user.mention} real hard"
    await message.channel.send(response)
    await message.send(t.random("anime punch"))


@client.command()
async def hug(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} is hugging {user.mention}"
    await message.channel.send(response)
    await message.send(t.random("anime hug"))


@client.command()
async def pat(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} gave a nice pat to {user.mention}"
    await message.channel.send(response)
    await message.send(t.random("anime pat"))








@client.command()
async def kiss(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} just kissed {user.mention} "
    await message.channel.send(response)
    await message.send(t.random("anime kiss"))


@client.command()
async def kill(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} just killed {user.mention} "
    await message.channel.send(response)
    await message.send(t.random("stab"))


@client.command()
async def fuck(message, user: discord.Member):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} just fucked {user.mention} and it felt great"
    await message.send(t.random("sex"))
    await message.channel.send(response)


@client.command(aliases=["w"])
async def waifu(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"Looks like  {mention} have found a waifu "
    await message.channel.send(response)
    await message.send(t.random("cute anime girl"))


@client.command(aliases=["h"])
async def husbando(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"Looks like  {mention} have found a husbando"
    await message.channel.send(response)
    await message.send(t.random("anime boys"))


@client.command()
async def blush(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"Looks like you made {mention} blush.."
    await message.channel.send(response)
    await message.send(t.random("anime blush"))


@client.command()
async def dance(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} is dancing"
    await message.channel.send(response)
    await message.send(t.random("dance"))


@client.command(aliases=["sad"])
async def cry(message):
    # No infinite bot loops
    if message.author == client.user or message.author.bot:
        return
    mention = message.author.mention
    response = f"{mention} is sad and probably crying"
    await message.channel.send(response)
    await message.send(t.random("anime cry"))


@client.command()
async def egg(message):
    await message.channel.send('Here comes Eggy')
    await message.send(t.random("gudetama"))


@client.command()
async def fun(message):
    await message.send(t.random("meme"))


@client.command()
async def sleep(message):
    mention = message.author.mention
    await message.send(f'{mention} "is feeling sleepy')
    await message.send(t.random("anime sleepy"))


@client.command()
async def food(message):
    await message.send(t.random("delicacies"))


@client.command()
async def laugh(message):
    await message.send(t.random("anime laugh"))


@client.command()
async def grim(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/750650684604416031/772812199038812190/image0.jpg?width=374&height=548')


@client.command()
async def ashby(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/750650684604416031/772855280055615508/image0.jpg?width=330&height=587')


@client.command()
async def keyur(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/734021581856178206/779689860365418506/Screenshot_2020-11-14-03-36-08-917_com.snapchat.android.jpg?width=264&height=588')


@client.command()
async def shoo(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/746003623036583960/780029098152034324/Screenshot_20200902_185526.jpg?width=492&height=542')


@client.command()
async def dilara(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/750650684604416031/772814184378793994/image0.jpg?width=308&height=548')


@client.command()
async def delilah(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/772316429495435274/772756851904479252/hottie2.png')


@client.command()
async def adrian(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/735697266437914708/768079308744294420/image0.jpg?width=406&height=542")


@client.command()
async def isabelle(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/768039377870782474/768039444493762580/Screenshot_20201020-101009_Snapchat.jpg?width=256&height=541")


@client.command()
async def ash(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/750650684604416031/772813989755224064/image0_36.jpg")


@client.command()
async def leon(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/772777158195412992/772779788372803594/image0.jpg?width=330&height=587")


@client.command()
async def eyes(ctx):
    await ctx.channel.send("https://media1.tenor.com/images/c1c7c53a93129ad7ca7cea4b72850076/tenor.gif?itemid=16906344")


@client.command()
async def gage(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/750650684604416031/771367987714064434/image0.jpg?width=330&height=587")


@client.command()
async def sum(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/750650684604416031/771773249990033418/20201023_220602.jpg?width=435&height=587")


@client.command()
async def drew(ctx):
    await ctx.channel.send('''Our bodies were covered in sweat. My breathing quickened as I felt him slowly, and oh-so pleasantly, put his nine-inch c--k inside me. I bit my lip, trying not to moan, trying not to give him what he wanted to hear, but it was too difficult and a soft, sexual sound escaped my lips. “A-Ah~! M-M-Master~! S-Start m-moving~!” I stuttered out. He chuckled, his lips curled into a devilish smirk. “Oh, I want to hear you beg for it~” he said. My face felt like the sun, heating up, and my mouth was open but no words would come out. I finally came to my thoughts and said, hesitantly. “M-Master, p-please start th-thrusting~! I-I want to f-feel you f-f--k m-me s-so hard~ P-Please, Mast- Ahh~!” Before I could even finish my sentence, my dear master had started thrusting rapidly, sending ripples of pleasure within me. “G-Gah~! H-Hah, m-master~! Y-Your cock i-is the best~!!” I wanted him to keep f**king me until I couldn’t walk anymore. I wanted him to do it to me and ONLY me. “F-F--k~! H-Hah~ K-Keep th-thrusting~ M-Mmmph~!”
 ''')


@client.command()
async def kok(ctx):
    await ctx.channel.send("AYO i'm out \n" + "https://cdn.discordapp.com/emojis/760673279442026537.png?v=1")


@client.command()
async def dog(ctx):
    await ctx.send(t.random("cute dogs"))


@client.command()
async def keria(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/735697266437914708/772087111901380608/image0.jpg?width=330&height=587")


@client.command()
async def soap(ctx):
    await ctx.channel.send("https://media.discordapp.net/attachments/735697266437914708/768055763112951838/image0.png?width=304&height=541")


@client.command()
async def spank(ctx):
    await ctx.channel.send("ahhh \n ahhhhh\nahhhhhhh\n senpaiiiii\nyameteeee\nahhhhhh\n i ....i love you daddy")
    await ctx.send(t.random('anime spank'))


@client.command()
async def brain(ctx):
    await ctx.channel.send("https://cdn.discordapp.com/emojis/765511732252114961.png?v=1")


@client.command()
async def gun(ctx):
    await ctx.channel.send("https://media1.giphy.com/media/69CKViM7D2PrG/200w.webp?cid=ecf05e47uky7d5szb6jovfs0aaonuxu6gme961p2zbn17np9&rid=200w.webp")


@client.command()
async def lurk(ctx):
    await ctx.channel.send(t.random('lurk'))


@client.command()
async def rick(ctx):
    await ctx.send("""We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
(Ooh) Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry""")


@client.command()
async def simp(ctx):
    await ctx.channel.send("Who do we simp for..........say it with me ｗｅｉｒｄｏｗｅｅｂ!! say it with me!!!!  ｗｅｉｒｄｏｗｅｅｂ.")
    await ctx.send(t.random("anime cheer"))


@client.command()
async def wall(ctx):
    await ctx.channel.send('https://media.discordapp.net/attachments/769442616697290772/770557090552610846/image0.gif')


@client.command()
async def light(ctx):
    await ctx.channel.send('https://media1.giphy.com/media/26uf4JMeuLpt0gpwY/200.gif')


@client.command()
async def cat(message):
    await message.send(t.random("cute cats"))


@client.command()
async def wut(ctx):
    await ctx.channel.send('https://cdn.discordapp.com/emojis/570964882497994753.gif?v=1')


@client.command()
async def spam(ctx):
    await ctx.channel.send('''i am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\ni am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n
i am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\ni am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\ni am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\ni am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\ni am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\ni am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n i am the spam aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n''')


@client.command()
async def chun1(message):

    await message.send(t.random("konosuba kazuma"))
    


@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

keep_alive()
client.run('NzQ1OTk3NDkwMTYzMDIzOTEy.Xz56TQ.Gk1Fg__N32W8mcGakT-tmuC2A-A')
