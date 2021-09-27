#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tweepy
import openai
import json
import os


# In[7]:


# API info
with open(r"C:\Users\satel\OneDrive\Escritorio\Code\Galia-Auth\Auth.json") as f:
    apis = json.load(f)

#  Tweeter API Auth
auth = tweepy.OAuthHandler(apis["api_key"], apis["api_key_secret"])
auth.set_access_token(apis["access_token"], apis["access_token_secret"])
oauth = auth
api = tweepy.API(oauth)


# In[84]:


# Preset pasado
# preset = "Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión y la buena música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo generara un Tweet según un tema a elección.\n\nTema: Música.\nTweet: Sin música, la vida sería un error. Pero un error mas grave seria decir que el reggaetón es música.\n###\nTema: Uso de las redes sociales.\nTweet: Las redes sociales son una herramienta muy buena, pero sin duda tenemos que cuidarnos de la posible adicción que nos pueden generar.\n###\nTema: El destino.\nTweet: Creer que nuestro camino en la vida ya fue forjado, tiene una directa relacion con el bajo uso de la curiosidad.\n###\nTema: El ocio. \nTweet: Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n###\nTema: La música.\nTweet: La música crea mas simpatía que el sexo.\n###\nTema: Paises sub desarrollados.\nTweet: Los paises subdesarrollados deberian ser mas estrictos con la migracion.\n###\nTema: Los carros.\nTweet: Me gusta mucho andar en bicicleta, pero estoy en contra de querer cambiar el mundo por ese termino.\n###\nTema: pornografia.\nTweet: me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una \"sorpresa\" a mi madre.\n###\nTema:"


# In[109]:


# SELECCIONAR EL TEMA
theme_selector = ""


# Uso de GPT-3
preset = 'Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión, el universo, el desarrollo humano, la antropología, distopias, Elon Musk, y música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo generara un Tweet de Galia según un tema a elección.\n\nTema: El ocio. \nTweet: Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n###\nTema: La música.\nTweet: La música crea mas simpatía que el sexo.\n###\nTema: Países sub desarrollados.\nTweet: Los países subdesarrollados deberían ser mas estrictos con la migración.\n###\nTema: Los carros.\nTweet: Me gusta mucho andar en bicicleta, pero estoy en contra de querer cambiar el mundo por ese termino.\n###\nTema: pornografía.\nTweet: me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una "sorpresa" a mi madre.\n###\nTema: Caleidoscopio.\nTweet: Mi vida es un caleidoscopio de emociones que se traslapan en cada momento. \n###\nTema:'
final = ".\nTweet:"

openai.api_key = apis["openai_api_key"]
response = openai.Completion.create(
    engine="curie",
    prompt=preset,
    temperature=0.75,
    max_tokens=75,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0.16,
    stop=["###"],
)
text = response.choices[0].text


# Limpieza del texto
cont = 0
for letter in text:
    if letter == ":":
        break
    cont += 1

theme = text[: cont - 6]
text = text[cont + 2 : len(text) - 1]
text = text.capitalize()

if text.find("\n") > 0:
    text = text[: text.find("\n")]

print("theme: " + theme)
print(text)


# In[104]:


def tweet(x):
    api.update_status(x)
    print("Tweeted")


tweet(text)
