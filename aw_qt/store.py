from .evnets import EventDetail, EventTypes
from .eventQueue import event_queue
class Store():
    def __init__(self) -> None:
        self.team_id = None
        self.token = None
        self.is_logged_in = None
    
    def update_team_id(self, team_id:int):
        self.team_id = team_id
        
    def update_token(self, token:str):
        self.token = token
    
    def update_login_state(self, state:bool):
        self.is_logged_in = state
        
state_management = Store()

def observe(event: EventDetail):
    if(event.type == EventTypes.SUCCESSFUL_LOGIN):
        state_management.update_token(event.data)
        state_management.update_login_state(True)
    elif(event.type == EventTypes.START_ACTIVITY):
        state_management.update_team_id(event.data)
    elif(event.type == EventTypes.RESET_ACTIVITY):
        state_management.update_team_id(event.data)
event_queue.subscribe(on_next=observe)
    