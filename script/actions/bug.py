from discord import Embed
from script.shared import Shared


class Bug:
    @staticmethod
    async def report_bug(msg, groups):
        src, des = groups.get_src(), groups.get_des()
        if msg.channel != src:
            return

        if des is not None:
            message = await des.send(
                embed=Embed(description="Bug:\n\n _" + msg.content[len(Shared.prefix + Shared.bug):] + '_',
                            colour=0x009F34).set_author
                (name=msg.author.name,
                 icon_url=msg.author.default_avatar_url)
            )
            for each in ["👍", "👎"]:
                await message.add_reaction(each)
            await msg.reply(
                f"Your Bug Report Has Been Successfully Sent To Group: `{groups.get_des().name}`\n"
                "Our Developers Will Respond And Fix Your Bug As Soon As They Confirm Your Bug Report!\n"
                "Thanks For Your Patience."
            )
        else:
            await msg.reply("Destination Groups Is Not Set!")
