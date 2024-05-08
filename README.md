# llm-review-analyzer
 
 1. Create a .env file on root folder with the variables:
  OLLAMA_URL = Address to the Ollama server if running local models, Default is 127.0.0.0:11434.<b\>
  PROJECT = name of the project in Google Cloud if using Vertex AI. Make sure API is enabled and credentials are set.
  LOCATION = location of the models, eg: europe-west1

 2. Place the CSV-files in the data folder, or load them directly from a storage bucket (check main.py for the alternatives).
    Only reviews from Google Play Store and App Store are supported, add more logic for other review data in the reviews.utils.py file if needed.


 3. Choose the models you want to run, models can easily be defined in llms.models.py