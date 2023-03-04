from FornyTranslator import FornyTranslator
from Action import Action

from pynput.keyboard import Key, Listener
from threading import Thread

class AlphaForny(FornyTranslator, Action):
    def __init__(self, scriptPath) -> None:
        self.action = Action()
        super().__init__(scriptPath, self.action)

        self.pause = False
        self.end = False
    def onPress(self, key):
        pass
    def onRelease(self, key):
        try:
            if key == Key.esc:
                print("[State]: Script has been killed")
                self.end = True
                return False
            elif key.char == 'p':
                if not self.pause:
                    print("[State]: Script has been paused")
                    self.pause = True
                else:
                    print("[State]: Script has been resumed")
                    self.pause = False
        except:
            print('[Error]: An error has been occured during input handling')
    def exec(self, skipStart = False):
        if not skipStart: # Start
            for instruction in self.cmds:
                if instruction != 'loop':
                    for cmd in self.cmds[instruction]:
                        while self.pause:
                            pass
                        self.translateCmd(cmd, self.cmds[instruction][cmd])
        while not self.end: # Loop
            for cmd in self.cmds['loop']:
                print(cmd) # Debug cmd
                while self.pause:
                    pass
                if self.end:
                    break
                self.translateCmd(cmd, self.cmds['loop'][cmd])
    def start(self):
        print("[State]: Starting AlphaForny...")

        # AlphaForny Thread
        executeThread = Thread(target = self.exec, args=(False, ))
        executeThread.start()

        # Input Handling Thread
        with Listener (
            on_press = self.onPress,
            on_release = self.onRelease) as listener:
            listener.join()