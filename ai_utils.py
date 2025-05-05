import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ad_copy(practice_area, location):
    prompt = f"Write a compelling Google ad for a {practice_area} attorney in {location}. Include a CTA."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
