#Automated EDA Pipeline for Structured Data:
colors = ["#0101DF", "#DF0101"]
sns.countplot("Class", data = df, palette = colors)
plt.title("Class Distribution \n (0: No Fraud || 1: Fraud)", fontsize = 1r)
fig, ax = plt.subplots(1, 2, figsize = (18, 4))
amount_val = df["Amount"].values
time_val = df["Time"].values
sns.distplot(amount_val, ax = ax[0], color = 'r')
ax[0].set_title("Distribution of Transaction Amount", fontsize = 14)
ax[0].set_xlim([min(amount_val), max(amount_val)])
sns.distplot(time_val, ax = ax[1], color = 'b')
ax[1].set_title("Distribution of Transaction Time", fontsize = 14)
ax[1].set_xlim([min(amount_val), max(time_val)])
plt.show()

std_scaler = StandardScaler()
rob_scaler = RobustScaler()
df["scaled_amount"] = rob_scaler.fit_transform(df["Amount"].values.reshape(-1, 1))
df["scaled_time"] = rob_scaler.fit_transform(df["Time"].values.reshape(-1, 1))a
df.drop(["Time", "Amount"], axis = 1, inplace = True)
scaled_amount = df["scaled_amount"]
scaled_time = df["scaled_time"]
df.drop(["scaled_amount", "scaled_time"], axis = 1, inplace = True)
df.insert(0, "scaled_amount", scaled_amount)
df.insert(1, "scaled_time", scaled_time)
df.head()

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report
from collections import Counter
from sklearn.model_selection import KFold, StratifiedKFold

fig, ax = plt.subplots(1, 2, figsize = (18, 4))
amount_val = df["Amount"].values
time_val = df["Time"].values
sns.distplot(amount_val, ax = ax[0], color = 'r')
ax[0].set_title("Distribution of Transaction Amount", fontsize = 14)
ax[0].set_xlim([min(amount_val), max(amount_val)])

f, axes = plt.subplots(ncols = 4, figsize = (20, 4))
sns.boxplot(x = "Class", y = "V19", data = new_df, palette = colors,
ax = axes[3])
axes[3].set_title("V19 vs Class Positive Correlation")



f, axes = plt.subplots(ncols = 4, figsize = (20, 4))


sns.distplot(v12_fraud_dist, ax = ax2, fit = norm, color = "#56F9BB")
ax2.set_title("V12 Distribution \n (Fraud Transaction)", fontsize = 14)





X = new_df.drop("Class", axis = 1)
y = new_df["Class"]
t0 = time.time()
X_reduced_tsne = TSNE(n_components = 2, random_state = 42).
fit_transform(X.values)
t1 = time.time()
print("T-SNE took {:.2} s".format(t1 - t0))

t0 = time.time()
X_reduced_pca = PCA(n_components = 2, random_state = 42).
fit_transform(X.values)
t1 = time.time()
print("T-SNE took {:.2} s".format(t1 - t0))

t0 = time.time()
X_reduced_Tsvd = TruncatedSVD(n_components = 2,
algorithm = "randomized", random_state = 42).
fit_transform(X.values)
t1 = time.time()
print("Truncated SVD took {:.2} s".format(t1 - t0))


f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (24, 6))
f.suptitle("Clusters using Dimensionality Reduction",
fontsize = 14)
blue_patch = mpatches.Patch(color = "#0A0AFF", label = "No Fraud")
red_patch = mpatches.Patch(color = "#AF0000", label = "Fraud")
ax1.scatter(X_reduced_tsne[:, 0], X_reduced_tsne[:, 1], c = (y == 0),
cmap = 'coolwarm', label = "No Fraud", linewidths = 2)
ax1.scatter(X_reduced_tsne[:, 0], X_reduced_tsne[:, 1], c = (y == 1),
cmap = 'coolwarm', label = 'Fraud', linewidths = 2)
ax1.set_title("t-SNE", fontsize = 14)


##########
X = new_df.drop("Class", axis = 1)
y = new_df["Class"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size = 0.25, random_state = 42)
X_train = X_train.values
X_test = X_test.values
y_train = y_train.values
y_test = y_test.values
classifiers = {
"LogisticRegression": LogisticRegression(),
"KNearest": KNeighborsClassifier(),
"SVC": SVC(),
"DecisionTreeClassifier": DecisionTreeClassifier()
}
from sklearn.model_selection import cross_val_score
for key, classifier in classifier.items():
    classifier.fit(X_train, y_train)
    training_score = cross_val_score(classifier, X_train, y_train, cv = 5)
    print("Classifiers: ", classifier.__class__.__name__,
    "Has a training score of", round(training_score.mean(), 2) * 100,
    "% accuracy score")

#
from scipy.stats import norm
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (20, 6))
v14_fraud_dist = new_df['V14'].loc[new_df['Class'] == 1].values
sns.distplot(v14_fraud_dist,ax=ax1, fit=norm, color='#FB8861')
ax1.set_title('V14 Distribution \n (Fraud Transactions)', fontsize=14)

v12_fraud_dist = new_df['V12'].loc[new_df['Class'] == 1].values
sns.distplot(v12_fraud_dist,ax=ax2, fit=norm, color='#56F9BB')
ax2.set_title('V12 Distribution \n (Fraud Transactions)', fontsize=14)


v10_fraud_dist = new_df['V10'].loc[new_df['Class'] == 1].values
sns.distplot(v10_fraud_dist,ax=ax3, fit=norm, color='#C5B3F9')
ax3.set_title('V10 Distribution \n (Fraud Transactions)', fontsize=14)

plt.show()



from scipy.stats import norm
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (20, 6))
v14_fraud_dist = new_df["V14"].loc[new_df["Class"] == 1].values



