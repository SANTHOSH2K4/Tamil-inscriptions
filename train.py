import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define preprocess_text function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    # Join tokens back into a single string
    text = ' '.join(tokens)
    return text

# Read data from Excel file
data = pd.read_excel("bot.xlsx")

# Check for and handle missing values
data.dropna(inplace=True)  # Remove rows with missing values
data.reset_index(drop=True, inplace=True)  # Reset the index

# Use the first column as X_train and the second column as y_train
X_train = data.iloc[:, 0].apply(preprocess_text)
y_train = data.iloc[:, 1]

# Create a pipeline with a CountVectorizer and Multinomial Naive Bayes classifier
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the intent classifier
pipeline.fit(X_train, y_train)

# Save the trained model using pickle
model_filename = "responser.pkl"
with open(model_filename, 'wb') as model_file:
    pickle.dump(pipeline, model_file)

print("Model saved as:", model_filename)
