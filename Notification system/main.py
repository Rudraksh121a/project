from plyer import notification
import time

if __name__ == '__main__':
    while True:
         notification.notify(
        title="*** Take Rest ***",
        message="Drink Water",
        # app_icon="Here we can add icon",
        timeout=5)
    time.sleep(3600)

   
