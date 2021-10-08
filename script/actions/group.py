from script.shared import Shared


class Group:
    @staticmethod
    async def group_action(args, ser, msg):
        channel_name = msg.channel.name
        if args[1] == Shared.src:
            ser.groups.set_source_group(msg.channel)
            await msg.reply(f"Source Group Has Been Set To `{channel_name}`")
        elif args[1] == Shared.des:
            ser.groups.set_destination_group(msg.channel)
            await msg.reply(f"Destination Group Has Been Set To `{channel_name}`")
        else:
            await msg.reply("Invalid Argument!")
