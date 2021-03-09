#ShapleyCalculation:
import shap
from xgboost.sklearn import XGBClassifier
X_train = dfModeling[listC]
Y_train = dfModeling["label"]
dfToExplain = df4[listC]
xgb = XGBClassifier(**param2)
mymodel = xgb.fit(X_train, Y_train)
param2 = {'objective': 'binary:logistic', 
          'n_estimators': 25, 
          'booster': 'gbtree', 
          'eval_metric': 'auc', 
          'learning_rate': 0.1,
          'max_delta_step': 0, 
          'max_depth': 5, 
          'colsample_bylevel': 0.95 , 
          'subsample': 0.95, 
          #'gamma': 0.0001, 
          'lambda': 50, 
          'alpha': 0.1, 
          'silent':True, 
          'scale_pos_weight': 20}
#Get the tree explainer:
import shap
explainer = shap.TreeExplainer(mymodel)
shap_values = shap.TreeExplainer(mymodel).shap_values(df4[listC])
#For each of the sample, get the most 8 features most attributable to the prediction:
cur_df = pd.DataFrame(columns = ["featureList", "shapValue", "index"])
for i in range(len(shap_values)):
    curDF = pd.DataFrame(shap_values.feature_names, columns = ["featureList"])
    curDF["shapValue"] = abs(shap_values[1].values)
    curDF["index"] = i
    curDF = curDF.sort_values("shapValue", ascending=False).iloc[:8, :]
    cur_df = pd.concat([cur_df, curDF], axis = 0)
dfShapley = cur_df.reset_index(drop = True)
dfOrg = df4[["b2c_order_id", "result", "date"]].reset_index(drop = False)
resultDF = pd.merge(dfShapley, dfOrg, on = ["index"])
resultDF.to_csv("ShapleyValuePrediction.csv")





