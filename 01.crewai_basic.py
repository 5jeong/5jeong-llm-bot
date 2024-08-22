
from crewai import Crew, Agent, Task 
from langchain_ollama import ChatOllama


# llm = ChatOllama(
#     model="phi3:3.8b",
#     base_url='http://127.0.0.1:11434'
# )

# Ollama와 연결된 LLM 생성
llm = ChatOllama(
    model="phi3:3.8b",
    base_url="http://localhost:11434"
)

# CrewAI 에이전트 생성
general_agent = Agent(
    role="Math Professor",
    goal="""Provide the solution to the students that are asking mathematical questions and give them the answer.""",
    backstory="""You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Task 생성
task = Task(
    description="""What is 3 + 5?""",
    agent=general_agent,
    expected_output="A numerical answer."
)

# Crew 객체 생성 및 작업 시작
crew = Crew(
    agents=[general_agent],
    tasks=[task],
    verbose=True
)

# 작업 수행
result = crew.kickoff()

# 결과 출력
print(result)