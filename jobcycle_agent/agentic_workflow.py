# jobcycle_agent/agentic_workflow.py

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent, AgentType 
import os

### INITIALIZE BACKEND LLM
## Uncomment ONE OPTION ONLY

# --- OPTION 1: OpenAI ---
# from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI(temperature=0, model="gpt-4")

# --- OPTION 2: Groq ---
# from langchain.llms import Groq
# llm = Groq(api_key=os.getenv("GROQ_API_KEY"), model_name="mixtral-8x7b")

# --- OPTION 3: Gemini (Google AI) ---
# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))

# --- OPTION 4: HuggingFace Local (Offline) ---
# from langchain.llms import HuggingFacePipeline
# from transformers import pipeline
# local_pipe = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", device=0)
# llm = HuggingFacePipeline(pipeline=local_pipe)

### SETUP PROMPTS

profile_prompt = PromptTemplate.from_template(
    """
You are a job coach. A user gave the following profile:
{input}
Extract the key professional and technical skills from this.
Respond with a comma-separated list.
"""
)

job_match_prompt = PromptTemplate.from_template(
    """
You are a job assistant. Given the following skills:
{skills}
Find 3 possible job roles that match this and explain why.
"""
)

### CHAINS

extract_skills_chain = LLMChain(llm=llm, prompt=profile_prompt)
job_match_chain = LLMChain(llm=llm, prompt=job_match_prompt)


### NODE LOGIC FOR LANGGRAPH FLOW 

def collect_profile(state):
    print("[INFO] Collecting profile data...")
    return state  # Already contains 'profile_data'

def extract_skills(state):
    profile = state["profile_data"]
    skills_raw = extract_skills_chain.run(input=profile)
    state["skills"] = [s.strip() for s in skills_raw.split(",")]
    return state

def match_jobs(state):
    skills_str = ", ".join(state["skills"])
    job_matches = job_match_chain.run(skills=skills_str)
    state["job_matches"] = [job_matches]
    return state

