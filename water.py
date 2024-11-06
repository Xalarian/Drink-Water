import time
from plyer import notification

def remind_to_drink_water():
    while True:
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink water! Stay hydrated.",
            timeout=10  # Notification timeout in seconds
        )
        time.sleep(60 * 60)  # Remind every hour (adjust as needed)

if __name__ == "__main__":
    remind_to_drink_water()
    