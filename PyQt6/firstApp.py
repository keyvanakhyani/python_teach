
from PyQt6.QtWidgets import QApplication,QWidget,QDialog,QDialogButtonBox,QVBoxLayout

import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        # Dialog-specific features
        # Dialog will return True if OK clicked, False if Cancel
        layout = QVBoxLayout()
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

         # ⭐ ADD BUTTONS TO LAYOUT - This is what you were missing!
        layout.addWidget(buttons)
        
        # ⭐ SET LAYOUT TO DIALOG
        self.setLayout(layout)

# Create a Qt widget, which will be our window.
window = MyDialog()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.