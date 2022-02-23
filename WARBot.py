from MEGABot import *
from BadCompany import *
import json
from automove_engine import *
from uberduck import Uberduck
import asyncio


# A bot used specifically for my 4th Corperate War Game

automove_engine = AutomoveEngine()
ud = Uberduck()
turn = 0
initiative_queue = ['']
    
@bot.command(name="corp_report", help="Prints out all the companies")
async def cmd(ctx):
    cw = CW()
    corps = cw.get_corps()
    for corp in corps:
        await ctx.send('|||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        await ctx.send('Company: ' + corp['name'])
        await ctx.send('Symbol: ' + corp['symbol'])
        await ctx.send('Company Head: ' + corp['company_head'])
        await ctx.send('Company HQ: ' + corp['hq'])
    await ctx.send('Each player can select one company to play with using the command "!select <company_symbol>"')


@bot.command(name="select", help="Let's a user select one company using the company's symbol. Example: !select BTEC")
async def cmd(ctx, *, msg):
    cw = CW()
    player_to_corp = cw.get_players()
    player = ctx.message.author.name
    if player in player_to_corp:
        await ctx.send('You already selected a company!')
        return
    corp = cw.get_corp_by_symbol(msg)
    if corp is not None:
        player_to_corp[player] = corp['symbol']
        await ctx.send('You have selected ' + corp['name'] + '!')
        await ctx.send('Company Background: ' + corp['background'])
    print(player_to_corp)
    cw.save_players(player_to_corp)

@bot.command(name="history", help="Check the current stock price from the companies")
async def cmd(ctx, *, msg):
    answer = pa.query_4CW_hist(msg)
    await ctx.send(answer)
    voice = "tom-hiddleston"
    voice_file = synth_voice(answer, voice)
    # have the bot play the voice file in the general voice channel
    await play(ctx, voice_file)
    

@bot.command(name="moves", help="Get the valid moves for the current player")
async def cmd(ctx):
    cw = CW()
    player = ctx.message.author.name
    moves = cw.player_to_moves(player)
    corp = cw.player_to_corp(player)
    # Make a string that will be sent to the user
    moves_string = '**MOVES for ' + corp + '**:\n'
    for move in moves:
        moves_string += '**' + move[0]+ '**' + '\n'
        moves_string += 'STAT: ' + move[2] + '\n'
        moves_string += move[1] + '\n'
        moves_string += '\n'
    await ctx.send(moves_string)

@bot.command(name="enable_ultimate_products", help="Enable ultimate products for all the players")
async def cmd(ctx):
    cw = CW()
    cw.enable_ultimate_products()

@bot.command(name="stats", help="Get the stats for the current player")
async def cmd(ctx):
    cw = CW()
    player = ctx.message.author.name
    corp = cw.player_to_corp(player)
    stats = cw.corp_to_stats(corp)
    stats_string = '**STATS for ' + corp + '**:\n'
    for stat in stats:
        stats_string += stat + ': ' + str(stats[stat]) + '\n'
    await ctx.send(stats_string)

def stock_ticker_msg(old_prices, new_prices):
    green = ':green_square:'
    red = ':red_square:'
    old_prices = json.loads(old_prices)
    new_prices = json.loads(new_prices)
   
    print(new_prices)
    ticker_msg = '**STOCK TICKER**\n'
    for ticker in new_prices:
        if old_prices[ticker] > new_prices[ticker]:
            ticker_msg += ticker + ': ' + red + str(new_prices[ticker]) + '\n'
        elif old_prices[ticker] < new_prices[ticker]:
            ticker_msg += ticker + ': ' + green + str(new_prices[ticker]) + '\n'
        else:
            ticker_msg += ticker + ': ' + str(new_prices[ticker]) + '\n'
    return ticker_msg

@bot.command(name="stocks", help="Update the stocks after the results of a move")
async def cmd(ctx, *, msg):
    cw = CW()
    # get the stock history
    stock_history = cw.get_stock_history()
    # get the last item in the stock_history list
    current_prices = stock_history[-1]
    
    # if the msg is empty, just print the current prices, with the item befor the last item
    if msg == '':
        await ctx.send(stock_ticker_msg(stock_history[-2], current_prices))
        return
    # use pa to query_stocks
    new_prices = pa.query_stocks(msg, current_prices)
    # add the new prices to the stock_history list
    stock_history.append(new_prices)
    # send the new prices to the user
    ticker_msg = stock_ticker_msg(current_prices, new_prices)
    await ctx.send(ticker_msg)
    # save the new stock_history list
    cw.save_stock_history(stock_history)

@bot.command(name="sxx", help="Get the corperate synergy SXX stats")
async def cmd(ctx):
    await ctx.send("SXX represents your corporate synergy with another corperation. During a corporation's move, you can help or hinder the other corporation by adding or subtracting SXX to your move. SXX can be positive or negative. Positve can only help, negative can only hurt.")
    cw = CW()
    player = ctx.message.author.name
    corp = cw.player_to_corp(player)
    sxx = cw.corp_to_sxx(corp)
    sxx_string = '**SXX for ' + corp + '**:\n'
    for s in sxx:
        sxx_string += "S(" + s[0] +"):" + str(s[1])+ '\n'
    await ctx.send(sxx_string)

@bot.command(name="slogan", help="Play a slogan")
async def cmd(ctx, *, msg):
    # get the corp name of the player
    cw = CW()
    player = ctx.message.author.name
    corp = cw.player_to_corp(player)
    # get the voice for that corp
    voice = cw.corp_to_voice(corp)
    # synthesize the slogan from the msg
    slogan_audio = synth_voice(msg, voice)
    # have the bot play the voice file in the general voice channel
    await play(ctx, slogan_audio)

@bot.command(name="rules", help="Get some rules")
async def cmd(ctx):
    rules = "1. To start, you can only play one move per turn.\n"
    rules += "2. To make a move, tell a little bit of story about how you make your move first.\n"
    rules += "3. When you make a move, roll 2d6 + stat. On a 10+ you sucseed\n"
    rules += "4. Before you roll, another can choose to help or hinder. \n"
    rules += "5. Only one corp can help, and another can hidner. They will add their sxx with you to your roll.\n"
    rules += "6. Use !moves to check your moves\n"
    rules += "7. Use !stats to check your stats\n"
    rules += "8. Use !sxx to check your SXX\n"
    rules += "9. Tonight we are telling a story and playing a game about it, so have fun with it.\n"
    await ctx.send(rules)



def synth_voice(msg, voice):
        return ud.synth_voice(msg, voice)

async def play(ctx, voice_file):
    # get the general voice channel
    voice_channel = ctx.message.author.voice.channel
    # join the voice channel
    vc = await voice_channel.connect()
    # play the voice file
    vc.play(discord.FFmpegPCMAudio(voice_file))
    # wait for the voice file to finish playing
    while vc.is_playing():
        await asyncio.sleep(1)
    # disconnect from the voice channel
    await vc.disconnect()

if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)

