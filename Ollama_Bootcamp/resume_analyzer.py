import ollama

MODEL = "qwen2.5:1.5b"

def analyze_resume(resume_text):

    prompt = f"""
You are an experienced HR Manager and ATS Resume Expert.

A candidate has already uploaded their resume.

Your job is to analyze it.

Never ask the user to upload the resume.
Never ask for more information.

Here is the resume:

------------------------
{resume_text}
------------------------

Please produce a report with these headings:

## ATS Score (out of 100)

## Professional Summary

## Technical Skills

## Strengths

## Weaknesses

## Missing Skills

## Resume Improvements

## Suitable Job Roles

## Five Interview Questions

Start your analysis immediately.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]