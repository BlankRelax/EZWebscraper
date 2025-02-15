import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AISummarize:

    api_key = os.environ["OPENAI_API_KEY"] 
    client = OpenAI(
        api_key=api_key
    )
        
    
    @classmethod
    def summarize(cls, text:str):
        print("------------------\n AI Summarization in Progress \n------------------")
        r = cls.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a world-renowed English professor, who made a career on summarizing news articles into 50 words or less. You will be given news articles which you NEED to summarize into 50 words.  ",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Summarize this news article for me: {text}. Give me the summary ONLY, and no extra text",
                        }
                    ],
                },
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "text"},
        )
        return r.choices[0].message.content

    
