import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from features import text_to_speech, speech_to_text, pdf_to_text, detect_language, translate_text
def get_similarity(sentence1, sentence2):
    vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
    similarity_matrix = cosine_similarity(vectorizer)
    similarity_score = similarity_matrix[0, 1]
    return similarity_score
def simplify_text(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    generated_ids = model.generate(input_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return generated_text
def load_model():
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer
def get_answer(user_input, qa_pairs, model, tokenizer):
    simplified_question = simplify_text(user_input, model, tokenizer)
    max_similarity = 0
    best_match = None
    for question, answer in qa_pairs.items():
        similarity = get_similarity(simplified_question, question)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = answer
    return best_match
def main():
    qa_pairs_file = "jason.json"
    personal_file = "personal.json"
    model, tokenizer = load_model()
    with open(qa_pairs_file, "r") as json_file:
        qa_pairs = json.load(json_file)
    print("MineMaw: Ask me anything about mining laws in India.\nType 'Thank you' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'thank you':
            print("MineMaw: Exiting. Goodbye!")
            break
        elif user_input.lower() == 'speech to text':
            language_input = input("Enter the language you want to record your message in : \n\n Avaliable options are : \nEnglish == 'en' \nHindi == 'hi' \nTamil == 'ta' \nTelugu == 'te' \nKannada == 'kn' \n\nEnter your choice :\n")
            user_input = speech_to_text(language=language_input)
            if user_input:
                print("You (Speech to Text):", user_input)
                user_lang = detect_language(user_input)
                if user_lang != 'en':
                    user_input = translate_text(user_input, target_lang='en')
            else:
                print("You (Speech to Text): Sorry, I could not understand you.")
        elif user_input.lower() == 'pdf to text':
            pdf_path = input("Enter the path to the PDF file: \n")
            #example here is the mine laws pdf 
            #pdf_text = pdf_to_text('C:\\Users\\91951\\OneDrive\\Desktop\\MPMCs\\mine_laws.pdf')
            pdf_text = pdf_to_text(pdf_path)
            user_input = simplify_text(pdf_text, model, tokenizer)
            print("You (Gist of the PDF):", user_input)
        if(len(user_input)>3):
            answer = get_answer(user_input, qa_pairs, model, tokenizer)
            print("MineMaw:", answer)
            #here is where answer and user input is stored in peronal json file
            with open(personal_file, 'a') as personal_json_file:
                personal_json_file.write(json.dumps({user_input: answer}) + '\n')
            a = str(input("Do you want to convert the answer to your language? (Yes/No): "))
            if a.lower() == 'yes':
                # Translate the answer back to user's language
                answer_lang = detect_language(user_input)
                if answer_lang != 'en':
                    answer = translate_text(answer, target_lang=answer_lang)
                    print("MineMaw (in {}): {}".format(answer_lang, answer))
                #now to get text to speech option 
            b = str(input("Do you want to convert the answer to speech? (Yes/No): "))
            if b.lower() == 'yes':
                answer_lang = detect_language(user_input)
                text_to_speech(answer, language=answer_lang)        
if __name__ == "__main__":
    main()
