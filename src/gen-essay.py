import csv
import requests
import json

def generate_essay(prompt, model="gpt-4-1106-preview"):
    """
    Generate an essay using OpenAI's GPT-3 or GPT-4 model.

    :param prompt: The prompt to provide to the model.
    :param model: The model to use ('text-davinci-003' for GPT-3, 'text-davinci-004' for GPT-4).
    :param max_tokens: The maximum number of tokens to generate.
    :return: The generated essay as a string.
    """
    api_key = ""  # Replace with your actual API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": model,
        "temperature": 0.7
    }

    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print(f"Error: {response.json()}")
        return None

# Example usage
prompt = """
More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends. Write a letter to your local newspaper in which you state your opinion on the effects computers have on people. Persuade the readers to agree with you.
"""

# prompt = """
# """

# prompt = """
# """

# Prepare CSV file for writing
with open('./data/gpt4-essays.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'prompt_id', 'text'])  # Write the header

    prompt_id = 1  # Assuming a static prompt_id for simplicity
    for i in range(1, 1786):  # Adjusted to start from 1 for better id management
        essay = generate_essay(prompt)  # Call the function to generate an essay
        if essay:  # If an essay is successfully generated
            writer.writerow([i, prompt_id, essay])  # Write the essay to the CSV file