import names
import random
import os
class Person:
    def __init__(self):
        self.name = names.get_first_name()
        self.in_tourny = True
        self.skill = random.randint(0,100)
        self.money = random.randint(0,10)
    def set_lost(self):
        self.in_tourny = False
    def get_status(self):
        return self.in_tourny
    def play_a_round(self,other_player_obj):
        x = random.randint(0, self.skill)
        y = random.randint(0,other_player_obj.skill)
        if x >= y:
            other_player_obj.set_lost()
            self.money += other_player_obj.money
        else:
            self.set_lost()
            other_player_obj.money += self.money
            self.money = 0

      
def report(player_list):
    print("----Leaderboard----")
    for i in range(len(player_list)):
        s = "Not Out"
        if (player_list[i].get_status() == False):
            s = "\033[0;31mOut\033[0;37m"
        print(str(i) + " " + player_list[i].name + ' $ ' + str(player_list[i].money) + " : " + s)
    print("-------------------")
num = random.randint(4,8)
player_list = []
for i in range(num):
    player_list.append(Person())    
while 1 == 1:
    count = 0
    for i in range(len(player_list)):
        if player_list[i].in_tourny == True:
            count += 1
    if count == 1:
        print("winner")
        break
    report(player_list)
    
    one = int(input("Choose first player:"))
   
    if player_list[one].in_tourny == False:
        print("that's not allowed")
        continue

    two = int(input("Choose second player:"))
    if player_list[two].in_tourny == False:
        print("that's not allowed")
        continue

    os.system("clear")


    player_list[one].play_a_round(player_list[two])
     
