import pyttsx3 as ptx
import time as t
engine = ptx.init()

i = 0
x = 130
count = 0

rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while True:
    t.sleep(1200)
    engine.setProperty('rate', x)
    
    count += 1
    times = count * 20
    hour = times // 60
    minute = times - (hour * 60)
    
    if hour == 0:
        engine.say(f"Sir, Your total screen time is {minute} minute.")
        engine.runAndWait()
        if hour >= 2:
            engine.say(f"Please Sir, take a short breake. Over 2 hour sitting fornt of computer is dangerous for eyes, back and your mental health.")
            engine.runAndWait()
    elif minute == 0:
        engine.say(f"Sir, Your total screen time is {hour} hour.")
        engine.runAndWait()
        if hour >= 2:
            engine.say(f"Please Sir, take a short breake. Over 2 hour sitting fornt of computer is dangerous for eyes, back and your mental health.")
            engine.runAndWait()
    else:
        engine.say(f"Sir, Your total screen time is {hour} hour and {minute} minute.")
        engine.runAndWait()
        if hour >= 2:
            engine.say(f"Please Sir, take a short breake. Over 2 hour sitting fornt of computer is dangerous for eyes, back and your mental health.")
            engine.runAndWait()
        
    engine.say("Please take some break. To long time looking at computer screen is harmful for eyesight. These screen breaks help prevent eye strain.")
    engine.runAndWait()
    
    for i in range(3):
        engine.setProperty('rate', 140)
        t.sleep(2)
        engine.say("Please Sir, take some breake.")
        engine.runAndWait()

    
    