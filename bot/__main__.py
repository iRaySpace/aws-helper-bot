import os
import discord 
from discord.ext import commands

from .whitelist import update_whitelist_rule


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author}!')


@bot.command(name='whitelist')
async def whitelist(ctx, ip_address):
    description = ctx.author.name
    update_whitelist_rule(description, ip_address)
    await ctx.send(f'IP Address {ip_address} has been whitelisted!')


def main():
    bot.run(os.environ.get('DISCORD_BOT_TOKEN'))


if __name__ == '__main__':
    main()
