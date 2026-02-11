# 🤖 Smart Arabic Sentiment Analysis API & Dashboard

A comprehensive AI-as-a-Service (AIaaS) system designed to analyze Arabic text sentiments from uploaded files (CSV/Excel). The system provides real-time classification, statistical insights, and an AI-driven executive summary.

## 🌟 Key Features
- **Specialized Arabic NLP:** Leverages the `CAMeL-Lab BERT` model, specifically fine-tuned for Arabic sentiment classification (Positive, Negative, Neutral).
- **Batch Processing:** Efficiently processes entire datasets from uploaded files, moving beyond single-text inputs to handle thousands of rows simultaneously.
- **Interactive Dashboard:** A modern, responsive web interface built with Tailwind CSS for seamless file uploads and data visualization.
- **AI-Driven Summary:** Generates a human-like summary of the data, providing actionable insights rather than just raw numbers.
- **Containerization:** Fully containerized using **Docker** to ensure consistent performance across any environment (Development to Production).

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **AI/ML:** Hugging Face Transformers, PyTorch
- **Data Science:** Pandas, OpenPyXL
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
- **DevOps:** Docker, UV (Package Manager)

## 📁 Project Structure
```text
smart-arabic-sentiment-api/
├── app/
│   ├── main.py          # API routes and application logic
│   ├── model.py         # AI model loading and inference
│   ├── ai_summary.py    # Logic for generating smart insights
│   ├── utils.py         # Data processing and file handling utilities
│   └── error_handler.py # Professional exception handling
├── frontend/
│   └── index.html       # Web dashboard interface
├── Dockerfile           # Container configuration
└── requirements.txt     # Project dependencies

**How to Run the Project**

Option 1: Using Docker (Recommended)
1. Build the image:
docker build -t smart-sentiment .
2. Run the container:
docker run -p 8000:8000 smart-sentiment
3. Access the application:
Go to http://localhost:8000


Option 2: Running Locally
1. Clone the repository:
git clone <your-repository-url>
2. Install dependencies:
uv sync
3. Start the FastAPI server:
uv run uvicorn app.main:app --reload