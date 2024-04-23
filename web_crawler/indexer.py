from sklearn.feature_extraction.text import TfidfVectorizer
import os
import json
import pickle

def construct_inverted_index(documents):
    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Construct inverted index
    inverted_index = {}
    terms = vectorizer.get_feature_names_out()
    for doc_id, term_index in zip(*tfidf_matrix.nonzero()):
        term = terms[term_index]
        tfidf_value = tfidf_matrix[doc_id, term_index]
        if term not in inverted_index:
            inverted_index[term] = []
        inverted_index[term].append((doc_id, tfidf_value))

    return inverted_index

def save_inverted_index(inverted_index, filename):
    # Save inverted index to file
    with open(filename, 'wb') as f:
        pickle.dump(inverted_index, f)


# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the full path to output.json
output_json_path = os.path.join(current_directory, 'output.json')

# Read contents of output.json file
with open(output_json_path, 'r') as f:
    data = json.load(f)

# Extract text content from crawled HTML pages
documents = []
for item in data:
    text_content = item.get('content', '')  # Assuming 'content' is the key for HTML content in output.json
    documents.append(text_content)

# Construct inverted index
inverted_index = construct_inverted_index(documents)

# Save inverted index to file
save_inverted_index(inverted_index, 'inverted_index.pkl')