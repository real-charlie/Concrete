import discord

from script.parser.groups import *
from script.parser.parser import Parser
from script.shared import Shared

class Discord(discord.Client):
    parser = Parser()
    servers = []

    async def on_ready(self):
        print("Concrete Has Been Started!")
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="Concrete")
        )

    async def on_message(self, msg):
        if str(msg.content).startswith(Shared.prefix) and msg.author != self.user:
            server = Server(msg.guild.id, Groups())
            found = False
            for server_ in self.servers:
                if server_.server_id == msg.guild.id:
                    server = server_
                    found = True
            if not found:
                self.servers.append(server)
            await self.parser.parser(msg, server)

discord_c = Discord()
discord_c.run("TOKEN")
