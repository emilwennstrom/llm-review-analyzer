from . import translate, CLIENT_OPTIONS, PROJECT, LOCATION
import tqdm

def detect_language(
    text: str, project=PROJECT, location=LOCATION
) -> translate.DetectLanguageResponse:
    """Detecting the language of a text string.

    Args:
        project_id: The GCP project ID.

    Returns:
        The detected language of the text.
    """
    if location is None or project is None:
        raise Exception("Either LOCATION or PROJECT is not defined.")

    parent = f"projects/{project}/locations/{location}"
    client = translate.TranslationServiceClient(client_options=CLIENT_OPTIONS)
    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.detect_language(
        content=text,
        parent=parent,
        mime_type="text/plain",  # mime types: text/plain, text/html
    )

    # Display list of detected languages sorted by detection confidence.
    # The most probable language is first.
    '''for language in response.languages:
        # The language detected
        print(f"Language code: {language.language_code}")
        # Confidence of detection result for this language
        print(f"Confidence: {language.confidence}")'''

    return response.languages[0].language_code

# Initialize Translation client
def translate_text(
    text: str, language_code = 'sv', target = 'en', project = PROJECT, location = LOCATION
) -> translate.TranslationServiceClient:
    """Translating Text."""
    if location is None or project is None:
        raise Exception("Either LOCATION or PROJECT is not defined.")

    if language_code == target: return text
    parent = f"projects/{project}/locations/{location}"
    client = translate.TranslationServiceClient(client_options=CLIENT_OPTIONS)
    
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": language_code,
            "target_language_code": target,
        }
    )

    # Display the translation for each input text provided
    #for translation in response.translations:
        #print(f"Translated text: {translation.translated_text}")

    return response.translations[0].translated_text


#tqdm.pandas(desc="Translating texts")
def apply_translation(text):
    lang_code = detect_language(text=text, location=LOCATION, project=PROJECT)
    return translate_text(text=text, language_code=lang_code, target='en', location=LOCATION, project=PROJECT)