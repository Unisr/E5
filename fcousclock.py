import time

def count_down(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, seconds = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time up!")
