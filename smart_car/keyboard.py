import sys,tty,termios
# from pynput.keyboard import Key
from enum import Enum

class Key(Enum):
        Up = 1
        Right = 2
        Down = 3
        Left = 4
        Esc = 5
        Unknown = 6

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def getKey() -> Key:
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return Key.Up
        elif k=='\x1b[B':
                return Key.Down
        elif k=='\x1b[C':
                return Key.Right
        elif k=='\x1b[D':
                return Key.Left
        elif k==chr(27).encode():
                return Key.Esc
        else:
                return Key.Unknown

def main():
        for i in range(0,20):
                print(getKey())

if __name__=='__main__':
        main()