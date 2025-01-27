import random

while(True):
    lucky_num=int(input("enter lucky number="))
    random_num=random.randint(1,10)
    print("random number=",random_num)

    if lucky_num==random_num:
        print("The random number matches lucky number")
        break
    else:
        print("random number not matches to lucky number\nchoose random number betwen 1 & 10")
        
