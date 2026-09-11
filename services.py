def calculate_result(number1,number2,operation):
    if operation=="add":
        return number1+number2
    if operation=="subtract":
        return number1-number2
    if operation=="multiply":
        return number1*number2
    if operation=="divide":
        if number2==0:
            raise ValueError("Cannot divide by zero")
        return number1/number2
    raise ValueError("Invalid operation")

def analyze_text(text):
    words=text.split()
    unique_words=set(word.lower().strip(".,!?") for word in words)
    sentence_count=sum(text.count(mark) for mark in ".!?")
    return {
        "word_count":len(words),
        "character_count":len(text),
        "sentence_count":sentence_count,
        "unique_words":len(unique_words)
    }

def generate_response(prompt):
    return "AI enables computers to perform tasks that normally require human intelligence."