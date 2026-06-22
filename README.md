# 🌟 LifeOS AI — Your Intelligent Life Operating System

A full-stack Streamlit app powered by Claude AI to manage every dimension of your life.

## Features

| Module | Description |
|--------|-------------|
| 🏠 Home Dashboard | Life score, balance radar, weekly forecast |
| 🎓 School Student | Marks tracker, grade prediction, AI study plan |
| 🎓 College Student | CGPA calculator, college guide, placement prep |
| 💼 Business User | Revenue analytics, SWOT analysis, marketing strategy |
| 🏠 Personal Life | Life balance wheel, AI advice, habit builder |
| 📔 Smart Diary | AI-reflected journal with streak tracking |
| 😊 Mood Analysis | Daily mood logging with trend charts |
| 📚 Book Recommendations | AI-curated personalized reading lists |
| 🎯 Career Guidance | Roadmap, resume review, interview prep, salary negotiation |
| 💰 Finance Analytics | Income/expense tracker with AI advice |
| ❤️ Health Tracker | Vitals logging, BMI calculator, AI wellness tips |
| ⏰ Time Management | Task manager with AI-optimized daily schedule |
| 🏆 Goal Tracker | Goal setting with AI action plans |
| 🤖 AI Assistant | Full conversational AI life coach |
| 🔮 Future Prediction | AI trajectory analysis |
| 📊 Reports | Comprehensive life analytics dashboard |

## Setup

```bash
# 1. Clone / extract the project
cd LifeOS_AI

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your Anthropic API key
export ANTHROPIC_API_KEY="your-key-here"
# Or create a .env file: ANTHROPIC_API_KEY=your-key-here

# 5. Run
streamlit run app.py
```

## Architecture

```
LifeOS_AI/
├── app.py                    # Entry point + auth UI
├── pages/                    # 16 Streamlit pages
├── modules/                  # AI + business logic engines  
├── utils/                    # DB, charts, helpers
├── config/                   # Theme + settings
└── .streamlit/config.toml    # Dark theme config
```

## Tech Stack
- **Frontend**: Streamlit
- **AI**: Anthropic Claude (claude-sonnet-4-6)
- **Database**: SQLite
- **Charts**: Plotly
- **Auth**: bcrypt + SHA-256

## API Key
Get your key at [console.anthropic.com](https://console.anthropic.com)
