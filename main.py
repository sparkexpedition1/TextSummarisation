import streamlit as st
import pydaisi as pyd
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#import nltk
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize, sent_tokenize
# def printSummary(text):  
#     # Tokenizing the text
#     stopWords = set(stopwords.words("english"))
#     words = word_tokenize(text)

#     # Creating a frequency table to keep the 
#     # score of each word

#     freqTable = dict()
#     for word in words:
#         word = word.lower()
#         if word in stopWords:
#             continue
#         if word in freqTable:
#             freqTable[word] += 1
#         else:
#             freqTable[word] = 1

#     # Creating a dictionary to keep the score
#     # of each sentence
#     sentences = sent_tokenize(text)
#     sentenceValue = dict()

#     for sentence in sentences:
#         for word, freq in freqTable.items():
#             if word in sentence.lower():
#                 if sentence in sentenceValue:
#                     sentenceValue[sentence] += freq
#                 else:
#                     sentenceValue[sentence] = freq



#     sumValues = 0
#     for sentence in sentenceValue:
#         sumValues += sentenceValue[sentence]

#     # Average value of a sentence from the original text

#     average = int(sumValues / len(sentenceValue))

#     # Storing sentences into our summary.
#     summary = ''
#     for sentence in sentences:
#         if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
#             summary += " " + sentence
#     st.title(summary)

st.set_page_config(layout = "wide")
text = st.sidebar.text_input("Text", "Sample Text")
analyzer = SentimentIntensityAnalyzer()
value = analyzer.polarity_scores(sentence)['compound']
# Converting Rating from -1 to 1 into 1 to 5
new_value = ((((value) - (-1)) * (5 - 1)) / (1 - (-1))) + 1
if new_value < 2.5:
    st.title("Negative")
elif new_value > 3.5:
    st.title("Positive")
else:
    st.title("Neutral")
# printSummary(text)
