from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def whatsapp_bot():
    msg = request.form.get("Body").strip().lower()
    response = MessagingResponse()
    reply = response.message()

    # Respostas personalizadas
    if "oi" in msg or "olá" in msg:
        reply.body("Olá! Como posso te ajudar hoje?")
    elif "anotar" in msg:
        reply.body("Certo! O que você quer que eu anote?")
    elif "obrigado" in msg:
        reply.body("De nada! Se precisar de mais alguma coisa, é só chamar. 😊")
    else:
        reply.body("Desculpe, não entendi. Pode reformular sua pergunta?")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)