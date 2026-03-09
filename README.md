# Celebrity Persona Chatbot

A hackathon project that creates a chatbot capable of simulating conversations with celebrities such as artists, musicians, actors, and influencers.  
The goal is to make interactions feel more personal, emotional, and immersive by combining celebrity-inspired responses, text generation, and voice-based interaction.

---

## Problem

Celebrities have limited time to generate personalized and personified responses for their fans.  
This creates a gap between public figures and their audiences, making it difficult to build a closer and more engaging connection.

---

## Solution

We developed a **celebrity persona chatbot** that simulates conversations with a celebrity by using:

- A database of predefined responses
- AI-generated answers for open-ended conversations
- Text and audio interaction
- Voice-to-text conversion for spoken questions

This allows users to feel as if they are talking directly with their favorite celebrity in a more natural and interactive way.

---

## Description

This chatbot is designed to answer user questions while simulating the personality and style of a celebrity.  
In the current prototype, the bot interacts through **Telegram** and supports both:

- **Text messages**
- **Voice messages**

When a user sends an audio message, the system converts it into text so it can be processed and answered.  
For known prompts, the chatbot can return:

- Predefined text responses
- Pre-recorded voice messages
- Images

For open-ended questions, the chatbot uses OpenAI text generation to continue the conversation dynamically. The implementation includes a conversation history so replies feel more contextual over time. :contentReference[oaicite:1]{index=1}

---

## Features

- Celebrity-style conversational experience
- Telegram bot integration
- Text-based interaction
- Voice message support
- Speech-to-text conversion
- AI-generated open responses
- Predefined responses for common fan questions
- Ability to send voice notes and images
- Context-aware conversation flow

---

## Tech Stack

- **Python**
- **Telegram Bot API**
- **OpenAI API**
- **SpeechRecognition**
- **SoundFile**
- **Audio processing with `.ogg` to `.wav` conversion**

---

## How It Works

1. The user sends a message through Telegram.
2. If the message matches a known prompt, the bot returns a predefined response.
3. If it is a voice message:
   - The bot downloads the audio
   - Converts it from `.ogg` to `.wav`
   - Transcribes it into text using speech recognition
4. If the input is not predefined, the chatbot generates a response using OpenAI.
5. The bot answers back in text, voice, or image format depending on the case. :contentReference[oaicite:2]{index=2}

---

## Project Structure

```bash
main.py
```

![picture1](https://github.com/GORDIAN12/hackatoon_chatbot/assets/91165071/0e2998b5-cb36-4cb1-8af1-d74c8a1ef21b)

![picture2](https://github.com/GORDIAN12/hackatoon_chatbot/assets/91165071/a51a28d4-bdc7-48a4-94b1-c4ee2a3858e9)

