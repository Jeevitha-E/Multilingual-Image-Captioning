import sys
import os
import webbrowser
from transformers import BlipProcessor, BlipForConditionalGeneration, MarianMTModel, MarianTokenizer
from PIL import Image

# --- Input
if len(sys.argv) < 3:
    print("Usage: python caption_translate.py <image_path> <language_choice>")
    sys.exit(1)

image_path = sys.argv[1]
language_choice = sys.argv[2]

languages = {
    '1': ('French', 'Helsinki-NLP/opus-mt-en-fr'),
    '2': ('Spanish', 'Helsinki-NLP/opus-mt-en-es'),
    '3': ('German', 'Helsinki-NLP/opus-mt-en-de'),
    '4': ('Hindi', 'Helsinki-NLP/opus-mt-en-hi'),
    '5': ('Italian', 'Helsinki-NLP/opus-mt-en-it'),
}

if language_choice not in languages:
    print("Invalid language choice.")
    sys.exit(1)

lang_name, model_name = languages[language_choice]

# --- Load image
try:
    image = Image.open(image_path).convert('RGB')
except Exception as e:
    print(f"Error loading image: {e}")
    sys.exit(1)

# --- Generate caption
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
inputs = blip_processor(image, return_tensors="pt")
out = blip_model.generate(**inputs)
caption_en = blip_processor.decode(out[0], skip_special_tokens=True)

# --- Translate caption
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(tokenizer(caption_en, return_tensors="pt", padding=True).input_ids)
caption_translated = tokenizer.decode(translated[0], skip_special_tokens=True)

# --- Show in browser
html_path = image_path.replace("\\", "/")
html = f"""
<html>
<head><title>Caption Translation</title></head>
<body style="font-family:sans-serif; text-align:center; padding:20px;">
    <h2>Translated Caption ({lang_name}):</h2>
    <p style="font-size:20px;">{caption_translated}</p>
    <img src="file:///{html_path}" style="max-width:512px; margin:20px;"/>
    <h3>Original (English):</h3>
    <p style="color:gray;">{caption_en}</p>
</body>
</html>
"""

html_file = os.path.join(os.path.dirname(image_path), "caption_output.html")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open("file://" + html_file)
