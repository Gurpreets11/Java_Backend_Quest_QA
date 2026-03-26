import json
import datetime
import requests
from bs4 import BeautifulSoup
import subprocess

print("🚀 Script started")

# -------------------------------
# Load Questions
# -------------------------------
try:
    with open('automation/questions.json', 'r') as f:
        questions = json.load(f)
    print(f"✅ Questions loaded: {len(questions)}")
except Exception as e:
    print("❌ Error loading questions:", e)
    exit()

# -------------------------------
# Load Processed Index
# -------------------------------
try:
    with open('automation/processed.json', 'r') as f:
        processed = json.load(f)
    print("✅ Processed file loaded")
except Exception as e:
    print("❌ Error loading processed.json:", e)
    exit()

index = processed.get("index", 0)
print(f"📌 Current index: {index}")

if index >= len(questions):
    print("⚠️ All questions processed")
    exit()

question = questions[index]
print(f"👉 Selected Question: {question}")

# -------------------------------
# Fetch Answer (StackOverflow)
# -------------------------------
def fetch_answer_stackoverflow(query):
    try:
        search_url = f"https://stackoverflow.com/search?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        res = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        # Get first question link
        question_link = soup.select_one(".question-summary .result-link a")
        if not question_link:
            return None

        question_url = "https://stackoverflow.com" + question_link['href']

        # Open question page
        res = requests.get(question_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        answer = soup.select_one(".answercell")
        if answer:
            return answer.get_text(strip=True)[:1000]  # limit size

        return None

    except Exception as e:
        print("Error fetching:", e)
        return None

# -------------------------------
# Generate Answer
# -------------------------------
answer = fetch_answer_stackoverflow(question)

if not answer:
    answer = "Answer not found. Please update manually."

# -------------------------------
# Write to Markdown
# -------------------------------
try:
    today = datetime.date.today()

    entry = f"""
## 🗓️ {today}

### ❓ {question}

**Answer:**
{answer}

---
"""

    with open('daily-updates.md', 'a', encoding='utf-8') as f:
        f.write(entry)

    print("✅ Written to daily-updates.md")

except Exception as e:
    print("❌ Error writing markdown:", e)
    exit()

# -------------------------------
# Update Index
# -------------------------------
try:
    processed["index"] = index + 1

    with open('automation/processed.json', 'w') as f:
        json.dump(processed, f)

    print("✅ Updated processed.json")

except Exception as e:
    print("❌ Error updating processed.json:", e)
    exit()



# -------------------------------
# Git Commit
# -------------------------------
try:
    print("📌 Checking git changes...")

    diff = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)

    print("Git Status:\n", diff.stdout)

    if diff.stdout.strip():
        subprocess.run(["git", "config", "user.name", "github-actions"])
        subprocess.run(["git", "config", "user.email", "actions@github.com"])

        # Pull latest changes (IMPORTANT)
        subprocess.run(["git", "pull", "--rebase"])

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Auto update: {question}"])
        subprocess.run(["git", "push"])

        print("✅ Changes pushed")
    else:
        print("⚠️ No changes detected")

except Exception as e:
    print("❌ Git error:", e)

print("🏁 Script finished")