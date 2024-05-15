import discord
from discord.ext import commands
import re
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
    people = ['Aidan', 'Oscar', 'Xavier', 'Mitchel', 'Guest', 'Peter', 'Ben', 'Cooper']
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

    @bot.command()
    async def chips(ctx):
        view = ChipView()
        await ctx.send(view=view)

        await view.wait()
        if view.buyinyn[0] == 'Y':
            await ctx.send("How many buyins")
            msg = await bot.wait_for(
                "message",
                timeout=60,
                check=lambda message: message.author == ctx.author and message.channel == ctx.channel
            )
            view.buyins = msg.content
            ctx.send("Buyins recorded")
        if view.revbuyyn[0] == 'Y':
            await ctx.send("How many revbuys")
            msg = await bot.wait_for(
                "message",
                timeout=60,
                check=lambda message: message.author == ctx.author and message.channel == ctx.channel
            )
            ctx.send("Revbuys recorded")
            view.revbuys = msg.content
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
                    ctx.send("Balance recorded")
                    break
                else:
                    ctx.send("Invalid input")
            except:
                ctx.send("Invalid input")
        
        results = {"name": view.name, "buyinyn": view.buyinyn, "revbuyyn": view.revbuyyn, "buyins": view.buyins, "revbuys": view.revbuys, "balance": view.balance}
        print([int(i) for i in [item for item in results.values()][-3:-1]])
        await ctx.send(f"{results}")
 
    bot.run(token=TOKEN)
run()