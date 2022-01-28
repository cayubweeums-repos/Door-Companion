import datetime
from time import sleep
import multiprocessing
from speech.engine import SpeechEngine


def main():
    try:
        print('~~~~~ Loading ~~~~~')
        _speechEngine = SpeechEngine()
        _speechEngine.run()
        while True:
            print('~~~~~ Running ~~~~~')
            sleep(1)
    except KeyboardInterrupt:
        print('~~~~~ Stopping ~~~~~')
        print('~~~~~ Done ~~~~~')


main()
