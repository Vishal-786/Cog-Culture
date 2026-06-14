import os
import json

from dotenv import load_dotenv
from groq import Groq

from prompts import VERIFY_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def verify_claim(claim, evidence):

    prompt = VERIFY_PROMPT.format(
        claim=claim,
        evidence=evidence
    )

    try:

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

        content = response.choices[0].message.content

        content = content.strip()

        result = json.loads(content)

        return result

    except Exception as e:

        return {
            "status": "ERROR",
            "explanation": str(e),
            "correct_fact": "Unable to verify"
        }