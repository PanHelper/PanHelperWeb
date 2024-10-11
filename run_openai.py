import openai
openai.api_key = 'sk-H82qB7DnMmEG3lJAu1WEpiN-ENRQ2S1hiODCFiA5VWT3BlbkFJgRqwVLAjvBPWtOVxyD03r4zfaXp5xhQ9ARoUs_X14A'

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        message = response['choices'][0]['message']['content']
        return message
    except Exception as e:
        return "Sorry, I couldn't answer your question. Please try again."

def chat_with_gpt(user_input):
    if user_input.lower() in ['hello', 'hi']:
        return "Hi there! How can I assist you today?"
    else:
        return "I'm here to help with any questions!"

def main():
    print("Chatbot: Hello! I'm here to help you. Ask me anything!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
