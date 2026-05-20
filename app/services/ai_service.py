import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_document(text: str):

    prompt = f"""
    Analise o documento abaixo.

    Retorne:
    - categoria do documento
    - resumo curto
    - principais tópicos

    Documento:
    {text[:1500]}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content