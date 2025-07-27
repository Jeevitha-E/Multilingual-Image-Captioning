#  Multilingual Image Captioning (Java + Python)

This project combines **Java and Python** to generate image captions in English using a machine learning model (BLIP), and then translates those captions into a user-selected language. The output is displayed in a styled HTML page that opens in your default browser.

---

## Features

- Upload any image (JPG/PNG)
- Select from 5 languages:
  - French
  - Spanish
  - German
  - Hindi
  - Italian
- English captions generated using BLIP (Salesforce)
- Translations done via MarianMT (Helsinki-NLP)
- Final output shown in your browser with both captions and the image

---

##  Technologies

- Java (for UI and file input)
- Python (for captioning + translation)
- Hugging Face Transformers
- PyTorch
- Pillow (PIL)
- SentencePiece

---

##  Files

CaptionTranslator.java     → Java code to prompt user and call Python  
caption_translate.py       → Python script to generate and translate captions  
requirements.txt           → List of required Python libraries  
README.md                  → This file (project info and instructions)

---

##  Setup Instructions

### 1.  Install Python Requirements

Make sure Python 3.11+ is installed.

Then run in terminal:

```bash
pip install -r requirements.txt

---

##  Team

- **Jeevitha E** – [@Jeevitha-E](https://github.com/Jeevitha-E)
- **Kethciyal** – [@kethciyal](https://github.com/kethciyal)
