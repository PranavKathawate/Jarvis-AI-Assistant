import json

MEMORY_FILE = "memory.json"

MAX_EXCHANGES = 6   # 6 user + 6 assistant = 12 messages total

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(history):
    # Keep only last 12 messages (6 exchanges)
    trimmed_history = history[-(MAX_EXCHANGES * 2):]

    with open(MEMORY_FILE, "w") as f:
        json.dump(trimmed_history, f, indent=2)