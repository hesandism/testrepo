#!/usr/bin/env python3
"""
Simple Voice Assistant using OpenAI's GPT-3
This assistant listens to voice input, sends it to GPT-3, and speaks the response.
"""

import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Initialize speech recognizer
recognizer = sr.Recognizer()


def speak(text):
    """Convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to user's voice input and convert to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None


def get_gpt3_response(prompt):
    """Get response from GPT-3"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant. Keep your responses concise and conversational."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting GPT-3 response: {e}")
        return "I'm sorry, I encountered an error processing your request."


def main():
    """Main function to run the voice assistant"""
    print("=" * 50)
    print("Voice Assistant with OpenAI GPT-3")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    speak("Hello! I'm your voice assistant. How can I help you today?")
    
    while True:
        # Listen for user input
        user_input = listen()
        
        if user_input is None:
            continue
        
        # Check for exit commands
        if any(word in user_input.lower() for word in ['exit', 'quit', 'goodbye', 'bye']):
            speak("Goodbye! Have a great day!")
            break
        
        # Get response from GPT-3
        response = get_gpt3_response(user_input)
        
        # Speak the response
        speak(response)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVoice assistant stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
