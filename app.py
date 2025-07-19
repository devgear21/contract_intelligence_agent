import streamlit as st
import os
from langsmith import Client
from contract_graph import create_contract_intelligence_agent
from tempfile import NamedTemporaryFile

# Initialize LangSmith client once
langsmith_client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))

# Create LangGraph agent with LangSmith tracing
agent = create_contract_intelligence_agent(langsmith_client)

st.title("Enterprise Contract Intelligence Agent")

uploaded_file = st.file_uploader("Upload a contract file (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    st.info(f"Processing file: {uploaded_file.name}")

    # Run LangGraph agent pipeline
    with st.spinner("Analyzing contract..."):
        try:
            result = agent.invoke({"contract_file": tmp_file_path})
            report = result.get("structured_report", "No report generated.")
            st.markdown(report)
        except Exception as e:
            st.error(f"Error during processing: {e}")

    # Clean up temp file
    os.remove(tmp_file_path)
else:
    st.info("Please upload a PDF or DOCX contract file to get started.")