from sklearn.model_selection import GridSearchCV
log_reg_params = {"penalty": ["l1", "l2"],
"C": [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
grid_log_reg = GridSearchCV(LogisticRegression(), log_reg_params)
grid_log_reg.fit(X_train, y_train)
log_reg = grid_log_reg.best_estimator_
svc_params = {"C": [0.5, 0.7, 0.9, 1],
"kernel": ["rbf", "poly", "sigmoid", "linear"]}
grid_svc = GridSearchCV(SVC(), svc_params)
grid_svc.fit(X_train, y_train)

#smote undersampling:
from sklearn.metrics import average_precision_score
undersample_average_precision = average_precision_score(original_ytest, undersample_y_score)
print("Average precision-recall score: {0:0.2f}".format(undersample_average_precision))

from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split, RandomizedSearchCV

original_Xtrain = original_Xtrain.values
original_Xtest = original_Xtest.values
original_ytrain = original_ytrain.values
originalYtest = original_ytest.values
accuracyLst = []
precisionLst = []
recallLst = []
f1Lst = []
aucLst = []
log_reg_sm = LogisticRegression()
log_reg_params = {"penalty": ["l1", "l2"], "C": [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
rand_log_reg = RandomizedSearchCV(LogisticRegression(), log_reg_params, n_iter = 10)
for train, test in sss.split(originalXtrain, originalYtrain):
    pipeline = imblanced_make_pipeline(SMOTE(sampling_strategy = "minority"),
    rand_log_reg)
    model = pipeline.fit(originalXtrain[train], originalYtrain[train])
    best_est = ran_log_reg.best_estimator_
    prediction = best_est.predict(originalXtrain[test])
    accuracyLst.append(pipeline.score(originalXtrain[test], prediction))
    precision_lst.append(precision_score(originalYtrain[test], prediction))
    recall_lst.append(recall_score(originalYtrain[test], prediction))
    f1_lst.append(f1_score(originalYtrain[test], prediction))
    auc_lst.append(roc_auc_score(originalYtrain[test], prediction))
y_score = best_est.decision_function(originalXtest)
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(originalYtest, y_score)
print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))


#Try undersampling:
from imblearn.under_sampling import NearMiss
undersample_X = df.drop('Class', axis=1)
undersample_y = df['Class']

for train_index, test_index in sss.split(undersample_X, undersample_y):
    print("Train:", train_index, "Test:", test_index)
    undersample_Xtrain, undersample_Xtest = undersample_X.iloc[train_index], undersample_X.iloc[test_index]
    undersample_ytrain, undersample_ytest = undersample_y.iloc[train_index], undersample_y.iloc[test_index]
    
undersample_Xtrain = undersample_Xtrain.values
undersample_Xtest = undersample_Xtest.values
undersample_ytrain = undersample_ytrain.values
undersample_ytest = undersample_ytest.values 

undersample_accuracy = []
undersample_precision = []
undersample_recall = []
undersample_f1 = []
undersample_auc = []

for train, test in sss.split(undersample_Xtrain, undersample_ytrain):
    undersample_pipeline = imbalanced_make_pipeline(NearMiss(sampling_strategy='majority'), log_reg) # SMOTE happens during Cross Validation not before..
    undersample_model = undersample_pipeline.fit(undersample_Xtrain[train], undersample_ytrain[train])
    undersample_prediction = undersample_model.predict(undersample_Xtrain[test])
    
    undersample_accuracy.append(undersample_pipeline.score(original_Xtrain[test], original_ytrain[test]))
    undersample_precision.append(precision_score(original_ytrain[test], undersample_prediction))
    undersample_recall.append(recall_score(original_ytrain[test], undersample_prediction))
    undersample_f1.append(f1_score(original_ytrain[test], undersample_prediction))
    undersample_auc.append(roc_auc_score(original_ytrain[test], undersample_prediction))



accuracy_lst = []
precision_lst = []
recall_lst = []
f1_lst = []
auc_lst = []
# Classifier with optimal parameters
# log_reg_sm = grid_log_reg.best_estimator_
log_reg_sm = LogisticRegression()
log_reg_params = {"penalty": ['l1', 'l2'], 'C': [0.001, 0.01, 0.1, 1, 5, 10, 100, 1000]}
rand_log_reg = RandomizedSearchCV(LogisticRegression(), log_reg_params, n_iter = 5)
for train, test in sss.split(originalXtrain, originalYtrain):
    pipeline = imbalanced_make_pipeline(SMOTE(sampling_strategy = "minority"), rand_log_reg)
    model = pipeline.fit(originalXtrain[train], originalYtrain[train])
    best_est = rand_log_reg.best_estimator_
    prediction = best_est.predict(originalXtrain[test])
    accuracy_lst.append(pipeline.score(originalXtrain[test], originalYtrain[test]))
    precision_lst.append(precision_score(originalYtrain[test], prediction))
    recall_lst.append(recall_score(originalYtrain[test], prediction))
    f1_lst.append(f1_score(originalYtrain[test], prediction))
    auc_lst.append(roc_auc_score(originalYtrain[test], prediction))
    

for train, test in sss.split(originalXtrain, originalYtrain):
    
print('---' * 45)
print('')
print("accuracy: {}".format(np.mean(accuracy_lst)))
print("precision: {}".format(np.mean(precision_lst)))
print("recall: {}".format(np.mean(recall_lst)))
print("f1: {}".format(np.mean(f1_lst)))
print('---' * 45)


# Create a confusion matrix, standardized plotting here.
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(cm)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=14)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

#using deep learning to tune the model:
for train, test in sss.split(originalXtrain, originalYtrain):
    

































