from flask import Flask, render_template, request
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the GPT-2 model using Hugging Face's pipeline
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get the prompt from the form
    prompt = request.form['prompt']
    
    # Generate text with GPT-2
    response = generator(prompt, max_length=100, num_return_sequences=1)
    generated_text = response[0]['generated_text']

    return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)