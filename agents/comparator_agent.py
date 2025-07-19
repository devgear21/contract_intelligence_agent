import json

def comparator_node(state: dict) -> dict:
    clauses = state.get("clauses")
    if not clauses:
        raise ValueError("No clauses found in state.")

    with open("./data/standards.json", "r") as f:
        standards = json.load(f)

    deviations = {}

    for clause_name, clause_text in clauses.items():
        standard_text = standards.get(clause_name, "")
        deviation_flag = clause_text.strip() != standard_text.strip()
        deviations[clause_name] = {
            "extracted": clause_text,
            "standard": standard_text,
            "deviation_flag": deviation_flag,
        }

    state["deviations"] = deviations
    return state
