import discord
from discord.ext import commands
import re
from dotenv import load_dotenv
import os
import bot_input
from data import *
import sqlite3 # This is being imported for error handling

# Loads discord token from .env
# .env has DISCORD_TOKEN set to the actual discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


'''
How the following three classes work is kind of scuffed
Essentially the program starts down in run() where the ChipView() class is called
The ChipView class then asks who is playing then calls the BuyinSelect class which 
further calls the respond_to_buyinyn function in ChipView
Then respond_to_buyinyn calls the RevbuySelect class which further calls respond_to_revbuyyn which finally halts
'''
class BuyinSelect(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label=opt) for opt in ["Y","N"]]
        super().__init__(options=options, placeholder="Did you buyin?")
    async def callback(self, interaction:discord.Interaction):
        await self.view.respond_to_buyinyn(interaction, self.values)

class RevbuySelect(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label=opt) for opt in ["Y","N"]]
        super().__init__(options=options, placeholder="Did you revbuy?")
    async def callback(self, interaction:discord.Interaction):
        await self.view.respond_to_revbuyyn(interaction, self.values)

class ChipView(discord.ui.View):
    people = [p.name for p in players]
    name = None
    buyinyn = None
    revbuyyn = None
    buyins = 0
    revbuys = 0
    balance = ""

    @discord.ui.select(
        placeholder = "Name?",
        options = [discord.SelectOption(label=person) for person in people]
    )
    async def select_player(self, interaction:discord.Interaction, select_item:discord.ui.Select):
        self.name = select_item.values
        self.children[0].disabled=True
        buyin_select = BuyinSelect()
        self.add_item(buyin_select)
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def respond_to_buyinyn(self, interaction: discord.Interaction, choices):
        self.buyinyn = choices
        self.children[1].disabled=True
        revbuy_select = RevbuySelect()
        self.add_item(revbuy_select)
        await interaction.message.edit(view=self)
        await interaction.response.defer()
    async def respond_to_revbuyyn(self,interaction: discord.Interaction, choices):
        self.revbuyyn = choices
        self.children[2].disabled = True
        await interaction.message.edit(view=self)
        await interaction.response.defer()
        self.stop()
    
def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)
    '''
    The first section of this function just calls the classes mentioned above but after that it then asks for how many buyins,
    revbuys and finally what the players actual balance is in the form of x W x R x B x G x Bl
    finally a dictionary of the values (which are countained in the chipview class still) given by this are outputted
    Actual processing within the main poker program has not been implemented which is currently priority #1
    '''
    @bot.command()
    async def chips(ctx):
        view = ChipView()
        await ctx.send(view=view)

        await view.wait()
        if view.buyinyn[0] == 'Y':
            while True:
                await ctx.send("How many buyins")
                msg = await bot.wait_for(
                    "message",
                    timeout=60,
                    check=lambda message: message.author == ctx.author and message.channel == ctx.channel
                )
                try:
                    if int(msg.content):
                        view.buyins = msg.content
                        await ctx.send("Buyins recorded")
                        break
                except Exception as e:
                    await ctx.send("Invalid input")
                    print(e)

        if view.revbuyyn[0] == 'Y':
            while True:
                await ctx.send("How many revbuys")
                msg = await bot.wait_for(
                    "message",
                    timeout=60,
                    check=lambda message: message.author == ctx.author and message.channel == ctx.channel
                )
                try:
                    if int(msg.content):
                        await ctx.send("Revbuys recorded")
                        view.revbuys = msg.content
                        break
                except Exception as e:
                    await ctx.send("Invalid input")
                    print(e)
        while True:
            await ctx.send("Input your balance")
            msg = await bot.wait_for(
                "message",
                timeout = 300,
                check=lambda message: message.author == ctx.author and message.channel == ctx.channel
            )
            try:
                if re.match(r"(\d+\s+?W)+?\s+?(\d+\s+?R)+?\s+?(\d+\s+?B)+?\s+?(\d+\s+?G)+?\s+?(\d+\s+?B)",msg.content) is not None:
                    view.balance = msg.content
                    await ctx.send("Balance recorded")
                    break
                else:
                    await ctx.send("Invalid input")
            except:
                await ctx.send("Invalid input")
        
        results = {"name": view.name, "buyinyn": view.buyinyn, "revbuyyn": view.revbuyyn, "buyins": view.buyins, "revbuys": view.revbuys, "balance": view.balance}
        returned_tple = bot_input.process_results(results)
        if returned_tple[0] is not None: await ctx.send(f"{returned_tple[0]}") 
        if returned_tple[1] is not None: await ctx.send(f"{returned_tple[1]}")
    @commands.has_role("Chip Merger")
    @bot.command()
    async def merge(ctx):
        try:
            bot_input.merge_results()
            await ctx.send("Sucess, the changes have been merged into the database")
        except sqlite3.OperationalError:
            await ctx.send("No changes have been made, not merged")
    @commands.has_role("Chip Merger")
    @bot.command()
    async def plz_fix(ctx):
        bot_input.plz_fix()
        await ctx.send("Temp.json has been reset")
    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send(error)
    bot.run(token=TOKEN)
run()