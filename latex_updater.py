import google.generativeai as genai
from config import GOOGLE_API

genai.configure(api_key=GOOGLE_API)

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def get_newresumelatex(old_latex, job_desc):
    prompt_parts = [
        f"""
        Make modifications in the following resume details {old_latex} to apply the following job description {job_desc}. Return the latex code (no markdown, pure code).  
        """
    ]

    # prompt_parts = "sachin"

    response = model.generate_content(prompt_parts)
    return response.text