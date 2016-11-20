import discord
from .permissions import Perms


class Commands:

    def __init__(self):
        pass

    @staticmethod
    async def on_message(parent, msg, bot: discord.Client):
        user = msg.author
        args = msg.content.split()
        parent.perm.set_failed(False)
        if args[0] == "$lvl" and await parent.perm.is_permitted(msg, bot):
            await parent.send_level(bot, msg, args)
            return
        elif args[0] == "$xp" and await parent.perm.is_permitted(msg, bot):
            await parent.send_xp(bot, msg, args)
            return
        elif args[0] == "$totalxp" and await parent.perm.is_permitted(msg, bot):
            await parent.send_total_xp(bot, msg, args)
            return
        elif args[0] == "$cooldown" and await parent.perm.is_permitted(msg, bot):
            await parent.send_timestamp(bot, msg, args)
            return
        elif args[0] == "$givexp" and await parent.perm.is_permitted(msg, bot):
            try:
                if args[2] == msg.mentions[0].mention:
                    user = msg.mentions[0]
                else:
                    user = msg.author
            except IndexError:
                user = msg.author
            try:
                parent.add_xp(user, int(args[1])+0)
                await bot.send_message(msg.channel, "{} received {}xp".format(user.mention, args[1]))
            except IndexError:
                await bot.send_message(msg.channel, "Syntax: $givexp [amount] @[user]")
        elif args[0] == "$setperm" and await parent.perm.is_permitted(msg, bot):
            if not parent.perm.is_role_prior(parent.get_role(user), args[1]):
                bot.send_message(msg.channel, "Your role is too low to change permissions for {}".format(args[1]))
            try:
                parent.perm.set_role_perm(args[1], args[2], args[3])
                await bot.send_message(msg.channel, "Set the {} command for {} to {}".format(args[2], args[1], args[3]))
            except:
                await bot.send_message(msg.channel, "Syntax: $setperm [role] [command] [value]")
        elif args[0].startswith("$") and not parent.perm.get_failed():
            await bot.send_message(msg.channel, "The command {} doesnt exist".format(args[0]))
            return
