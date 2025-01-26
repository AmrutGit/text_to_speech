import pyttsx3
from config.settings import DEFAULT_RATE, VOICE_MALE, VOICE_FEMALE

def text_to_speech(text, rate, voice_type):
    """Convert text to speech."""
    engine = pyttsx3.init()
    
    # Set the rate of speech
    engine.setProperty('rate', rate)
    
    # Set the voice type (male/female)
    voices = engine.getProperty('voices')
    if voice_type == "male":
        engine.setProperty('voice', VOICE_MALE)
    else:
        engine.setProperty('voice', VOICE_FEMALE)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to the Text-to-Speech Converter!")
    text = input("Enter the text you want to convert to speech: ")
    
    print("\nChoose a voice type:")
    print("1. Male")
    print("2. Female")
    voice_choice = input("Enter your choice (1/2): ")
    voice_type = "male" if voice_choice == "1" else "female"
    
    rate = input(f"Enter the speech rate (default is {DEFAULT_RATE}): ")
    rate = int(rate) if rate.isdigit() else DEFAULT_RATE
    
    print("\nConverting text to speech...")
    text_to_speech(text, rate, voice_type)
    print("Conversion complete!")
