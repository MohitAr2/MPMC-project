import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import flask
from flask import request

app = flask.Flask(__name__)

def get_similarity(sentence1, sentence2):
    vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
    similarity_matrix = cosine_similarity(vectorizer)
    similarity_score = similarity_matrix[0, 1]
    return similarity_score

def simplify_text(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    generated_ids = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
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

qa_pairs_file = "jason.json"
model, tokenizer = load_model()
with open(qa_pairs_file, "r") as json_file:
    qa_pairs = json.load(json_file)

@app.route('/answer', methods=['GET'])
def answer():
    prompt = request.args.get('prompt')
    answer = get_answer(prompt, qa_pairs, model, tokenizer)
    return answer

if __name__ == "__main__":
    app.run()
    