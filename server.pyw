import pytesseract
from PIL import Image
import mss
import mss.tools
import keyboard
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import threading

flag = False

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

def capture_full_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  
        width, height = monitor["width"], monitor["height"]
        left = monitor["left"]  
        top = monitor["top"] + int(height * 0.15)
        right = width  
        bottom = int(height * 0.85)
        screenshot = sct.grab({"left": left, "top": top, "width": right - left, "height": bottom - top})
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        # img.save("img.png") - uncomment if you want to see the image
        return img



def ocr_image(img):
    text = pytesseract.image_to_string(img)
    return text

def read_prompt_template():
    with open('prompt.txt', 'r', encoding='utf-8') as file:
        return file.read().strip()

def set_volume_based_on_response(response):
    global flag
    volume.SetMute(0, None)
    response = response.strip().upper()[0]
    if response == "1" or response == "A":
        volume.SetMasterVolumeLevelScalar(0, None)  
    elif response == "2" or response == "B":
        volume.SetMasterVolumeLevelScalar(0.25, None)  
    elif response == "3" or response == "C":
        volume.SetMasterVolumeLevelScalar(0.5, None)  
    elif response == "4" or response == "D":
        volume.SetMasterVolumeLevelScalar(1.0, None)  
    else:
        volume.SetMute(1, None)
        print("Unknown response. Volume not changed.")
    flag = False

def on_hotkey():
    global flag
    try:
        if(flag):
            return
        flag = True
        volume.SetMute(1, None)
        img = capture_full_screen()
        text = ocr_image(img)
        prompt_template = read_prompt_template()
        prompt = prompt_template.format(clipboard_content=text)
        response = chat_session.send_message(prompt)
        generated_text = response.text.strip()
        set_volume_based_on_response(generated_text)

    except Exception as e:
        print(f"Error: {str(e)}")
def listen_keys():
    keyboard.wait('esc')
    
if __name__ == "__main__":
    listener_thread = threading.Thread(target=listen_keys, daemon=True)
    listener_thread.start()
    keyboard.add_hotkey('shift', on_hotkey)
    keyboard.wait()