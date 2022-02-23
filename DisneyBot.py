#Dis Ney
import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl
import json
import random
import time

#######################################################################################
################################CONFIG#################################################
#######################################################################################
current_session = 'Finale.json'
tarot_session = 'tarot.json'
def load_session():
    f = open(current_session)
    session_json = json.load(f)
    return session_json

def load_tarot():
    f = open(tarot_session)
    session_json = json.load(f)
    return session_json




@bot.command(name = 'teaser', help = "Prints details of Author")
async def teaser(ctx) :
    await ctx.send('Disney')
    await ctx.send(file=discord.File('Disney.png'))
    await ctx.send(file=discord.File('teaser.wav'))
    await ctx.send('Transcript:')
    await ctx.send('\'Our greatest natural resource is the minds of our children. He alone! who owns the youth! gains the future...\'')





def get_bot_channel():
    for channel in guild.text_channels:
        if str(channel) == "bot_channel" :
            return channel
    print("error getting bot_channel)")

def get_names(session):
    charecters = session['charecters']
    names = [i["name"] for i in charecters]
    return names

def get_voice_files(session, charecter):
    voice_files = charecter['voice_files']
    return voice_files

def get_voice_transcripts(session, charecter):
    voice_transcripts = charecter['voice_transcripts']
    return voice_transcripts

async def test_bot_channel_charecter_names():
    channel = get_bot_channel()   
    session = load_session()   
    names = get_names(session)
    await channel.send('Charecter name test')
    for name in names:
        await channel.send(name)


#######################################################################################
################################!commands##############################################
#######################################################################################

class cmd():

    ###CMD HELPERS###
    def get_general_channel():
        for channel in guild.text_channels:
            if str(channel) == "general" :
                return channel
        print("error getting general channel)")

    def menu():
        

@bot.command(name = 'name_test', help = "Prints out names of charecters in a session")
async def name_test(ctx) :
    session = load_session()   
    names = get_names(session)
    await ctx.send('Charecter name test')
    for name in names:
        await ctx.send(name)





async def voice(ctx, voice_file_path):
    await play(ctx, voice_file_path)
    


    

@bot.command(name = 'pin', help = "session scripting power!")
async def pin(ctx) :
    await ctx.send("bot pinned")
    await join(ctx)
    session = load_session()
    while(True):
        names = get_names(session)
        print("Select a charecter")
        for i in range(len(names)):
            name = names[i]
            print(str(i)+") "+name)
        name_int = int(input())
        if name_int == 99:
            continue
        name = names[name_int]
        charecter = session["charecters"][name_int]


        voice_files = get_voice_files(session, charecter)
        voice_transcripts = get_voice_transcripts(session, charecter)

        print("Select a voice line")
        for i in range(len(voice_files)):
            print(str(i)+")   "+ voice_files[i])
            print("Transcript: "+ voice_transcripts[i])

        voice_int = int(input())
        if voice_int == 99:
            continue

        voice_file = voice_files[voice_int]
        voice_transcript = voice_transcripts[voice_int]

        await say(ctx, session, charecter, voice_file, voice_transcript)


###TAROT###
tarot_deck_ints = [21, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
@bot.command(name = 'tarot', help = "Tempt fate!")
async def tarot(ctx) :
    session = load_tarot()
    cmd = tarot_cmd()
    random.shuffle(tarot_deck_ints)
    await ctx.send("Now let's draw a card")
    time.sleep(1)
    image, name, effect, flavor = cmd.pick_card(session)
    await cmd.say_tarot(ctx, session, image, name, effect, flavor)
    random.shuffle(tarot_deck_ints)

class tarot_cmd:
    def pick_card(session):
        card_int = tarot_deck_ints.pop()
        image = session["images"][card_int]
        name = session["names"][card_int]
        effect = session["effects"][card_int]
        flavor = session["flavor"][card_int]
        return image,name,effect,flavor

    async def say_tarot(ctx, session, image, name, effect, flavor):
        folder_path = session['prep_folder_path']
        await ctx.send(name)
        image_file_path = folder_path + '\\' + image
        await ctx.send(file=discord.File(image_file_path))
        time.sleep(1)
        await ctx.send(flavor)
        time.sleep(3)
        await ctx.send(effect)
    
#######################################################################################
################################DISCORD API############################################
#######################################################################################



######DISCORD CONFIG#####
load_dotenv()
# Get the API token from the .env file.
DISCORD_TOKEN = os.getenv("discord_token")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

#####DISCORD FUNCTIONS#####
async def say(ctx, session, charecter, voice_file, voice_transcript):
    folder_path = session['prep_folder_path']

    if 'name' in charecter:
        await ctx.send(charecter['name'])

    if 'image' in charecter:
        image_file_path = folder_path + '\\' + charecter['name'] +'\\'+ charecter['image']
        await ctx.send(file=discord.File(image_file_path)) 

    if "voice_files" in charecter:
        voice_file_path = folder_path + '\\' + charecter['name'] +'\\'+ voice_file
        print("Saying "+ voice_file_path)
        await ctx.send(file=discord.File(voice_file_path))
        await ctx.send("Transcript:\n"+voice_transcript)
        await voice(ctx, voice_file_path)


if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)

