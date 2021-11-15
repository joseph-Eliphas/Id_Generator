import random
import time

x = ["abcdefghijklmnopqrstuvwxyz","0123456789"]

def generate(length):
    global x
    global y
    id = ""
    for i in range(length):
        state = random.randint(0,1)
        opt = random.randint(0,1)
        if(opt == 0):
            if(state == 0):
                key = str(x[opt][random.randint(0,25)]).capitalize()
            else:
                key = str(x[opt][random.randint(0,25)]).lower()
        else:
            key = str(x[opt][random.randint(0,9)])
        id += key
    return id      
    pass

while True:
    time.sleep(0.5)
    print(generate(10))