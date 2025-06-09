
def get_response(message):
    message = message.lower()
    if "d2l" in message:
        return "You can access D2L here: https://d2l.msu.edu/"
    elif "brody" in message or "dining" in message:
        return "Today’s Brody menu is: 🍕 Pizza, 🍝 Pasta, 🥗 Salad Bar (sample data)"
    elif "wells hall" in message:
        return "Wells Hall is located at 619 Red Cedar Rd. 📍 Google Maps: https://goo.gl/maps/..."
    else:
        return "Sorry, I'm still learning! Try asking about dining, D2L, or buildings on campus."

def get_ai_response(message):
    message = message.lower()
    return message