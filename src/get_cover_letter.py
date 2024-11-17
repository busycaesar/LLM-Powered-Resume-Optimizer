import generate_response as gen_resp
from langchain.prompts import PromptTemplate
from documents import get_job_description, get_resume

# Get Job Description and Resume.
job_description = get_job_description()
resume = get_resume()

# Creates a Prompt Template
prompt = PromptTemplate(
    input_variables=["job_description","resume"],
    template="""
    Please analyze the following job posting and my resume content. Based on my experience, skills, and projects, provide me with three very strong reasons why I am the most ideal candidate for the position. Each point should be in the first person, no more than 3-4 sentences, and should clearly persuade and convince the reader that I am the most eligible candidate for the job. Please do not use high vocabulary.

    Job Posting: {job_description}

    Resume Content: {resume}
    """
)

# Calls the function to generate the response by passing the prompt template
cover_letter = gen_resp.generate_response(
    prompt=prompt, 
    input_variables={'job_description': job_description, 'resume': resume}
    )

# Prints the response.
print(cover_letter)