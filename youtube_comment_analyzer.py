# -*- coding: utf-8 -*-
"""youtube_comment_analyzer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p4csu9-cGz5zwHNb8P3t0fp4mexL5EGp
"""

import re

def clean_text(text):
    # Remove special characters, URLs, and non-alphanumeric characters
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text



def tokenize_text(text):
    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)
    return tokens



def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return tokens



def lemmatize_words(tokens):
    lemmatizer = WordNetLemmatizer()
    # Lemmatize words
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized_tokens

def preprocess_text(comment):
    cleaned_comment = clean_text(comment)
    tokens = tokenize_text(cleaned_comment)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_words(tokens)
    return ' '.join(tokens)



def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    # Assign a sentiment score
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def perform_sentiment_analysis(preprocessed_comments):
    sentiment_scores = {'positive': 0, 'neutral': 0, 'negative': 0}

    for comment in preprocessed_comments:
        sentiment = analyze_sentiment(comment)
        sentiment_scores[sentiment] += 1

    return sentiment_scores



def plot_sentiment_distribution(sentiment_scores):
    labels = sentiment_scores.keys()
    sizes = [sentiment_scores[label] for label in labels]

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99', '#ff9999'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sentiment Distribution of Comments')
    plt.show()

# Example usage
sentiment_scores = {'positive': 30, 'neutral': 50, 'negative': 20}
plot_sentiment_distribution(sentiment_scores)





# Function to fetch comments using YouTube Data API
def fetch_youtube_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        order="relevance",
        maxResults=100
    )

    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments

# Use the API key and video ID to fetch comments
api_key = "AIzaSyCSSgeaDnJwCtV4iRHXXTFJWh93wMnaDBE"  # Replace with your YouTube Data API key
video_id = "KAh2TOrtTq4"  # Replace with the YouTube video ID you want to analyze

comments = fetch_youtube_comments(api_key, video_id)

# Continue with preprocessing, sentiment analysis, and visualization...
# ... (use the pre-processing, sentiment analysis, and visualization code from previous steps)

# Example usage: Print the comments fetched
print("Comments fetched from the video:")
for comment in comments:
    print(comment)

# Perform sentiment analysis on the comments and plot the sentiment distribution
preprocessed_comments = [preprocess_text(comment) for comment in comments]
sentiment_scores = perform_sentiment_analysis(preprocessed_comments)
plot_sentiment_distribution(sentiment_scores)





# Define the Streamlit app
st.title('YouTube Video Analyzer')

# Add input for YouTube video URL
video_url = st.text_input('Enter YouTube Video URL:')



# Function to fetch YouTube comments using the YouTube Data API
def fetch_youtube_comments(api_key, video_id):
    """
    Fetches comments for a YouTube video using the YouTube Data API.

    Parameters:
        api_key (str): The YouTube Data API key.
        video_id (str): The YouTube video ID for which to fetch comments.

    Returns:
        list: A list of comments for the specified video.
    """
    # Use the YouTube Data API to fetch comments
    # ...
    return comments

# Function to preprocess text
def preprocess_text(comment):
    """
    Preprocesses a comment text.

    Parameters:
        comment (str): The comment text to be preprocessed.

    Returns:
        str: The preprocessed comment text.
    """
    # Preprocess the comment
    # ...
    return preprocessed_comment

# Function to analyze sentiment
def analyze_sentiment(comment):
    """
    Analyzes the sentiment of a given comment using TextBlob.

    Parameters:
        comment (str): The comment text to be analyzed.

    Returns:
        str: Sentiment label ('positive', 'negative', or 'neutral').
    """
    # Analyze sentiment
    # ...
    return sentiment_label

# Function to perform sentiment analysis
def perform_sentiment_analysis(preprocessed_comments):
    """
    Performs sentiment analysis on a list of preprocessed comments.

    Parameters:
        preprocessed_comments (list): A list of preprocessed comments.

    Returns:
        dict: A dictionary containing sentiment labels and their corresponding counts.
    """
    # Perform sentiment analysis
    # ...
    return sentiment_scores

# Function to plot sentiment distribution
def plot_sentiment_distribution(sentiment_scores):
    """
    Plots the sentiment distribution pie chart.

    Parameters:
        sentiment_scores (dict): A dictionary containing sentiment labels and their corresponding counts.
    """
    labels = sentiment_scores.keys()
    sizes = [sentiment_scores[label] for label in labels]

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99', '#ff9999'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sentiment Distribution of Comments')
    plt.show()

# Define the Streamlit app
st.title('YouTube Video Analyzer')

# Add input for YouTube video URL
video_url = st.text_input('Enter YouTube Video URL:')

# Fetch comments and display sentiment analysis results
if video_url:
    # Replace with your YouTube API key
    api_key = "AIzaSyCSSgeaDnJwCtV4iRHXXTFJWh93wMnaDBE"

    comments = fetch_youtube_comments(api_key, video_id)
    preprocessed_comments = [preprocess_text(comment) for comment in comments]
    sentiment_scores = perform_sentiment_analysis(preprocessed_comments)

    # Display sentiment distribution
    st.write('### Sentiment Distribution')
    plot_sentiment_distribution(sentiment_scores)

# Display information about the app
if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable a Streamlit warning
    st.write("## Analyze YouTube Comments")
    st.write("Enter a YouTube video URL above to analyze comments.")

