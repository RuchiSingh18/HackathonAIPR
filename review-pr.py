# review-pr.py
import os
import openai
import sys
import requests

# Get OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get diff input
diff = sys.stdin.read()

# Call ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a senior software engineer helping with code review. Provide feedback on the pull request diff provided."
        },
        {
            "role": "user",
            "content": f"Here is the diff:\n\n{diff}"
        }
    ],
    temperature=0.3,
    max_tokens=1000
)

review = response.choices[0].message["content"]
print(review)
