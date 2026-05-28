from crewai import Agent

report_agent = Agent(
    role="Audit Reporting Specialist",

    goal="Generate audit-ready evidence summaries",

    backstory="Expert audit documentation specialist",

    verbose=True
)