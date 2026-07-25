from services.llm import generate_response


def career_agent(user_query):

    prompt = f"""
You are an IT career assistant.

User question:
{user_query}

Give professional IT career guidance with skills, roadmap and advice.
"""

    return generate_response(prompt)