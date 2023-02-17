import openai


class ChatBot:
	def __init__(self):
		openai.api_key = "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"

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
