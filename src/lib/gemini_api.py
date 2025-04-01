import os

from google import genai

GEMINI_KEY = os.environ.get("GEMINI_KEY")


def query(prompt):
    try:
        client = genai.Client(api_key=GEMINI_KEY)
        response = client.models.generate_content(
            # model="gemini-2.0-flash",
            model="gemini-2.0-flash-lite",
            # model="gemini-2.0-pro-exp-02-05",
            contents=prompt,
        )
    except Exception as e:
        print(f"Gemini APIエラー: {e}")
        return None

    output_text = response.text
    return output_text.strip()
