# AI--SURVIVAL-TRADING

AI Survival Trading System

Educational paper-trading project.

The system:
- collects market data
- analyzes evidence
- generates AI decisions
- applies risk controls
- simulates trades
- evaluates performance


AI Survival Trading System

«Trade to survive. Survive by managing risk.»

A modular, multi-source AI-assisted paper-trading and market-research platform designed for systematic market analysis, evidence fusion, backtesting, risk control, paper execution, AI memory, and mobile monitoring.

The system is designed around one core principle:

«The AI may propose a decision, but the Risk Engine has final authority over whether a paper trade is allowed.»

This project is intended for research, education, experimentation, and paper trading. It is not a system for guaranteeing profits or providing financial advice.

---

1. Project Overview

The AI Survival Trading System is a central intelligence platform that collects information from multiple sources, validates and normalizes that information, generates technical features, detects conflicts, evaluates market conditions, produces an AI decision, applies strict risk controls, and optionally executes the decision in a simulated paper-trading environment.

The long-term system is designed to work with:

- Windows laptop
- Android mobile
- TradingView
- Market-data APIs
- News sources
- Screeners
- Options/derivatives data
- Fundamental/event information
- Technical indicators
- Machine-learning models
- LLM/AI models
- Historical datasets
- Paper broker
- Backtesting engine
- AI memory
- Android floating overlay

---

2. Main Architecture

                         DATA SOURCES
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
      Market Data           News              Screeners
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                              ▼
                  ┌─────────────────────┐
                  │   DATA INGESTION    │
                  │    CONNECTORS       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │      VALIDATION     │
                  │ Quality + Freshness │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    NORMALIZATION    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   FEATURE ENGINE    │
                  │ EMA RSI ATR Volume  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   EVIDENCE ENGINE   │
                  │ Fusion + Conflicts  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │      CENTRAL AI     │
                  │ Decision + Memory   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     RISK ENGINE     │
                  │ Immutable Controls  │
                  └──────────┬──────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
               NO TRADE          PAPER TRADE
                                      │
                                      ▼
                              ┌───────────────┐
                              │   PORTFOLIO   │
                              │    ENGINE     │
                              └───────┬───────┘
                                      │
                                      ▼
                              ┌───────────────┐
                              │ AI PERFORMANCE│
                              │    MEMORY     │
                              └───────┬───────┘
                                      │
                                      ▼
                              EVALUATION LOOP

---

3. Platform Architecture

Windows Laptop

The Windows laptop is the primary development and computing platform.

It runs:

- Python
- FastAPI
- Data processing
- Indicators
- Feature generation
- AI models
- Evidence engine
- Risk engine
- Backtesting
- Paper broker
- Portfolio
- Database
- Reports
- Development tools

Android Mobile

The Android phone is the mobile monitoring and control platform.

The planned Android application will provide:

- Dashboard
- AI status
- Paper-trading status
- Alerts
- Market information
- Full analysis
- AI explanations
- Risk status
- Floating overlay
- TradingView-related visual information
- System controls
- Pause/resume controls

TradingView

TradingView is intended primarily for:

- Charts
- Technical visualization
- Pine Script indicators
- Alerts
- Visual confirmation
- Chart marking/integration

The Python backend remains the central intelligence layer.

---

4. Core Design Principles

4.1 More Data Does Not Automatically Mean Better Decisions

The system does not blindly trust every source.

Each source can have:

- Reliability
- Freshness
- Verification status
- Timestamp
- Data quality
- Historical performance

---

4.2 Evidence Before Decision

The AI should receive structured evidence rather than random raw information.

Evidence is separated into:

RAW FACT
    ↓
VALIDATED DATA
    ↓
DERIVED SIGNAL
    ↓
EXTERNAL EVENT
    ↓
INTERPRETATION
    ↓
AI DECISION

---

4.3 Conflict Detection

Example:

Technical Analysis       → BULLISH
Momentum                 → BULLISH
Volume                   → BULLISH
News                     → BEARISH
Options                  → BEARISH
Market Regime            → UNCERTAIN

The system should not automatically force:

BUY

Instead:

CONFLICTED
       ↓
WAIT / NO TRADE

---

5. Decision States

The system supports multiple decision states:

BUY
SELL
HOLD
WAIT
NO TRADE
INSUFFICIENT DATA
CONFLICTED

This is important because not trading is a valid system decision.

---

6. Confidence System

The project does not treat confidence as a guaranteed probability of profit.

Instead, confidence can incorporate:

Signal Strength
       +
Evidence Quality
       +
Source Reliability
       +
Source Agreement
       +
Data Freshness
       +
Historical Similarity
       +
Market Regime
       +
