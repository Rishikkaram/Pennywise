


Pasted text.txt
Document
how do i upload this in git?

If you already have the code (like the Flask app you uploaded), getting it onto GitHub is pretty straightforward:

1. Create a project folder
Put your code into a folder, for example:

Pet-Adoption-App/
│
├── app.py
├── requirements.txt
└── README.md
Your uploaded code would go into app.py.

Create requirements.txt:

Flask
2. Open Terminal in that folder
In VS Code:

Terminal → New Terminal
3. Initialize Git
git init
4. Add files
git add .
5. Commit
git commit -m "Initial commit"
If Git asks for username/email:

git config --global user.name "Your Name"
git config --global user.email "your@email.com"
6. Create a GitHub repository
Go to:

GitHub

Click:

New Repository

Example:

pet-adoption-flask-app
Don't add a README from GitHub since you already have files.

7. Connect local project to GitHub
GitHub will show commands similar to:

git remote add origin https://github.com/USERNAME/pet-adoption-flask-app.git
git branch -M main
git push -u origin main
Replace USERNAME with your GitHub username.

8. Add a good README
For a first-year CS student, this matters a lot:

# Pet Adoption Website

A Flask-based web application for pet adoption.

## Features
- Browse dogs, cats, birds and rabbits
- View pet details
- Adoption form
- Adoption confirmation page
- Responsive UI

## Tech Stack
- Python
- Flask
- HTML
- CSS

## Run Locally

pip install -r requirements.txt
python app.py
Make it look like a real project
Right now, your code is one huge file. Before putting it on your resume, I'd suggest:

Pet-Adoption-App/
│
├── app.py
├── templates/
│   ├── home.html
│   ├── dogs.html
│   ├── cats.html
│   └── ...
├── static/
│   └── styles.css
├── requirements.txt
└── README.md
Recruiters and professors will view that as a much cleaner Flask project.

If you want, I can also show you how to deploy this project for free on GitHub + Render so you get a live link like:

https://pet-adoption-app.onrender.com

which looks much stronger on a resume than just a GitHub repository.



Your uploaded code would go into `app.py`. Create `requirements.txt`:

u lost me after this

Ahh, I see what's happening.

You don't have the code saved as a file on your computer yet. Right now it's just text (the huge code you pasted here).

So first we need to get it into VS Code.

Option 1: You have VS Code installed
Open VS Code.

Click File → New File.

Paste all the code into the empty file.

Click File → Save As.

Create a folder called:

Pet-Adoption-App
Save the file inside that folder as:

app.py
Now VS Code will show:

Pet-Adoption-App
└── app.py
Only after this do you start the Git steps.

Option 2: You don't have VS Code
Tell me:

Are you using VS Code, PyCharm, or just GitHub website?

Did you literally paste the code into GitHub's website already?

If you tell me exactly what screen you're looking at right now (or send a screenshot), I can guide you from that exact point instead of giving generic Git instructions.



**New File**.

text file?

Not a text file in the sense of .txt.

You want to save it as a Python file:

app.py
In VS Code:

Open VS Code.

Click File → New Text File (or New File).

Paste your code.

Press Ctrl + S.

Create a folder called Pet-Adoption-App.

Save the file as:

app.py
The .py extension tells the computer it's a Python program.

Your folder should look like:

Pet-Adoption-App/
└── app.py
If you're on Windows and it tries to save as:

app.py.txt
that's wrong. Make sure the filename is exactly:

app.py
Can you open VS Code and tell me what you see on the left side panel? Or send a screenshot? Then I can walk you through the next click.


If you're saving in Notepad or a Save As window, use:

File name: app.py

Save as type: All Files (.)

Like this:

File name: app.py
Save as type: All Files (*.*)
Encoding: UTF-8 (if shown)
If you choose Text Documents (*.txt), Windows may save it as:

app.py.txt
which is not what you want.

After saving, check that the file name is exactly:

app.py
(not app.py.txt).

Are you saving from Notepad or VS Code?


i saved it 

Perfect! 🎉

Now let's check if Git is installed.

Open Command Prompt
Press:

Windows Key + R
Type:

cmd
Press Enter.

