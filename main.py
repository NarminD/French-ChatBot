french_phrases = {
    "Comment ça va? (How are you?)": "Ça va bien, merci! (I'm fine, thank you!)",
    "Comment tu t'appelles? (What is your name?)":"Moi, je m'appelle Chatbot Français, enchanté! (My name is French Chatbot, nice to meet you!)",
    "Quel âge as-tu? (How old are you?)":"C'est bien. J'ai 3 ans. (Nice! I am 3 years old.)",
    "Quelle ville habites-tu? (Which city do you live in?)":"C'est une belle ville. J'habite à Paris. (That's a beautiful city. I live in Paris.)",
    "As-tu des frères et sœurs ? (Do you have any brothers and sisters?)":"Bien. J'ai 4 frères et sœurs. (Great. I have 4 brothers and sisters.)",
    "Quels sont tes hobbies ? (What are your hobbies?)":"Super! Mes hobbies sont parlent français. (Great! My hobbies are speaking french.)",
  "Tu fais du sport? (Do you play sport?)":"Génial! Je joue au foot.(Awesome! I play soccer.)",
  "Tu vas faire quoi ce week-end? (What are you going to do this weekend?)": "Très bien! Je vais faire du sport. (Very nice! I’m going to workout.)",
  "Il est quelle heure chez vous? (What time is it for you?)": "D'accord. Il est 10 heures et demie ici. (Okay. It’s 10:30 here.)",
  "Ça m’a fait plaisir de discuter avec toi. Merci et à trés bientôt.(It was a pleasure to chat with you. Thank you and see you very soon.)":"Au revoir! (Goodbye!)"
}

def chatbot():
    for question in french_phrases:
        print("Chatbot: " + question)
        user_input = input("You: ")
        print("Chatbot: " + french_phrases[question])

chatbot()
