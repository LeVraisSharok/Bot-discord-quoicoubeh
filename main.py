import discord
from discord.ext import commands

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Discord
bot_token = 'YOUR_BOT_TOKEN'

# Remplacez 'YOUR_TWITCH_STREAM_URL' par l'URL de votre stream Twitch
twitch_stream_url = 'https://www.twitch.tv/exemple'

# Définissez les intents que votre bot utilisera
intents = discord.Intents.default()
intents.message_content = True  # Permet de recevoir les événements de messages

# Créez une instance du bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement de démarrage du bot
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Définir le statut du bot en tant que "streaming" avec l'URL du stream Twitch
    await bot.change_presence(activity=discord.Streaming(name="Name", url=twitch_stream_url))

# Événement pour répondre automatiquement aux messages contenant 'quoi', 'quoicoubeh', etc.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Liste des mots que le bot cherchera dans les messages pour répondre
    mots_cles = ['quoi', 'quoicoubeh']

    # Vérifie si le message de l'utilisateur contient un mot clé
    if any(mot in message.content.lower() for mot in mots_cles):
        # Répond avec le message souhaité
        await message.channel.send("quoicoubeh")

    # N'oubliez pas de traiter les autres événements comme d'habitude
    await bot.process_commands(message)

# Lancer le bot avec le token spécifié
bot.run(bot_token)
