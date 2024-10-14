import pickle

# Load the saved model using pickle
model_filename = "responser.pkl"
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Chatbot loop for prediction
print("Chatbot: Hello! How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    predicted_response = loaded_model.predict([user_input])
    print("Chatbot:", predicted_response[0])
