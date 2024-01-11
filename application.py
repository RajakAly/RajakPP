from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle as pickle
file=open('power_pipe.pkl','rb')
model=pickle.load(file,encoding='latin1')
file.close()


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        mydict=request.form
        Ambient_Temperature=float(mydict['Ambient_Temperature'])
        Exhaust_Vacuum=float(mydict['Exhaust_Vacuum'])
        Ambient_Pressure=float(mydict['Ambient_Pressure'])
        Relative_Humidity=float(mydict['Relative_Humidity'])
        inputfeatures=[[Ambient_Temperature,Exhaust_Vacuum,Ambient_Pressure,Relative_Humidity]]
        res=np.round(model.predict(inputfeatures),2)
        result=np.array(res).item()
        return render_template('show.html',result=result,placed=True)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)