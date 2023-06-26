import os
import PyPDF2
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
import heapq
import nlp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Step 1: Load the dataset

# Function for extracting text content from PDF files
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def load_dataset(folder_path):
    dataset = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            text = extract_text_from_pdf(file_path)
            dataset.append(text)
    return dataset

# Example usage
dataset_folder_path = r"C:\Users\Lenovo\Downloads\nlp"
dataset = load_dataset(dataset_folder_path)

# Step 2: Preprocessing

# Function for preprocessing the text
def preprocess_text(text):
    # Example implementation of text preprocessing steps (lowercasing and removing stopwords)
    nlp=spacy.load("en_core_web_sm")
    text = text.lower()
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

# Apply preprocessing to the dataset
preprocessed_dataset = [preprocess_text(text) for text in dataset]

# Step 3: Training

# Function for training the model
def train_model(dataset):
    # Example implementation of model training (TF-IDF vectorization and K-means clustering)
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(dataset)
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X_train)
    return kmeans

# Train the model
trained_model = train_model(preprocessed_dataset)

# Step 4: User Input

# Get the keyword from the user
keyword = input("Enter a keyword: ")

# Step 5: Information Extraction

# Function for extracting relevant information from papers
def extract_information(text, keyword):
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(text)
    sentences=[sent.text.strip() for sent in doc.sents]
    extracted_info=[sent for sent in sentences if keyword in sent]
    return extracted_info
    
# Function to display extracted information in a formatted way
def display_information(extracted_info):
    if extracted_info:
        print("Extracted Information:")
        print("----------------------")
        for idx, info in enumerate(extracted_info, start=1):
            print(f"{idx}. {info}")
            print()
    else:
        print("No information found.")

# Example usage
for idx, text in enumerate(preprocessed_dataset, start=1):
    print(f"Processing Document {idx}")
    extracted_info = extract_information(text, keyword)
    display_information(extracted_info)
