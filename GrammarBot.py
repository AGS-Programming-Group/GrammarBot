# GrammarBot v1.0

# Import external dependencies
import discord
import logging
from yaml import load
from sys import exit as sys_exit
from os import startfile

# Import internal dependencies
from src import talk, cli

# Constants
CONFIG = "./data/config.yaml"
PERMS = 3136

# Get arguments form the command line
args = cli.parse()

# Sets up the logging system
logging.basicConfig(level=logging.INFO if args.info else logging.ERROR)
log = logging.getLogger()

# Get setup information from config
try:
    with open(CONFIG, "r") as file:
        try:
            data = load(file.read())
            token = data["token"]
            owner_id = str(data["owner_id"])
        except:
            log.error("Parsing the config.yaml file. Please make sure that it is formatted correctly.")
except:
    log.error("Reading the config.yaml file. Make sure such a file exists.")
    sys_exit()

# Initalise the client
client = discord.Client()
reload = False

# Events

@client.event
async def on_ready():
    global client, log
    print("GrammarBot is ready!")
    id = client.user.id
    print("With the id ~", id)
    print("Link to add the bot to a server")
    print(f"  https://discordapp.com/api/oauth2/authorize?client_id={id}&scope=bot&permissions={PERMS}")
    servers = client.servers
    n = len(servers)
    if n != 0:
        print("On", n, "Servers =>")
        for s in servers:
            print(" ", s.name)
    else:
        print("On no servers")
    print("="*8)
    await client.change_presence(game=discord.Game(name="with the 1%ers", type=1))

@client.event
async def on_message(message):
    msg = message.content.lower()
    ch = message.channel
    if msg.startswith("!ping"):
        await client.send_message(ch, "Pong!")
    elif msg.startswith("!read"):
        await client.send_message(ch, talk.reading())
    elif msg.startswith("!eval"):
        await client.send_message(ch, talk.eval(message.content[5:]))
    elif msg.startswith("!quit"):
        if message.author.id == owner_id:
            print("Exit command called from Discord. Exiting.")
            await client.logout()


# Run the bot
client.run(args.token if (args.token is not None) else token)
# End the bot
sys_exit()
