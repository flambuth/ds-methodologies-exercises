#Je achete le boeuf!
#plotting imports
%matplotlib inline
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

#pipeline modules
import acquire
import explore
import prepare

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

def do_the_decisionTree():
    clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=123)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_train)
    y_pred_proba = clf.predict_proba(X_train)
    score = clf.score(X_train, y_train)
    return score