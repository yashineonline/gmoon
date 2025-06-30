[Start]
   ↓
[Collect Profile Info]
   ↓
[LangChain Agent: Skill Extractor]
   ↓
[LangChain Agent: Job Matcher]
   ↓
[Output: Job Suggestions + Links + Score]

from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

response = agent.run("What kind of job fits someone skilled in carpentry, driving, and electrical wiring?")
