import json
from pathlib import Path

def extract_demo_data(transcript):

    memo = {
        "account_id": "bens_electric",
        "company_name": "Ben's Electric",
        "business_hours": {
            "days": None,
            "start": None,
            "end": None,
            "timezone": None
        },
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": None,
        "non_emergency_routing_rules": "Collect job details and schedule service",
        "call_transfer_rules": None,
        "integration_constraints": [],
        "after_hours_flow_summary": None,
        "office_hours_flow_summary": None,
        "questions_or_unknowns": [],
        "notes": ""
    }

    text = transcript.lower()

    if "residential" in text:
        memo["services_supported"].append("residential electrical work")

    if "commercial" in text:
        memo["services_supported"].append("commercial electrical work")

    if "service calls" in text:
        memo["services_supported"].append("electrical service calls")

    if "jobber" in text:
        memo["integration_constraints"].append("CRM: Jobber")

    return memo


def save_memo(memo):

    output_path = Path("outputs/accounts/bens_electric/v1")
    output_path.mkdir(parents=True, exist_ok=True)

    with open(output_path / "memo.json", "w") as f:
        json.dump(memo, f, indent=2)


if __name__ == "__main__":

    with open("data/demo_transcripts/bens_demo.txt") as f:
        transcript = f.read()

    memo = extract_demo_data(transcript)
    save_memo(memo)

    print("Memo JSON created successfully")