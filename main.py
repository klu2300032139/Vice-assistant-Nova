import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif "what's the weather like today" in query:
            speak("Good morning! Today's forecast predicts a sunny day with a high of 75 degrees Fahrenheit. It's a perfect day to go outside!")
            speak("Do you have any recommendations for outdoor activities?")
        elif "recommendations for outdoor activities" in query:
            speak("Absolutely! You could go for a hike in the nearby nature reserve or maybe have a picnic at the park. If you're feeling adventurous, you could even try out paddleboarding at the lake.")
            speak("I love paddleboarding! Can you check if there are any paddleboarding rentals available?")
        elif "paddleboarding rentals available" in query:
            speak("Of course! Give me a moment. I'll find the information for you. Yes, there's a paddleboarding rental shop called 'Water Adventures' just a few miles away from your location. They offer hourly rentals and have excellent customer reviews.")
            speak("That's perfect! Please check their availability for this afternoon.")
        elif "availability for this afternoon" in query:
            speak("I just checked, and they have availability from 2 PM to 5 PM this afternoon. Would you like me to make a reservation for you?")
            speak("Yes, please! Book it for two people at 3 PM.")
        elif "make a reservation" in query:
            speak("Reservation confirmed! You and your companion are all set for paddleboarding at 3 PM. Enjoy your time on the water!")
            speak("Thanks, Nova! You're the best. While we're at it, could you recommend a good restaurant for dinner afterward?")
        elif "recommend a good restaurant" in query:
            speak("Of course! What type of cuisine are you in the mood for?")
            speak("I'm in the mood for some Italian food. Any suggestions?")
        elif "Italian food" in query:
            speak("I recommend 'La Trattoria.' It's a cozy Italian restaurant known for its authentic dishes and charming atmosphere. It's just a short drive from your current location.")
            speak("That sounds lovely! Can you check if they have any available reservations for tonight?")
        elif "available reservations for tonight" in query:
            speak("Let me check for you. Yes, they have a few available slots. How about 7:30 PM?")
            speak("Sounds perfect! Please make a reservation for two at 7:30 PM at La Trattoria.")
        elif "make a reservation for two" in query:
            speak("Reservation made for 7:30 PM at La Trattoria. Enjoy your evening and the delicious Italian cuisine!")
            speak("Thank you, Nova! You've been a great help.")
            speak("You're welcome! It's my pleasure to assist you. Have a fantastic day and enjoy your activities and dinner. If you need any further assistance, feel free to ask.")
        else:
            speak("Sorry, I'm not sure how to help with that.")