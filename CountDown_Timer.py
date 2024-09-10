import time
import keyboard
def countdown_time(hrs, mins, secs,t):

    while t: 
        hrs, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60) 
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
        if keyboard.is_pressed('esc'):
            print("Timer stopped.")
            break
    print("Time up")

h=int(input("enter hour -> "))
m=int(input("enter min -> "))
s=int(input('enter seconds -> '))
t=(h*3600)+(m*60)+(s)
countdown_time(h,m,s,t)
