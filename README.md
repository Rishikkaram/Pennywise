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
