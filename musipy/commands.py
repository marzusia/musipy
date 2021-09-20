class Command:
    def __init__(self, database):
        self.database = database

class TokiCommand(Command):
    name = 'toki'

    async def on_command(self, message):
        await message.channel.send('toki a!')