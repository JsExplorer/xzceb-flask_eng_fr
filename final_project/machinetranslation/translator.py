import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(englishtext):
    translation_e2f = language_translator.translate(
    text=englishtext, model_id='en-fr').get_result()
    frenchtext = translation_e2f['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    translation_f2e = language_translator.translate(
    text=frenchtext, model_id='fr-en').get_result()
    englishtext = translation_f2e['translations'][0]['translation']
    return englishtext
