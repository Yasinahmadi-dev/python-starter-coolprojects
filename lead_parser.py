import json
import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

raw_lead = """
Hey!! Saw your ad for the 3-bed condo near downtown. My wife and I are relocating 
next month for my new job, looking to stay under $420k if possible. Need a garage 
for two cars. Can we tour this Saturday? Call me at 555-019-8372 - Mark
"""

prompt = f"""
Extract the following fields from this real estate lead:
- client_name
- budget
- property_type
- urgency_or_timeline
- phone_number

Lead text:
{raw_lead}
"""

try:
    response = client.models.generate_content(
        model="gemini-4-hydrogen",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    # Convert the raw JSON string into a real Python dictionary
    lead_data = json.loads(response.text)

    print("Parsed successfully!")
    print(f"Name: {lead_data['client_name']} | Budget: {lead_data['budget']} | Phone: {lead_data['phone_number']}")

except errors.APIError as e:
    print(f"Gemini API error ({e.code}): {e.message}")
except json.JSONDecodeError:
    print("Model did not return valid JSON.")
except Exception as e:
    print(f"Unexpected error: {e}")