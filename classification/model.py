#Je achete le boeuf!
#plotting imports
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

# ignore warnings
import warnings
warnings.filterwarnings("ignore")


#modeling imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, LogisticRegression, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier



#pipeline modules
import acquire
import explore
import prepare

#Acquire and Prep
df = prepare.prep_titanic()
df.dropna(inplace=True)
df.isnull().sum()
#DATA IS ACQUIRED AND PREPARED.
#LETS DO THE 4 WAY SPLIT OF X-y, and each of those are split into train and test.
X=df[['pclass','age','fare','sibsp','parch']]
y=df[['survived']]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.30,random_state=123)

#1
# Fit the logistic regression classifier to your training sample and transform, 
# i.e. make predictions on the training sample
logit = LogisticRegression(C=1,class_weight={1:2},random_state=123,solver='saga')
logit.fit(X_train, y_train)

y_pred = logit.predict(X_train)
y_pred_proba=logit.predict_proba(X_train)

# Evaluate your in-sample results using the model score, confusion matrix, and classification report.
    #a confusion matrix, made with sklearn.metrics
blob = confusion_matrix(y_train, y_pred)
    #THE BIG REPORT. With all the classification metrics saved. 
cr=(classification_report(y_train,y_pred))
    #using the score method in the LogReg object
score = logit.score(X_test,y_test)

# Print and clearly label the following: Accuracy, true positive rate, false positive rate, true negative rate, false negative rate, precision, recall, f1-score, and support.
true_negative = blob[0][0]
true_positive = blob[1][1]
false_negative = blob[1][0]
false_positive = blob[0][1]

#All the correct predictions with all entries as the denominator.
accuracy=((true_negative+true_positive)/len(y_train))
#all the correctly predicted positives divided by that AND the ones that were predicted negative but shouldn't have
recall=true_positive/(true_positive+false_negative)
#All the corretly predicted positives, divied by that and the ones that the model was too eager to predict as positive
precision=true_positive/(true_positive+false_positive)
#Works horizontally along the actual positive. FP/FP+TN
false_positive_rate=false_positive/(false_positive+true_negative)

print(f"The accuracy is {accuracy}")
print(f"The recall is {recall}")
print(f"The precision is {precision}")


# Look in the scikit-learn documentation to research the solver parameter. What is your best option(s) for the particular problem you are trying to solve and the data to be used?

# Run through steps 2-4 using another solver (from question 5)
def do_the_logRegression(X_train, y_train, my_solver):
    logit = LogisticRegression(C=1,class_weight={1:2},random_state=123,solver=my_solver)
    logit.fit(X_train, y_train)
    y_pred = logit.predict(X_train)
    y_pred_proba=logit.predict_proba(X_train)
    score = logit.score(X_train,y_train)
    return score

solvers = ["lbfgs", "liblinear", "sag", "saga", "newton-cg"]
for i in solvers:
    print(f"The accuracy for {i} as the solver is {do_the_logRegression(X_train, y_train, i)}")


# Which performs better on your in-sample data?
#   All the non-saga solvers got the same score, of around .71



############
#DECISION TREE

# Fit the decision tree classifier to your training sample and transform (i.e. make predictions on the training sample)
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=123)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_train)
y_pred_proba = clf.predict_proba(X_train)

# Evaluate your in-sample results using the model score, confusion matrix, and classification report.
conf_matx = confusion_matrix(y_train, y_pred)
print(classification_report(y_train, y_pred))

# Print and clearly label the following: Accuracy, true positive rate, false positive rate, true negative rate, false negative rate, precision, recall, f1-score, and support.
# Run through steps 2-4 using entropy as your measure of impurity.
# Which performs better on your in-sample data?

def do_the_decisionTree(my_criterion):
    clf = DecisionTreeClassifier(criterion=my_criterion, max_depth=3, random_state=123)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_train)
    y_pred_proba = clf.predict_proba(X_train)
    score = clf.score(X_train, y_train)
    return score

#############
#Random Forest

# Fit the Random Forest classifier to your training sample and transform (i.e. make predictions on the training sample) 
# setting the random_state accordingly and setting min_samples_leaf = 1 and max_depth = 20.
rf = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=1,
                            n_estimators=100,
                            max_depth=20, 
                            random_state=123)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_train)
y_pred_proba = rf.predict_proba(X_train)

# Evaluate your results using the model score, confusion matrix, and classification report.
print('Accuracy of random forest classifier on training set: {:.2f}'
     .format(rf.score(X_train, y_train)))


# Print and clearly label the following: Accuracy, true positive rate, false positive rate, true negative rate, false negative rate, precision, recall, f1-score, and support.
print(classification_report(y_train, y_pred, output_dict=True))
class_report = classification_report(y_train, y_pred, output_dict=True)
class_report['1']
# Run through steps increasing your min_samples_leaf to 5 and decreasing your max_depth to 3.
rf2 = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=5,
                            n_estimators=100,
                            max_depth=3, 
                            random_state=123)
rf2.fit(X_train, y_train)
y_pred2 = rf2.predict(X_train)
y_pred_proba2 = rf2.predict_proba(X_train)

# What are the differences in the evaluation metrics? Which performs better on your in-sample data? Why?
class_report2 = classification_report(y_train, y_pred2, output_dict=True)
class_report2['1']
    #The accuracy went up using these new parameters, but the precisions and recall seemed to get worse. huh?

##############
#K Nearest Neighbor
# Fit a K-Nearest Neighbors classifier to your training sample and transform (i.e. make predictions on the training sample)
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
knn.fit(X_train, y_train)
y_pred = knn.predict(X_train)
y_pred_proba = knn.predict_proba(X_train)



# Evaluate your results using the model score, confusion matrix, and classification report.
# 
# Print and clearly label the following: Accuracy, true positive rate, false positive rate, true negative rate, 
# false negative rate, precision, recall, f1-score, and support.
# 
# Run through steps 2-4 setting k to 10
# 
# Run through setps 2-4 setting k to 20
# 
# What are the differences in the evaluation metrics? Which performs better on your in-sample data? Why?