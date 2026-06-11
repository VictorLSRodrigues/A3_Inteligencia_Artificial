import sys
import time

if not hasattr(time, "clock"):
    time.clock = time.perf_counter

import aiml
import unicodedata
import re


# Efetua uma filtragem no texto de entrada
def filter(text):
    # Normaliza o texto entrado como parâmetro e remove os acentos
    text = unicodedata.normalize("NFKD", text) \
        .encode("ASCII", "ignore") \
        .decode("utf-8")
    # Remove pontuação e caracteres especiais
    text = re.sub(r"[^\w\s]", "", text)
    return text


kb = sys.argv[1]
k = aiml.Kernel()
k.learn(kb)

while True:
    message = input("> ")
    message = filter(message)
    response = k.respond(message)
    response = response.replace('\\n', '\n')
    print(response)