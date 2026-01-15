# Voice Assistant with OpenAI GPT-3

A simple voice-activated assistant powered by OpenAI's GPT-3 that listens to your voice commands, processes them using GPT-3, and responds with natural speech.

## Features

- 🎤 Voice input using speech recognition
- 🤖 AI-powered responses using OpenAI's GPT-3.5-turbo
- 🔊 Text-to-speech output
- 💬 Natural conversation flow
- ⚡ Simple and easy to use

## Prerequisites

- Python 3.7 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Microphone for voice input

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hesandism/testrepo.git
cd testrepo
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

**Note for Linux users**: You may need to install additional dependencies:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio espeak
```

**Note for macOS users**: PyAudio can be installed via Homebrew:
```bash
brew install portaudio
pip install pyaudio
```

3. Set up your OpenAI API key:
```bash
cp .env.example .env
```
Then edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your-actual-api-key-here
```

## Usage

Run the voice assistant:
```bash
python voice_assistant.py
```

The assistant will greet you and start listening. Simply speak your questions or commands, and it will respond using GPT-3.

### Example Interactions

- "What's the weather like today?"
- "Tell me a joke"
- "Explain quantum physics in simple terms"
- "What's the capital of France?"

### Stopping the Assistant

Say any of these phrases to exit:
- "exit"
- "quit"
- "goodbye"
- "bye"

Or press `Ctrl+C` to stop the program.

## How It Works

1. **Voice Input**: The assistant uses the `speech_recognition` library to capture and convert your speech to text using Google's speech recognition API.

2. **AI Processing**: The transcribed text is sent to OpenAI's GPT-3.5-turbo model, which generates an intelligent, contextual response.

3. **Voice Output**: The response is converted to speech using the `pyttsx3` text-to-speech engine and played back to you.

## Configuration

You can customize the assistant's behavior by modifying these parameters in `voice_assistant.py`:

- **Speech Rate**: Adjust `engine.setProperty('rate', 150)` (default: 150)
- **Volume**: Adjust `engine.setProperty('volume', 0.9)` (range: 0.0 to 1.0)
- **GPT-3 Model**: Change the `model` parameter in `get_gpt3_response()` (e.g., "gpt-4")
- **Response Length**: Modify `max_tokens` in the API call (default: 150)
- **Temperature**: Adjust creativity with `temperature` (0.0-1.0, default: 0.7)

## Troubleshooting

### Microphone Issues
- Make sure your microphone is properly connected and configured
- Check system permissions for microphone access
- Test your microphone with other applications

### API Key Issues
- Verify your API key is correctly set in the `.env` file
- Check that your OpenAI account has available credits
- Ensure there are no extra spaces in the `.env` file

### Audio Output Issues
- Check system volume settings
- On Linux, ensure espeak is installed: `sudo apt-get install espeak`

## Dependencies

- `openai` - OpenAI API client
- `SpeechRecognition` - Speech-to-text conversion
- `pyttsx3` - Text-to-speech conversion
- `python-dotenv` - Environment variable management
- `PyAudio` - Audio I/O

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Acknowledgments

- OpenAI for providing the GPT-3 API
- The developers of speech_recognition and pyttsx3 libraries
