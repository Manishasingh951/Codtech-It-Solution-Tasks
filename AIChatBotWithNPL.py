import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only the first time)
nltk.download('punkt')

# Define chatbot patterns 
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hi there!", "Hello!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["I'm an AI chatbot created by Manisha."]
    ],
    [
        r"how are you ?",
        ["I'm doing well. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries."]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!"]
    ],
    [
        r"bye|exit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Can you rephrase?"]
    ]
]

chatbot = Chat(pairs, reflections)
print("Hi! I'm your chatbot. Type 'bye' to exit.\n")
chatbot.converse()

