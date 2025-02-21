import speech_recognition as sr
import os
from colorama import Fore, init

# Initialize colorama for colored text in the terminal
init(autoreset=True)


def get_valid_audio_path():
    """Loop until a valid audio file path is provided."""
    while True:
        audio_path = input(
            Fore.CYAN + "Enter the path to the audio file: ").strip()
        if os.path.isfile(audio_path):
            return audio_path
        print(Fore.RED + "Invalid path. Please enter a valid file.")


def get_output_path(audio_path):
    """Get the output file name and directory from the user."""
    default_folder = os.path.dirname(
        audio_path)  # Same folder as the audio file
    print(Fore.YELLOW + f"Transcription will be saved in: {default_folder}")

    output_name = input(
        Fore.CYAN + "Enter the name for the transcription file (leave empty to use the same as the audio): ").strip()

    # Use the audio filename if no custom name is given
    if not output_name:
        output_name = os.path.splitext(os.path.basename(audio_path))[0]

    return os.path.join(default_folder, f"{output_name}.txt")


def get_language():
    """Allow the user to select a language from a predefined list."""
    languages = {
        "1": ("English", "en-US"),
        "2": ("Español (Perú)", "es-PE"),
        "3": ("Español (México)", "es-MX"),
        "4": ("Français", "fr-FR")
    }

    print(Fore.GREEN + "\nSelect a language:")
    for key, (name, _) in languages.items():
        print(Fore.YELLOW + f"{key}. {name}")

    choice = input(Fore.CYAN + "Enter the number of your choice: ").strip()
    return languages.get(choice, ("English", "en-US"))[1]  # Default to English


def transcribe_audio(audio_path, output_path, language):
    """Transcribe the audio and save it to a file."""
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            print(Fore.MAGENTA + "Processing audio... Please wait.")
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language=language)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

        print(Fore.GREEN + f"✅ Transcription saved as: {output_path}")

    except sr.UnknownValueError:
        print(Fore.RED + "❌ Could not understand the audio.")
    except sr.RequestError:
        print(Fore.RED + "❌ Error connecting to the recognition service.")


# Main execution
print(Fore.BLUE + "=" * 40)
print(Fore.BLUE + "       Audio Transcriber CLI Tool")
print(Fore.BLUE + "=" * 40)

audio_path = get_valid_audio_path()
output_path = get_output_path(audio_path)
language = get_language()

transcribe_audio(audio_path, output_path, language)
