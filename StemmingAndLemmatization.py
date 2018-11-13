#nltk.download('wordnet')
#nltk.download('punkt')



# nltk basic usage
# from nltk.stem.wordnet import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('gathering', 'v'))
# print(lemmatizer.lemmatize('gathering', 'n'))


from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
wordnet_tags = ['n', 'v']
corpus = [
'He ate the sandwiches',
'Every sandwich was eaten by him'
]
#https://blog.csdn.net/whuslei/article/details/7398443
stemmer = PorterStemmer()
#https://blog.csdn.net/baishuiniyaonulia/article/details/79301092
print('Stemmed:', [[stemmer.stem(token) for token in word_tokenize(document)] for document in corpus])

def lemmatize(token, tag):
    if tag[0].lower() in ['n', 'v']:
        return lemmatizer.lemmatize(token, tag[0].lower())
    return token
lemmatizer = WordNetLemmatizer()
tagged_corpus = [pos_tag(word_tokenize(document)) for document in corpus]
print ('Lemmatized:', [[lemmatize(token, tag) for token, tag in document] for document in tagged_corpus])