# Contract Analysis System

A sophisticated contract analysis system built with LangGraph and LangChain that automatically extracts, compares, and analyzes legal clauses from contracts.

## Features

- **Contract Parsing**: Supports PDF and DOCX contract documents
- **Clause Extraction**: Automatically extracts key clauses (Termination, Indemnity, Confidentiality, Jurisdiction, Payment terms)
- **Comparison Analysis**: Compares extracted clauses against standard templates
- **Risk Assessment**: Evaluates legal risk levels (Low, Medium, High) for deviations
- **Report Generation**: Creates comprehensive analysis reports

## Architecture

The system uses a LangGraph-based agent architecture with the following components:

- **Reader Agent**: Parses and extracts text from contract documents
- **Clause Extractor**: Uses LLM to identify and extract specific clause types
- **Comparator Agent**: Compares extracted clauses with standard templates
- **Risk Analyzer**: Assesses legal risk levels for clause deviations
- **Report Generator**: Creates final analysis reports

## Models Used

- **Clause Extraction**: LLaMA 3 70B via Groq
- **Risk Analysis**: DeepSeek R1 Distill LLaMA 70B via Groq

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd contract-analysis-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Groq API key:
```bash
export GROQ_API_KEY="your-api-key-here"
```

## Usage

Run the main application:
```bash
python main.py
```

Or use the Flask web interface:
```bash
python app.py
```

## Project Structure

```
├── agents/
│   ├── clause_extractor.py    # Extracts clauses from contracts
│   ├── comparator_agent.py    # Compares against standards
│   ├── reader_agent.py        # Document parsing
│   ├── report_generator.py    # Report creation
│   └── risk_analyzer.py       # Risk assessment
├── data/
│   ├── standards.json         # Standard clause templates
│   └── contracts/            # Sample contracts
├── utils/
│   ├── docx_parser.py        # DOCX document parser
│   └── pdf_parser.py         # PDF document parser
├── contract_graph.py         # LangGraph workflow definition
├── main.py                   # CLI interface
├── app.py                    # Flask web interface
└── requirements.txt          # Python dependencies
```

## License

This project is licensed under the MIT License.
