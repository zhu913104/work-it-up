import os
import time
class tic_tac_toe(object):
    def __init__(self):
        self.status=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = ["O", 'X']
        self.turn=""
        self.round=0

    def reset(self):
        self.status=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = ["O", 'X']
        self.turn=""
        self.round=0

    def checkgame(self):
        for i in range(3):
            if self.status[i][0] == self.status[i][1] == self.status[i][2] == self.turn:
                return True
            elif self.status[0][i] == self.status[1][i] == self.status[2][i] == self.turn:
                return True
        if self.status[0][0] == self.status[1][1] == self.status[2][2] == self.turn or self.status[2][0] == self.status[1][1] == self.status[0][2] == self.turn:
            return True
        return False

    def render(self):
        os.system("cls")
        print("")
        for i in range(2, -1, -1):
            print('  ' + self.status[i][0] + "|" + self.status[i][1] + '|' + self.status[i][2])

    def update(self,action):
        self.turn=self.player[self.round%2]
        try:
            action = int(action)
        except:

            self.render()
            action = input("\n請輸入半形數字: ")
            self.update(action)
        else:
            try:
                if self.status[(action - 1) // 3][(action - 1) % 3] == " ":
                    self.status[(action - 1) // 3][(action - 1) % 3] = self.turn
                else:

                    self.render()
                    action = input("\n請畫其他格")
                    self.update(action)
            except:

                self.render()
                action = input("\n請輸入0~9的數字")
                self.update(action)
        self.round+=1



    def main(self):
        self.render()

        action=input()
        self.update(action)
        if self.checkgame():
            os.system("cls")
            print("{} WIN!!!".format(self.turn))
            time.sleep(2)
            self.render()
            print("\n-------------------------\n")
            self.reset()



game = tic_tac_toe()
while __name__ == '__main__':
    game.main()