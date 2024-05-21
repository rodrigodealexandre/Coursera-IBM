from openai import OpenAI
import requests

openai_client = OpenAI()

def speech_to_text(audio_binary):
    # Set up Watson Speech-to-Text HTTP API URL
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = base_url + '/speech-to-text/api/v1/recognize'

    # Set up parameters for our HTTP request
    params = {
        'model': 'en-US_Multimedia',  # Using the confirmed available model
    }

    headers = {
        'Content-Type': 'audio/webm'  # Ensure this matches your audio data format
    }

    print(f"Sending audio data of length: {len(audio_binary)} bytes")

    # Send an HTTP POST request
    response = requests.post(api_url, params=params, headers=headers, data=audio_binary)
    
    # Check if the response is JSON and parse it
    try:
        response_json = response.json()
    except ValueError:
        print("Invalid response format, not JSON")
        return "null"
    
    # Log and parse the response to get our transcribed text
    print('Response from Watson:', response_json)
    text = 'null'
    if 'results' in response_json and response_json['results']:
        text = response_json['results'][0]['alternatives'][0]['transcript']
        print('Recognized text:', text)
    else:
        print('No speech recognized or invalid response:', response_json)

    return text

def text_to_speech(text, voice=""):
    # Set up Watson Text-to-Speech HTTP Api url
    base_url = "https://sn-watson-tts.labs.skills.network"
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    # Set the headers for our HTTP request
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # Set the body of our HTTP request
    json_data = {
        'text': text,
    }

    # Send a HTTP Post request to Watson Text-to-Speech Service
    response = requests.post(api_url, headers=headers, json=json_data)
    print('text to speech response:', response)
    return response.content

def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
    # Call the OpenAI Api to process our prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=4000
    )
    print("openai response:", openai_response)
    # Parse the response to get the response message for our prompt
    response_text = openai_response.choices[0].message.content
    return response_text