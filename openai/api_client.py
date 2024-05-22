import openai

class APIClient:
    def __init__(self):
        openai.api_key = 'your-api-key'

    def get_response(self, message):
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=message,
          temperature=0.5,
          max_tokens=100
        )

        return response.choices[0].text.strip()