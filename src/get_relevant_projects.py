from documents import get_job_description, get_projects
from langchain.prompts import PromptTemplate
from generate_response import generate_response

# Get the job description and list of projects
job_description = get_job_description()
projects = get_projects()

# Create a prompt template
prompt = PromptTemplate(
    input_variables=['job_description', 'projects'],
    template="""
    Given the following job posting and ATS keywords, along with my list of existing projects, can you provide a curated list of 3 projects most relevant to this role? I’d like the selection to highlight projects that align well with the required skills, experience, and job responsibilities described. Return me the list of project in the order of relevance along with the updated, maximum 2-3 line, description which increases the chances that ATS passes my resume. All the sentences of the description should be in active voice and starting with action word.

    Job Posting: {job_description}

    List of Projects: {projects}
    """
    )

# Call the function to generate the content
relevant_projects = generate_response(
    prompt=prompt, 
    input_variables={'job_description': job_description, 'projects': projects}
    )

# Print the response
print(relevant_projects)