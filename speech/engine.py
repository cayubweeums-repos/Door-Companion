from os import system as sys


class SpeechEngine:
    def __init__(self):
        super(SpeechEngine, self).__init__()
        self.on = True
        self.cmdBegin = "espeak -ven+m1 "
        self.cmdContent = None
        self.cmdEnd = " 2>/dev/null"

    def run(self):
        while self.on:
            self.getinput()
            print("{}'{}'{}".format(self.cmdBegin, self.cmdContent, self.cmdEnd))
            sys("{}'{}'{}".format(self.cmdBegin, self.cmdContent, self.cmdEnd))

    def getinput(self):
        self.cmdContent = str(input('What do you want to say?\n> '))

