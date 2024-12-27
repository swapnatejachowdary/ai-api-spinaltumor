import pickle
from flask import Flask,request 
api=Flask(_name_)
with open('ai.pkl','rb') as f:
    ai=pickle.load(f)
@api.route('/')
def home():
    return "API Server Running"
@api.route('/predict',methods=['GET'])
def predict():
    moisture=request.args.get('moisture')
    moisture=float(moisture)
    
    data=[[moisture]]
    response=ai.predict(data)[0]
    return response
if _name=="main_":
    api.run(
        host='0.0.0.0',
        port=2000
    )