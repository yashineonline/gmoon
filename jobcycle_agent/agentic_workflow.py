# jobcycle_agent/agentic_workflow.py

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent, AgentType
import os

# Define prompt templates
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

# Initialize LLM
llm = ChatOpenAI(temperature=0, model="gpt-4")

extract_skills_chain = LLMChain(llm=llm, prompt=profile_prompt)
job_match_chain = LLMChain(llm=llm, prompt=job_match_prompt)

# Node logic for LangGraph flow

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
