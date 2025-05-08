import os
import discord 
from discord.ext import commands

from .whitelist import update_whitelist_rule
from .instances import find_all_instances
from .utils import get_tag_value


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author}!')


@bot.command(name='whitelist')
async def whitelist(ctx, ip_address, name=None):
    description = ctx.author.name
    if name:
        description = name
    update_whitelist_rule(description, ip_address)
    await ctx.send(f'IP Address {ip_address} has been whitelisted!')


@bot.command(name='instances')
async def instances(ctx, query):
    instances = find_all_instances(query)

    message_lines = []
    for instance in instances:
        instance_name = get_tag_value(instance.tags, 'Name')
        message_lines.append(
            f"**Name**: {instance_name}\n"
            f"State: {instance.state.get('Name')}\n"
            f"Instance Id: {instance.id}\n"
            f"Private IP: {instance.private_ip_address}\n"
        )

    message = "\n".join(message_lines)
    if len(message) > 2000:
        await ctx.send('The response is too large. Please query for a smaller dataset.')
        return

    await ctx.send(message)


def main():
    bot.run(os.environ.get('DISCORD_BOT_TOKEN'))


if __name__ == '__main__':
    main()
