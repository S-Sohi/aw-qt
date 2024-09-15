from PyQt6 import QtCore
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QPushButton,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QDialog,
    QStackedWidget
)
import sys
from .client import client
from .datastore import DataStore
from .login import LoginPage
from .dashboard import DashboardPage
from .evnets import EventTypes,EventDetail
from .eventQueue import event_queue

class MainWindow(QDialog):
    def __init__(self, url):
        super().__init__()
        self.datastore = DataStore()
        self.stacked_widget = QStackedWidget(self)
        self.event_queue = event_queue
        self.login_page = LoginPage(url)
        self.dashboard_page = DashboardPage(url)

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.dashboard_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
        
        self.setWindowTitle("Time Tracking Application")
        self.setGeometry(100, 100, 300, 150)
        
        self.event_queue.subscribe(on_next=self.observe_changes)

    def observe_changes(self, event:EventDetail):
        if(event.type == EventTypes.SUCCESSFUL_LOGIN):
            self.show_dashboard()
        elif(event == EventTypes.TOKEN_EXPIRED):
            pass
        elif(event == EventTypes.LOGOUT):
            self.logout()
        
    def show_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_page)
        
    def logout(self):
        self.stacked_widget.setCurrentWidget(self.login_page)
            
   