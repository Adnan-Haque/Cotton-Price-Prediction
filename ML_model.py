import joblib
import pandas as pd

def telangana(district,variety,year,no):
    dtr = joblib.load('./ml_models/models for Telangana/decision_tree_telangana.pkl')

    le_1 = joblib.load('./ml_models/models for Telangana/le_1.pkl')
    le_2 = joblib.load('./ml_models/models for Telangana/le_2.pkl')

    # y_pred = dtr.predict([[2020,le_1.transform(['Adilabad']) ,le_2.transform(['Cotton (Unginned)']),3]])
    y_pred = dtr.predict([[year,le_1.transform([district]) ,le_2.transform([variety]),no]])
    return(y_pred[0])

def andhrapradesh(district,variety,year,no):
    dtr = joblib.load('./ml_models/models for Andhra Pradesh/decision_tree_andhra_pradesh.pkl')

    le_1 = joblib.load('./ml_models/models for Andhra Pradesh/le_1.pkl')
    le_2 = joblib.load('./ml_models/models for Andhra Pradesh/le_2.pkl')

    # y_pred = dtr.predict([[2020,le_1.transform(['Guntur']) ,le_2.transform(['Other']),3]])
    y_pred = dtr.predict([[year,le_1.transform([district]) ,le_2.transform([variety]),no]])
    return(y_pred[0])

def gujarat(district,variety,year,no):
    dtr = joblib.load('./ml_models/models for gujarat/decision_tree_gujarat.pkl')

    le_1 = joblib.load('./ml_models/models for gujarat/le_1.pkl')
    le_2 = joblib.load('./ml_models/models for gujarat/le_2.pkl')

    # y_pred = dtr.predict([[2020,le_1.transform(['Guntur']) ,le_2.transform(['Other']),3]])
    y_pred = dtr.predict([[year,le_1.transform([district]) ,le_2.transform([variety]),no]])
    return(y_pred[0])    

def maharashtra(district,variety,year,no):
    dtr = joblib.load('./ml_models/models for Maharashtra/decision_tree_maharashtra.pkl')

    le_1 = joblib.load('./ml_models/models for Maharashtra/le_1.pkl')
    le_2 = joblib.load('./ml_models/models for Maharashtra/le_2.pkl')

    # y_pred = dtr.predict([[2020,le_1.transform(['Guntur']) ,le_2.transform(['Other']),3]])
    y_pred = dtr.predict([[year,le_1.transform([district]) ,le_2.transform([variety]),no]])
    return(y_pred[0]) 

def rajasthan(district,variety,year,no):
    dtr = joblib.load('./ml_models/models for Rajasthan/decision_tree_rajasthan.pkl')

    le_1 = joblib.load('./ml_models/models for Rajasthan/le_1.pkl')
    le_2 = joblib.load('./ml_models/models for Rajasthan/le_2.pkl')

    # y_pred = dtr.predict([[2020,le_1.transform(['Guntur']) ,le_2.transform(['Other']),3]])
    y_pred = dtr.predict([[year,le_1.transform([district]) ,le_2.transform([variety]),no]])
    return(y_pred[0])

def tamilnadu(district,variety,year,no):
    dtr = joblib.load('./ml_models/models for Tamil Nadu/decision_tree_tamil_nadu.pkl')

    le_1 = joblib.load('./ml_models/models for Tamil Nadu/le_1.pkl')
    le_2 = joblib.load('./ml_models/models for Tamil Nadu/le_2.pkl')

    # y_pred = dtr.predict([[2020,le_1.transform(['Guntur']) ,le_2.transform(['Other']),3]])
    y_pred = dtr.predict([[year,le_1.transform([district]) ,le_2.transform([variety]),no]])
    return(y_pred[0])    

def returnDistrict(state):
    if state.lower() == 'telangana':
    	record = pd.read_csv('./ml_models/models for Telangana/telangana_final.csv')
    if state.lower() == 'andhra pradesh':
    	record = pd.read_csv('./ml_models/models for Andhra Pradesh/andhra_pradesh_final.csv')
    if state.lower() == 'gujarat':
    	record = pd.read_csv('./ml_models/models for gujarat/reduced_gujarat.csv')
    if state.lower() == 'maharashtra':
    	record = pd.read_csv('./ml_models/models for Maharashtra/maharashtra_final_2.csv')
    if state.lower() == 'rajasthan':
    	record = pd.read_csv('./ml_models/models for Rajasthan/rajasthan_final.csv')
    if state.lower() == 'tamil nadu':
    	record = pd.read_csv('./ml_models/models for models for Tamil Nadu/tamil_nadu_final.csv')
    
    data = []
    district =  record['district'].unique()

    for i in district:
    	data.append(i)
    return data
