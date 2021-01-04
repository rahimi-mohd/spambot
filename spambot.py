import pyautogui, time

num = int(input("How many time do you want to spam the enemy 😛️? \n")) #how many time do you want to spam
spam = input("Insert spam text: \n") #what do you want to spam
time.sleep(1) 

print("⚔️⚔️⚔️⚔️⚔️Time to destroy the enemy ⚔️⚔️⚔️⚔️⚔️⚔")
time.sleep(1)

for i in range(num):
    pyautogui.typewrite(spam)
    pyautogui.press("enter")
    time.sleep(1) 
    
