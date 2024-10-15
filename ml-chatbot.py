import json
from difflib import get_close_matches
from typing import Optional
import re

def load(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading the knowledge base: {e}")
        return {"questions": [], "unanswered_questions": []} 

def save(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_exact_match(user_q: str, questions: list) -> Optional[str]:
    for question in questions:
        if isinstance(question, list):
            for q in question:
                if user_q.lower() == q.lower():
                    return q
        elif isinstance(question, str) and user_q.lower() == question.lower():
            return question
    return None

def correct_typos(user_q: str) -> str:
    corrections = {
        'si': 'is',
        'whot': 'who',
        'wat': 'what',
        'wer': 'where',
        'whenr': 'when',
        'howa': 'how',
        'coud': 'could',
        'woud': 'would',
        'you': 'u',
        'pleas': 'please',
        'thx': 'thanks',
        'thnaks': 'thanks',
        'ok': 'okay',
        'ur': 'your',
        'their': 'there',
        'its': 'it’s',
        'im': 'i’m',
        'youd': 'you’d',
        'yours': 'your',
        'wanna': 'want to',
        'gonna': 'going to',
    }
    
    words = user_q.split()
    corrected_words = [corrections.get(word.lower(), word) for word in words]
    
    return ' '.join(corrected_words)

def suggest_similar_questions(user_q: str, questions: list, threshold: float = 0.6) -> list[str]:
    corrected_user_q = correct_typos(user_q)
    
    flat_questions = [q for question in questions for q in (question if isinstance(question, list) else [question])]
    match = re.match(r'^(Who is|What is|Where is|When is|How is|Why is)', corrected_user_q, re.IGNORECASE)
    if match:
        prefix = match.group(0) 
        structured_questions = [q for q in flat_questions if q.lower().startswith(prefix.lower())]
        suggestions = get_close_matches(corrected_user_q, structured_questions, n=3, cutoff=threshold)
        if not suggestions:
            return structured_questions[:3]
        
        return suggestions

    return []

def get_answer(question: str, knowledge_base: dict) -> Optional[str]:
    for q in knowledge_base["questions"]:
        if isinstance(q["question"], list):
            if question in q["question"]:
                return q["answer"]
        elif q["question"].lower() == question.lower():
            return q["answer"]
    return None

def print_link(text, url) -> str:
    return f'{text}: {url}'

def contains_sensitive_topics(user_in: str) -> bool:
    sensitive_keywords = [
        'alcohol', 'drugs', 'hazing', 'bullying', 'harassment', 
        'abuse', 'assault', 'suicide', 'self-harm', 'violence', 
        'racism', 'sexism', 'homophobia', 'stalking', 'rape', 
        'discrimination'
    ]
    return any(keyword in user_in.lower() for keyword in sensitive_keywords)

def extract_questions(knowledge_base: dict) -> list:
    return [q["question"] for q in knowledge_base["questions"]]

def chat_bot():
    knowledge_base = load('knowledge_base.json')
    print("Hello! I'm PaigePal, How can I help you today?")
    
    while True:
        user_in = input('Please enter your question and end with a "?" (type "quit" to quit the chatbot): ')
        
        if user_in.lower() == 'quit':
            break

        if not user_in.endswith('?'):
            print('PaigePal: Error - Please ask a question that ends with a "?".')
            continue 
        
        if contains_sensitive_topics(user_in):
            print(f"PaigePal: Unfortunately, I am not able to answer questions regarding that topic at this time. Please refer to RPI's {print_link('Student Rights, Responsibilities, and Conduct', 'https://info.rpi.edu/dean-students/student-rights-responsibilities-and-conduct')}")
            continue
        
        questions = extract_questions(knowledge_base)
        best_match = find_exact_match(user_in, questions)
        
        if best_match:
            answer = get_answer(best_match, knowledge_base)
            print(f'PaigePal: {answer}')
        else:
            similar_questions = suggest_similar_questions(user_in, questions)
            if similar_questions:
                print("PaigePal: I couldn't find an exact match, but did you mean one of these questions?")
                for i, suggestion in enumerate(similar_questions, 1):
                    print(f"{i}. {suggestion}")
            else:
                print("PaigePal: I have never received this question before. I will save it for the team to address.")
                knowledge_base['unanswered_questions'].append({"question": user_in, "response": None})
                save('knowledge_base.json', knowledge_base)
                print(f'PaigePal: Your question has been noted for future reference!')

if __name__ == '__main__':
    chat_bot()
