#standardized modeling pipeline:
import lightgbm as lgbm 
import xgboost as xgb 
from sklearn.model_selection import StratifiedKFold

#Calculate the Gini Index which is equivalent to 2 * AUROC - 1
def eval_giniIndex(y_true, y_pred):
  assert y_true.shape == y_pred.shape
  n_sample = y_true.shape[0]
  L_mid = np.linspace(1/ n_sample, 1, n_sample)
  #####
  pred_order = y_true[y_pred.argsort()]
  L_pred = np.cumsum(pred_order)/ np.sum(pred_order)
  G_pred = np.sum(L_mid - L_pred)
  #####
  true_order = y_true[y_true.argsort()]
  L_true = np.cumsum(true_order)/ np.sum(true_order)
  G_true = np.sum(L_mid - L_true)
  return G_pred/ G_true

def gini_lgb(preds, dtrain):
  labels = dtrain.get_label()
  return 'gini', eval_gini(labels, preds), True

def gini_xgb(preds, dtrain):
  labels = dtrain.get_label()
  return 'gini', eval_gini(labels, preds)

#You need to input the parameter lists:
def ModelingPipeline(X, y, eval_Methodology = "AUC", nfolds = 5, modelUse: "LightGBM", params):
  foldSplit = StratifiedKFold(n_splits = nfolds, shuffle = True, randomstate = 1994)
  oof_valid_pred = np.zeros(X.shape[0])
  for idx, (train_idx, valid_idx) in enumerate(foldSplit.split(X, y)):
    X_train, y_train = X[train_idx], y[train_idx]
    X_valid, y_valid = X[valid_idx], y[valid_idx]
    if modelUse == "LightGBM":
      dtrain = lgbm.Dataset(X_train, y_train)
      dvalid = lgbm.Dataset(X_valid, y_valid)
      lgbmModel = lgbm.train(params = params, train_set = dtrain, valid_sets = dvalid,
      feval = eval_Methodology, verbose_eval = 50)
      bestIter = lgbmModel.best_iteration
      oof_valid_pred[valid_idx] += lgbmModel.predict(X_valid, num_iteration = bestIter)
      score = eval_Methodology(y_valid, oof_valid_pred[valid_idx])
      print(f'LightGBM Model Fold {idx + 1} ' + eval_Methodology + f': {score}\n')
      return lgbmModel
    elif modelUse == "XGBoost":
      dtrain = xgb.DMatrix(X_train, y_train)
      dvalid = xgb.DMatrix(X_valid, y_valid)
      watchlist = [(dtrain, 'train'), (dvalid, 'valid')]
      xgbModel = xgb.train(params = params, train_set = dtrain, valid_sets = dvalid,
      evals = watchlist, maximize = True, feval = eval_Methodology, 
      early_stopping_rounds = 50, verbose_eval = 50)
      bestIter = xgbModel.best_iteration
      oof_valid_pred[valid_idx] += xgbModel.predict(dvalid, n_tree_limit = bestIter)
      score = eval_Methodology(y_valid, oof_valid_pred[valid_idx])
      print(f'XGBoost Model Fold {idx + 1} ' + eval_Methodology + f': {score}\n')
      return xgbModel
    else:
      return -1

#Combining logistic regression, Naive_Bayes, SVM Classifier 
#together:

#Get the counters:
spam_words = Counter()
for msg in words:
  spam_words.update(msg)






