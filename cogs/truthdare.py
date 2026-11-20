import discord
from discord.ext import commands

import random
import json
from pathlib import Path

truthdares_file = Path('resources/truthdare.json')

class TruthDare(commands.Cog):

    def __init__(self, bot: discord.Bot):
        self.bot = bot

        file_content = json.loads(truthdares_file.read_text())
        self.truths: list[str] = file_content['truths']
        self.dares: list[str] = file_content['dares']

    class TruthDareButtonView(discord.ui.View):

        def __init__(self, truths: list[str], dares: list[str]):
            super().__init__(timeout=240)
            self.truths = truths
            self.dares = dares

        @discord.ui.button(label="Truth", style=discord.ButtonStyle.green)
        async def truth_button(
            self,
            button: discord.ui.Button[discord.ui.View],
            interaction: discord.Interaction,
        ):
            embed = discord.Embed(
                title="🤔 Truth",
                description=random.choice(self.truths),
                color=discord.Color.green(),
            )
            embed.set_footer(text="Answer honestly... or idk")

            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="Dare", style=discord.ButtonStyle.red)
        async def dare_button(
            self,
            button: discord.ui.Button[discord.ui.View],
            interaction: discord.Interaction,
        ):
            embed = discord.Embed(
                title="🗡️ Dare",
                description=random.choice(self.dares),
                color=discord.Color.red(),
            )
            embed.set_footer(text="Answer honestly... or idk")

            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="Random", style=discord.ButtonStyle.gray)
        async def random_button(
            self,
            button: discord.ui.Button[discord.ui.View],
            interaction: discord.Interaction,
        ):
            
            if random.choice([True, False]):

                embed = discord.Embed(
                    title="🗡️ Dare",
                    description=random.choice(self.dares),
                    color=discord.Color.red(),
                )
                embed.set_footer(text="Answer honestly... or idk")

            else:

                embed = discord.Embed(
                    title="🤔 Truth",
                    description=random.choice(self.truths),
                    color=discord.Color.green(),
                )
                embed.set_footer(text="Answer honestly... or idk")
            
            await interaction.response.edit_message(embed=embed, view=self)

    @discord.slash_command(
            name="truth",
            description="Asks a random 'truth' question."
    )
    async def truth(self, ctx: discord.ApplicationContext):

        embed = discord.Embed(
            title="🤔 Truth",
            description=random.choice(self.truths),
            color=discord.Color.green(),
        )
        embed.set_footer(text="Answer honestly... or idk")

        await ctx.respond(embed=embed, view=self.TruthDareButtonView(truths=self.truths, dares=self.dares))

    @discord.slash_command(
            name="dare",
            description="Gives a random 'dare' challenge" 
    )
    async def dare(self, ctx: discord.ApplicationContext):

        embed = discord.Embed(
            title="🗡️ Dare",
            description=random.choice(self.dares),
            color=discord.Color.red(),
        )
        embed.set_footer(text="Answer honestly... or idk")

        await ctx.respond(embed=embed, view=self.TruthDareButtonView(truths=self.truths, dares=self.dares))

    @discord.slash_command(
            name="truthdare",
            description="Picks a 'truth' or 'dare' randomly." 
    )
    async def truthordare(self, ctx: discord.ApplicationContext):

        if random.choice([True, False]):

            embed = discord.Embed(
                title="🗡️ Dare",
                description=random.choice(self.dares),
                color=discord.Color.red(),
            )
            embed.set_footer(text="Answer honestly... or idk")

        else:

            embed = discord.Embed(
                title="🤔 Truth",
                description=random.choice(self.truths),
                color=discord.Color.green(),
            )
            embed.set_footer(text="Answer honestly... or idk")
        
        await ctx.respond(embed=embed, view=self.TruthDareButtonView(truths=self.truths, dares=self.dares))

def setup(bot: discord.Bot):
    bot.add_cog(TruthDare(bot))