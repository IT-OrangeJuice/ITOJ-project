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

print('Did you say: ' + you + ' ?')