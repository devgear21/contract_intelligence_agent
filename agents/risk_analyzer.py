from langchain_groq.chat_models import ChatGroq
import os

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    reasoning_format="parsed",
    timeout=30,
    max_retries=2,
)

def risk_analyzer_node(state: dict) -> dict:
    deviations = state.get("deviations")
    if not deviations:
        raise ValueError("No deviations found in state.")

    risk_results = {}

    for clause_name, info in deviations.items():
        prompt = f"""
        Evaluate the legal risk of the following clause. Label as Low, Medium, or High risk and explain why.

        Clause Name: {clause_name}
        Clause Text: {info['extracted']}
        Standard Clause: {info['standard']}
        Deviation Flag: {info['deviation_flag']}
        """

        messages = [
            {"role": "system", "content": "You are a legal risk assessment assistant."},
            {"role": "user", "content": prompt},
        ]

        response = llm.invoke(messages)
        risk_results[clause_name] = response.content

    state["risk_analysis"] = risk_results
    return state
