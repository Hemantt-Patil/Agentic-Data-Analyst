import os
import aiohttp
import json

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class SummaryAgent:
    async def summarize(self, analysis: str, insights: str):
        prompt = (
            "You are a senior AI analyst preparing an executive report. "
            "Combine the technical analysis and the business insights below "
            "into a concise, professional markdown summary.\n\n"
            f"TECHNICAL ANALYSIS:\n{analysis}\n\n"
            f"BUSINESS INSIGHTS:\n{insights}\n\n"
            "Format with headings: 'Summary', 'Key Insights', 'Next Steps'."
        )

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.25,
            "max_tokens": 800
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(GROQ_API_URL, json=payload, headers=headers, timeout=40) as resp:
                res = await resp.json()
                try:
                    return res["choices"][0]["message"]["content"]
                except Exception:
                    return "ERROR_SUMMARY: " + json.dumps(res)
