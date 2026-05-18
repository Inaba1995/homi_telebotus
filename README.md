# Homi Telebotus

Telegram-бот для перевода текста на английский язык с озвучкой.

## Возможности

- Переводит русский текст на английский через Google Translate
- Отправляет голосовое сообщение с произношением перевода (TTS)
- Сохраняет фотографии, отправленные пользователем

## Стек

- Python
- Aiogram 3
- Google Translate API (googletrans)
- gTTS (Google Text-to-Speech)

## Установка и запуск

1. Установите зависимости:
```bash
pip install aiogram gtts googletrans==4.0.0-rc1
```

2. Укажите токен бота в `config.py`

3. Запустите:
```bash
python main.py
```
