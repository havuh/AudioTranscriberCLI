# 🎙️ Audio Transcriber CLI

A simple command-line tool to transcribe audio files into text using Google Speech Recognition.

## ✨ Features
- 🔹 Supports multiple languages (English, Spanish, French, etc.).
- 🔹 Automatically saves the transcription in the same folder as the audio.
- 🔹 Allows custom naming for the output file.
- 🔹 Color-coded interface for better readability.
- 🔹 Handles errors gracefully (invalid paths, unsupported audio, etc.).

## 🚀 Installation

1. **Clone the repository**  
2. **Create a virtual environment** (optional but recommended)
  ```sh
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
   ```
3. **Install dependencies** 
  ```sh
    pip install -r requirements.txt
   ```
## 🎧 Usage
Run the script and follow the instructions:
   ```sh 
   python transcriber.py
   ```
You'll be asked to:

* Enter the path to an audio file (.wav format).
* Choose the transcription language.
* (Optional) Set a custom name for the output file.

## 📦 Creating an Executable (Optional)
To generate a standalone `.exe` (Windows only):
   ```sh
    pip install -r dev-requirements.txt
    pyinstaller --onefile transcriber.py
   ```
The executable will be in the `dist/` folder.

## 📝 Requirements
* Python 3.8+
* SpeechRecognition
* colorama

## ⚠️ Limitations
* Requires an internet connection for Google Speech Recognition.
* Only supports .wav files (convert other formats first).

## 📄 License
MIT License

