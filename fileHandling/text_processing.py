import string
import inflect
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

# Convert to Lowercase
def text_lowercase(text):
    return text.lower()

input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
print(text_lowercase(input_str))
print("*"*50)

# Removing Numbers - here we used regular expressions to remove numbers.
def remove_numbers(text):
    return re.sub(r'\d+', '', text)


input_str = "There are 3 balls in this bag, and 12 in the other one."
print(remove_numbers(input_str))
print("*"*50)

# We can also convert the numbers into words. This can be done by using the inflect library.
p = inflect.engine()

def convert_number(text):
    temp_str = text.split()
    new_string = []

    for word in temp_str:
        if word.isdigit():
            new_string.append(p.number_to_words(word))
        else:
            new_string.append(word)

    return ' '.join(new_string)
input_str = "There are 3 balls in this bag, and 12 in the other one."
print(convert_number(input_str))
print("*"*50)

# We remove punctuations so that we don't have different forms of the same word. For example if we don't remove the punctuation then been. been, been! will be treated separately.
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
print(remove_punctuation(input_str))
print("*"*50)

# We can use the join and split functions to remove all the white spaces in a string.
def remove_whitespace(text):
    return " ".join(text.split())
input_str = "we don't need   the given   questions"
print(remove_whitespace(input_str))
print("*"*50)

# Stopwords are words that do not contribute much to the meaning of a sentence hence they can be removed. The NLTK library has a set of stopwords and we can use these to remove stopwords from our text.
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')


def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower()
                     not in stop_words]
    return filtered_text


example_text = "This is a sample sentence and we are going to remove the stopwords from this."
print(remove_stopwords(example_text))
print("*"*50)

# Stemming is the process of getting the root form of a word. Stem or root is the part to which affixes like -ed, -ize, -de, -s, etc are added. The stem of a word is created by removing the prefix or suffix of a word.
stemmer = PorterStemmer()


def stem_words(text):
    word_tokens = word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return stems


text = "data science uses scientific methods algorithms and many types of processes"
print(stem_words(text))
# There are mainly three algorithms for stemming. These are the Porter Stemmer, the Snowball Stemmer and the Lancaster Stemmer. Porter Stemmer is the most common among them.
print("*"*50)


# Lemmatization is an NLP technique that reduces a word to its root form. This can be helpful for tasks such as text analysis and search as it allows us to compare words that are related but have different forms.
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


def lemma_words(text):
    word_tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(word) for word in word_tokens]
    return lemmas


input_str = "data science uses scientific methods algorithms and many types of processes"
print(lemma_words(input_str))
print("*"*50)

# POS tagging is the process of assigning each word in a sentence its grammatical category, such as noun, verb, adjective or adverb. It helps machines understand the structure and meaning of text, enabling tasks like parsing, information extraction and text analysis.
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import os
import sys

nltk_data_dir = '/usr/local/share/nltk_data'
if nltk_data_dir not in nltk.data.path:
    nltk.data.path.append(nltk_data_dir)

nltk.download('averaged_perceptron_tagger_eng')


def pos_tagging(text):
    word_tokens = word_tokenize(text)
    return pos_tag(word_tokens)


input_str = "Data science combines statistics, programming, and machine learning."
print(pos_tagging(input_str))
print("*"*50)