Risk Conditions

The final value is a system confidence score, not a guarantee.

---

7. Market Regime Detection

The future regime engine will classify conditions such as:

TRENDING
RANGING
HIGH_VOLATILITY
LOW_VOLATILITY
BREAKOUT
BREAKDOWN
NEWS_DRIVEN
UNCERTAIN

Strategies and AI interpretation can then be evaluated differently under different regimes.

---

8. Time and Session Engine

The system includes a dedicated time engine.

backend/time_engine/
├── __init__.py
├── clock.py
├── market_calendar.py
├── session_manager.py
├── scheduler.py
└── freshness.py

It provides:

- UTC time
- Indian Standard Time
- Timezone conversion
- Market session status
- Data freshness
- Scheduled tasks

Example:

{
    "timestamp": "2026-09-30T14:30:00+05:30",
    "timezone": "Asia/Kolkata",
    "market": "NSE",
    "status": "OPEN"
}

The current basic calendar checks weekdays and standard session hours. Exchange holidays and special sessions should be added before using it for serious research.

---

9. Current Project Structure

ai-survival-trading/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── requirements/
│   ├── base.txt
│   ├── ai.txt
│   ├── research.txt
│   └── dev.txt
│
├── backend/
│   ├── __init__.py
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── time_engine/
│   │   ├── __init__.py
│   │   ├── clock.py
│   │   ├── market_calendar.py
│   │   ├── session_manager.py
│   │   ├── scheduler.py
│   │   └── freshness.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── loader.py
│   │   └── validator.py
│   │
│   ├── indicators/
│   │   ├── __init__.py
│   │   ├── trend.py
│   │   ├── momentum.py
│   │   ├── volatility.py
│   │   └── volume.py
│   │
│   ├── features/
│   │   ├── __init__.py
│   │   └── generator.py
│   │
│   ├── evidence/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── fusion.py
│   │   └── conflict.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── decision.py
│   │   └── memory.py
│   │
│   ├── risk/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   ├── execution/
│   │   ├── __init__.py
│   │   └── paper_broker.py
│   │
│   ├── portfolio/
│   │   ├── __init__.py
│   │   └── manager.py
│   │
│   ├── survival/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   ├── backtest/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   └── reports/
│       ├── __init__.py
│       └── generator.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_data.py
│   ├── test_risk.py
│   └── test_indicators.py
│
├── tradingview/
│   └── pine/
│       └── README.md
│
├── notebooks/
│   └── README.md
│
└── docs/
    ├── architecture.md
    ├── development.md
    └── decisions.md

---

10. Requirements

Base

pandas
numpy
scipy
pandas-ta

matplotlib
plotly

scikit-learn

fastapi
uvicorn
pydantic
pydantic-settings

SQLAlchemy
aiosqlite

httpx
requests
websockets

python-dotenv
python-dateutil

AI

xgboost
lightgbm
joblib
optuna

ollama
transformers
sentence-transformers

Research

jupyterlab
ipykernel

openpyxl
jinja2
reportlab

Development

pytest
pytest-asyncio
ruff

---

11. Installation

Step 1 — Install Python

Install Python 3.12 or a compatible newer Python version on Windows.

Check:

python --version

Expected:

Python 3.12.x

---

12. Step 2 — Clone the Repository

git clone YOUR_REPOSITORY_URL

Enter the project:

cd ai-survival-trading

---

13. Step 3 — Create Virtual Environment

Windows:

python -m venv .venv

Activate:

PowerShell

.venv\Scripts\Activate.ps1

Command Prompt

.venv\Scripts\activate

---

14. Step 4 — Upgrade pip

python -m pip install --upgrade pip

---

15. Step 5 — Install Requirements

For the complete project:

pip install -r requirements.txt

For only the current basic backend:

pip install -r requirements/base.txt

For development:

pip install -r requirements/dev.txt

---

16. Step 6 — Run Tests

python -m pytest

All tests should pass before continuing development.

---

17. Step 7 — Start FastAPI

uvicorn backend.main:app --reload --host 0.0.0.0

The backend will run on:

http://127.0.0.1:8000

---

18. Step 8 — Open API Documentation

Open:

http://127.0.0.1:8000/docs

FastAPI provides an interactive API interface.

Available basic endpoints:

GET /
GET /health
GET /status
GET /time

---

19. Step 9 — Test the API

Root:

/

Health:

/health

System:

/status

Time/session:

/time

---

20. Step 10 — Git Commit

After successful testing:

git status

Then:

git add .

Commit:

git commit -m "Create initial AI trading system backend"

Push:

git push

---

21. Development Using GitHub Codespaces

Codespaces can be used when developing from Android or Windows.

