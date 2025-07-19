import os
from utils.pdf_parser import extract_text_from_pdf
from utils.docx_parser import extract_text_from_docx

def reader_node(state: dict) -> dict:
    file_path = state.get("contract_file")
    if not file_path or not os.path.exists(file_path):
        raise ValueError("Contract file path is missing or invalid.")
        

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")

    state["raw_text"] = text
    return state  # ✅ LangGraph expects a state dict, not Command
