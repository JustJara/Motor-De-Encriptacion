import sys

sys.path.append('src')

import encriptation_console.encriptation_console as encriptation_console

if __name__ == '__main__':

    Console = encriptation_console.ConsoleUI()
    Console.run_application()