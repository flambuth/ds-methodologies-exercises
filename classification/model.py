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
print(f"The true negatives: {blob[0][0]}")
print(f"The true positives: {blob[1][1]}")
print(f"The false negatives: {blob[1][0]}")
print(f"The false positives: {blob[0][1]}")

#All the correct predictions with all entries as the denominator.
accuracy=((true_negative+true_positive)/len(y_train))
#all the correctly predicted positives divided by that AND the ones that were predicted negative but shouldn't have
recall=true_positive/(true_positive+false_negative)
#All the corretly predicted positives, divied by that and the ones that the model was too eager to predict as positive
precision=true_positive/(true_positive+false_positive)



# Look in the scikit-learn documentation to research the solver parameter. What is your best option(s) for the particular problem you are trying to solve and the data to be used?

# Run through steps 2-4 using another solver (from question 5)

# Which performs better on your in-sample data?