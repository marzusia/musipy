import discord
from .database import Database
from .commands import TokiCommand

class MusipyClient(discord.Client):
    prefix = 'ilo musi o '
    prefix_len = len(prefix)
    
    def _addCommand(self, command):
        if not hasattr(self, 'commands'):
            self.commands = {}
        self.commands[command.name] = command(self.database)

    def __init__(self):
        super().__init__()
        self.database = Database()
        self._addCommand(TokiCommand)

    async def _tryCommand(self, command, message):
        if command in self.commands:
            await self.commands[command].on_command(message)
        else:
            await message.channel.send(
                'toki ni li ike a! mi sona e toki ni: %s'
                % ' en '.join(list(self.commands.keys()))
            )

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith(self.prefix):
            await self._tryCommand(message.content[self.prefix_len:], message)

    async def on_ready(self):
        print('Logged on as %s' % self.user)