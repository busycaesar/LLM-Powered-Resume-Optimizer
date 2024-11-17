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
    Please analyze the following job posting and resume content for ATS compatibility. Assess how well the resume aligns with the job re71uirements, and provide a score (from 0 to 100) indicating the likelihood of the ATS selecting this resume. Additionally, offer specific suggestions with the updated content for each section wherever required, to improve the resume to increase its score to 80%.

    Job Posting: {job_description}

    Resume Content: {resume}
    """
)

# Calls the function to generate the response by passing the prompt template
resume_score_and_suggestions = gen_resp.generate_response(
    prompt=prompt,
    input_variables={'job_description': job_description, 'resume': resume}
    )

# Prints the response.
print(resume_score_and_suggestions)