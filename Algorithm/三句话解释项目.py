#三句话解释项目:

#Merchant Fraud prevention model:
#1. Developing classification model in the merchant level to identify 
#whether the merchant is involved in these fraud behaviors in a daily basis.
#2. Guided the expansion of scope of small consumer loan on the online E-commerce platform
#with the assistance of (past period average score/ high score times conut) human review, since the model launched 
#in early 2020, the scope expanded by 450% -> served as the key component of financial risk controlling.
#3. Developed a feature attribution mechanism to enable automatic case study for the fraud sample.
#It efficiently calculate the top contribution features for the prediction of each merchant, it answer a question:
#which feature is most closely related to the fraud behavior, which would be a guidance for the business.

#Anti-Money Laundering project:
#1. Deep dive into multiple data sources across Suning from both transaction level and enterprise level, identified
#multiple risk factors including unreasonable transaction amount, qualification fraud of enterprise and gambling related behavior.
#For example, connect the behavior history with the ip trace information to identify the abnormal patterns
#Connect the unreasonable transaction orders with the different ones
#2. Developed rules actively blocking both of the suspect merchants and transaction.
#3. How can you evaluate your model? 

#Short-term Bcard project:
#1. Developed 400 features closely related to the behavior including purchasing history, 
#app browsing trajectory and ip profile.
#2. Designed a model-stacking procedure where the first level was multiple sub-models and
#then -> the data after rejection inference
#3. Multiple datasets, features -> they will introduce extra selection bias and the 
#missing patterns -> detection -> adjust for the selection bias at the time of the development of each model.

#Model monitoring procedure:
#1. Low-level naive metrics: shift of missing value ratio, feature quality detection, percentage of unit value
#of a features
#2. Higher-level: shap-value, lime -> feature contribution rank correlation with the initial feature importance ranking
#in the training data
#3. Served as a reminder for the data quality issue and user-segment shift(taking merchant model for example)

#Trajectory inference procedure:
#1. recover the stages of the data via ranking the cell clusters along the developmental trajectories through the
#development trajectory.
#2. Starting by dimensionality reduction -> clustering -> ranking each sample in the low dimensional embedding by projection.

#Collaboration Project:
#Detected differential behaviors genes across different subpopulations and performed visualization via ggplot2.

#video-streaming data & event-data

#video-streaming data or the event data here.


#Trajectory Inference procedure:
#1. recover the stages of the data via ranking the cells along the inferred trajectories
#2. 










