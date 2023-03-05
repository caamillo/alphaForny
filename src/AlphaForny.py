from FornyTranslator import FornyTranslator
from Action import Action

from pynput.keyboard import Key, Listener
from threading import Thread

class AlphaForny(FornyTranslator, Action):
    def __init__(self, scriptPath, t, clear) -> None:
        self.action = Action()
        self.t = t
        self.clear = clear

        super().__init__(scriptPath, self.action, self.t, self.clear)

        # Thread Handling
        self.pause = False
        self.end = False

        # PokeMMO Handling
        self.run = False
        self.bike = False

    def onPress(self, key):
        pass
    def onRelease(self, key):
        try:
            if key == Key.esc:
                print(f"[{ self.t('general.status.state') }]: { self.t('alphaforny.killed') }")
                self.end = True
                return False
            elif key.char == 'p':
                if not self.pause:
                    print(f"[{ self.t('general.status.state') }]: { self.t('alphaforny.paused') }")
                    self.pause = True
                else:
                    print(f"[{ self.t('general.status.state') }]: { self.t('alphaforny.resumed') }")
                    self.pause = False
        except AttributeError:
            pass
        except Exception as err:
            print(f'[{ self.t("general.status.state") }]: { self.t("alphaforny.handling_error") }')
            print(err)
    def exec(self, skipStart = False):
        if not skipStart: # Start
            for instruction in self.cmds:
                if instruction != 'loop':
                    for cmd in self.cmds[instruction]:
                        while self.pause:
                            pass
                        if type(cmd) is dict:
                            key, value = next(iter(cmd.items()))
                            self.translateCmd(key, value)
                        else:
                            self.translateCmd(cmd)
        while not self.end: # Loop
            for cmd in self.cmds['loop']:
                while self.pause:
                    pass
                if self.end:
                    break
                if type(cmd) is dict:
                    key, value = next(iter(cmd.items()))
                    print(key, value) # [ DEBUG ]
                    self.translateCmd(key, value)
                else:
                    print(cmd)
                    self.translateCmd(cmd)
    def start(self):
        print(f"[{ self.t('general.status.state') }]: { self.t('alphaforny.start') }")

        # AlphaForny Thread
        executeThread = Thread(target = self.exec, args=(False, ))
        executeThread.start()

        # Input Handling Thread
        with Listener (
            on_press = self.onPress,
            on_release = self.onRelease) as listener:
            listener.join()