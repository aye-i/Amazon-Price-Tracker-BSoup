from pushbullet import Pushbullet

class NotifManager:

    def __init__(self):
        self.PUSHBULLET_APIKEY = ""

    def send_notif(self, price, threshold, product):
        pb = Pushbullet(api_key=self.PUSHBULLET_APIKEY)
        pb.push_note(f"{product} available @ ₹{price}!",
                     f"{product} available @ ₹{price}! | Save: ₹{threshold-price}! ")
        print(f"Notification sent")
