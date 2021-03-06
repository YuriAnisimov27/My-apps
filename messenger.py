from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import clientui


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.url = url

        self.pushButton.pressed.connect(self.send_message)

        self.last_timestamp = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def send_message(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()

        requests.get(
            self.url + '/send_message',
            json={
                'username': username,
                'password': password,
                'text': text
            }
        )

        self.textEdit.setText('')
        self.textEdit.repaint()

    def update_messages(self):
        response = requests.get(
            self.url + '/get_messages',
            params={'after': self.last_timestamp}
        )
        messages = response.json()['messages']

        for message in messages:
            dt = datetime.fromtimestamp(message['timestamp'])
            dt = dt.strftime('%H:%M:%S %d/%m/%Y')
            self.textBrowser.append(dt + ' ' + message['username'])
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')
            self.last_timestamp = message['timestamp']


app = QtWidgets.QApplication([])
window = ExampleApp('https://c91b347b7872.ngrok.io')
window.show()
app.exec_()
