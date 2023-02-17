import openai
import os


class ChatBot:
	def __init__(self):
		openai.api_key = os.getenv('OPENAI_API_KEY', default="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")

	@staticmethod
	def get_response(text):
		response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=text,
			temperature=0.5,
			max_tokens=4050).choices[0].text
		return response


if __name__ == "__main__":
	chatbot = ChatBot()
	while True:
		text = input("Enter your message: ")
		response = chatbot.get_response(text)
		print(response)
