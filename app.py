from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

draw_synonyms = ["draw", "paint", "image", "picture", "painting", "drawing"]

de generate_image(text_prompt):
    generation_response = openai.Image.create(
    prompt = text_prompt,
    n=1,
    size = "1024x1024",
    response_format="url",
    )

    print(generation_response)

    generated_image_url = generation_response["data"][0]["url"]
    return generated_image_url
