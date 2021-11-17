import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

restart_sequence = "\n###\nTema y Tweet:"

response = openai.Completion.create(
    engine="davinci",
    prompt='Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión y la buena música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo hará 4 generaciones, cada una deberá tener un tema, luego un guion y por ultimo el Tweet en base al tema.\n\nTema y Tweet:\n1. La música - La música crea mas simpatía que el sexo\n2. Los autos - Me gusta mucho andar en bicicleta, pero estoy en contra de querer cambiar el mundo por ese termino\n3. El ocio - Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n4. Países sub desarrollados - Los países subdesarrollados deberían ser mas estrictos con la migración\n###\nTema y Tweet:\n1. pornografía - me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una "sorpresa" a mi madre\n2. Caleidoscopio - Mi vida es un caleidoscopio de emociones que se traslapan en cada momento\n3. Ropa - A veces me gustaría vivir sin ropa, pero siempre hay un factor social que impide ese hecho\n4. Bio de Twitter - El que no tiene la suficiente creatividad para hacer una buena bio debería dejar de utilizar las redes sociales\n###\nTema y Tweet:',
    temperature=0.82,
    max_tokens=190,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["###", "Tema y"],
)
