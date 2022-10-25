from asyncore import loop
from unicodedata import name
from PyQt5 import QtCore, QtGui, QtWidgets
import asyncio
import websockets
import json
import time

from send_sms import send_sms

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 643)
        MainWindow.setWindowTitle("SMS Sender App")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # URL label
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.url_label.setObjectName("url_label")
        self.url_label.setText("URL")
        # URL input
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(20, 41, 300, 30))
        self.url_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.url_input.setStyleSheet("padding: 50px 0;")
        self.url_input.setCursorPosition(21)
        self.url_input.setObjectName("url_input")
        self.url_input.setText("127.0.0.1:5005")
        # Port input
        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setGeometry(QtCore.QRect(20, 100, 300, 30))
        self.port_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.port_input.setText("")
        self.port_input.setPlaceholderText("")
        self.port_input.setObjectName("port_input")
        # Port label
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setGeometry(QtCore.QRect(20, 80, 91, 17))
        self.port_label.setObjectName("port_label")
        self.port_label.setText("USB Port")
        # Port label
        self.app_input = QtWidgets.QLineEdit(self.centralwidget)
        self.app_input.setGeometry(QtCore.QRect(20, 160, 300, 30))
        self.app_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.app_input.setText("")
        self.app_input.setObjectName("app_input")
        # App label
        self.app_label = QtWidgets.QLabel(self.centralwidget)
        self.app_label.setGeometry(QtCore.QRect(20, 140, 90, 17))
        self.app_label.setObjectName("app_label")
        self.app_label.setText("App Name")
        # Start button
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(20, 205, 60, 25))
        self.start_button.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.start_button.setObjectName("start_button")
        self.start_button.setText("Start")
        # Stop button
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(90, 205, 60, 25))
        self.stop_button.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setText("Stop")
        self.stop_button.setEnabled(False)
        # Status label
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(160, 210, 67, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.status_label.setText("Status:")
        # Status value
        self.status_value = QtWidgets.QLabel(self.centralwidget)
        self.status_value.setGeometry(QtCore.QRect(220, 210, 100, 17))
        self.status_value.setStyleSheet("color: rgb(136, 138, 133);")
        self.status_value.setObjectName("status_value")
        self.status_value.setText("Inactive")
        # Queue label
        self.queue_label = QtWidgets.QLabel(self.centralwidget)
        self.queue_label.setGeometry(QtCore.QRect(350, 20, 67, 17))
        self.queue_label.setObjectName("queue_label")
        self.queue_label.setText("Queue")
        # Horizontal line
        self.h_line = QtWidgets.QFrame(self.centralwidget)
        self.h_line.setGeometry(QtCore.QRect(-10, 250, 2000, 20))
        self.h_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line.setObjectName("h_line")
        # Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 22))
        self.menubar.setObjectName("menubar")
        # Actions menu
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuActions.setTitle("Actions")
        # Help menu
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.setTitle("Help")
        # Help > Doc meun
        self.menuDoc = QtWidgets.QMenu(self.menuHelp)
        self.menuDoc.setObjectName("menuDoc")
        self.menuDoc.setTitle("Doc")
        MainWindow.setMenuBar(self.menubar)
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Actions > Reset menu
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.setText("Reset")
        # Actions > Reset menu
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionRestart.setText("Restart")
        # Actions > Exit menu
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("Exit")
        # Help > About menu
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setText("About")
        # Help > Doc > For Window menu
        self.actionFor_Windows = QtWidgets.QAction(MainWindow)
        self.actionFor_Windows.setObjectName("actionFor_Windows")
        self.actionFor_Windows.setText("For Windows")
        # Help > Doc > For Mac menu
        self.actionFor_Mac = QtWidgets.QAction(MainWindow)
        self.actionFor_Mac.setObjectName("actionFor_Mac")
        self.actionFor_Mac.setText("For Mac")
        # Help > Doc > For Linux menu
        self.actionFor_Linux = QtWidgets.QAction(MainWindow)
        self.actionFor_Linux.setObjectName("actionFor_Linux")
        self.actionFor_Linux.setText("For Linux")
        # Actions menu
        self.menuActions.addAction(self.actionReset)
        self.menuActions.addAction(self.actionRestart)
        self.menuActions.addAction(self.actionExit)
        # Help > Doc menu
        self.menuDoc.addAction(self.actionFor_Windows)
        self.menuDoc.addAction(self.actionFor_Mac)
        self.menuDoc.addAction(self.actionFor_Linux)
        # Help menu
        self.menuHelp.addAction(self.menuDoc.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # List Widget
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(350, 40, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.queue = []

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.start_button.clicked.connect(lambda: asyncio.run(self.ws_connect()))
        self.thread = {}
        self.start_button.clicked.connect(self.start_worker_ws)
        self.stop_button.clicked.connect(self.stop_worker_ws)

    def loop_check(self):
        while True:
            if len(self.queue) > 0:
                self.queue.pop(0)
                self.add_item()
                time.sleep(5)

    def connection_error(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.url_input.setEnabled(True)
        self.port_input.setEnabled(True)
        self.app_input.setEnabled(True)
        self.status_value.setText("Failed")
        self.status_value.setStyleSheet("color: rgb(164, 0, 0);")

    def start_worker_check(self):
        self.thread[1] = ThreadClass(parent=None,index=1, name="Check", loop_check=self.loop_check, connection_error=self.connection_error)
        self.thread[1].start()

    def start_worker_ws(self):
        self.thread[2] = ThreadClass(parent=None,index=2, add_item=self.add_item, connection_error=self.connection_error, host=self.url_input.text(), app=self.app_input.text(), status=self.status_value, port=self.port_input.text())
        self.thread[2].start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.url_input.setEnabled(False)
        self.port_input.setEnabled(False)
        self.app_input.setEnabled(False)
        self.status_value.setText("Connecting...")
        self.status_value.setStyleSheet("color: rgb(78, 154, 6);")
        self.start_worker_check()

    def stop_worker_ws(self):
        self.thread[2].stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.url_input.setEnabled(True)
        self.port_input.setEnabled(True)
        self.app_input.setEnabled(True)
        self.status_value.setText("Inactive")
        self.status_value.setStyleSheet("color: rgb(136, 138, 133);")

    def add_item(self, item=None):
        self.listWidget.clear()
        if item:
            self.queue.append({"phone": item["phone"], "msg": item["msg"]})
        for q in self.queue:
            q_item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(q_item)
            q_item.setText(q["phone"])


class ThreadClass(QtCore.QThread):
    
    any_signal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None,index=0, add_item=None, name=None, loop_check=None, connection_error=None, host=None, app=None, status=None, port=None):
        super(ThreadClass, self).__init__(parent)
        self.index=index
        self.name = name
        self.add_item = add_item
        self.loop_check = loop_check
        self.connection_error = connection_error
        self.host = host
        self.app = app
        self.status = status
        self.port = port
        self.is_running = True
        
    async def handler(self, websocket):
        while True:
            message = await websocket.recv()
            json_data = json.loads(message)
            if json_data["type"] == "send_to_gui":
                self.add_item(json_data)
                # Write here sms send code over USB Port with USB Modem. It's easy!
                send_sms(json_data["phone"], json_data["msg"], self.port)
                print('Recivied "'+json_data["msg"]+'" from '+json_data["phone"]+" via port "+self.port)
            self.status.setText("Connected")

    async def ws_connect(self):
        url = "ws://"+self.host+"/ws/sms-server/" + self.app
        try:
            async with websockets.connect(url) as ws:
                await self.handler(ws)
                await ws.close()
                await asyncio.Future()  # run forever
        except:
            self.connection_error()

    def run(self):
        if self.name == "Check":
            print('Starting loop_check thread...')
            self.loop_check()
        else:
            print('Starting ws thread...')
            asyncio.run(self.ws_connect())

    def stop(self):
        self.is_running = False
        print('Stopping ws thread...')
        self.terminate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
