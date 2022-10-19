from msilib.schema import Icon
import time
from plyer import notification
from datetime import datetime

def waterFunc() :
	if __name__=="__main__":
		notification.notify(
		title = "Water Alert",
		message="TAKE A SIP OF WATER" ,
		app_icon = r"C:\Users\mrohith\Downloads\water.ico",
		# displaying time
		timeout=2
		)
		


while True :
    if datetime.now().minute in (0,15,30,45):
        waterFunc()
        time.sleep(60)
    time.sleep(1)


