# Crea una funcion que reciba un texto y devuelva una lista de tweets


def tweet_creation(text):
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
        sections = text[tweets_starts[i] : tweets_ends[i]].split(" - ")
        tweets.append([sections[1], sections[2]])

    return tweets


text = "1. - Pablo Picasso - La Guernica. 2. - Salvador Dalí - La persistencia de la memoria. 3. - Joan Miró - La mujer desnuda. 4. - Joan Miró - El grito."
tweet_creation(text)
