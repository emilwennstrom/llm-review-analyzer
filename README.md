# LLM Review Analyzer

LLM Review Analyzer is a Python-based tool designed to automate the analysis of app reviews from the Google Play Store and Apple App Store. This tool utilizes local and cloud-based language models to process and analyze review data, providing insights and summaries to help improve app performance and user satisfaction.

## Features

- Support for Google Play Store and Apple App Store reviews.
- Integration with local Ollama server and Google Cloud Vertex AI for advanced data processing.
- Extensible framework to add additional sources and review types.

## Getting Started

### Prerequisites

- Python 3.8 or higher.
- Pip for managing Python packages.
- Access to Google Cloud with the Vertex AI and associated APIs enabled and/or a server running Ollama

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourgithubusername/llm-review-analyzer.git
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

Install all required Python packages
pip install -r requirements.txt


