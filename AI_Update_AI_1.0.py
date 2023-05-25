import pyttsx3
robot_mouth = pyttsx3.init()
import speech_recognition 
robot_brain = "Hello, How can I help you?"
print("Robot: " + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
robot_ear = speech_recognition.Recognizer()
print("----------")
while True:
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        robot_brain = "Sorry, I don't know that"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    print('You: ' + you)
    print("----------")
    if "time" in you:
        from datetime import datetime
        now = datetime.now()
        time = "It's " + now.strftime("%H:%M")
        robot_brain = time
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "master" in you:
        robot_brain = "Tuan Tran is my master"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "today" in you:
        from datetime import date
        today = date.today()
        today = today.strftime("%d-%m-%Y")
        robot_brain = str(today)
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "your name" in you:
        robot_brain = "My name is AI 1.0"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "bye" in you:
        robot_brain = "Ok good bye"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Sorry, I don't know that"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break