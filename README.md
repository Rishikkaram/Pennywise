# Pennywiseimport streamlit as st
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

# NEW: Import libraries for OCR
import pytesseract
from PIL import Image

# NEW (Windows Only): Set the path to the Tesseract executable
# If you are on Windows, uncomment the line below and replace the path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# --- Database Setup ---
DB_PATH = 'expenses.db'
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# Create or update expenses table (with emotion column)
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY,
              amount REAL,
              category TEXT,
              date TEXT,
              note TEXT,
              emotion TEXT)''')

# Create or update income table
c.execute('''CREATE TABLE IF NOT EXISTS income
             (id INTEGER PRIMARY KEY,
              amount REAL,
              date TEXT,
              source TEXT)''')

# Create or update settings table
c.execute('''CREATE TABLE IF NOT EXISTS settings
             (key TEXT PRIMARY KEY,
              value TEXT)''')

# Gamification table for weekly streak
c.execute('''CREATE TABLE IF NOT EXISTS gamification_data
             (key TEXT PRIMARY KEY,
              value TEXT)''')
conn.commit()

# --- LLM and ML Configuration ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    llm_model = genai.GenerativeModel("gemini-1.5-flash")
except KeyError:
    st.error("API key not found! Please create a .streamlit/secrets.toml file with your Google API Key.")

# Load VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Helper functions for expenses
def add_expense(amount, category, date_str, note, emotion=""):
    c.execute('INSERT INTO expenses (amount, category, date, note, emotion) VALUES (?, ?, ?, ?, ?)',
              (amount, category, date_str, note, emotion))
    conn.commit()
    check_and_update_streak()

def get_expenses():
    c.execute('SELECT * FROM expenses')
    return c.fetchall()

# Helper functions for income
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

# Settings functions
def get_setting(key, default=None):
    c.execute('SELECT value FROM settings WHERE key=?', (key,))
    row = c.fetchone()
    return row[0] if row else default

def set_setting(key, value):
    c.execute('REPLACE INTO settings (key, value) VALUES (?, ?)', (key, value))
    conn.commit()

# --- Gamification Functions ---
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

# --- ML Interaction Functions ---

# Sentiment Analysis (Using Vader)
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

# Anomaly Detection
def train_and_detect_anomalies(df):
    if df.empty or len(df) < 2:
        return pd.DataFrame()

    df_for_model = df[['Amount']].copy()
    
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(df_for_model)
    
    df_for_model['anomaly'] = model.predict(df_for_model)
    
    anomalies = df[df_for_model['anomaly'] == -1]
    
    return anomalies

# LLM interaction functions
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
        json_match = re.search(r'\{.*\}', response_text)
        if json_match:
            json_str = json_match.group(0)
            return eval(json_str)
        else:
            return None
    except Exception as e:
        st.warning(f"Could not parse LLM response: {e}")
        return None

# NEW FUNCTION: OCR and LLM Integration
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

# UI Helper Functions
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

# ----------------- Streamlit UI -----------------

# Custom CSS for a better visual appeal
st.markdown("""
<style>
.stApp {
    background-color: #F0F2F6;
}
.title-font {
    font-size: 3em !important;
    font-weight: bold;
    color: #4B0082;
    text-align: center;
}
.header-font {
    font-size: 2em !important;
    font-weight: bold;
    color: #6A5ACD;
    padding-top: 15px;
    padding-bottom: 5px;
}
.metric-box {
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.positive-metric {
    background-color: #D4EDDA;
    color: #155724;
}
.negative-metric {
    background-color: #F8D7DA;
    color: #721C24;
}
</style>
""", unsafe_allow_html=True)

# Main Title and Lottie Animation
st.markdown("<h1 class='title-font'>Pennywise – Your Smart Money Mentor</h1>", unsafe_allow_html=True)


# Sidebar: Budget and Income Settings
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

# --- Display the current streak ---
st.subheader('Your Progress')
streak_count, _ = get_streak_data()
st.metric(label="🔥 Current Streak", value=f"{streak_count} weeks")

# Add Expense Section
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

# Quick add via Smart Chat & OCR
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

# Fetch current data
expenses_data = get_expenses()
income_data = get_income()
df_expenses = pd.DataFrame(expenses_data, columns=['ID', 'Amount', 'Category', 'Date', 'Note', 'Emotion'])
df_income = pd.DataFrame(income_data, columns=['ID', 'Amount', 'Date', 'Source'])

# Display Expenses and Alerts
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

# Achievements
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

# Future Savings Projection
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

# Savings Goals Progress Bar
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

# Smart Investment & Wishlist Savings Advisor
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

# LLM Financial Advisor Chat
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
# Pennywise: Your Smart Money Mentor

Pennywise is a smart, interactive personal finance tracker and advisor built with Streamlit. This application goes beyond basic expense tracking by integrating machine learning and large language models to provide valuable financial insights, emotional spending analysis, and future projections.

## ✨ Features

- **📊 Comprehensive Dashboard:** Visualize your spending with interactive charts, including "Spending by Category," "Spending by Emotion," and "Weekly Expense Trend."
- **🤖 Smart Expense Entry:** Quickly add new expenses using a smart chat interface. Simply type a natural language note like "I spent 500 on dinner with friends," and the app will automatically extract the amount and category.
- **📷 Receipt OCR:** Upload a photo of a receipt, and the app uses Optical Character Recognition (OCR) and an AI model to automatically log the expense for you.
- **🧠 AI Financial Advisor:** Interact with a personal AI financial advisor to get personalized insights and advice based on your spending data.
- **🚨 Anomaly Detection:** The app uses machine learning to detect unusual or unusually high expenses, helping you spot potential budget overruns.
- **🏆 Gamification:** Stay motivated with a weekly streak feature that encourages consistent tracking.
- **🎯 Savings Goals & Projections:** Set savings goals and see your progress in real-time. The app also provides a projection of your future savings based on your current spending habits.

## 🚀 How to Run Locally

### Prerequisites

- Python 3.8 or newer
- Git (optional, but recommended for version control)

### 1. Clone the Repository (Optional)

If you're using Git, you can clone the project.
```bash
git clone [https://github.com/your-username/Pennywise-App.git](https://github.com/your-username/Pennywise-App.git)
cd Pennywise-App