Workflow:

GitHub
   ↓
Repository
   ↓
Codespaces
   ↓
Browser VS Code
   ↓
Terminal
   ↓
Python
   ↓
FastAPI
   ↓
Tests
   ↓
Git Commit
   ↓
Git Push

---

22. Fast Project Creation

Instead of manually creating every directory:

mkdir -p backend/{api,config,data,indicators,features,evidence,ai,risk,execution,portfolio,survival,backtest,reports,time_engine}

Create Python package files:

touch backend/__init__.py
touch backend/api/__init__.py
touch backend/config/__init__.py
touch backend/data/__init__.py
touch backend/indicators/__init__.py
touch backend/features/__init__.py
touch backend/evidence/__init__.py
touch backend/ai/__init__.py
touch backend/risk/__init__.py
touch backend/execution/__init__.py
touch backend/portfolio/__init__.py
touch backend/survival/__init__.py
touch backend/backtest/__init__.py
touch backend/reports/__init__.py
touch backend/time_engine/__init__.py

---

23. Data Pipeline

The intended data pipeline is:

Source
  ↓
Connector
  ↓
Raw Data
  ↓
Validation
  ↓
Normalization
  ↓
Timestamp
  ↓
Freshness Check
  ↓
Feature Generation
  ↓
Evidence
  ↓
AI

---

24. OHLCV Data

The current system expects:

timestamp
open
high
low
close
volume

Example:

timestamp,open,high,low,close,volume
2026-01-01,100,105,99,103,1000
2026-01-02,103,108,101,106,1200

---

25. Data Validation

The validator checks:

- Required columns
- Empty datasets
- Duplicate timestamps
- Invalid prices
- High/low consistency

Example:

result = validate_ohlcv(df)

Possible result:

{
    "valid": true,
    "errors": [],
    "rows": 1000
}

---

26. Technical Indicators

Current indicators:

Trend

- EMA
- SMA

Momentum

- RSI

Volatility

- ATR

Volume

- Volume SMA
- Relative Volume

More indicators can be added later.

---

27. Feature Engine

The feature engine combines indicators into one DataFrame.

OHLCV
 ↓
EMA
SMA
RSI
ATR
Volume
 ↓
Feature Dataset

Future features may include:

- Price returns
- Volatility
- Momentum
- Trend strength
- Volume anomalies
- Breakout conditions
- Market regime
- Multi-timeframe features
- Relative strength
- Correlation

---

28. Evidence Engine

The Evidence Engine stores structured evidence.

Example:

Source:
TradingView

Category:
Technical

Value:
+0.7

Reliability:
0.9

Confidence:
0.8

Timestamp:
2026-09-30T09:30:00Z

Evidence can originate from:

- Technical analysis
- Market data
- News
- Fundamentals
- Options
- Screeners
- Events
- Historical patterns
- ML models

---

29. Evidence Fusion

Different evidence sources can be combined according to:

Signal
×
Source Reliability
×
Evidence Confidence

The result produces a combined directional state.

Possible outputs:

BULLISH
BEARISH
NEUTRAL
INSUFFICIENT DATA

---

30. Conflict Detection

Example:

Technical      +0.8
Momentum       +0.6
Volume         +0.5
News           -0.8
Options        -0.6

The system identifies:

BULLISH EVIDENCE
        +
BEARISH EVIDENCE
        ↓
CONFLICT
        ↓
AI → CONFLICTED
        ↓
WAIT / NO TRADE

---

31. AI Decision Engine

The AI decision layer can output:

BUY
SELL
HOLD
WAIT
NO TRADE
INSUFFICIENT DATA
CONFLICTED

The AI does not have unrestricted authority.

---

32. Risk Engine

The Risk Engine is a separate layer.

AI Proposal
     ↓
Risk Engine
     ↓
 ┌───┴────┐
 │        │
APPROVE  REJECT
 │        │
 ▼        ▼
Paper    NO TRADE
Trade

The AI cannot override risk controls.

The survival mechanism also cannot override risk controls.

---

33. Paper Broker

The current broker is completely simulated.

It supports:

BUY
SELL

Orders contain:

Symbol
Side
Quantity
Price
Timestamp
Status

No real-money order is sent.

---

34. Portfolio

The portfolio tracks:

- Initial capital
- Cash
- Positions
- Average entry price
- Realized P&L
- Equity

Future versions will add:

- Unrealized P&L
- Fees
- Taxes
- Slippage
- Position sizing
- Margin simulation
- Multiple instruments

---

35. Backtesting

The backtesting system will eventually allow:

Historical Data
       ↓
Strategy
       ↓
Signal
       ↓
Risk Engine
       ↓
