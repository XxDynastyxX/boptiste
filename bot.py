import discord
from discord.ext.commands import Bot
import random

import secrets

messageMort = ["J'ai humilier {0} sur un jeu, il s'est suicidé", "Léa ne veut pas de moi, de rage j'ai tué {0}", "J'ai tuer {0}, en l'étouffant dans mes bourlets..."]

boptiste = Bot(command_prefix="!")


@boptiste.event
async def on_ready():
    print("En cours de connexion...")
    print("Bot <" + boptiste.user.name + "> connecter")


@boptiste.command(pass_context = True)
async def baptou(ctx, *args):
    await boptiste.delete_message(ctx.message)
    await boptiste.say("Bonjour je suis Baptiste, le bot Autiste !")
    await boptiste.say("Je suis pâtissier, comme ça je peux manger !")
    await boptiste.say("J'aime beacoup Dinsey, et surtout les pin's :o")
    await boptiste.say("J'ai pas de copine, mais je suis à fond sur LEA")
    await boptiste.say("FAIT UN DON : https://www.leetchi.com/c/boptiste")

@boptiste.command(pass_context = True)
async def say(ctx, *, message : str):
    await boptiste.delete_message(ctx.message)
    if ctx.message.author.id == "186171679163154441" or "303470630114820097":
        await boptiste.say(":microphone2: " + message + " :microphone2:")
        return
    else:
        await boptiste.say(":warning: " + ctx.message.author.mention + " : Tu n'as pas le droit de faire la commande !say")
        return

@boptiste.command(pass_context = True)
async def don(ctx, *args):
    await boptiste.delete_message(ctx.message)
    await boptiste.say(":moneybag:  https://www.leetchi.com/c/boptiste :moneybag:")

@boptiste.command(pass_context = True)
async def kill(ctx, member : discord.Member = None):
    await boptiste.delete_message(ctx.message)
    if member is None:
        await boptiste.say("Eh tu dois me dire qui tuer :o")
        return
    elif member.id == ("186171679163154441" or "303470630114820097"):
        await boptiste.say("On ne tue pas un Dieu !!!!")
        return
    elif member.id == ctx.message.author.id:
        await boptiste.say("Sa sert à rien de se tuer -_-")
        return
    else:
        nombre = random.randint(0, len(messageMort))
        text = messageMort[nombre].format(member.mention)
        await boptiste.say(":knife: " + text + " :knife:")
        return


boptiste.run(secrets.BOT_TOKEN)
