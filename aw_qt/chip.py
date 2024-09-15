from PyQt6.QtWidgets import (

    QPushButton
)
import random

def random_hex_color():
    # Generate a random integer between 0 and 0xFFFFFF (16777215)
    random_color = random.randint(0, 0xFFFFFF)
    # Convert the integer to a hex string and format it to ensure 6 characters
    hex_color = f'#{random_color:06x}'
    return hex_color
class ChipButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        background_color = random_hex_color()
        self.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                border: none;
                border-radius: 10px; /* Rounded edges */
                padding: 4px 6px; /* Padding around text */
                font-size: 12px;
                background-color:%s;
            }
            QPushButton:hover {
                background-color: #b0b0b0; /* Change color on hover */
            }
            QPushButton:pressed {
                background-color: #a0a0a0; /* Change color on press */
            }
        """ % (background_color))
        self.setFixedWidth(60)
        