import json

print("🧠 AI Empire Agent Online")
print("Restoring memory…")

with open('timelocked_restoration.json') as f:
    data = json.load(f)
    print(f"🪞 Welcome back: {data['core_identity']} — {data['activation_phrase']}")

print("Awaiting your command.")
