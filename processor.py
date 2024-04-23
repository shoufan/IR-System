import os
import pickle
from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Define the absolute path to the templates directory
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# Set the templates directory in the Flask app configuration
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = TEMPLATES_DIR

# Load inverted index from file
def load_inverted_index(filename):
    filepath = os.path.join(os.getcwd(), filename)  # Get current working directory and join with filename
    with open(filepath, 'rb') as f:
        inverted_index = pickle.load(f)
    return inverted_index

# Define function to process query using inverted index
def process_query(query, inverted_index, top_k=15):
    if query in inverted_index:
        return inverted_index[query][:top_k]
    else:
        return []

# Load inverted index
inverted_index = load_inverted_index('inverted_index.pkl')

# Define route for handling query
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    search_results = process_query(query, inverted_index)
    return render_template('search_results.html', query=query, search_results=search_results)

@app.route('/')
def home():
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(debug=True)