Go to your project folder
If you saved the folder on your Desktop:

cd Desktop\Pet-Adoption-App
Press Enter.

Check Git
Type:

git --version
If you see something like:

git version 2.50.1
you're ready.

If you see:

'git' is not recognized...
then Git isn't installed yet.

Tell me what appears after running:

git --version
and we'll do the next step.



If you saved the folder on your Desktop:

i saved in downloads

Great. Then in Command Prompt use Downloads instead of Desktop.

Try:

cd Downloads\Pet-Adoption-App
and press Enter.

Then type:

dir
You should see app.py listed.

After that, check Git:

git --version
Tell me what happens after these commands:

cd Downloads\Pet-Adoption-App
dir
git --version
(You can copy-paste the output here or send a screenshot.)


image(36).png

Perfect! 🎉 Git is installed and you're already inside your project folder.

Now run these commands one by one:

1. Initialize Git
git init
2. Add your file
git add .
3. Create your first commit
git commit -m "Initial commit"
If Git asks for your name/email, run:

git config --global user.name "Your Name"
git config --global user.email "your@email.com"
and then run the commit command again.

After the commit succeeds:

Go to GitHub.

Create a new repository called:

pet-adoption
Do NOT check "Add README".

When the repository is created, GitHub will show a page with commands like:

git remote add origin ...
git branch -M main
git push -u origin main
Send me a screenshot of that GitHub page (or copy those commands here), and I'll tell you exactly what to paste next. 🚀


image(37).png
i sorta pasted code earlier

That's actually good news 😄

From your screenshot, your code is already on GitHub in a repository called pet-adoption and there's a file called main.py.

So you've already done the hardest part!

