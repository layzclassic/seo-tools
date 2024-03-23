import spacy
from collections import Counter

def process_article(article):
    # Load the spaCy English language model
    nlp = spacy.load('en_core_web_sm')
    
    # Tokenize the article into individual words
    doc = nlp(article)
    
    # Filter out stop words and punctuation
    filtered_words = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    # Count the frequency of each term
    term_freq = Counter(filtered_words)
    
    return term_freq

# Example usage
input_article = "This is an example sentence to remove stop words from. This is another example sentence."
result = process_article(input_article)
print("Term frequency in the article:", result)
