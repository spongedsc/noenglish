import discord
import dotenv
import json
import os
import requests
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="[[", intents=intents)
tree = client.tree
with open("silly_words.json") as f:
    words = (
        list(
            requests.get(
                "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"
            )
            .json()
            .keys()
        )
        + json.load(f)["words"]
    )  # only use of requests im so good at this stuff


@client.event
async def on_ready():
    for guild in client.guilds:
        # someone online said you shouldn't do this but fuck them
        await tree.sync(guild=guild)
    print("nya~ im ready!!!! :3 :3 :3 :3")


@client.event
async def on_message(msg: discord.Message):
    await client.process_commands(msg)
    if msg.channel.id != 1232165944168546346:
        return
    print("omg message :3 :3 :3 :3")
    if msg.author.bot:
        print("bot :(")
        return 0
    messagecontent = msg.content
    messagecontent = (
        input.casefold()
        .replace("'", "")
        .replace(",", "")
        .replace(".", "")
        .replace("!", "")
        .replace("?", "")
        .replace(";", "")
        .replace('"', "")
        .replace("0", "")
        .replace("1", "")
        .replace("2", "")
        .replace("3", "")
        .replace("4", "")
        .replace("5", "")
        .replace("6", "")
        .replace("7", "")
        .replace("8", "")
        .replace("9", "")
        .replace(":", "")
        .replace("/", " ")
        .replace("\\", "")
        .replace("(", "")
        .replace(")", "")
        .split()
    )
    # above code is so fucking great
    for word in messagecontent:
        print(word)
        print(type(words))
        if word.strip() in words:
            print("omg english D:<")
            # send message to gulag
            try:
                await msg.delete()
            except discord.Forbidden:
                await msg.channel.send(
                    "nyaaaa i dont have permission to delete messages!!!!! >///< >///< >///<"
                )  # great error message
            except Exception as e:
                await msg.channel.send(
                    f"python error!!!! >///< NERDS ONLY: ||{type(e)}: {e}||"
                )
            break  # :P


dotenv.load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))
