import os

from dotenv import load_dotenv

from google import genai


def generate_test_cases(context):

    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:

        raise ValueError(
            "GOOGLE_API_KEY not found in .env"
        )

    client = genai.Client(
        api_key=api_key
    )

    prompt = f"""
You are a Senior QA Engineer.

Generate test cases from these requirements.

Requirements:

{context}

Return ONLY a JSON array.

Format:

[
  {{
    "TC_ID":"TC001",
    "Description":"Valid login",
    "Preconditions":"User account exists",
    "Test_Steps":"Enter email, Enter password, Click Login",
    "Expected_Result":"User is redirected to dashboard",
    "Priority":"High"
  }}
]

Rules:

1. Return ONLY JSON.

2. No explanations.

3. No markdown.

4. Include positive, negative and edge cases.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    import json

    return json.loads(response.text)


if __name__ == "__main__":

    sample = """
The system shall allow users to log in using a registered email address and password.
"""

    output = generate_test_cases(
        sample
    )

    print(output)