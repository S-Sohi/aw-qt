from plyer import notification

class NotificationManager:
    def __init__(self) -> None:
        pass
    
    def show(self, msg):
        notification.notify(title='SecondsMaster',
                            message=msg,
                            timeout=10)