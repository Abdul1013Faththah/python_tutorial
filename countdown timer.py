import time

def coutdown(t):
    while t: # until t is 0 or null for loop will run  
        mins,secs = divmod(t,60) # divmod()is built in function that divdes the 1 st value with the second value and asigns it as a tupple
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r") # here \r means move the course to the beginnig of  the same line 
        time.sleep(1)
        t=t-1

    print('timer completed')
    time.sleep(5)


t=input('enter the time in seconds : ')

coutdown(int(t))
    
