import requests
import csv
from openai import OpenAI


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

