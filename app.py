import sys

sys.path.append('src')
from console.encriptation_console import ConsoleUI



if __name__ == '__main__':

    Console = ConsoleUI()
    Console.run_application()