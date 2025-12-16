
from PyQt6.QtWidgets import QApplication,QWidget,QDialog

import sys



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)


class mymanin(QWidget):
    def __init__(self):
        super().__init__()
        # self.setMaximumSize(500,500)
        # self.setMinimumSize(200,200)
        self.setFixedSize(500,500)

window = mymanin()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.