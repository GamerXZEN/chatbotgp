from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, \
	QPushButton, QTextEdit
import sys
from backend import ChatBot
import threading


class ChatbotWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("ChatbotGPT")
		self.setMinimumSize(505, 410)
		self.chatbot = ChatBot()

		self.chat_area = QTextEdit(self)
		self.chat_area.setGeometry(10, 10, 480, 320)
		self.chat_area.setReadOnly(True)
		self.verScrollBar = self.chat_area.verticalScrollBar()

		self.input_box = QLineEdit(self)
		self.input_box.returnPressed.connect(self.send_message)
		self.input_box.setGeometry(10, 340, 380, 30)

		send_button = QPushButton("Send", self)
		send_button.clicked.connect(self.send_message)
		send_button.setGeometry(400, 340, 90, 30)

		clear_button = QPushButton("Clear", self)
		clear_button.clicked.connect(self.chat_area.clear)
		clear_button.setGeometry(400, 372, 90, 30)

		self.show()

	def send_message(self):
		user_input = self.input_box.text().strip()
		if user_input:
			self.chat_area.append(f"<p style='color:#333333'>You: {user_input}\n</p>")
			self.input_box.clear()

			thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
			thread.start()

	def get_bot_response(self, user_input):
		response = self.chatbot.get_response(user_input)
		self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}\n</p>")


try:
	if __name__ == "__main__":
		app = QApplication(sys.argv)
		window = ChatbotWindow()
		sys.exit(app.exec())
except ValueError:
	raise Exception("OpenAI GPT Error")
