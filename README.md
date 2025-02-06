# Exam Helper

Exam Helper is a tool designed to assist with passing exams with single answer like A,B,C,D or 1,2,3,4 using AI. 
It generates right answers and displays them by adjusting the sound bar level when the **Shift** key is pressed.

## Installation

Install Tesseract, here's nice tutorial: https://www.youtube.com/watch?v=HNCypVfeTdw&ab_channel=JayMartMedia

Make sure you have Python installed, then install the required dependencies:

```bash
pip install Flask keyboard google-generativeai pyperclip python-dotenv
```
After that, create an .env file with 
```bash
API_KEY=YOUR_API_KEY_HERE
```
from https://aistudio.google.com
