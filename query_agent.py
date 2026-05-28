from crewai import Agent

query_agent = Agent(
    role="Audit Query Analyzer",

    goal="Understand audit requests and identify entities",

    backstory="Expert audit assistant with accounting knowledge",

    verbose=True
)