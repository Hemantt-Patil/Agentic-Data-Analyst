import os
import aiohttp
import json
import pandas as pd

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class AnalystAgent:
    async def analyze(self, df: pd.DataFrame):
        sample_data = df.head(10).to_dict(orient="records")
        prompt = (
            "You are a data scientist. Analyze this dataset for patterns, outliers, "
            "and key correlations. Return a professional markdown report.\n\n"
            f"DATA SAMPLE:\n{sample_data}"
        )

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 1000
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(GROQ_API_URL, json=payload, headers=headers, timeout=60) as resp:
                res = await resp.json()
                try:
                    return res["choices"][0]["message"]["content"]
                except Exception:
                    return "ERROR_ANALYST: " + json.dumps(res)