Paper Execution Simulation
       ↓
Portfolio
       ↓
Performance Metrics

Planned metrics include:

- Total return
- Drawdown
- Win rate
- Loss rate
- Profit factor
- Sharpe-like measures
- Trade count
- Average trade
- Maximum losing streak
- Risk violations
- Exposure
- Stability

Performance metrics are for research and comparison, not guarantees of future results.

---

36. Walk-Forward Testing

The future validation system will use:

Historical Data
       ↓
Training Period
       ↓
Validation Period
       ↓
Testing Period
       ↓
Walk Forward
       ↓
Paper Testing

This helps reduce the risk of relying on a strategy that only works on the historical data used to design it.

---

37. AI Memory

The AI Memory system stores previous decisions.

Example:

Symbol
Action
Confidence
Outcome
Timestamp

Future memory will include:

- Market regime
- Evidence
- Conflicts
- Entry conditions
- Exit conditions
- Risk state
- Similar historical situations
- Mistakes
- Model version

---

38. Continuous Improvement

The intended improvement loop is:

DATA
 ↓
ANALYSIS
 ↓
DECISION
 ↓
PAPER TRADE
 ↓
RESULT
 ↓
EVALUATION
 ↓
ERROR ANALYSIS
 ↓
MODEL/STRATEGY UPDATE
 ↓
BACKTEST
 ↓
WALK-FORWARD TEST
 ↓
PAPER TEST
 ↓
APPROVAL
 ↓
DEPLOY

The AI should not automatically rewrite and deploy itself merely because a previous trade lost money.

---

39. AI Survival System

The AI has a virtual survival state.

It can track:

Virtual Capital
Drawdown
Risk Violations
Decision Quality
Consistency
Evidence Quality

Example:

AI STATUS: ALIVE

Capital: 97,500
Drawdown: 2.5%
Risk Violations: 0
Decision Quality: monitored

The survival system does not allow the AI to increase risk merely to remain alive.

---

40. AI Retirement

Future AI agents can be retired when they repeatedly fail defined validation criteria.

Possible lifecycle:

CREATED
   ↓
TRAINING
   ↓
BACKTEST
   ↓
VALIDATION
   ↓
PAPER TEST
   ↓
ACTIVE
   ↓
EVALUATION
   ↓
RETIRED

A retired model remains available for research/history.

---

41. Multiple AI Agents

Future versions may use specialized agents.

Example:

             CENTRAL AI
                  │
     ┌────────────┼────────────┐
     │            │            │
Technical     News Agent   Market Regime
  Agent                      Agent
     │            │            │
     └────────────┼────────────┘
                  │
            Evidence Fusion
                  │
             Risk Engine
                  │
           Paper Execution

Possible agents:

- Technical Agent
- Momentum Agent
- Volume Agent
- News Agent
- Fundamental Agent
- Options Agent
- Market Regime Agent
- Risk Agent
- Historical Pattern Agent
- Portfolio Agent

---

42. TradingView Integration

TradingView will primarily be used for:

- Charts
- Pine Script
- Alerts
- Visual analysis

Possible future communication:

TradingView
     │
     │ Webhook
     ▼
FastAPI
     │
     ▼
Evidence Engine
     │
     ▼
AI

The system should use supported TradingView integration mechanisms rather than attempting to directly manipulate the internal TradingView application.

---

43. Pine Script

Future Pine indicators can display information such as:

Trend
Momentum
Signals
Regime
Risk State
AI State

The Pine layer remains separate from the Python backend.

---

44. Android Application

The future Android application will be written separately from the Python backend.

Planned architecture:

Android App
     │
     ├── Dashboard
     ├── Alerts
     ├── AI Status
     ├── Analysis
     ├── Portfolio
     ├── Paper Trades
     └── Floating Overlay
             │
             ▼
        FastAPI Backend

---

45. Floating Overlay

The Android application is planned to provide a unified floating control center.

Example:

┌──────────────────────────────┐
│ AI SURVIVAL                  │
│                              │
│ NIFTY                        │
│ STATUS: WAIT                 │
│                              │
│ Technical       ✓            │
│ Momentum        ✓            │
│ Volume          ✓            │
│ News            ⚠            │
│ Options         ⚠            │
│                              │
│ Evidence: CONFLICTED         │
│ Risk: SAFE                    │
│                              │
│ [FULL ANALYSIS]              │
│ [REPORT] [PAUSE AI]          │
└──────────────────────────────┘

The overlay can sit above other Android applications when the appropriate Android overlay permission is enabled.

---

46. TradingView + Android Overlay

The intended experience:

Android Screen
┌─────────────────────────────┐
│                             │
│      TradingView Chart      │
│                 