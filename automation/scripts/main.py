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
        headers = {"User-Agent": "Mozilla/5.0"}

        # Step 1: Search
        search_url = f"https://stackoverflow.com/search?q={query.replace(' ', '+')}"
        res = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        # Updated selector (NEW StackOverflow UI)
        result = soup.select_one("div.s-post-summary a.s-link")
        if not result:
            print("❌ No search results found")
            return None

        question_url = "https://stackoverflow.com" + result['href']
        print("🔗 URL:", question_url)

        # Step 2: Open question page
        res = requests.get(question_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        # Get top answer
        answer_div = soup.select_one("div.answer div.s-prose")
        if answer_div:
            text = answer_div.get_text("\n", strip=True)
            return text[:1500]  # limit size

        print("❌ No answer found on page")
        return None

    except Exception as e:
        print("❌ Error fetching:", e)
        return None


# -------------------------------
# Fetch Answer (GFG)
# -------------------------------

def fetch_answer_gfg(query):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}

        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}+site:geeksforgeeks.org"
        res = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        link = soup.select_one("a")
        if not link:
            return None

        url = link.get("href")
        if not url or "geeksforgeeks" not in url:
            return None

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        article = soup.select_one("div.text")
        if article:
            return article.get_text("\n", strip=True)[:1500]

        return None

    except:
        return None

# -------------------------------
# Generate Answer
# -------------------------------
answer = fetch_answer_stackoverflow(question)

if not answer:
    print("🔁 Trying GeeksforGeeks...")
    answer = fetch_answer_gfg(question)

if not answer:
    answer = "Answer not found. Please update manually."


answer = f"```\n{answer}\n```"

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
    print("📌 Configuring git...")

    subprocess.run(["git", "config", "user.name", "github-actions"])
    subprocess.run(["git", "config", "user.email", "actions@github.com"])

    # ✅ STEP 1: Pull latest FIRST (before checking changes)
    print("📥 Pulling latest changes...")
    subprocess.run(["git", "pull", "--rebase"])

    # ✅ STEP 2: Check for changes AFTER your script modified files
    print("📌 Checking git changes...")
    diff = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)

    print("Git Status:\n", diff.stdout)

    if diff.stdout.strip():
        print("📌 Adding changes...")
        subprocess.run(["git", "add", "."])

        print("📌 Committing changes...")
        subprocess.run(["git", "commit", "-m", f"Auto update: {question}"])

        print("🚀 Pushing changes...")
        subprocess.run(["git", "push"])

        print("✅ Changes pushed")
    else:
        print("⚠️ No changes detected")

except Exception as e:
    print("❌ Git error:", e)

print("🏁 Script finished")