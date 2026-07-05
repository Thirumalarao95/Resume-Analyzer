import ollama

def analyze_resume(resume_text):

    response = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert ATS Resume Reviewer and HR Manager. "
                    "Never ask the user to upload or provide the resume. "
                    "The resume is already included in the next message."
                )
            },
            {
                "role": "user",
                "content": f"""
Below is a candidate's resume.

========================
{resume_text}
========================

Analyze ONLY the resume above.

Return your response in this format:

# ATS Score

# Resume Summary

# Strengths

# Weaknesses

# Missing Skills

# Improvements

# Suitable Job Roles

# Five Interview Questions

Do not ask me to upload the resume.
Do not ask for additional information.
Start the analysis immediately.
"""
            }
        ]
    )

    return response["message"]["content"]