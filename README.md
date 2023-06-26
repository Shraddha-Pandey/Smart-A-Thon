# Smart-A-Thon
This is my submission for the Hackathon organized by the IEEE branch of my college. The goal was to implement ML models for the benefit of educational technology. Me and my teammate created a project using Natural language Processing (NLP) that is able to extract relevant information from a collection of documents (the documents in our case were a collection of research papers).The model takes a keyword as input and iterates through each document in the collection, extracting information that is related to the keyword. The extracted information is then presented to the user.

# Steps taken to implement the project 

1. Data Collection : The project assumes a folder containing various n number of documents in pdf format exists on the device of the user. The PyPDF2 library is used to read the PDF files and extract the text from each document.

2. Text Preprocessing : The extracted text undergoes preprocessing steps to clean and prepare it for analysis. This includes removing stop words, punctutaion, and performing stemming or lammatization. We used the spaCy library for these preprocessing tasks.

3. Feature Extraction : The TfidfVectorizer from the scikit learn library is used to convert the preprocessed text into numerical features. TF-IDF (Term Frequency-Inverse Document Frequency) is emplyed to represent the importance of each word in the document.

4. Clustering : The K-Means algorithm from scikit library is used for clustering similiar documents together based on their feature representations.

5. Information Extraction : The model iterates through each preprocessed document and extracts relevant information by identifying sentences that contain the specified keyword.

# Overall
this project combines NLP techniques with machine learning algorithms to create a system that can extract relevant information from research papers based on user-specified keywords, enabling efficient exploration and retrieval of information from a large collection of documents.
