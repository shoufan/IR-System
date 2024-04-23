import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_index(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    with open('beethoven_index.pickle', 'wb') as f:
        pickle.dump({'vectorizer': vectorizer, 'tfidf_matrix': tfidf_matrix}, f)

def search_index(query, k=3):
    with open('beethoven_index.pickle', 'rb') as f:
        data = pickle.load(f)
        vectorizer = data['vectorizer']
        tfidf_matrix = data['tfidf_matrix']

    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    top_results = similarities.argsort()[0, :(-k - 1):-1]  # Top K results (descending order)

    return [(documents[i], similarities[0, i]) for i in top_results]

# Example usage
documents = ['content from Beethoven page 1', 'content from Beethoven page 2']  # Replace with actual scraped content
create_index(documents)
query = 'Life of Beethoven'
results = search_index(query)
print(results)
