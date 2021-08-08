#587. Erect the fence:


def calModelPSI(df_score, df_bin, label = 'is_overdue_m2'):
    colList = ['x_range', 'base_rate', 'count', 'rate',
    'rate-diff', 'log', 'psi']
    df_bin_res = pd.DataFrame(columns = colList)
    df_score_m = df_score[(df_score[label].isin([0, 1]))].reset_index()
    df_bin_res['count'] = utils.count_in_bin(df_score_m['score'], df_bin['score'])
    df_bin_res['x_range'] = df_bin['score']
    df_bin_res['rate'] = df_bin_res['count']/ df_bin_res['count'].sum()
    df_bin_res['base-rate'] = df_bin['total']
    df_bin_res['rate-diff'] = round(df_bin_res['rate'] - df_bin_res['base-rate'], 4)
    df_bin_res['log'] = round((df_bin_res['rate']/ df_bin_res['base-rate']).apply(np.log), 4)
    df_bin_res.loc[(df_bin_res['rate'] == 0) | (df_bin_res['base-rate'] == 0), 'log'] = 0
    df_bin_res['psi'] = round(df_bin_res['log'] * df_bin_res['rate-diff'], 4)
    index_new = len(df_bin.index)
    #change to %:
    df_bin_res['base-rate'] = round(df_bin_res['base-rate'] * 100, 2)
    df_bin_res['rate'] = round(df_bin_res['rate'] * 100, 2)
    df_bin_res['rate-diff'] = df_bin_res['rate-diff'] * 100
    #add a sum into line:

#machine translation, question answering, sentiment analysis,
#text summarization etc....

#fine tuning the bert to learn specific task
#machine translation, multi-head attention + add/norm

#design, develop and implement advanced predictive models using 
#advanced machine learning techniques including neural networks
#and tree-based models

#collaborate with other data scientists and engineers to formulate innovative solutions to 
#experiment and implement advanced data mining techniques.

#being able to work with large volumes of data, extracting and analyzing big data using
#high-level 

#Graham Scan to find the convex hull of a series of points here:


#Construct a convex hull here:
class Solution:
    def outerTrees(self, trees: List[List[int]]):



#append the list onto the current dictionary here.
hashMap.get(key, []) + [s]
#the length of the shortest path between different users here.
#
while deque:
    

#standardized pipeline:
def thresholdEvaluation(model, Y_test, binsCount):
    rowList = []
    for i in np.linspace(0, 1, binsCount + 1):
        dicts = {}
        g = np.vectorize(lambda x: 0 if x < i else 1)
        test_y_pred = g(Y_test)
        #calculate the confusion matrix at threshold k here:
        conf = confusion_matrix(Y_test, test_y_pred, labels = [0, 1])
        TN = conf[0][0]
        FP = conf[0][1]
        FN = conf[1][0]
        TP = conf[1][1]
        dicts.update({'threshold': i, 'recall': TP/(TP + FN), 'fpr': TP/(TP + FP), 'tpr': TP/(TP + FN)})
        rowList.append(dicts)
    dfMetric = pd.DataFrame(rowList)
    dfMetric["diff"] = dfMetric["recall"] - dfMetric["fpr"]
    dfMetric["threshold"] = dfMetric["threshold"] * 100
    return dfMetric
        

def thresholdEvaluation(model, Y_test, binsCount):
    rowList = []
    for i in np.linspace(0, 1, binsCount + 1):
        dicts = {}
        g = np.vectorize(lambda X: 0 if X < i else 1)
        test_y_pred = g(Y_test)
        conf = confusion_matrix(Y_test, test_y_pred)
        TN = conf[0][0]
        FP = conf[0][1]
        FN = conf[1][0]
        TP = conf[1][1]
        dicts.update({'threshold': i, 'recall': TP/(TP + FN), 'fpr': TP/(TP + FP), 'tpr': TP/(TP + FN)})
        rowList.append(dicts)
    dfMetric = pd.DataFrame(rowList)
    dfMetric['diff'] = dfMetric["recall"] - dfMetric['fpr']
    dfMetric["threshold"] = dfMetric['threshold'] * 100
    return dfMetric

#To calculate the recall at threshold 0.95:
dfMetric.iloc[(dfMetric["recall"] < 0.96) & (dfMetric["recall"] > 0.94), :]

dfMetric.iloc[(dfMetric["recall"] < 0.96) & (dfMetric["recall"] > 0.94), :]




def process_data(data_path):
    df = pd.read_csv(data_path, encoding = 'latin-1')
    df.loc[:, "Sentence #"] = df["Sentence #"].fillna(method = "fill")
    encPos = preprocessing.LabelEncoder()
    encTag = preprocessing.LabelEncoder()
    df.loc[:, "POS"] = encPos.fit_transform(df["POS"])
    df.loc[:, "Tag"] = encTag.fit_transform(df["Tag"])
    sentences = df.groupby("Sentence #")["Word"].apply(list).values
    pos = df.groupby("Sentence #")["POS"].apply(list).values
    
























