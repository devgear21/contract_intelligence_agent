import os
from langsmith import Client
from contract_graph import create_contract_intelligence_agent


def main():
    langsmith_client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))
    agent = create_contract_intelligence_agent(langsmith_client)

    input_data = {"contract_file": "./data/contracts/sample_contract.pdf"}

    result = agent.invoke(input_data)

    print(result.get("structured_report"))

if __name__ == "__main__":
    main()
