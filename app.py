from flask import Flask, render_template, request
app = Flask(__name__)
def generate_acronym(phrase):
    """Generate an acronym from a given phrase."""
    words = phrase.split()  
    acronym = ''.join(word[0].upper() for word in words)  
    return acronym

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    phrase = request.form.get('phrase', '')
    if phrase:
        acronym = generate_acronym(phrase)
        return render_template('index.html', acronym=acronym, phrase=phrase)
    return render_template('index.html', error="Please enter a valid phrase!")

if __name__ == '__main__':
    app.run(debug=True)
