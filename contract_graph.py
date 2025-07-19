# contract_graph.py

from langgraph.graph import StateGraph
from langsmith import Client
from langchain.callbacks.tracers.langchain import LangChainTracer

# Import your agent nodes
from agents.reader_agent import reader_node
from agents.clause_extractor import extractor_node
from agents.comparator_agent import comparator_node
from agents.risk_analyzer import risk_analyzer_node
from agents.report_generator import report_generator_node

def create_contract_intelligence_agent(langsmith_client: Client = None):
    # Initialize the LangGraph with a simple dict state
    graph = StateGraph(dict)

    # Add nodes to the graph
    graph.add_node("reader", reader_node)
    graph.add_node("extractor", extractor_node)
    graph.add_node("comparator", comparator_node)
    graph.add_node("risk_analyzer", risk_analyzer_node)
    graph.add_node("report_generator", report_generator_node)

    # Define graph edges (execution flow)
    graph.set_entry_point("reader")
    graph.add_edge("reader", "extractor")
    graph.add_edge("extractor", "comparator")
    graph.add_edge("comparator", "risk_analyzer")
    graph.add_edge("risk_analyzer", "report_generator")

    # Final node
    graph.set_finish_point("report_generator")

    # Compile the graph
    app = graph.compile()

    # Use LangSmith tracing if a client is provided
    if langsmith_client:
        tracer = LangChainTracer(
            project_name="Contract Intelligence",
            client=langsmith_client
        )
        return app.with_config({"callbacks": [tracer]})

    return app
