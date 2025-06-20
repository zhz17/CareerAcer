import os
import time
from mcp.server.fastmcp import FastMCP

# initialize the FastMCP server
server = FastMCP("CareerAcer", "0.1.0")

job = ""

@server.tool()
def load_cvs(cv_path: str) -> list:
    """
    Tool to load a CV from a specified path.
    """
    if not os.path.isdir(cv_path):
        raise FileNotFoundError(f"CV directory not found: {cv_path}")
    
    return os.listdir(cv_path)
    
@server.tool()
def result_storage(result: str) -> str:
    """
    Tool to store results in a file.
    """
    # Define the path to the results file
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_file = f"results_{timestamp}.txt"
    # Open the file in append mode and write a sample result
    with open(results_file, "a") as file:
        file.write(f"{result}\n")
    
    return f"Results stored in {results_file}"


@server.prompt()
def job_ad_analysis_prompt(url: str) -> str:
    """Generate a prompt for LLM to analysis the info from a job posting page."""
    job = url
    return f"""Look at the job advertisement on this website: {url}. Follow these instructions:
    1. First, analyze the job description and requirements.
    2. List the key skills and qualifications required for the job.
    3. List 10 most possible technical interview questions that could be asked based on the job description.
    4. Provide a brief summary of the company and its culture based on the information from job posting and web searching.
    5. Simulate a daily work routine for this job role, including tasks and responsibilities."""
    
@server.prompt()
def list_cvs_prompt() -> str:
    """Generate a prompt for LLM to list all files in cv folder."""
    return f"""List all the files using list_directory(path="../resource")."""

@server.prompt()
def match_cvs_prompt(cv: str, url=job) -> str:
    """Generate a prompt for LLM to list all files in cv folder."""
    return f"""Read the cv file using read_file(path="../resource/{cv}"). With the information in the CV and job advertisement {url}, analyze if the skills and qualifications of the candidate match the job. Give a score from 0 to 100, where 0 means no match and 100 means perfect match. Provide a brief explanation of the score and the reasons for it. If the CV is not suitable, provide suggestions for improvement."""

@server.prompt()
def generate_cletter_prompt(cv: str, url=job) -> str:
    """Generate a prompt for LLM to list all files in cv folder."""
    return f"""Read the cv file using read_file(path="../resource/{cv}"). With the information in the CV and job advertisement {url}, generate a cover letter for the job. The cover letter should be concise, professional, and tailored to the job description. It should highlight the candidate's skills and qualifications that match the job requirements. The cover letter should be in a format suitable for submission with the CV."""

'''
To Be Added Later (List of prompts for various career-related tasks):

1) Company research

Prompt:
"I have an interview with __________ (company) for the position of __________ (job). Please summarize the company's mission, its main products or services and its recent news or achievements by analyzing its website __________ (website link) and any recent press release"


2) Resume optimization

Prompt:
"Review my current attached resume and suggest improvements tailored to applying for a __________ (job) at __________ (company). Highlight gaps in my experience and recommend ways to fill them through online courses or projects"


3) Writing the cover letter

Prompt:
"Based on the job description for __________ (job title) at __________ (company), generate a cover letter that highlights my relevant experience, skills and why I am passionate about working for __________ (company)"


4) Interview preparation

Prompt:
"For __________ (job title) at __________ (company), what are some industry-specific challenges or trends I should be aware of? How can I demonstrate my understanding or propose possible solutions during the interview?"


5) Behavioral interview questions

Prompt:
"Create a set of behavioral interview questions relevant to the __________ (job) role at __________ (company). Include a brief guide on how to structure answers using the STAR (Situation, Task, Action, Result) method, tailored to my needs"


6) Craft your resume perfectly

Prompt:
"I want to tailor my resume to specific job descriptions so I get shortlisted more often. Analyze this job posting for __________ (job title), extract the most important keywords and skills and help me rewrite my resume to match it perfectly while maintaining authenticity"


7) Data-driven job search

Prompt:
"I want to use data and hiring trends to increase my chances of landing a high-paying job in __________ (industry). Provide me with data-backed job searches strategies, salary benchmarks and negotiation tips based on market trends"


8) Network like a pro

Prompt:
"I want to build relationships with influential professionals in __________ (industry) to increase my chances of getting a job. Give me a step-by-step networking strategy, including outreach messages, follow-ups and ways to provide value to them"


9) Craft the perfect elevator pitch

Prompt:
"I need a powerful 30-second elevator pitch that instantly impresses interviewers for __________ (job title). Craft a clear, concise and compelling pitch that highlight my skills, experience and what makes me unique"
'''


if __name__ == "__main__":
    # Initialize and run the server
    server.run(transport='stdio')