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





