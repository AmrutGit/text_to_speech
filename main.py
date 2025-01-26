from TTS.api import TTS
from TTS.utils.manage import ModelManager  # Import ModelManager for handling models

def list_available_models():
    """Lists all available pre-trained TTS models."""
    print("\nFetching available TTS models...")
    model_manager = ModelManager()  # Use ModelManager to handle models
    models = model_manager.list_models()  # Get the list of available models
    print("Available models:")
    for idx, model in enumerate(models):
        print(f"{idx + 1}. {model}")
    return models

def text_to_speech_ml(text, model_name, voice=None):
    """Convert text to speech using an ML-based pre-trained model."""
    print("\nLoading the model...")
    tts = TTS(model_name)  # Load the pre-trained model
    
    print("Generating speech...")
    if voice:
        tts.tts_to_file(text=text, speaker=voice, file_path="output_audio.wav")
    else:
        tts.tts_to_file(text=text, file_path="output_audio.wav")  # Default speaker
    print("Speech has been saved to 'output_audio.wav'.")

if __name__ == "__main__":
    print("Welcome to the ML-Based Text-to-Speech Converter!")

    # List available models and choose one
    available_models = list_available_models()
    model_choice = int(input("\nSelect a model by entering the number: ")) - 1
    if model_choice < 0 or model_choice >= len(available_models):
        print("Invalid choice! Exiting...")
        exit()
    model_name = available_models[model_choice]

    # Input text
    text = input("\nEnter the text you want to convert to speech: ")

    # Fetch available speakers for the selected model
    print("\nFetching available voices...")
    tts = TTS(model_name)
    speakers = tts.speakers  # Fetch speakers for the selected model

    # Handle case with no available speakers
    selected_voice = None
    if speakers:
        print("Available voices:")
        for idx, speaker in enumerate(speakers):
            print(f"{idx + 1}. {speaker}")
        voice_choice = int(input("Select a voice by entering the number: ")) - 1
        if voice_choice < 0 or voice_choice >= len(speakers):
            print("Invalid choice! Exiting...")
            exit()
        selected_voice = speakers[voice_choice]
    else:
        print("No speakers available for this model. Using the default voice.")

    # Convert text to speech
    print("\nConverting text to speech using machine learning...")
    text_to_speech_ml(text, model_name, selected_voice)
    print("Conversion complete!")
