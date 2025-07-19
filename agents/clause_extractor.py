import os
from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import JsonOutputKeyParser

# Initialize Groq LLM (LLaMA 3 or Mixtral preferred)
llm = ChatGroq(
    model="llama3-70b-8192",  # Or: "mixtral-8x7b-32768"
    temperature=0,
    max_tokens=2048,
    timeout=30,
    max_retries=2,
)

# Define prompt template for clause extraction
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a contract clause extraction assistant."),
    ("human", """
Extract the following clauses from the contract text below:
- Termination
- Indemnity
- Confidentiality
- Jurisdiction
- Payment terms

Respond ONLY with a valid JSON object like:
{
  "Termination": "...",
  "Indemnity": "...",
  "Confidentiality": "...",
  "Jurisdiction": "...",
  "Payment terms": "..."
}

Do not include any extra text, markdown, or explanation.

Contract Text:
\"\"\"
{contract_text}
\"\"\"
""")
])

# Output parser that expects JSON with a single top-level key
parser = JsonOutputKeyParser(key_name="clauses")

# Chain = prompt -> LLM -> parser
chain = prompt | llm | parser

# LangGraph node function
def extractor_node(state: dict) -> dict:
    raw_text = state.get("raw_text", "")
    if not raw_text:
        raise ValueError("[Extractor] No raw text found in state.")

    print(f"[Extractor] Raw text length: {len(raw_text)}")

    try:
        # Invoke the chain with raw contract text
        clauses = chain.invoke({"contract_text": raw_text})
        print("[Extractor] Extracted clauses:", clauses)
    except Exception as e:
        print("[Extractor] LLM or parser failed:", e)
        raise ValueError("[Extractor] Clause extraction failed.") from e

    # Inject into LangGraph state
    state["clauses"] = clauses
    return state
