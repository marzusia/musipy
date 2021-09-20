import os
import sys
from dotenv import load_dotenv
from musipy.client import MusipyClient

class Manage:
    class MissingEnvKeyException(Exception):
        pass

    def _getEnv(self, key):
        env = os.getenv(key)
        if not env:
            raise self.MissingEnvKeyException(
                'Missing environment variable: %s' % key
            )
        return env
    
    def _printHelp(self):
        print('Usage: manage.py <command> [arguments]')
        print('======================================')
        print('commands:')
        print('* run : starts up the discord bot')
        print('======================================')

    def _loadEnv(self):
        load_dotenv()
        self.token = self._getEnv('TOKEN')

    def _runServer(self):
        client = MusipyClient()
        client.run(self.token)

    def __init__(self, args):
        self.args = args
        self._loadEnv()
        commands = {
            'run': self._runServer
        }
        print('mi ilo musi a, beep boop.')
        if len(args) == 0 or args[0] not in commands:
            return self._printHelp()
        else:
            commands[args[0]]()

if __name__ == '__main__':
    manage = Manage(sys.argv[1:])