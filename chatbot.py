import json

def load(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_exact_match(user_q: str, questions: list) -> str | None:
    for question in questions:
        # Check if the question is a list of possible questions
        if isinstance(question, list):
            for q in question:
                if user_q.lower() == q.lower():
                    return q
        elif isinstance(question, str) and user_q.lower() == question.lower():
            return question
    return None

def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if isinstance(q["question"], list):
            if question in q["question"]:
                return q["answer"]
        elif q["question"].lower() == question.lower():
            return q["answer"]
    return None

def print_link(text, url):
    return f'{text}: {url}'

def contains_sensitive_topics(user_in: str) -> bool:
    sensitive_keywords = [
        'alcohol', 
        'drugs', 
        'hazing', 
        'bullying', 
        'harassment', 
        'abuse', 
        'assault', 
        'suicide', 
        'self-harm', 
        'violence', 
        'racism', 
        'sexism', 
        'homophobia', 
        'stalking', 
        'rape', 
        'discrimination'
    ]
    for keyword in sensitive_keywords:
        if keyword in user_in.lower():
            return True
    return False

def chat_bot():
    knowledge_base: dict = load('knowledge_base.json')
    print("Hello! I'm PaigePal, How can I help you today?")
    
    while True:
        user_in: str = input('Please enter your question and end with a "?" (type "quit" to quit the chatbot): ')
        
        # Check if the user wants to quit
        if user_in.lower() == 'quit':
            break
        
        # Check if the input ends with a '?'
        if not user_in.endswith('?'):
            print('PaigePal: Error - Please ask a question that ends with a "?".')
            continue  # Ask the user for input again

        # Check for sensitive topics
        if contains_sensitive_topics(user_in):
            print(f"PaigePal: Unfortunately, I am not able to answer questions regarding that topic at this time. Please refer to RPI's {print_link('Student Rights, Responsibilities, and Conduct', 'https://info.rpi.edu/dean-students/student-rights-responsibilities-and-conduct')}")
            continue
        
        # Find an exact match for the question
        best_match: str | None = find_exact_match(user_in, [q["question"] for q in knowledge_base["questions"]])
        
        # If a match is found, provide the answer
        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f'PaigePal: {answer}')
        else:
            # If no match is found, log the unanswered question
            print("PaigePal: I have never received this question before. I will send it to the team to answer.")
            knowledge_base['unanswered_questions'].append({"question": user_in})
            save('knowledge_base.json', knowledge_base)
            print(f'PaigePal: Your question has been noted for the team to address!')

if __name__ == '__main__':
    chat_bot()
