from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def construct_inverted_index(documents):
    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Construct inverted index
    inverted_index = {}
    terms = vectorizer.get_feature_names_out()
    for i, term in enumerate(terms):
        inverted_index[term] = [(doc_id, tfidf) for doc_id, tfidf in zip(tfidf_matrix.indices[tfidf_matrix.indptr[i]:tfidf_matrix.indptr[i+1]], tfidf_matrix.data[tfidf_matrix.indptr[i]:tfidf_matrix.indptr[i+1]])]

    return inverted_index

def save_inverted_index(inverted_index, filename):
    # Save inverted index to file
    with open(filename, 'wb') as f:
        pickle.dump(inverted_index, f)

# Sample documents
documents = [
    "Sample document 1",
    "Sample document 2",
]

# Construct inverted index
inverted_index = construct_inverted_index(documents)

# Save inverted index to file
save_inverted_index(inverted_index, 'inverted_index.pkl')
