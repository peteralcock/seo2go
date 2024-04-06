import requests
import csv
from openai import OpenAI

def openai_api_calculate_cost(usage,model="gpt-4-1106-preview"):
    pricing = {
        'gpt-3.5-turbo-1106': {
            'prompt': 0.001,
            'completion': 0.002,
        },
        'gpt-4-1106-preview': {
            'prompt': 0.01,
            'completion': 0.03,
        },
        'gpt-4': {
            'prompt': 0.03,
            'completion': 0.06,
        }
    }

    try:
        model_pricing = pricing[model]
    except KeyError:
        raise ValueError("Invalid model specified")

    prompt_cost = usage.prompt_tokens * model_pricing['prompt'] / 1000
    completion_cost = usage.completion_tokens * model_pricing['completion'] / 1000

    total_cost = prompt_cost + completion_cost
    # round to 6 decimals
    total_cost = round(total_cost, 6)

    print(f"\nTokens used:  {usage.prompt_tokens:,} prompt + {usage.completion_tokens:,} completion = {usage.total_tokens:,} tokens")
    print(f"Total cost for {model}: ${total_cost:.4f}\n")

    return total_cost


def read_meta_data_from_csv(file_path):
    pages = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['title']
            description = row['description']
            url = row['url']
            pages.append(f"{title}: {description} \n\nSource:({url})")
    return pages


seo_keywords = [
    'growth hacking','seo optimization', 'puppies'
]
openai_api_key = "YOUR_OPENAI_KEY"
client = OpenAI(api_key=openai_api_key)
response = requests.get(url)
messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Title: {page_title}\nDescription: {page_description}\n\nGiven the above meta data, generate a wordpress blog post in your own words and output the content optimized for these SEO keywords: {' '.join(seo_keywords)}"}
                ]
openai_response = client.chat.completions.create(
model="gpt-3.5-16k",
messages = messages,
max_tokens = 16000,
temperature = 0.3)
new_post = openai_response.choices[0].message.content
print(f"Title: {title}")
print(f"Content: {content}")

