import tweepy
import openai
import os

# SELECT THE THEME HERE
theme_selector = ""  # Leave blank for automatic theme selection


def gpt3_call(theme):
    preset = (
        'Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión, el universo, el desarrollo humano, la antropología, distopias, Elon Musk, y música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo generara un Tweet de Galia según un tema a elección.\n\nTema: El ocio. \nTweet: Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n###\nTema: La música.\nTweet: La música crea mas simpatía que el sexo.\n###\nTema: Países sub desarrollados.\nTweet: Los países subdesarrollados deberían ser mas estrictos con la migración.\n###\nTema: Los carros.\nTweet: Me gusta mucho andar en bicicleta, pero estoy en contra de querer cambiar el mundo por ese termino.\n###\nTema: pornografía.\nTweet: me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una "sorpresa" a mi madre.\n###\nTema: Caleidoscopio.\nTweet: Mi vida es un caleidoscopio de emociones que se traslapan en cada momento. \n###\nTema:'
        + theme
    )
    if theme != "":
        preset += ".\nTweet"

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="davinci",
        prompt=preset,
        temperature=0.75,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0.16,
        stop=["###"],
    )
    text = response.choices[0].text

    # Text cleaning
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
    return text


def tweet(x):
    #  Twitter API Auth
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET")
    )
    auth.set_access_token(os.getenv("TWITTER_TOKEN"), os.getenv("TWITTER_TOKEN_SECRET"))
    oauth = auth
    t_api = tweepy.API(oauth)

    # Tweet
    t_api.update_status(x)
    print("Tweeted")


text = gpt3_call(theme_selector)
tweet(text)
