from sklearn.feature_extraction import DictVectorizer
onehot_encoder = DictVectorizer()
instances = [{'city': 'New York'},{'city': 'San Francisco'}, {'city': 'Chapel Hill'}, {'city': 'sss'}]
print (onehot_encoder.fit_transform(instances).toarray())