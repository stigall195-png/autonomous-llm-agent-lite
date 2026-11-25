from datetime import datetime, timezone

def tool_utc_now(_arg=""):
    return datetime.now(timezone.utc).isoformat()

def tool_word_count(text):
    return str(len(text.split()))

TOOLS = {
    "utc_now": tool_utc_now,
    "word_count": tool_word_count,
}

def run_agent(task):
    steps = []
    if "time" in task.lower():
        obs = TOOLS["utc_now"]("")
        steps.append({"tool": "utc_now", "observation": obs})
        return {"answer": f"Current UTC time is {obs}", "steps": steps}
    obs = TOOLS["word_count"](task)
    steps.append({"tool": "word_count", "observation": obs})
    return {"answer": f"Task contains {obs} words.", "steps": steps}
