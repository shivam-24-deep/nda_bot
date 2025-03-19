import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 📌 NDA Free Resource Links (Updated with 24/7 accessible links)
NDA_RESOURCES = {
    "NCERT Textbooks": "https://ncert.nic.in/textbook.php",
    "Mathematics": "https://byjus.com/nda/mathematics/",
    "General Ability (GAT)": "https://www.defenceguru.co.in/nda-preparation-material",
    "General Knowledge": "https://www.gktoday.in/",
    "Physics": "https://www.vedantu.com/jee-main/physics-important-questions",
    "Chemistry": "https://byjus.com/nda/chemistry/",
    "English": "https://www.grammarbook.com/",
    "Current Affairs": "https://www.jagranjosh.com/current-affairs",
    "SSB Interview": "https://ssbcrackexams.com/",
    "Full NDA Preparation": "https://www.adda247.com/defence-jobs/nda-preparation/",
    "Examrace NDA Resources": "https://www.examrace.com/NDA/"
}

# 📌 NDA Question Resources
NDA_QUESTIONS = {
    "Math MCQs": "https://www.examsnet.com/tests/nda-maths-mcq-questions",
    "GK MCQs": "https://www.gkduniya.com/nda-gk",
    "English Vocabulary MCQs": "https://testbook.com/objective-questions/mcq-on-english",
    "Previous Year Papers": "https://www.upsc.gov.in/examinations/previous-question-papers",
    "History MCQs": "https://www.clearias.com/history-quiz-upsc/",
    "Geography MCQs": "https://www.clearias.com/geography-quiz-upsc/",
    "Examrace NDA Questions": "https://www.examrace.com/NDA/NDA-Mathematics-Questions/"
}

# 📌 Mock Test Resources
MOCK_TEST_RESOURCES = {
    "Embibe NDA Mock Tests": "https://www.embibe.com/exams/nda-mock-test/",
    "Testbook NDA Mock Tests": "https://testbook.com/nda/test-series",
    "Mockers NDA Mock Tests": "https://www.mockers.in/exam/nda-mock-test",
    "FlexiQuiz NDA GAT Mock Test": "https://www.flexiquiz.com/SC/N/Shiksha-NDA-GAT-Mock-Test-2",
    "Study Campus NDA Mock Tests": "https://studycampus.in/nda-mock-test/"
}

# 📌 Command: /resources - Provides free NDA preparation resources
@dp.message(lambda message: message.text == "/resources")
async def resources_handler(message: Message):
    resources_text = "📚 NDA Free Preparation Resources:\n"
    for subject, link in NDA_RESOURCES.items():
        resources_text += f"🔗 {subject}: [Click Here]({link})\n"
    await message.answer(resources_text, parse_mode="Markdown")

# 📌 Command: /questions - Provides NDA question resources
@dp.message(lambda message: message.text == "/questions")
async def questions_handler(message: Message):
    questions_text = "📖 NDA Exam Questions & Practice:\n"
    for subject, link in NDA_QUESTIONS.items():
        questions_text += f"🔗 {subject}: [Click Here]({link})\n"
    await message.answer(questions_text, parse_mode="Markdown")

# 📌 Command: /mock_test - Provides NDA mock test resources
@dp.message(lambda message: message.text == "/mock_test")
async def mock_test_handler(message: Message):
    mock_test_text = "📝 Free NDA Mock Test Resources:\n"
    for subject, link in MOCK_TEST_RESOURCES.items():
        mock_test_text += f"🔗 {subject}: [Click Here]({link})\n"
    await message.answer(mock_test_text, parse_mode="Markdown")

# 📌 Command: /start - Provides options
@dp.message(lambda message: message.text == "/start")
async def start_handler(message: Message):
    options_text = "👋 Welcome! What type of resources do you need?\n\n"
    options_text += "📌 Type '/resources' for NDA preparation resources\n"
    options_text += "📌 Type '/questions' for NDA exam practice questions\n"
    options_text += "📌 Type '/mock_test' for NDA mock test resources\n"
    await message.answer(options_text)

# Function to start the bot
async def main():
    print("🚀 Bot is running...\nSend /resources to get NDA study materials.\nSend /questions to get NDA exam questions.\nSend /mock_test to get NDA mock test resources.")
    await dp.start_polling(bot)

# Run the bot when this script is executed
if __name__ == "__main__":
    asyncio.run(main())
