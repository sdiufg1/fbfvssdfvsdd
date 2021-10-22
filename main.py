from asyncio.runners import run
from re import L
import discord
from discord import *
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import command
from datetime import *
from datetime import time
from time import *
import random
import asyncio
import aiohttp
from discord.utils import get
from discord.ext.commands import check
import os

client = commands.Bot(command_prefix = "+")
client.remove_command("help")

heures = datetime.now().strftime('%H:%M:%S')

@client.event
async def on_ready():
    global heures
    print(f"----------------------------------------------------------------------\nenregistrer en temps que {client.user.name} Voici l'id de mon createur:\n 658316777981345792 \nvoici mon id:\n{client.user.id}\ncette session a etais ouverte a {heures}\n----------------------------------------------------------------------")
    await client.change_presence(activity = discord.Game("Call of duty Mobile"))



@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("La commande que tu a tapé n'existe pas.")
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Ta pas oublier un truc la ?")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Ta pas les permission d'uttiliser cette commande.")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send("vous ne pouvez pas utilisez cette commande.")
	if isinstance(error.original, discord.Forbidden):
		await ctx.send("Je n'ai pas les permissions nécéssaires pour faire cette commmande.")



# Debut de la commande shutdown
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Je m'arrete aurevoir ^^")
    await ctx.bot.logout()

#Fin de la commande shutdown



# Debut de la commande pour le test de ping.

@client.command()
async def ping(ctx):
    await ctx.send(f"Ma lantence est de `{round(client.latency * 1000)}` ms")

# Fin de la commande pour le test de ping



# Début de la commande snipe (Pour reccuperer les msg supprimer.).

snipe_message_content = None
snipe_message_author = None
snipe_message_tag = None
@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_tag
    # Les variables en dehors d'une fonction doivent être déclarées comme "global" pour être modifiées.

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_tag = message.author.discriminator


newUserDMMessage = "Bienvenue!"


