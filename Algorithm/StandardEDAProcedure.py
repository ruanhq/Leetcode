#Standardized EDA Procedure

#Calculate the correlation between features and the label:
def calNumericalFeatureLabelCorrelation(df, responseVariable = "label", goldenFeatureCorrelationThreshold = 0.4):
  dfNumericalFeatures = df.select_dtypes(include = ["float64",
  "float32", "float16", "int8", "int16", "int32", "int64"])
  dfNumCorr = dfNumericalFeatures()[responseVariable][:-1]
  goldenFeatureList = dfNumCorr[abs(dfNumCorr) > goldenFeatureCorrelationThreshold].sort_values(ascending = False)
  dfFeatureInfo = pd.DataFrame(goldenFeatureList).reset_index().rename(columns = {'index': 'Feature'})
  return dfFeatureInfo

#Draw the boxplot for the predictor variable VS the response variable:
def drawingQuantitativeResponseVersusCategoricalFeature(df, responseVariable = "label", cateFeature):
  f, ax = plt.subplots(figsize = (12, 6))
  dataToPlot = pd.concat([df[responseVariable], df[cateFeature]], axis = 1)
  fig = sns.boxplot(x = cateFeature, y = responseVariable, data = dataToPlot)
  fig.axis(ymin = 0, ymax = max(df[responseVariable] * 1.05))
  plt.xticks(rotation = 60)

#HeatmapStyleDrawing For highly correlated features:
def drawingCorrelationHeatmap(df, responseVariable = "label", numberOfFeaturesPlot = 10):
  corrMat = df.corr()
  colsToDraw = corrMat.nlargest(numberOfFeaturesPlot, responseVariable)[responseVariable].index
  cm = np.corrcoef(df[colsToDraw].values.T)
  plt.figure(figsize = (12, 12))
  sns.set(font_scale = 1.25)
  hm = sns.heatmap(cm, cbar = True, annot = True, square = True, fmt = '.3f',
  annot_kws = {'size': 14}, yticklabels = colsToDraw.values, xticklabels = colsToDraw.values)
  plt.show()

#Plot the relationship Between Quantitative Variable vs Quantitative Variable, three plots each line:
def drawingCorrelationQuantitative(df, responseVariable = "label", featureToAnalysis):
  fig, ax = subplots(round(len(featureToAnalysis) / 3), 3, figsize = (21, 14))
  for i, ax in enumerate(fig.axes):
  	if i < len(featureToAnalysis) - 1:
  		sns.regplot(x = featureToAnalysis[i], y = responseVariable, data = df[featureToAnalysis], ax = ax)
  plt.show()

#Calculate the gini-index from scratch:
def giniIndexEvaluation(y_true, y_pred):
  assert y_true.shape == y_pred.shape
  n_sample = y_true.shape[0]
  L_mid = np.linspace(1/ n_sample, 1, n_sample)
  pred_order = y_true[y_pred.argsort()]
  L_pred = np.cumsum(pred_order)/ np.sum(pred_order) #Lorentz curve.
  G_pred = np.sum(L_mid - L_pred)
  true_order = y_true[y_true.argsort()]
  L_true = np.cumsum(true_order)/ np.cumsum(true_order)
  G_true = np.sum(L_mid - L_true)
  return G_pred/ G_true

#Calculate the missing statistics from the dataframe:
def missingValueTable(df):
  missStats = df.isnull().sum()
  missPercent = 100 * df.isnull().sum()/ len(df)
  missValTable = pd.DataFrame(zip(missStats, missPercent), columns = ["missingValues", "missingPercentage"]).sort_values("missingValues", ascending = False)
  missValTableMissingOnly = missValTable[missValTable.iloc[:, 1] != 0]
  print("The select dataframes has {0} features with missing values".format(len(missValTableMissingOnly)))
  return missValTableMissingOnly

def dropConstantCols(df):
  distinctValues = df.apply(lambda X: len(X.unique()))
  for i in distinctValues.keys()[np.where(distinctValues == 1)]:
    df = df.drop(i, axis = 1)
  return df

#label encoding of the key value pairs, for continuous response
def label_encoding(df, list_of_categories, limitMaxValue = True, responseCol):
  for i in list_of_categories:
    col = i
    colDistribution = df.groupby([col])[responseCol].sum().reset_index().sort_values([responseCol], ascending = False)
    mapping_col_name = colDistribution[col]
    if(limitMaxValue == True):
      mapping_col_value = list(range(list_of_categories[i], 0, -1))
      mapping_col_value.extend([1 for val in range(df[col].nunique() - list_of_categories[col], 0, -1)])
    else:
      mapping_col_value = list(range(df[col].nunique(), 0, -1))
    mappingDict = dict(zip(mapping_col_name, mapping_col_value))
    mappingDict['Other'] = 1
    df[col] = [mappingDict[v] for v in df[col] if v in mappingDict]
  return df

#label-encoder, 
X_cat = X.select_dtypes(include = ['object'])
#Perform simulation for the specific dataset:

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from math import sqrt














