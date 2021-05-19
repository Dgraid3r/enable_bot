# bot.py
#enable bot token
#
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
from keep_alive import keep_alive

load_dotenv()
#loads the .env file in the same directory
keep_alive()
TOKEN = os.getenv('DISCORD_TOKEN')
#connection token

#client = discord.Client()
#we can use client as an alternative to bot; but bot is built off of client so
#bot is just easier to use

bot = commands.Bot(command_prefix = '$')

#startup confirmation connection event
@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')


#response to a key phrase event
@bot.event
async def on_message(message):
    if message.content == 'dan':
        await message.channel.send("Kuang Feng Zhi Li!")
    elif message.content == 'danz':
        await message.channel.send("Kuang Feng Zhi Li!")
    elif message.content == 'g spow':
        await message.channel.send("Dgraider")
    elif message.content == 'dgraider':
        await message.channel.send("G Spow")
    elif message.content == 'youtube':
        await message.channel.send("https://www.youtube.com/channel/UCQLTAfUsBPB8XCW0STltqZQ")
    elif message.content == 'twitch':
        await message.channel.send("https://www.twitch.tv/dgraider")
    elif message.content == 'enable':
        await message.channel.send("enable activated")

        
    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    Channel = bot.get_channel('YOUR_CHANNEL_ID')
    if reaction.message.channel.id != Channel:
        return
    if reaction.emoji == "🏃":
      Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
      await bot.add_roles(Role)

#adds a role with the command $add _role_
@bot.command(pass_context = True)
async def add(ctx, role: discord.Role, member: discord.Member=None):
    member = ctx.message.author
    await member.add_roles(role)

#leaves a role with the command $leave _role_
@bot.command(pass_context = True)
async def leave(ctx, role: discord.Role, member: discord.Member = None):
    member = ctx.message.author
    await member.remove_roles(role)

#sends a random picture of a cat
@bot.command(pass_context = True)
async def cat(message):
    response = requests.get('https://aws.random.cat/meow')
    temp = response.json()
    await message.channel.send(temp['file'])

    
    
#welcome/leaver messages
@bot.event
async def on_member_join(member):
    await bot.send_message(member, "Welcome to the server!")
    await bot.send_message(discord.Object(id = 'CHANNELID'), 'Welcome! ')

@bot.event
async def on_member_remove(member):
    await bot.send_message(discord.Object(id = 'CHANNELID'), '**' + member.mention + '** just left.')
    

bot.run(TOKEN)
