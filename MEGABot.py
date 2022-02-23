#import DisneyBot
import os
from pyanswers import PyAnswers, FileMgmt
from uberduck import Uberduck
from netrunning import NetRun
import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv

# subbot init
load_dotenv()
# discord bot init
DISCORD_TOKEN = os.getenv("discord_token")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


# pyanswers init
pa = PyAnswers()
ud = Uberduck()
nr = NetRun()

class Mechanic():
    def __init__(self):
        self.name = "MEGABot"

    @bot.command(name='test-not-a-command', help='this is not a real command')
    async def cmd(ctx):
        await ctx.send('this is not a real command')

    @bot.command(name='echo', help='echo a message')
    async def cmd(ctx, *, msg):
        await ctx.send(msg)
    
class Tarot(Mechanic):
    @bot.command(name='tarot', help='tarot')
    async def cmd(ctx):
        await ctx.send('tarot')

class Skills(Mechanic):
    def __init__(self):
        self.jsonl_name = "skills.jsonl"
    @bot.command(name='skills', help='ask a question about the skills')
    async def cmd(ctx, *, msg):
        answer = pa.query_skills(msg)
        await ctx.send(answer)

class AutoRoll(Mechanic):
    jsonl_name = "autoroll.jsonl"
    voice = "jeremy-clarkson"

    def synth_voice(msg):
        return ud.synth_voice(msg, AutoRoll.voice)
    @bot.command(name='autoroll', help='Helps you figure out a roll')
    async def cmd(ctx, *, msg):
        answer = pa.query_autoroll(msg)
        await ctx.send(answer)
        voice_file = AutoRoll.synth_voice(answer)
        await ctx.send(file=discord.File(voice_file))

class Bernie(Mechanic):
    def __init__(self):
        self.jsonl_name = "bernie.jsonl"
    @bot.command(name='bernie', help='Send your local plug Bernie a text message')
    async def cmd(ctx, *, msg):
        answer = pa.query_bernie(msg)
        await ctx.send(answer)

class Falcone(Mechanic):
    jsonl_name = "falcone.jsonl"
    voice = "oblivion-guard"

    def synth_voice(msg):
        return ud.synth_voice(msg, Falcone.voice)

    @bot.command(name='falcone', help='Whats this guy up to?')
    async def cmd(ctx, *, msg):
        answer = pa.query_falcone(msg)
        await ctx.send(answer)
        voice_file = Falcone.synth_voice(answer)
        await ctx.send(file=discord.File(voice_file))

class NetRun(Mechanic):
    def __init__(self):
        self.jsonl_name = "netrunning.jsonl"
    @bot.command(name='netrun', help='Netrunning all Night Running')
    async def cmd(ctx, *, msg):
        all_cards = nr.get_all_cards()
        all_file_paths = nr.get_all_file_paths()
        for i in range(len(all_cards)):
            if msg in all_cards[i]:
                await ctx.send(file=discord.File(all_file_paths[i]))
                return

        # send it all if no match found
        for i in range(len(all_cards)):
            await ctx.send(file=discord.File(all_file_paths[i]))
            os.sleep(1)
        

class Menu(Mechanic):
    @bot.command(name='menu', help='menu')
    async def cmd(ctx):
        await ctx.send('menu')

 
