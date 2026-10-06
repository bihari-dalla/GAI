#3. WAP to convert english to hindi
# 1. Install deep-translator (if not already installed)
!pip install -q deep-translator

# 2. Translate text using MyMemory API with specific region-based language codes
from deep_translator import MyMemoryTranslator

try:
    text = input("Enter English text: ")
    # Using 'en-US' for English and 'hi-IN' for Hindi
    translation = MyMemoryTranslator(source='en-US', target='hi-IN').translate(text)
    print("Hindi:", translation)
except Exception as e:
    print("Error:", e)

------------------------------------------------------------------------------------
#maam's code
!pip install googletrans==4.0.0-rc1

from googletrans import Translator

text = input("Enter English text: ")

try:
    print("Hindi:", Translator().translate(text, dest='hi').text)
except Exception as e:
    print("error:", e)
