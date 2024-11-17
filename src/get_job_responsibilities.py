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
    Please update the content of my resume based on the job posting below. I want you to analyze the job description and incorporate relevant keywords and phrases into my existing resume content to improve ATS compatibility.

    I want you to try to keep the length of the resume content the same as before so that it does not exceed the second page. Please highlight all and only the areas which you update.

    Here’s the job posting: {job_description}

    And here’s my current resume content: {resume}
    """
)

# Calls the function to generate the response by passing the prompt template
job_responsibilities = gen_resp.generate_response(
    prompt=prompt,
    input_variables={'job_description': job_description, 'resume': resume}
    )

# Prints the response.
print(job_responsibilities)