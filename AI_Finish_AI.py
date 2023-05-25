# Thứ tự xử lý Ear->Brain->Mouth
# Ear
import speech_recognition 
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
# 3 dòng lệnh trên là cần thiết và cần học thuộc

    print('Robot :' + " I'm listening")
    audio = robot_ear.listen(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
# try and except là mệnh đề bắt lỗi nếu thử xảy ra lỗi sẽ chuyển sang except
print(you)

# Brain
if you == "":
    robot_brain = "I can't hear you, try again"
elif you == 'hello':
    robot_brain = 'hello my master'
elif you == "what's your name":
    robot_brain = 'AI 01 is my name'
else:
    robot_brain = "I'm fine thank you and you"
print(robot_brain)

# Mouth
import pyttsx3
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
