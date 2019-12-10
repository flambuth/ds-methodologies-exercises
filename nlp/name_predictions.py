import random
import pandas as pd 
import nltk 
from nltk.corpus import names

from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing 
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

#I'm sure theres a DF.str method that could do this, but I'm not bright enough to find it right now.
def gender_features(word):
    return word[-1]

#Download this before doing anything
#nltk.download('names')

#Make a list of named tuples with the male/female tagged to each name
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
#Mix up the order
random.shuffle(labeled_names)

#Put those into a dataframe
df_names = pd.DataFrame(labeled_names, columns=['Name','Sex'])

#Get the last letter of each name and make it a column
df_names['Last_letter'] = df_names['Name'].apply(gender_features)

#If you wanto to save it for later
#df_names.to_csv('first_names.csv')

#Make each last letter a numerical value. I think maybe one-hot-encoding would work better. I forgot a lot.
le = preprocessing.LabelEncoder()
last_letter_encoded = le.fit_transform(df_names.Last_letter)
df_names["Encoded_Last_Letter"] = last_letter_encoded

X = df_names.Encoded_Last_Letter
y = df_names.Sex

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2)


model = GaussianNB()
model.fit(pd.DataFrame(X_train),y_train)

predicted = model.predict(pd.DataFrame(X_train))
print('Accuracy: {:.2%}'.format(accuracy_score(y_train, predicted)))

test_predictions = model.predict(pd.DataFrame(X_test))
print('Accuracy: {:.2%}'.format(accuracy_score(y_test, test_predictions)))


#####
# With One-Hot Encoding!
x = pd.get_dummies(df_names.Encoded_Last_Letter,prefix=['Letter'])
X = x
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2)
model2 = GaussianNB()
model2.fit(X_train,y_train)
new_predictions = model2.predict(pd.DataFrame(X_train))
print('Accuracy: {:.2%}'.format(accuracy_score(y_train, new_predictions)))

new_test_predictions = model.predict(pd.DataFrame(X_test)) 
print('Accuracy: {:.2%}'.format(accuracy_score(y_test, new_test_predictions)))                                                    

#Test results somehow got worse. I dunno. Whatever.