import tweepy
import openai
import os


def gpt3_call():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    restart_sequence = "\n###\nTema y Tweet:"

    response = openai.Completion.create(
        engine="davinci",
        prompt='Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión y la buena música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo hará 4 generaciones, cada una deberá tener un tema, luego un guion y por ultimo el Tweet en base al tema.\n\nTema y Tweet:\n1. La música - La música crea mas simpatía que el sexo\n2. Filosofía psicodélica - La distancia es un caudal de eternidad agazapada sobre la espalda de un león\n3. El ocio - Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n4. Países sub desarrollados - Los países subdesarrollados deberían ser mas estrictos con la migración.\n###\nTema y Tweet:\n1. pornografía - me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una "sorpresa" a mi madre\n2. Caleidoscopio - Mi vida es un caleidoscopio de emociones que se traslapan en cada momento\n3. Memes - En los 2010s los memes impulsaban la cultura, en los 2020s impulsan la economía\n4. Bio de Twitter - El que no tiene la suficiente creatividad para hacer una buena bio debería dejar de utilizar las redes sociales\n###\nTema y Tweet:',
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3,
        stop=["###", "Tema y"],
    )
    text = response.choices[0].text

    print(text)
    print()
    return text


def text_cleaning(text):
    # divide that text into 4 strings
    tweets_starts = []
    tweets_ends = []
    for i, word in enumerate(text):
        if word == "1" and text[i + 1] == ".":
            tweets_starts.append(i + 3)

        elif (
            (word == "2" and text[i + 1] == ".")
            or (word == "3" and text[i + 1] == ".")
            or (word == "4" and text[i + 1] == ".")
        ):
            tweets_starts.append(i + 3)
            tweets_ends.append(i - 1)
    tweets_ends.append(len(text))

    tweets = []
    for i in range(len(tweets_starts)):
        tweets.append(text[tweets_starts[i] : tweets_ends[i]].split(" - ")[1])

    return tweets


def tweet(tweets):
    #  Twitter API Auth
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET")
    )
    auth.set_access_token(os.getenv("TWITTER_TOKEN"), os.getenv("TWITTER_TOKEN_SECRET"))
    oauth = auth
    t_api = tweepy.API(oauth)

    # Tweet
    for tweet in tweets:
        t_api.update_status(tweet)
        print("Tweeted")


response = gpt3_call()
tweets = text_cleaning(response)
tweet(tweets)
