import tiktoken

def count_tokens_with_tiktoken(text, model_name="gpt-3.5-turbo"):
    """Return the number of tokens in a text string using tiktoken."""
    encoding = tiktoken.encoding_for_model(model_name)
    return len(encoding.encode(text))

text_sample = "ChatGPT is great!"
tokens = count_tokens_with_tiktoken(text_sample)
print(f"'{text_sample}' consists of {tokens} tokens.")

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
