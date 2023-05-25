import pyttsx3
robot_brain = "Hello my master, I'm your assistant"
robot_mouth = pyttsx3.init()

# 2 dòng dưới để thực hiện robot_mouth nói một str bất kỳ bằng tiếng anh
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()