import os
from dotenv import load_dotenv
from groq import Groq

from prompts import CLAIM_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_claims(text):

    prompt = CLAIM_PROMPT.format(text=text)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    claims_text = response.choices[0].message.content

    claims = []

    for line in claims_text.split("\n"):

        line = line.strip()

        if line:
            claims.append(line)

    return claims