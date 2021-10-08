from script.actions.group import Group
from script.actions.bug import Bug
from script.shared import Shared


class Parser:
    server = None

    async def parser(self, msg, server):
        content, self.server = msg.content[len(Shared.prefix):], server
        args = str(content).split(" ")
        if args[0] == Shared.group:
            
                await Group.group_action(args, self.server, msg)

        elif args[0] == Shared.inf:
            src_group = self.server.groups.get_src()
            des_group = self.server.groups.get_des()
            if src_group or des_group is not None:
                await msg.reply(
                    f"Source Group: `{self.server.groups.get_src().name}`\n"
                    f"Destination Group: `{self.server.groups.get_des().name}`"
                )
            else:
                await msg.reply("You Should Set Source And Destination Groups.")
        elif args[0] == Shared.bug:
            await Bug.report_bug(msg, self.server.groups)
