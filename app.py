from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)
openai.api_key = ""

draw_synonyms = ["draw", "paint", "image", "picture", "painting", "drawing"]

def generate_image(text_prompt):
    generation_response = openai.Image.create(
    prompt = text_prompt,
    n=1,
    size = "1024x1024",
    response_format="url",
    ) 

    print(generation_response)

    generated_image_url = generation_response["data"][0]["url"]
    return generated_image_url


def generate_answer(question):
    completions = openaiCompletion.create(
    model = "text-davinci-004",
    temperature = 0.5,
    prompt = question,
    max_tokens = 100,
    n=1,
    stop = none,
    )

    return completions.choices[0].text



@app.route("/whatsapp", methods=['POST'])


def wa_reply():

    query = request.form.get('Body').lower()
    print("user Query ", query)
    twilio_response = MessagingResponse()
    reply = twilio_response.message()

    if query.split(" ")[0].lower() in draw_synonyms:
         img_url = generate_image(query)
         reply.media(img_url, caption = query)

    else: 

        answer = generate_answer(query)
        reply.body(answer)

    return str(twilio_response)
     
