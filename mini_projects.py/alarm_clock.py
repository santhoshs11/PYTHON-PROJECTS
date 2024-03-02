import time
CLEAR= "\033[2J"
CLEAR_AND_RETURN="\033[H"
def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while (time_elapsed<seconds):
        time.sleep(1)
        time_elapsed+=1
        time_left = seconds-time_elapsed
        minutes=time_left//60
        second=time_left%60
       
        print(f"{CLEAR_AND_RETURN}{minutes:02d}:{second:02d}")
        
alarm(int(input("set timer : ")))

