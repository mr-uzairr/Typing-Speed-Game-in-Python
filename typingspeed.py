from time import time # to record the time

# to calculate accuracy of input prompt
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords) - 1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i + 1] == words[i + 1]) & (inwords[i - 1] == words[i - 1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
        return errors
    
# to calculate speed of typing words per minute
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()  
    twords = len(inwords)
    speed = twords / time

    return speed

# calculate the total elapsed time

def elapsedtime(stime, etime):
    time = etime - stime
    return time

if __name__ == '__main__':

    prompt = "Test your typing speed with a fun Python game! Type the given sentence as fast and accurately as possible, and see your words per minute (WPM) score."
     # paragraph which you have to type to check your speed
    print("type this:- ", prompt, " ")
    

                    


