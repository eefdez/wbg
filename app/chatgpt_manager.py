import openai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config.get("GPT", 'api_key')


def get_summary(text):
    prompt = f'Summarize the following text:\n{text}'

    response = openai.Completion.create(
        engine="text-davinci-003",   # GPT-3.5 Turbo
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()
