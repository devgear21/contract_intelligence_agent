def report_generator_node(state: dict) -> dict:
    deviations = state.get("deviations", {})
    risk_analysis = state.get("risk_analysis", {})

    report_lines = ["# Contract Review Report\n"]

    for clause, deviation_info in deviations.items():
        risk = risk_analysis.get(clause, "No risk analysis available.")
        flag = "⚠️" if deviation_info.get("deviation_flag") else "✅"

        report_lines.append(f"## {clause} {flag}")
        report_lines.append(f"**Extracted Clause:**\n{deviation_info.get('extracted')}\n")
        report_lines.append(f"**Standard Clause:**\n{deviation_info.get('standard')}\n")
        report_lines.append(f"**Risk Analysis:**\n{risk}\n")

    report = "\n".join(report_lines)
    state["structured_report"] = report

    return state
