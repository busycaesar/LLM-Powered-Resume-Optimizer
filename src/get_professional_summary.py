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
    Please analyze the following job posting and my current resume content, and generate a professional summary that aligns with the job description. The summary should highlight my relevant skills, experience, and accomplishments that are a strong match for the role. Please make sure the summary is 3 lines max, concise, impactful, and tailored to the job posting while keeping the tone professional.

    Here’s the job posting: {job_description}

    And here’s my current resume content: {resume}

    Please focus on the key qualifications and tailor the summary accordingly.
    """
)

# Calls the function to generate the response by passing the prompt template
professional_summary = gen_resp.generate_response(
    prompt=prompt, 
    input_variables={'job_description': job_description, 'resume': resume}
    )

# Prints the response.
print(professional_summary)