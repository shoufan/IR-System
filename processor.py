import pickle
from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import os

app = Flask(__name__)

# Load inverted index from file
def load_inverted_index(filename):
    with open(filename, 'rb') as f:
        inverted_index = pickle.load(f)
    return inverted_index

# Define function to process query using inverted index
def process_query(query, inverted_index, top_k=15):
    # Placeholder function, replace with actual query processing logic
    # Here, we simply return the top k documents based on their relevance to the query
    if query in inverted_index:
        return inverted_index[query][:top_k]
    else:
        return []

# Load inverted index
inverted_index = load_inverted_index('inverted_index.pkl')

# Define route for handling query
@app.route('/search', methods=['GET'])
def search():
    # Get query from request parameters
    query = request.args.get('query')

    # Validate query
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    # Process query using inverted index
    search_results = process_query(query, inverted_index)

    # Render template with search results
    return render_template('search_results.html', query=query, search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)