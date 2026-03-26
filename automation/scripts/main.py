import json
import datetime
import requests
from bs4 import BeautifulSoup
import subprocess

# -------------------------------
# Load Questions
# -------------------------------
with open('automation/questions.json', 'r') as f:
    questions = json.load(f)

# -------------------------------
# Load Processed Index
# -------------------------------
with open('automation/processed.json', 'r') as f:
    processed = json.load(f)

index = processed.get("index", 0)

if index >= len(questions):
    print("All questions processed")
    exit()

question = questions[index]

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
# Append to Markdown
# -------------------------------
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

# -------------------------------
# Update Index
# -------------------------------
processed["index"] = index + 1

with open('automation/processed.json', 'w') as f:
    json.dump(processed, f)

print(f"Processed: {question}")



print("📌 Committing changes...")

subprocess.run(["git", "config", "user.name", "github-actions"])
subprocess.run(["git", "config", "user.email", "actions@github.com"])

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Auto update: {question}"])
subprocess.run(["git", "push"])

print("✅ Changes pushed to repository")