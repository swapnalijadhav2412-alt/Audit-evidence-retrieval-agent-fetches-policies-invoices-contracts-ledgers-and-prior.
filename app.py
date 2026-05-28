from crewai import Task, Crew

from agents.query_agent import query_agent
from agents.planner_agent import planner_agent
from agents.retrieval_agent import retrieval_agent
from agents.validation_agent import validation_agent
from agents.report_agent import report_agent
query_task = Task(
    description="""
    Analyze the audit request.

    Identify:
    - transaction IDs
    - vendors
    - control names
    - evidence needed
    """,

    agent=query_agent
)
planning_task = Task(
    description="""
    Determine required evidence.

    Required documents may include:
    - invoices
    - contracts
    - approvals
    - policies
    - ledger entries
    - prior workpapers
    """,
    agent=planner_agent
)


retrieval_task = Task(
    description="""
    Retrieve relevant documents from vector database.
    """,

    agent=retrieval_agent
)
validation_task = Task(
    description="""
    Validate evidence quality.

    Check:
    - completeness
    - relevance
    - confidence score
    - duplicates
    """,

    agent=validation_agent
    )


report_task = Task(
    description="""
    Generate final audit evidence report.
    """,

    agent=report_agent
)


crew = Crew(
    agents=[
        query_agent,
        planner_agent,
        retrieval_agent,
        validation_agent,
        report_agent
    ],

    tasks=[
        query_task,
        planning_task,
        retrieval_task,
        validation_task,
        report_task
    ],

    verbose=True
)


result = crew.kickoff(
    inputs={
        "query": "Fetch invoice and approval evidence for vendor ABC Ltd"
    }
    )

print(result)