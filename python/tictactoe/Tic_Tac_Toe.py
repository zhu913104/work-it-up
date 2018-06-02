import os
import time
import numpy as np
class tic_tac_toe(object):
    def __init__(self,gamemode="man2man"):
        self.status=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player = ['1','2']
        self.turn=0
        self.round=0
        self.gamemode=gamemode
        self.actions=['1','2','3','4','5','6','7','8','0']
        self.done = False

    def reset(self):
        self.status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.turn=0
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
        tran=self.status.copy()
        for i in range(len(tran)) :
            if tran[i] == '1':
                tran[i]= 'O'
            elif tran[i]=='2':
                tran[i]= 'X'
        for i in range(3):
            print('  ' + tran[i*3] + "|" + tran[i*3+1] + '|' + tran[i*3+2])

    def update(self,action):
        self.turn=self.player[self.round%2]
        action = int(action)
        self.leg=False
        r=0
        if self.status[action] == " ":
            self.status[action] = self.turn
            self.round+=1
            self.leg = True
            if self.checkgame() and self.turn=="1":
                r=10
                self.done = True
                self.leg=False

            elif self.checkgame() and self.turn=="2":
                r=-10
                self.done = True
                self.leg = False

            return self.status ,r,self.done, self.leg
        else:
            if  " "not in self.status:
                self.done = True
                self.leg = True
            return self.status ,r,self.done, self.leg



    def main(self):
        self.render()
        print(self.status)
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