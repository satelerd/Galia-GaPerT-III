import tweepy
import openai
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import os
import io
from PIL import Image


def gpt3_call():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    restart_sequence = "\n###\nTema y Tweet:"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt='Galia es una filósofa culta, creativa, de moral propia y una mujer seductora. Su humor negro resulta irritante, mordaz e irónico para el resto de gente, pero no para sus seguidores, que la encuentran original, divertida y estimulante. Galia se creó Twitter para compartir sus opiniones y su fin es hacer que la gente piense por sí misma. No tiene miedo de decir lo que piensa.\n\nEste modelo hará 4 generaciones, cada una deberá tener un tema y un Tweet sobre el tema.\n\nTema y Tweet:\n1. La música - La música crea más simpatía que el sexo\n2. Filosofía psicodélica - La distancia es un caudal de eternidad agazapada sobre la espalda de un león\n3. El ocio - Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n4. Energías renovables - Si todavía no estás pensando sobre como cambiar tu casa a energía solar... se nota que eres boomer\n###\nTema y Tweet:\n1. Pornografía - me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una "sorpresa" a mi madre\n2. Caleidoscopio - Mi vida es un caleidoscopio de emociones que se traslapan en cada momento\n3. Memes - En los 2010s los memes impulsaban la cultura, en los 2020s impulsan la economía\n4. Bio de Twitter - El que no tiene la suficiente creatividad para hacer una buena bio debería dejar de utilizar las redes sociales\n###\nTema y Tweet:',
        temperature=0.8,
        max_tokens=190,
        top_p=1,
        frequency_penalty=0.7,
        presence_penalty=0.7,
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

    return tweets[:2]


def sd_call(tweets):
    print(os.getenv("STABILITY_API_KEY"))
    stability_api = client.StabilityInference(
        key="sk-PKx2Fh0nJlsurlyJMOdFFjbvHYOMRPr9qtk2XCO7nsPBWsoj",
        verbose=True,
    )

    cont = 0
    for tweet in tweets:
        answers = stability_api.generate(prompt=tweet)

        for rep in answers:
            for artifact in rep.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    print("Filtered")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    img.save(f"image{cont}.png")
                    cont += 1

    return "img generated"


def tweet(tweets):
    #  Twitter API Auth
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET")
    )
    auth.set_access_token(os.getenv("TWITTER_TOKEN"), os.getenv("TWITTER_TOKEN_SECRET"))
    oauth = auth
    t_api = tweepy.API(oauth)

    # Tweet
    cont = 0
    for tweet in tweets:
        media = t_api.media_upload(f"image{cont}.png")
        t_api.update_status(status=tweet, media_ids=[media.media_id])
        cont += 1
        print("Tweeted")


response = gpt3_call()
tweets = text_cleaning(response)
# tweets = ["la tierra es como una manzana", "la sensacion del vertigo"]
sd_call(tweets)
tweet(tweets)
