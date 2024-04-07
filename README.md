# seo2go
Use AI to steal millions of dollars worth of content marketing from your competitors and level the SEO playing field. Performs text summarization through Telegram bot that generates concise summaries of text, URLs, PDFs and YouTube videos.

## Features

- Supports text
- Supports URLs
- Supports PDFs
- Supports YouTube videos (no support for YouTube Shorts)

## Usage

Launch a OpenAI GPT-4 summary bot that only can be used by your friend and you.

```sh
docker run -d \
    -e LLM_MODEL=gpt-4 \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    -e TELEGRAM_TOKEN=$YOUR_TG_TOKEN \
    -e TS_LANG=$YOUR_LANGUAGE \
    -e ALLOWED_USERS=<your_friends_id>,<your_id> \
    tonypai/summary-gpt-bot:latest
```

Launch a summary bot using Azure OpenAI.

```sh
docker run -d \
    -e AZURE_API_BASE=https://<your_azure_resource_name>.openai.azure.com \
    -e AZURE_API_KEY=$AZURE_API_KEY \
    -e AZURE_API_VERSION=2024-02-15-preview \
    -e LLM_MODEL=azure/<your_deployment_name> \
    -e TELEGRAM_TOKEN=$YOUR_TG_TOKEN \
    -e TS_LANG=$YOUR_LANGUAGE \
    tonypai/summary-gpt-bot:latest
```

LLM Variables

| Environment Variable | Description |
|----------------------|-------------|
| AZURE_API_BASE       | API URL base for AZURE OpenAI API |
| AZURE_API_KEY        | API key for AZURE OpenAI API |
| AZURE_API_VERSION    | API version for AZURE OpenAI API |
| OPENAI_API_KEY       | API key for OpenAI API |

Bot Variables

| Environment Variable | Description |
|----------------------|-------------|
| CHUNK_SIZE           | The maximum token of a chunk when receiving a large input (default: 10000) |
| LLM_MODEL            | LLM Model to use for text summarization (default: gpt-3.5-turbo-16k) |
| TELEGRAM_TOKEN       | Token for Telegram API (required) |
| TS_LANG              | Language of the text to be summarized (default: Taiwanese Mandarin) |
| ALLOWED_USERS        | You can get your own ID by asking to @myidbot (optional) |


# SUMMARIZER

Takes any news article and extract a brief summary from it. 

Summaries are created by ranking sentences in a news article according to how relevant they are to the entire text. The top 5 sentences are used to form a "summary". Each sentence is ranked by using four criteria:

Relevance to the title
Relevance to keywords in the article
Position of the sentence
Length of the sentence
Installation:

Requires Python 2.7. (Need Collections.Counter)

sudo pip install pyteaser
These dependency packages will be automatically installed:

Pillow
lxml
cssselect
jieba
beautifulsoup
Note: if you're installing on Windows, you have to install one of the dependency package lxml manually using:

easy_install lxml==2.3.3
More information about this issue here: #17

Usage:

sample command:

>>> from pyteaser import SummarizeUrl
>>> url = 'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html'
>>> summaries = SummarizeUrl(url)
>>> print summaries
output

["Twitter\'s move is the latest response from U.S. Internet firms following disclosures by former spy agency contractor Edward Snowden about widespread, classified U.S. government surveillance programs.", "\\"Since then, it has become clearer and clearer how important that step was to protecting our users\' privacy.\\"", "The online messaging service, which began scrambling communications in 2011 using traditional HTTPS encryption, said on Friday it has added an advanced layer of protection for HTTPS known as \\"forward secrecy.\\"", "\\"A year and a half ago, Twitter was first served completely over HTTPS,\\" the company said in a blog posting.", " \\"I\'m glad this is the direction the industry is taking.\\" \\n\\n(Reporting by Jim Finkle; editing by Andrew Hay)"]

you can use Summarize(title, text) directly if you already have the text and the title. Otherwise you must install Python Goose to extract text from url.
