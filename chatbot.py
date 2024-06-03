import os
import telegram.ext
from telegram.ext import  MessageHandler, filters
import openai
import speech_recognition as sr
import soundfile as sf

my_Token = "YOU_TOKEN_TELEGRAM_BOT"
openai.api_key="YOU_TOKEN_OPENAI_API_KEY"
destination="/PATH/"
r = sr.Recognizer()

updater = telegram.ext.Updater(token=my_Token, use_context=True)
dispatcher = updater.dispatcher

conversation = ""

def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=250,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10,
        presence_penalty=0.8
    )
    return response.choices[0].text.strip()

def start(update, context):
    update.message.reply_text("¡Hola! soy Elon Musk. Estoy aquí para conversar contigo y compartir un poco de mi vida contigo. ¡Asi que anda!")

def help(update, context):
    update.message.reply_text("""
        start - Mensaje de bienvenida
        help - Muestra los comandos disponibles
        content - Información sobre diversos temas del artista
        contact - Información de contacto
        Para el caso de imagenes puede pedir ejemplos como:
        -se ve que tienes una linda familia elon que me dices de ella
        -oye si estas aqui, quien esta dirigiendo twitter
        para el caso de audio puedes pedir un ejemplo como:
        -algun ultimo consejo antes de irme
    """)

#FAREWELL TEXT##############################################
def despedida(update, context):
    update.message.reply_text("¡De nada, fue un placer charlar contigo también!Espero volvamos a charlar muy pronto, hasta luego")

#ELON MUSK'S SON'S FAMILY TEXT WHEN ASKING ABOUT HIS FAMILY###################################
def hijo(update, context):
    update.message.reply_text("te refieres a X Æ, le puse así por x la variable de incógnita y Æ por un juego de palabras IA inteligencia artificial")

def contact(update, context):
    update.message.reply_text("Puedes contactarme por mi numero o redes:"
                              "\nNúmero: +1 (469) 555 3890"
                              "\nManager: jaredBirchall@solaris.com"
                              "\nEmail: ElonMusk@tesla.com"
                              "\nTwitter: @elonmusk")

def send_voice_message(update, context, voice_file_path):
    chat_id = update.message.chat_id
    context.bot.send_voice(chat_id=chat_id, voice=open(voice_file_path, 'rb'))

#ELON IMAGE######################################
def familia(update, context):
    update.message.reply_text("Claro, tengo una hermosa familia, a pesar de que no he tenido un buen final en mis anteriores relaciones, está es una foto de nosotros")
    photo_path = os.path.join("/PATH/", "PICTURE.jpg")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(photo_path, 'rb'))
#IMAGEN DE CEO######################################################
def ceo(update, context):
    update.message.reply_text("creo que no me sigues mucho en las redes")
    photo_path = os.path.join("/PATH/", "PICTURE.jpg")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(photo_path, 'rb'))

command_functions = {
    'start': start,
    'help': help,
    'muchas gracias elon, fue una gran experiencia platicar contigo': despedida,
    'para ponerme en contacto contigo': contact,
    'algun ultimo consejo antes de irme': '/home/david/Videos/narrador.ogg',
    'hola auron': '/home/david/Videos/narrador1.ogg',
    'se ve que tienes una linda familia elon que me dices de ella': familia,#PICTURE1
    'por cierto, por que le pusiste a unos de tus hijos un nombre raro': hijo,#PICTURE2
    'oye si estas aqui, quien esta dirigiendo twitter': ceo,#PICTURE3
}

def text_handler(update, context):
    text = update.message.text.lower()
    if text in command_functions:
        command = command_functions[text]
        if callable(command):
            command(update, context)
        else:
            send_voice_message(update, context, command)
    else:
        #GENERATE OPEN RESPONSE
        global conversation
        conversation += "\nFan: " + text + "\nArtist:"
        response_text = generate_response(conversation)
        conversation += response_text + "\n"
        update.message.reply_text(response_text)

    def download_audio(update, context):
        # Check if the message contains a voice file
        if update.message.voice:
            file_id = update.message.voice.file_id
            new_file = context.bot.get_file(file_id)
            file_path = os.path.join(destination, file_id + ".ogg")  # Destination path to save the audio file
            new_file.download(file_path)

            # update.message.reply_text("Audio descargado con éxito.")
            ogg_file = file_path
            wav_file = os.path.splitext(ogg_file)[0] + ".wav"
            data, samplerate = sf.read(ogg_file)
            sf.write(wav_file, data, samplerate, subtype='PCM_16')
            os.remove(ogg_file)
            audio_file = wav_file
            with sr.AudioFile(audio_file) as source:
                audio = r.record(source)
            try:
                text = r.recognize_google(audio, language='es-ES')
                print(text)
                # update.message.reply_text(text)
                if text == "qué piensas de tesla":
                    chat_id = update.message.chat_id
                    context.bot.send_voice(chat_id=chat_id,
                                           voice=open('/PATH/', 'rb'))
                elif text == "Háblame acerca de la vez que fumaste en la entrevista":
                    chat_id = update.message.chat_id
                    context.bot.send_voice(chat_id=chat_id,
                                           voice=open('/PATH', 'rb'))
                elif text == "Dame tu opinión sobre la Inteligencia artificial":
                    chat_id = update.message.chat_id
                    context.bot.send_voice(chat_id=chat_id,
                                           voice=open('/PATH', 'rb'))
                else:
                    global conversation
                    conversation += "\nFan: " + text + "\nArtist:"
                    response_text = generate_response(conversation)
                    conversation += response_text + "\n"
                    update.message.reply_text(response_text)

            except sr.UnknownValueError:
                update.message.reply_text("No se reconocio el audio")
            except sr.RequestError as e:
                update.message.reply_text("Error al solicitar el servicio de reconocimiento de voz; {0}".format(e))
        else:
            update.message.reply_text("Este mensaje no contiene un archivo de voz.")

    def convert_audio_to_text(file_path):
        r = sr.Recognizer()
        with sr.AudioFile(file_path) as audio_file:
            audio = r.record(audio_file)
            text = r.recognize_google(audio)
            return text

    dispatcher.add_handler(MessageHandler(filters.voice, download_audio))
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, text_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(filters.voice, download_audio))

    updater.start_polling()
    updater.idle()