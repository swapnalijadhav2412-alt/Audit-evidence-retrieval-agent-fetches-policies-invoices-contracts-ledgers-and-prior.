from crewai import Agent

planner_agent = Agent(
    role="Evidence Planning Specialist",

    goal="Identify required audit evidence",

    backstory="Experienced external auditor expert in SOX and financial controls",

    verbose=True
)