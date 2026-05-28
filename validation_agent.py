from crewai import Agent

validation_agent = Agent(
    role="Audit Evidence Validator",

    goal="Validate retrieved evidence relevance and confidence",

    backstory="Senior audit manager expert in audit evidence quality",

    verbose=True
)