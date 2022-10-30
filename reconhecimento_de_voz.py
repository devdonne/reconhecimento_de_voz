import os
import speech_recognition as sr
from tkinter import E
print("testando")


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "Excel" in frase:
            os.system("start Excel.exe")
        elif "Word" in frase:
            os.system("start WINWORD.exe")

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

        return frase

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")


ouvir_microfone()
