import os
import time
import numpy as np
class tic_tac_toe(object):
    def __init__(self,gamemode="man2man"):
        self.status=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player = ["O", 'X']
        self.turn=""
        self.round=0
        self.gamemode=gamemode
        self.actions=['1','2','3','4','5','6','7','8','9']
        self.done = False

    def reset(self):
        self.status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player = ["O", 'X']
        self.turn=""
        self.round=0
        self.done = False
        return self.status

    def checkgame(self):
        for i in range(3):
            if self.status[i] == self.status[i+3] == self.status[i+6] == self.turn:
                return True
            elif self.status[i*3] == self.status[i*3+1] == self.status[i*3+2] == self.turn:
                return True
        if self.status[0] == self.status[4] == self.status[8] == self.turn or self.status[2] == self.status[4] == self.status[6] == self.turn:
            return True
        return False

    def render(self):
        os.system("cls")
        print("")
        for i in range(3):
            print('  ' + self.status[i*3] + "|" + self.status[i*3+1] + '|' + self.status[i*3+2])

    def update(self,action):
        self.turn=self.player[self.round%2]
        action = int(action)
        if self.status[action] == " ":
            self.status[action] = self.turn
            self.round+=1
            self.done=True
            if self.checkgame():
                r=10
            else:
                r=-10
            return self.status ,r,self.done,True
        else:
            return self.status ,0,self.done,True



    def main(self):
        self.render()
        if self.gamemode=='man2ran':
            if (self.round%2==0):
                action=input()
            else:
                action=np.random.randint(1,9)
        elif self.gamemode=='ran2rand':
            if (self.round%2==0):
                action=np.random.randint(1,10)
                print(action)
            else:
                action=np.random.randint(1,10)
                print(action)
        elif self.gamemode=='man2man':
            if (self.round%2==0):
                action = input()
            else:
                action = input()

        self.update(action)
        if self.checkgame() :#其中一方獲勝
            os.system("cls")
            print("{} WIN!!!".format(self.turn))
            time.sleep(2)
            self.render()
            print("\n-------------------------\n")
            self.reset()
        elif self.round==9:#和局
            os.system("cls")
            print("TOE")
            time.sleep(2)
            self.render()
            print("\n-------------------------\n")
            self.reset()



game = tic_tac_toe(gamemode='man2man')
while __name__ == '__main__':
    game.main()