@client.command(pass_context=True)
@commands.has_any_role("Rôle Snipe")
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("Il n'a rien a snipe pour le moment :eyes:.")
    else:
        embed = discord.Embed(color = 0x4dce46)
        embed.set_footer(text=f"Command send by {message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
        embed.set_author(name= "YYT BOT")
        embed.add_field(name = f"J'ai trouver un message supprimer de {snipe_message_author}#{snipe_message_tag} le voici: ", value = f"\n{snipe_message_content}", inline = False)
        embed.set_thumbnail(url = "https://c.tenor.com/_DOAnKatq7EAAAAM/cod-chost.gif")
        await message.channel.send(embed=embed)
        return

# Fin du code de la commande snipe.

# Debut de la commande pour le help.
@client.command()
async def help(ctx, message = None):
    if message == "snipe":
        embed=discord.Embed(title="Snipe Command", description="Cette commande sert a reccuperer le dernier message supprimer par un uttilisateur", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+snipe`", inline=True)
        await ctx.send(embed=embed)
    if message == None:
        embed = discord.Embed()
        embed=discord.Embed(title="Liste des commandes 🍏", description="**Prefix** `+`\n**Plus d'information** `+help <command>`", color=0x3ee378)
        embed.set_thumbnail(url="https://c.tenor.com/_DOAnKatq7EAAAAM/cod-chost.gif")
        embed.add_field(name="🤷‍♂️・User", value="`help` `ping` `pp` `say`", inline=False)
        embed.add_field(name="👌・Mod", value="`snipe` `nuke` `mute` `voicemove` `lock` `unlock`", inline=False)
        embed.add_field(name="🎉・Fun", value="`emote` `chinese` `coinflip` `cat` `hug` `dog` `duck`", inline=False)
        embed.set_footer(text=f"Commande envoyer par {ctx.author} à {heures}")
        await ctx.send(embed=embed)
    if message == "ping":
        embed=discord.Embed(title="Ping Command", description="Cette commande sert a regarder ma latence ^^", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+ping`", inline=True)
        await ctx.send(embed=embed)
    if message == "pp":
        embed=discord.Embed(title="Picture Pick Command", description="Cette commande sert a reccuperer la photo de profil d'un uttilisateur", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+pp {<id>},{<mention>},{<pseudo>}`", inline=True)
        await ctx.send(embed=embed)
    if message == "nuke":
        embed=discord.Embed(title="Nuke Command", description="Cette commande sert a supprimer et recrée un channel faite attention !", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+nuke` (dans le bon channel)", inline=True)
        await ctx.send(embed=embed)
    if message == "say":
        embed=discord.Embed(title="Say Command", description="Je répète juste ce que tu a écris !", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+say + <str>`", inline=True)
        await ctx.send(embed=embed)
    if message == "emote":
        embed=discord.Embed(title="Emote Command", description="Je fais un emoji pour toi meme animé sans nitro !", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+emote + <str>`", inline=True)
        await ctx.send(embed=embed)
    if message == "chinese":
        embed=discord.Embed(title="Chinese Command", description="Cette commande permet de faire des caractere chinois sur des mot francais", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+chinese + <str>`", inline=True)
        await ctx.send(embed=embed)
    if message == "coinflip":
        embed=discord.Embed(title="Coinflip Command", description="Cette commande permet de faire un pile ou face au hasard", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+coinflip + <rdm>`", inline=True)
        await ctx.send(embed=embed)
    if message == "mute":
        embed=discord.Embed(title="Mute Command", description="Cette commande permet de mute un uttilisateur", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+mute + <mention,id,name>` optional `<raison>`", inline=True)
        await ctx.send(embed=embed)
    if message == "cat":
        embed=discord.Embed(title="Cat Command", description="Cette commande permet d'avoir un chat au hasard !", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+cat", inline=True)
        await ctx.send(embed=embed)
    if message == "dog":
        embed=discord.Embed(title="Dog Command", description="Cette commande permet d'avoir un dog au hasard !", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+dog", inline=True)
        await ctx.send(embed=embed)
    if message == "duck":
        embed=discord.Embed(title="Duck Command", description="Cette commande permet d'avoir un Canard au hasard !", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+duck", inline=True)
        await ctx.send(embed=embed)
    if message == "hug":
        embed=discord.Embed(title="Hug Command", description="Cette commande permet de faire un calin a qu'elle q'un ou au bot", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+hug` optional `<mention,id,name>`", inline=True)
        await ctx.send(embed=embed)
    if message == "lock":
        embed=discord.Embed(title="Lock Command", description="Cette commande permet de bloquer un salon", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+voicemove`", inline=True)
        await ctx.send(embed=embed)
    if message == "unlock":
        embed=discord.Embed(title="Unlock Command", description="Cette commande permet de debloquer un salon", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+unlock`", inline=True)
        await ctx.send(embed=embed)
    if message == "voicemove":
        embed=discord.Embed(title="VoiceMove Command", description="Cette commande permet de deplacer tout les uttilisateur d'un channel vocal a un autre via un id", color=0x07caf3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/871526418578825226.png?v=1")
        embed.add_field(name="uttilisation:", value="`+voicemove` + `<id VOCAL_CHANNEL>`", inline=True)
        await ctx.send(embed=embed)


# Fin de la commande help

# Debut de la commande pp

@client.command()
async def pp(ctx, *,  avamember : discord.Member=None):
    if not avamember:
        url = ctx.message.author
        userAvatar = url.avatar_url
        await ctx.send(userAvatar)
    if avamember:
            userAvatarUrl = avamember.avatar_url
            await ctx.send(userAvatarUrl)

# Fin de la commande pp

# Debut de la commande say

@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

# Fin de la commande say

# Debut de la commande emote

@client.command()
async def emote(ctx, text = None):
    id = ctx.author.id
    if text != (None):
        message = ctx.message
        await message.delete()
        emoji = discord.utils.get(client.emojis, name=f"{text}")
        await ctx.send(emoji)
        await ctx.send(f"<@{id}>")
    else:
        await ctx.send("Tu doit taper un nom d'emote !")

# Fin de la commande emote

# Debut de la commande chinese
@client.command()
async def chinese(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))
# Fin de la commande chinese

# Debut de la commande mute

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

@client.command()
@commands.has_any_role("PermChat")
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison a été renseigné"):
    role = discord.utils.find(lambda r: r.name == 'Muted', ctx.message.guild.roles)
    if role in member.roles:
        await ctx.send("L'user mentionner est deja mute !")
    else:
        mutedRole = await getMutedRole(ctx)
        await member.add_roles(mutedRole, reason = reason)
        await ctx.send(f"{member.mention} a été mute ! raison = {reason}")

# Fin de la commande mute

# Debut de la commande unmute

@client.command()
@commands.has_any_role("PermChat")
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison a été renseigné"):
    role = discord.utils.find(lambda r: r.name == 'Muted', ctx.message.guild.roles)
    if role in member.roles:
        mutedRole = await getMutedRole(ctx)
        await member.remove_roles(mutedRole, reason = reason)
        await ctx.send(f"{member.mention} a été unmute ! pour la raison {reason}")
    else:
        await ctx.send("L'user mentionner na pas de mute enregistrer !")

# Fin de la commande unmute

# Debut de la commande coinsflip

coinsides = ["Pile", "Face"]
@client.command()
async def coinflip(ctx):
    global coinsides
    await ctx.send(f"**{ctx.author.name}** Tourne la piece est tombe sur **{random.choice(coinsides)}**!")

# Fin de la commande coinflip

 #Debut de la commande cat

@client.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get("https://some-random-api.ml/img/cat")
        catjson = await request.json()
        embed = discord.Embed(title="CHAT !", color = discord.Color.random())
        embed.set_image(url = catjson["link"])
        await ctx.send(embed=embed)

# Fin de la commande cat

# Debut de la commande hug

@client.command()
async def hug(ctx, text : discord.Member = None):
    async with aiohttp.ClientSession() as session:
        if text == None:
            heures = datetime.now().strftime('%H:%M:%S')
            request = await session.get("https://some-random-api.ml/animu/hug")
            hugjson = await request.json()
            embed = discord.Embed(title=f"{ctx.author.name} fais un calin a YYT BOT c trop mignooon 💕", color = discord.Color.random())
            embed.set_image(url = hugjson["link"])
            embed.set_footer(text=f"Commande envoyer par {ctx.author.name} à {heures}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            heures = datetime.now().strftime('%H:%M:%S')
            request = await session.get("https://some-random-api.ml/animu/hug")
            hugjson = await request.json()
            embed = discord.Embed(title=f"{ctx.author.name} fais un calin a {text.display_name} c trop mignooon 💕", color = discord.Color.random())
            embed.set_image(url = hugjson["link"])
            embed.set_footer(text=f"Commande envoyer par {ctx.author.name} à {heures}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)

# Fin de la commande hug

# Debut de la commande dog

@client.command()
async def dog(ctx, text : discord.Member = None):
    async with aiohttp.ClientSession() as session:
        if text == None:
            heures = datetime.now().strftime('%H:%M:%S')
            request = await session.get("https://some-random-api.ml/animal/dog")
            dogjson = await request.json()
            embed = discord.Embed(title="CHIEN !", color = discord.Color.random())
            embed.set_image(url = dogjson["image"])
            embed.set_footer(text=f"Commande envoyer par {ctx.author.name} à {heures}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)

# Fin de la commande dog

# Debut de la commande duck

@client.command()
async def duck(ctx, text : discord.Member = None):
    async with aiohttp.ClientSession() as session:
        if text == None:
            heures = datetime.now().strftime('%H:%M:%S')
            request = await session.get("https://random-d.uk/api/v1/random")
            duckjson = await request.json()
            embed = discord.Embed(title="CANARD !", color = discord.Color.random())
            embed.set_image(url = duckjson["url"])
            embed.set_footer(text=f"Commande envoyer par {ctx.author.name} à {heures}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)


# Debut de la commande nuke

letter = ("💌")
@client.command()
@commands.has_any_role("nuke")
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel is None: 
        channel = ctx.channel
        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        msg = await ctx.send(f"Tu a besoin de m'envoyer un mot de passe en mp pour nuke {channel}!")
        await msg.add_reaction(emoji = letter)
        await ctx.author.send("Juste ici pour le mot de passe ^^")
    def check(m):
        return ctx.author == m.author and isinstance(m.channel, discord.DMChannel)
    try:
        test = await client.wait_for('message', check=check, timeout=60)
        if test.content == "lkytgrde":
            await ctx.author.send("Bon mot de passe jfais peter le salon.")
            await ctx.send("Le mot de passe est le bon !")
        if test.content != "lkytgrde":
            await ctx.author.send("Mauvais mot de passe recommence la commande !")
            await ctx.send("Le mot de passe qui ma etais envoyer en mp est pas le bon")
            return False
        if nuke_channel is not None:
            pos = ctx.channel.position
            await ctx.channel.delete()
            channel = await ctx.channel.clone()
            await channel.edit(position=pos)
            await channel.send("Le channel a bien etais nuke !")
            await channel.send("https://i.makeagif.com/media/4-16-2016/1hdns9.gif")
    except asyncio.TimeoutError:
        await ctx.author.send("Le temps est ecouler snif")
        await ctx.send("Le mot de passe n'a pas etais donner a temps")

# Fin de la commande nuke

# Debut de la commande voicemove

def in_voice_channel():  # check pour voir si le channel ctx existe
    def predicate(ctx):
        return ctx.author.voice and ctx.author.voice.channel
    return check(predicate)

@in_voice_channel()
@client.command()
@commands.has_any_role("move")
async def voicemove(ctx, *, channel : discord.VoiceChannel):
    for members in ctx.author.voice.channel.members:
        await members.move_to(channel)
    youpi = discord.utils.get(client.emojis, name="youpi")
    await ctx.send(f"Tous les membre ont etais deplacer aves succes {youpi}")

# Fin de la commande voicemove

# Debut de la commande lock

@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    id = ctx.author.id
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"Channel Bloquer par <@{id}>")

# Fin de la commande lock

# Debut de la commande unlock

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    id = ctx.author.id
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"Channel Debloquer par <@{id}>")

# fin de la commande unlock

# Debut de la commande serverinfo

@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  owner = str(ctx.guild.owner_id)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  textChannel = len(ctx.guild.text_channels)
  voiceChannel=len(ctx.guild.voice_channels)
  role_nbr=len(ctx.guild.roles)
  icon = str(ctx.guild.icon_url)
  heures = datetime.now().strftime('%H:%M:%S')

  embed = discord.Embed(
      title=f"Information du serveur: **{name}** <a:youpi:880128555810435152>",
      description="Je ne c pas quoi mettre ici mdr",
      color=discord.Color.green()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Createur", value=(f"<@{owner}>"), inline=True)
  embed.add_field(name="Id du serveur", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Nombre de Membres", value=memberCount, inline=False)
  embed.add_field(name="Nombre de Channels Textuels", value=textChannel, inline=False)
  embed.add_field(name="Nombre de Channels Vocals", value=voiceChannel, inline=False)
  embed.add_field(name="Nombre de Roles", value=role_nbr,inline=False)
  embed.set_footer(text=f"Commande Envoyée par {ctx.author.name} à {heures}", icon_url = ctx.author.avatar_url)
  await ctx.send(embed=embed)

# Fin de la commande serverinfo

client.run(os.environ['token'])
