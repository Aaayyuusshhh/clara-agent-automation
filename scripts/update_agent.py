import json
from pathlib import Path

print("Updating memo and generating agent v2...")

with open("data/onboarding_audio/onboarding_transcript.txt", encoding="utf-8") as f:
    onboarding_text = f.read().lower()

with open("outputs/accounts/bens_electric/v1/memo.json", encoding="utf-8") as f:
    memo = json.load(f)


if "jobber" in onboarding_text:
    if "Uses Jobber CRM" not in memo["integration_constraints"]:
        memo["integration_constraints"].append("Uses Jobber CRM")

if "after hours" in onboarding_text:
    memo["after_hours_flow_summary"] = "Emergency calls should attempt transfer to the on-call electrician. Non-urgent calls should be logged for next-day follow-up."

if "business hours" in onboarding_text:
    memo["office_hours_flow_summary"] = "Calls during office hours should collect customer details and schedule service calls."


v2_path = Path("outputs/accounts/bens_electric/v2")
v2_path.mkdir(parents=True, exist_ok=True)

with open(v2_path / "memo.json", "w", encoding="utf-8") as f:
    json.dump(memo, f, indent=2)

print("Memo v2 saved.")


services = ", ".join(memo["services_supported"])
emergency = ", ".join(memo["emergency_definition"])

system_prompt = f"""
You are the AI receptionist for {memo['company_name']}.

Services Provided:
{services}

Emergency Situations:
{emergency}

Office Hours Call Handling:
- Greet the caller
- Collect caller name and phone number
- Understand the electrical issue
- Schedule service calls or route urgent issues

After Hours Handling:
- Ask if the issue is an emergency
- If emergency attempt transfer
- If not emergency collect details for next day follow-up

Always remain polite, professional, and concise.
"""

agent_v2 = {
    "agent_name": f"{memo['company_name']} AI Receptionist",
    "version": "v2",
    "voice_style": "professional, friendly, calm",
    "system_prompt": system_prompt
}

with open(v2_path / "agent_spec.json", "w", encoding="utf-8") as f:
    json.dump(agent_v2, f, indent=2)

print("Agent v2 generated.")

# Create changelog

changelog = """
Ben's Electric Agent Update

Changes from v1 to v2:

- Updated call handling rules based on onboarding discussion
- Added clearer after-hours emergency handling
- Confirmed CRM integration with Jobber
"""

Path("changelog").mkdir(exist_ok=True)

with open("changelog/bens_electric_changes.md", "w", encoding="utf-8") as f:
    f.write(changelog)

print("Changelog generated.")