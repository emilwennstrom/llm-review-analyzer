# LLM Review Analyzer

LLM Review Analyzer is a Python-based tool designed to automate the analysis of app reviews from the Google Play Store and Apple App Store. This tool utilizes local and cloud-based language models to process and analyze review data, providing insights and summaries to help improve app performance and user satisfaction.

## Features

- Support for Google Play Store and Apple App Store reviews.
- Integration with local Ollama server and Google Cloud Vertex AI for data processing.

## Getting Started

### Prerequisites

- Pip for managing Python packages.
- Access to Google Cloud with the Vertex AI and associated APIs enabled and authenticated.
- Local Ollama running if you want to run local models.

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/emilwennstrom/llm-review-analyzer.git
cd llm-review-analyzer
```

2. **Set Up Environment**

Create a virtual environment and activate it:

```bash
python -m venv venv
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
```


3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### Configuration

Environment Variables

Create a .env file in the root folder and set up the following variables:

- OLLAMA_URL=127.0.0.0:11434  # Address to the Ollama server if running local models
- PROJECT=your-google-cloud-project-id  # Google Cloud project name
- LOCATION=europe-west1  # Location of the models
- BUCKET=your-storage-bucket # Name of the storage bucket with the reviews

Data Preparation:
Place your CSV files containing app reviews in the data folder or specify a path to a storage bucket in main.py.

### Usage

Run the main script to start analyzing the review data:

```bash
python main.py
```

### Customization

- Adding New Review Sources: Modify reviews.utils.py to integrate more data sources.
- Defining Models: Define new models or modify existing ones in llms.models.py.


### Run with docker

- Set environment variables in the Dockerfile
- Copy application_default_credentials.json to root folder in project (see Dockerfile for default location).
- docker build -t llm-review-analyzer .
- docker run -it --rm llm-review-analyzer
