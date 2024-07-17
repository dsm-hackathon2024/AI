import openai
from fastapi import APIRouter, HTTPException
from model.gpt import Prompt
import os

os.environ["OPENAI_API_KEY"] = "#"
api_key = os.environ["OPENAI_API_KEY"]
if not api_key:
    raise ValueError("OpenAI API key is not set in the environment variables.")
openai.api_key = api_key

router = APIRouter()

@router.post("/")
def generate_answer(prompt: Prompt):
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key is not set.")
    
    pre_prompt = "한국어로 :)\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "안녕하세요 Noise 입니다!"},
            {"role": "user", "content": pre_prompt + prompt.prompt}
        ],
        max_tokens=3000,
        stop=None,
        temperature=0.5
    )
    answer = response.choices[0].message.content.strip()
    return {'answer': answer}
