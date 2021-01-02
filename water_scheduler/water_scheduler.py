import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
        title = "Please Drink Water Now",
        message = "carrying nutrients and oxygen to your cellsflushing bacteria from your bladderaiding digestionpreventing constipationnormalizing blood pressurestabilizing the heartbeatcushioning jointsprotecting organs and tissues",
        app_icon = "C:\\Users\\91989\\Desktop\\Dice Roll\\icon.ico",
        timeout=2
    )
    time.sleep(6)
    
# "pythonw .\water_scheduler.py" run this to make script run in background