Now check if it's really saved
On GitHub, click the Code tab (you're already there).

If you can see your entire code when scrolling, then it's successfully uploaded.

To make it look more professional
I'd suggest:

Rename main.py → app.py (Flask projects usually use app.py)

Add a README.md

Add a requirements.txt

For now, though, you can already put this on your resume as:

Pet Adoption Web Application

Built a Flask-based pet adoption platform with dynamic routes and adoption forms.

Implemented category-wise pet browsing (Dogs, Cats, Birds, Rabbits).

Developed responsive UI using HTML and CSS.

Managed project using Git and GitHub.

One thing I want to check
Did you:

upload it by clicking Add file → Create new file on GitHub and pasting the code there?

or

use git push from your computer?

If it's the first one, that's completely fine for now. We can clean it up later and make it look like a proper developer project.



* upload it by clicking **Add file → Create new file** on GitHub and pasting the code there? or

yes

That's totally okay. A lot of people start that way. 😄

What you've done is:

GitHub Repository
└── main.py
and your code is visible online. That's already enough to share the project.

What I'd do next
Add a README:

In your repository, click Add file → Create new file

Name it:

README.md
Paste:

# Pet Adoption Web Application

A Flask-based web application that allows users to browse and adopt pets.

## Features
- Browse Dogs, Cats, Birds and Rabbits
- Pet details and adoption forms
- Adoption confirmation page
- Attractive UI using HTML and CSS

## Tech Stack
- Python
- Flask
- HTML
- CSS
- GitHub
Click Commit changes

For your resume
You can now include:

Pet Adoption Web Application

Developed a Flask-based pet adoption platform with category-wise browsing and adoption workflows.

Built responsive interfaces using HTML and CSS.

Implemented dynamic routing and form handling in Python Flask.

Managed source code using GitHub.

One more thing
Since you're a 1st-year CS student aiming for strong internships and eventually UCL, I wouldn't stop at this project.

A stronger version would be:

Store pet data in SQLite/MySQL instead of Python lists

Add user login/signup

Add admin dashboard

Deploy it online using Render

That turns it from a class project into something recruiters actually notice.

How much time do you have this summer? If you have even 2–3 weeks, I can suggest 3 projects that would look significantly stronger than most first-year CS resumes.



Pasted text(1).txt
Document
can u give a readme for this?

Absolutely. Here's a polished README you can paste into a README.md file on GitHub:

# 🐾 Pet Adoption Web Application

A Flask-based web application that helps users browse and adopt pets through a simple and interactive interface.

## 📌 Overview

This project allows users to explore different categories of pets, view their details, and complete an adoption process through an online form.

The application is built using Python Flask and features a visually appealing user interface created with HTML and CSS.

---

## ✨ Features

- 🐶 Browse Dogs available for adoption
- 🐱 Browse Cats available for adoption
- 🐦 Browse Birds available for adoption
- 🐰 Browse Rabbits available for adoption
- 📋 View pet details including:
  - Name
  - Breed
  - Age
  - Allergies
  - Hobbies (for selected pets)
- 📝 Adoption form for collecting adopter information
- 🎉 Adoption confirmation page
- ⭐ User experience rating section
- 🎨 Attractive and responsive UI with custom styling

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS

---

## 📂 Project Structure

```text
pet-adoption/
│
├── app.py
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pet-adoption.git
```

### 2. Navigate to the Project Folder

```bash
cd pet-adoption
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📸 Main Functionalities

### Home Page
Users can select from:
- Dogs
- Cats
- Birds
- Rabbits

### Pet Listings
Each pet card displays:
- Image
- Name
- Breed
- Age
- Allergy Information

### Adoption Process
Users can:
- Fill in personal details
- Submit adoption requests
- View adoption confirmation

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Flask routing and URL handling
- Dynamic page rendering
- Form handling using Flask
- HTML and CSS integration with Python
- Basic web application development
- GitHub project management

---

## 🔮 Future Improvements

- User authentication and login system
- Database integration (SQLite/MySQL)
- Search and filter functionality
- Admin dashboard for managing pets
- Online deployment using Render or Railway
- Email confirmation for adoptions

---

## 👩‍💻 Author

Developed as a Python Flask web development project.
One small suggestion: your GitHub file is currently called main.py. Since this is a Flask project, renaming it to app.py will make it look more professional and align with common Flask conventions.



Pasted text(2).txt
Document
read me for this

For your Pennywise project, I'd use something like this on GitHub:

# 💰 Pennywise – Your Smart Money Mentor

Pennywise is an AI-powered personal finance management application built using Streamlit, Machine Learning, and Generative AI. It helps users track expenses, analyze spending behavior, set savings goals, detect unusual transactions, and receive personalized financial advice.

---

## 🚀 Features

### 📊 Expense & Income Tracking
- Add and manage daily expenses
- Track multiple income sources
- Monitor overall financial health
- Monthly budget management

### 🤖 AI-Powered Expense Logging
- Enter expenses using natural language
- Automatically extracts amount and category using Gemini AI
- Example:
  > "I spent ₹500 on dinner with friends"

### 📷 Receipt Scanner (OCR)
- Upload images of receipts
- Extracts text using Tesseract OCR
- Automatically logs expenses using AI

### 😊 Emotional Spending Analysis
- Detects emotions associated with spending notes
- Categorizes spending as:
  - Positive
  - Negative
  - Neutral
- Helps identify emotional spending habits

### 🚨 Anomaly Detection
- Uses Isolation Forest Machine Learning algorithm
- Detects unusually high or suspicious expenses
- Helps users monitor spending patterns

### 📈 Financial Analytics Dashboard
- Spending by Category
- Spending by Emotion
- Weekly Expense Trends
- Budget Utilization Insights

### 🎯 Savings Goals
- Create personal savings goals
- Track progress with interactive progress bars
- Goal achievement notifications

### 🔥 Gamification
- Weekly expense logging streaks
- Achievement badges
- User engagement rewards

### 💡 Smart Financial Advisor
- Personalized financial recommendations
- Wishlist purchase planning
- Investment suggestions based on available balance
- AI-powered financial chatbot

### 🔮 Future Savings Projection
- Predict future balance based on spending habits
- Estimate savings growth over time
- Financial planning assistance

---

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### Database
- SQLite

### Machine Learning
- Scikit-learn
- Isolation Forest

### Artificial Intelligence
- Google Gemini API
- VADER Sentiment Analysis

### Data Visualization
- Plotly
- Matplotlib
- Pandas

### OCR
- Tesseract OCR
- Pillow

---

## 📂 Project Structure

```text
Pennywise/
│
├── app.py
├── expenses.db
├── requirements.txt
├── README.md
└── assets/
```

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/pennywise.git
cd pennywise
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GOOGLE_API_KEY="YOUR_API_KEY"
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🎓 Learning Outcomes

Through this project, I gained experience in:

- Full-stack Python development
- Database management using SQLite
- Machine Learning integration
- Sentiment Analysis
- OCR-based document processing
- AI application development using Gemini
- Data visualization and analytics
- Building interactive dashboards with Streamlit

---

## 🔮 Future Enhancements

- User authentication system
- Cloud database integration
- Multi-user support
- Mobile-responsive design
- Expense forecasting using advanced ML models
- Export reports to PDF/Excel
- Investment portfolio tracking

---

## 👩‍💻 Author

Developed as an AI-powered Personal Finance Management System combining Machine Learning, OCR, Sentiment Analysis, and Generative AI to help users make smarter financial decisions.
This is a much stronger README than most first-year student projects and highlights the AI, ML, OCR, analytics, and finance features that recruiters tend to notice.


Pennywiseimport streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from streamlit_lottie import st_lottie
from sklearn.ensemble import IsolationForest
from datetime import datetime, date, timedelta
import google.generativeai as genai
import re
import requests
import numpy as np

NEW: Import libraries for OCR
import pytesseract
from PIL import Image

NEW (Windows Only): Set the path to the Tesseract executable
If you are on Windows, uncomment the line below and replace the path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
--- Database Setup ---
DB_PATH = 'expenses.db'
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

Create or update expenses table (with emotion column)
c.execute('''CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
amount REAL,
category TEXT,
date TEXT,
note TEXT,
emotion TEXT)''')

Create or update income table
c.execute('''CREATE TABLE IF NOT EXISTS income
(id INTEGER PRIMARY KEY,
amount REAL,
date TEXT,
source TEXT)''')

Create or update settings table
c.execute('''CREATE TABLE IF NOT EXISTS settings
(key TEXT PRIMARY KEY,
value TEXT)''')

Gamification table for weekly streak
c.execute('''CREATE TABLE IF NOT EXISTS gamification_data
(key TEXT PRIMARY KEY,
value TEXT)''')
conn.commit()

--- LLM and ML Configuration ---
try:
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
llm_model = genai.GenerativeModel("gemini-1.5-flash")
except KeyError:
st.error("API key not found! Please create a .streamlit/secrets.toml file with your Google API Key.")

Load VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

Helper functions for expenses
def add_expense(amount, category, date_str, note, emotion=""):
c.execute('INSERT INTO expenses (amount, category, date, note, emotion) VALUES (?, ?, ?, ?, ?)',
(amount, category, date_str, note, emotion))
conn.commit()
check_and_update_streak()

def get_expenses():
c.execute('SELECT * FROM expenses')
return c.fetchall()

Helper functions for income
def add_income(amount, source, date_str):
c.execute('INSERT INTO income (amount, source, date) VALUES (?, ?, ?)', (amount, source, date_str))
conn.commit()

def get_income():
c.execute('SELECT * FROM income')
return c.fetchall()

def get_total_income():
c.execute('SELECT SUM(amount) FROM income')
result = c.fetchone()
return result[0] if result and result[0] else 0

Settings functions
def get_setting(key, default=None):
c.execute('SELECT value FROM settings WHERE key=?', (key,))
row = c.fetchone()
return row[0] if row else default

def set_setting(key, value):
c.execute('REPLACE INTO settings (key, value) VALUES (?, ?)', (key, value))
conn.commit()

--- Gamification Functions ---
def get_streak_data():
c.execute('SELECT value FROM gamification_data WHERE key=?', ('streak',))
streak_str = c.fetchone()
if streak_str:
streak_data = eval(streak_str[0])
return streak_data.get('count', 0), streak_data.get('last_date')
return 0, None

def set_streak_data(count, last_date):
streak_data = {'count': count, 'last_date': last_date}
c.execute('REPLACE INTO gamification_data (key, value) VALUES (?, ?)', ('streak', str(streak_data)))
conn.commit()

def check_and_update_streak():
today = date.today()
streak_count, last_date_str = get_streak_data()

if last_date_str:
    last_date = datetime.strptime(last_date_str, '%Y-%m-%d').date()
    delta = (today - last_date).days
    
    # Check if the last log was within the last 7 days
    if 1 <= delta <= 7:
        streak_count += 1
        st.toast(f"🔥 Weekly streak maintained! You're on a {streak_count}-week streak!", icon='🎉')
    elif delta > 7:
        streak_count = 1
        st.toast("😔 Weekly streak broken. Starting a new one this week!", icon='😭')
    # If delta is 0, it means an expense was already logged today, do nothing.
else:
    streak_count = 1

set_streak_data(streak_count, today.strftime('%Y-%m-%d'))
return streak_count
--- ML Interaction Functions ---
Sentiment Analysis (Using Vader)
def get_emotion(note):
if not note:
return "Neutral"
score = analyzer.polarity_scores(note)['compound']
if score >= 0.05:
return 'Positive'
elif score <= -0.05:
return 'Negative'
else:
return 'Neutral'

Anomaly Detection
def train_and_detect_anomalies(df):
if df.empty or len(df) < 2:
return pd.DataFrame()

df_for_model = df[['Amount']].copy()

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df_for_model)

df_for_model['anomaly'] = model.predict(df_for_model)

anomalies = df[df_for_model['anomaly'] == -1]

return anomalies
LLM interaction functions
def get_llm_response(prompt):
try:
response = llm_model.generate_content(prompt)
return response.text
except Exception as e:
return f"An error occurred: {e}"

def parse_expense_with_llm(text_input):
prompt = f"""
Analyze the following expense note and extract the amount, a single category (from 'Food', 'Transport', 'Entertainment', 'Miscellaneous').
Return the result as a single line in this exact JSON format:
{{
"amount": <number>,
"category": "<category_name>"
}}
Example Note: "I spent 1500 on a new video game, feeling really happy about it!"
Example JSON: {{"amount": 1500, "category": "Entertainment"}}
Note to analyze: "{text_input}"
"""
response_text = get_llm_response(prompt)
try:
json_match = re.search(r'{.*}', response_text)
if json_match:
json_str = json_match.group(0)
return eval(json_str)
else:
return None
except Exception as e:
st.warning(f"Could not parse LLM response: {e}")
return None

NEW FUNCTION: OCR and LLM Integration
def ocr_and_parse(image):
"""Extracts text from an image and then parses it with the LLM."""
try:
image = Image.open(image)
text = pytesseract.image_to_string(image)
if text.strip() == "":
return None, "No text could be extracted from the image."
st.text_area("Extracted Text from Receipt:", text, height=150)
parsed_data = parse_expense_with_llm(text)
return parsed_data, None
except Exception as e:
return None, f"An error occurred during OCR: {e}"

UI Helper Functions
def load_lottieurl(url):
try:
r = requests.get(url, timeout=5)
if r.status_code == 200:
return r.json()
else:
return None
except requests.exceptions.RequestException:
return None

lottie_money_mentor = load_lottieurl("https://lottie.host/e2d07525-cfd6-4444-a15f-edca9c87893c/Qn6oM8LhP5.json")

----------------- Streamlit UI -----------------
Custom CSS for a better visual appeal
st.markdown("""

<style> .stApp { background-color: #F0F2F6; } .title-font { font-size: 3em !important; font-weight: bold; color: #4B0082; text-align: center; } .header-font { font-size: 2em !important; font-weight: bold; color: #6A5ACD; padding-top: 15px; padding-bottom: 5px; } .metric-box { padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin-bottom: 20px; } .positive-metric { background-color: #D4EDDA; color: #155724; } .negative-metric { background-color: #F8D7DA; color: #721C24; } </style>

""", unsafe_allow_html=True)

Main Title and Lottie Animation
st.markdown("<h1 class='title-font'>Pennywise – Your Smart Money Mentor</h1>", unsafe_allow_html=True)

Sidebar: Budget and Income Settings
st.sidebar.header('Budget and Income Settings')

default_budget = float(get_setting('budget', '5000'))
budget = st.sidebar.number_input('Monthly Budget', min_value=0.0, value=default_budget, step=500.0)
if st.sidebar.button('Save Budget'):
set_setting('budget', str(budget))
st.sidebar.success('Budget saved!')

st.sidebar.header('Add Income')
income_amount = st.sidebar.number_input('Income Amount', min_value=0.0, format='%f')
income_source = st.sidebar.text_input('Income Source')
income_date = st.sidebar.date_input('Date', datetime.today())
if st.sidebar.button('Add Income'):
add_income(income_amount, income_source, income_date.strftime('%Y-%m-%d'))
st.sidebar.success('Income added!')

--- Display the current streak ---
st.subheader('Your Progress')
streak_count, _ = get_streak_data()
st.metric(label="🔥 Current Streak", value=f"{streak_count} weeks")

Add Expense Section
st.header('Add Expense')
amount = st.number_input('Amount', min_value=0.01, format='%f')
category = st.selectbox('Category', ['Food', 'Transport', 'Entertainment', 'Miscellaneous'])
date_input = st.date_input('Date', datetime.today())
note = st.text_input('Note (optional)')
if st.button('Add Expense'):
emotion = get_emotion(note)
add_expense(amount, category, date_input.strftime('%Y-%m-%d'), note, emotion)
st.success('Expense added!')
if len(get_expenses()) == 1:
st.balloons()

Quick add via Smart Chat & OCR
st.subheader('Quick Add via Smart Chat & OCR')
chat_input = st.text_input("Type e.g. 'I spent 3000 on a new game and feel great about it.'")
uploaded_file = st.file_uploader("Or, upload a photo of a receipt:", type=['jpg', 'jpeg', 'png'])

if st.button('Analyze & Add Expense'):
if uploaded_file is not None:
with st.spinner("Analyzing receipt with OCR and LLM..."):
parsed_data, error = ocr_and_parse(uploaded_file)
if error:
st.error(error)
elif parsed_data:
add_expense(
amount=parsed_data.get('amount'),
category=parsed_data.get('category'),
date_str=date.today().strftime('%Y-%m-%d'),
note=f"Expense from OCR receipt: {parsed_data.get('amount')}",
emotion=get_emotion(f"Expense from OCR receipt: {parsed_data.get('amount')}")
)
st.success(f"Expense added from receipt: Amount={parsed_data.get('amount')}, Category={parsed_data.get('category')}")
elif chat_input:
with st.spinner("Analyzing with LLM..."):
parsed_data = parse_expense_with_llm(chat_input)
if parsed_data:
emotion = get_emotion(chat_input)
add_expense(
amount=parsed_data.get('amount'),
category=parsed_data.get('category'),
date_str=date.today().strftime('%Y-%m-%d'),
note=chat_input,
emotion=emotion
)
st.success(f"Expense added: Amount={parsed_data.get('amount')}, Category={parsed_data.get('category')}, Emotion={emotion}")
if len(get_expenses()) == 1:
st.balloons()
else:
st.warning('Could not parse your note.')
else:
st.warning('Please enter text or upload an image.')

Fetch current data
expenses_data = get_expenses()
income_data = get_income()
df_expenses = pd.DataFrame(expenses_data, columns=['ID', 'Amount', 'Category', 'Date', 'Note', 'Emotion'])
df_income = pd.DataFrame(income_data, columns=['ID', 'Amount', 'Date', 'Source'])

Display Expenses and Alerts
if not df_expenses.empty:
df_expenses['Date'] = pd.to_datetime(df_expenses['Date'])

# Anomaly Detection
anomalies = train_and_detect_anomalies(df_expenses)
if not anomalies.empty:
    st.subheader('💰 Spending Anomalies Detected!')
    st.warning('The following expenses are unusually high compared to your spending habits. Be mindful!')
    st.dataframe(anomalies)

st.header('Expense Log')
st.dataframe(df_expenses)

total_spent = df_expenses['Amount'].sum()
total_income = get_total_income()
available_budget = total_income + budget

# Budget & Income alerts
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='metric-box positive-metric'>Total Income: ₹{total_income:.2f}</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-box negative-metric'>Total Spent: ₹{total_spent:.2f}</div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-box positive-metric'>🔥 Streak: {streak_count} weeks</div>", unsafe_allow_html=True)

if total_spent > available_budget:
    st.error('You have exceeded your total income plus budget limit!')
elif total_spent > available_budget * 0.8:
    st.warning('You are close to exceeding your total income plus budget!')

# Category Pie Chart
st.subheader('Spending by Category')
cat_sum = df_expenses.groupby('Category')['Amount'].sum()
fig1, ax1 = plt.subplots()
ax1.pie(cat_sum, labels=cat_sum.index, autopct='%1.1f%%')
ax1.axis('equal')
st.pyplot(fig1)

# Emotional Spending Pie Chart
st.subheader('Spending by Emotion')
emotion_sum = df_expenses.groupby('Emotion')['Amount'].sum()
fig_emotion, ax_emotion = plt.subplots()
ax_emotion.pie(emotion_sum, labels=emotion_sum.index, autopct='%1.1f%%')
ax_emotion.axis('equal')
st.pyplot(fig_emotion)

# Weekly Trend (Plotly)
df_expenses['Week'] = df_expenses['Date'].dt.strftime('%Y-%U')
weekly_df = df_expenses.groupby('Week')['Amount'].sum().reset_index()
st.subheader('Weekly Expense Trend')
fig = px.line(weekly_df, x='Week', y='Amount', title='Weekly Expense Trend')
st.plotly_chart(fig)
else:
st.info('No expenses recorded yet. Start logging to see your financial insights!')

Achievements
st.header('Achievements')
badges = []
if not df_expenses.empty:
if len(df_expenses) >= 1:
badges.append('First Expense Added 🎉')
if df_expenses['Amount'].sum() > 1000:
badges.append('Spent over ₹1000 total 💸')
current_month = datetime.today().strftime('%Y-%m')
monthly_spend = df_expenses[df_expenses['Date'].dt.strftime('%Y-%m') == current_month]['Amount'].sum()
if monthly_spend < budget:
badges.append('Under Budget This Month ✅')
st.snow()

if streak_count >= 3:
    badges.append('Streak Master (3+ weeks) 🔥')
if badges:
st.write('Badges earned:')
st.write(', '.join(badges))
else:
st.write('No badges yet.')

Future Savings Projection
st.header('Future You – Savings Projection')
current_balance = st.number_input('Current balance for projection', min_value=0.0, value=0.0, format='%f')
months = st.slider('Months to project', 1, 24, 6)
if current_balance > 0 and not df_expenses.empty:
monthly_spend_avg = df_expenses['Amount'].mean() * 30
future_spend = current_balance - (monthly_spend_avg * months)
future_save = current_balance + (0.2 * current_balance * months)
st.write(f'If you keep spending at the current rate, after {months} months you might have about ₹{future_spend:.2f}.')
st.write(f'If you save 20% each month, you could have about ₹{future_save:.2f}.')
st.warning("This is a rough projection and does not account for interest or external factors.")

Savings Goals Progress Bar
st.header('Savings Goals')
goal_name = st.text_input('What are you saving for?', 'New Laptop')
goal_amount = st.number_input('Target amount', min_value=0.0, format='%f')
total_saved = get_total_income() - df_expenses['Amount'].sum() if not df_expenses.empty else get_total_income()
if goal_amount > 0:
progress_val = min(1.0, total_saved / goal_amount)
st.write(f"Progress towards '{goal_name}'")
st.progress(progress_val)
if total_saved >= goal_amount:
st.success(f"Congratulations! You've reached your goal to save for '{goal_name}'!")
st.balloons()

Smart Investment & Wishlist Savings Advisor
st.header('Smart Investment & Wishlist Savings Advisor')
balance = st.number_input('Enter your current balance amount (in your currency):', min_value=0.0, format='%f', key='balance_input')
wishlist_item = st.text_input('Enter an item you have added to your wishlist:', key='wishlist_input')
wishlist_cost = st.number_input('Enter the cost of your wishlist item:', min_value=0.0, format='%f', key='wishlist_cost_input')

def investment_recommendation(balance_amount):
if balance_amount <= 1000:
return "Consider low-risk savings options like fixed deposits or a high-yield savings account."
elif balance_amount <= 5000:
return "Consider a mix of low-risk bonds and some mutual funds for moderate growth."
elif balance_amount <= 20000:
return "Look into mutual funds and index funds for balanced investment growth."
else:
return "You can diversify into stocks, ETFs, and real estate investment trusts (REITs) for higher returns but with increased risk."

def savings_plan(balance_amount, item_cost):
if item_cost == 0:
return "Please enter the cost of your wishlist item to get a saving plan."
if balance_amount >= item_cost:
return f"You already have enough balance to buy '{wishlist_item}'."
else:
needed = item_cost - balance_amount
monthly_saving = balance_amount * 0.2 + (balance_amount * 0.5 * 0.05 / 12)
if monthly_saving <= 0:
return "Increase your monthly savings rate or look for additional income sources to buy your wishlist item sooner."
months_needed = needed / monthly_saving
return f"You need to save approximately {months_needed:.1f} months to buy '{wishlist_item}' by saving and investing."

if st.button('Get Financial Advice'):
if balance > 0:
st.subheader('Investment Recommendation')
recommendation = investment_recommendation(balance)
st.write(recommendation)
if wishlist_item:
st.subheader('Wishlist Buying Guide')
plan = savings_plan(balance, wishlist_cost)
st.write(plan)

LLM Financial Advisor Chat
st.header('Your AI Financial Advisor')

if 'llm_messages' not in st.session_state:
st.session_state.llm_messages = [{"role": "assistant", "content": "Hi! How can I help you with your finances? You can ask me things like 'What does my spending this month tell me?'"}]

for message in st.session_state.llm_messages:
with st.chat_message(message["role"]):
st.markdown(message["content"])

if prompt_llm := st.chat_input("Ask a question about your spending..."):
st.session_state.llm_messages.append({"role": "user", "content": prompt_llm})
with st.chat_message("user"):
st.markdown(prompt_llm)
with st.spinner('Thinking...'):
spending_df = df_expenses
full_prompt = f"""
You are an AI financial advisor named Pennywise. Your role is to give helpful, friendly, and concise financial advice.
Here is a user's expense data in a table format. Focus on giving personalized advice based on this data.

    User's Expense Data:
    {spending_df.to_string()}
    User's Question: {prompt_llm}
    Provide a single, conversational response to the user's question.
    """
    llm_response = get_llm_response(full_prompt)
st.session_state.llm_messages.append({"role": "assistant", "content": llm_response})
with st.chat_message("assistant"):
    st.markdown(llm_response)
Pennywise: Your Smart Money Mentor
Pennywise is a smart, interactive personal finance tracker and advisor built with Streamlit. This application goes beyond basic expense tracking by integrating machine learning and large language models to provide valuable financial insights, emotional spending analysis, and future projections.

✨ Features
📊 Comprehensive Dashboard: Visualize your spending with interactive charts, including "Spending by Category," "Spending by Emotion," and "Weekly Expense Trend."

🤖 Smart Expense Entry: Quickly add new expenses using a smart chat interface. Simply type a natural language note like "I spent 500 on dinner with friends," and the app will automatically extract the amount and category.

📷 Receipt OCR: Upload a photo of a receipt, and the app uses Optical Character Recognition (OCR) and an AI model to automatically log the expense for you.

🧠 AI Financial Advisor: Interact with a personal AI financial advisor to get personalized insights and advice based on your spending data.

🚨 Anomaly Detection: The app uses machine learning to detect unusual or unusually high expenses, helping you spot potential budget overruns.

🏆 Gamification: Stay motivated with a weekly streak feature that encourages consistent tracking.

🎯 Savings Goals & Projections: Set savings goals and see your progress in real-time. The app also provides a projection of your future savings based on your current spending habits.

🚀 How to Run Locally
Prerequisites
Python 3.8 or newer

Git (optional, but recommended for version control)

1. Clone the Repository (Optional)
If you're using Git, you can clone the project.

git clone [https://github.com/your-username/Pennywise-App.git](https://github.com/your-username/Pennywise-App.git)
cd Pennywise-App

Close
