from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear una instancia de ChatBot
chatbot = ChatBot('MiChatBot')

# Crear un entrenador para el chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Entrenar el chatbot con el corpus en inglés
trainer.train('chatterbot.corpus.english')

# Preguntas precargadas
preguntas_precargadas = [
    "Hola",
    "¿Cómo estás?",
    "¿De qué te gustaría hablar?"
]

# Agregar preguntas precargadas al conocimiento del chatbot
for pregunta in preguntas_precargadas:
    respuesta = chatbot.get_response(pregunta)

# Definir la pregunta para ingresar nuevo conocimiento
pregunta_nueva_conocimiento = "No entiendo, ¿puedes proporcionar más información?"

# Iniciar el bucle de conversación
print("¡Hola! Soy tu chatbot. Puedes preguntarme lo que quieras. Para salir, escribe 'adiós'.")

while True:
    usuario_input = input("Tú: ")
    
    if usuario_input.lower() == 'adiós':
        print("Chatbot: ¡Hasta luego!")
        break
    else:
        # Obtener la respuesta del chatbot
        respuesta = chatbot.get_response(usuario_input)
        
        # Verificar si la respuesta no es muy confiable
        if float(respuesta.confidence) < 0.5:
            print("Chatbot:", pregunta_nueva_conocimiento)
            
            # Obtener nueva información del usuario
            nuevo_conocimiento = input("Tú: ")
            
            # Aprender de la conversación
            chatbot.learn_response(usuario_input, nuevo_conocimiento)
            
            print("Chatbot: Gracias por la información. ¿Hay algo más en lo que pueda ayudarte?")
        else:
            print("Chatbot:", respuesta)