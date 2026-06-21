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

Generate software test cases from these requirements.

Requirements:

{context}

For every requirement generate:

- Test Case ID
- Description
- Preconditions
- Test Steps
- Expected Result
- Priority

Include:

- Positive test cases

- Negative test cases

- Edge cases

Format the response clearly.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    sample = """
The system shall allow users to log in using a registered email address and password.
"""

    output = generate_test_cases(
        sample
    )

    print(output)