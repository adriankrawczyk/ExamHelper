# Exam Helper

Exam Helper is a tool designed to assist with passing exams with single answer like A,B,C,D or 1,2,3,4 using AI. 
<br/>
<br/>
It uses Tesseract OCR to get the question from your screen, generates right answers with Gemini 2.0 Flash and then displays them by adjusting the sound bar level when the Shift key is pressed.
<br/>
<br/>
You can open it just double-clicking on server.py, it will be opened as proccess. If you want to exit click CTRL+ALT+H.

## Installation

Install Tesseract and have it in PATH in enviroment variables, here's nice tutorial: https://www.youtube.com/watch?v=HNCypVfeTdw&ab_channel=JayMartMedia
<br/>
<br/>
Make sure you have Python installed, then install the required dependencies:

```bash
pip install Flask keyboard google-generativeai pyperclip python-dotenv pytesseract pillow mss pycaw comtypes
```
<br/>
After that, create an .env file with 
```bash
API_KEY=YOUR_API_KEY_HERE
```
from https://aistudio.google.com
