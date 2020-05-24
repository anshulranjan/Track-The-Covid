# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:08:20 2020

@author: anshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:30:51 2020

@author: anshu
"""

from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.models import load_model

c1i1 = pd.read_csv("dataset//c1i1.csv")
c1i2 = pd.read_csv("dataset//c1i2.csv")
c1i3 = pd.read_csv("dataset//c1i3.csv")
c2i1 = pd.read_csv("dataset//c2i1.csv")
c2i2 = pd.read_csv("dataset//c2i2.csv")
c2i3 = pd.read_csv("dataset//c2i3.csv")
c3i1 = pd.read_csv("dataset//c3i1.csv")
c3i2 = pd.read_csv("dataset//c3i2.csv")
c3i3 = pd.read_csv("dataset//c3i3.csv")
l1 = ["Mumbai","Pune","Nagpur"]
dataset = pd.read_csv("dataset//dataset_train.csv")
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
scaled_training = sc.fit_transform(dataset)
model = load_model('predict.h5')
graph = tf.get_default_graph()


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/check', methods = ['POST'])
def check():
    a = request.form['log']
    b = request.form['pass']
    if a=="admin" and b == "admin1234":
        return render_template('dashboard.html')
    else:
        return render_template('login.html', message = "Wrong Credentials")

@app.route('/calorie')
def calorie():
    return render_template('calorie.html')

@app.route('/zones')
def zones():
    return render_template('zonesvariation.html')

@app.route('/dates')
def dates():
    return render_template('dates.html')

@app.route('/ration')
def ration():
    return render_template('ration.html')


@app.route('/sales')
def sales():
    return render_template('dashboard.html')

@app.route('/predict' , methods = ['POST'])
def predict():
    global graph
    with graph.as_default():
        m = request.form['city']
        n = request.form['items']
        a = int(m)
        b = int(n)
        if(a==1):
            if(b==1):
                df = c1i1
            elif(b==2):
                df = c1i2
            elif(b==3):
                df = c1i3
        if(a==2):
            if(b==1):
                df = c2i1
            elif(b==2):
                df = c2i2
            elif(b==3):
                df = c2i3
        if(a==3):
            if(b==1):
                df = c3i1
            elif(b==2):
                df = c3i2
            elif(b==3):
                df = c3i3
        dataset_total = pd.concat((dataset,df),axis =0)
        inputs = dataset_total[len(dataset_total)-len(df)- 4 :]
        inputs = np.array(inputs)
        inputs = inputs.reshape(-1,1)
        x_test = []
        for i in range(4,11):
            x_test.append(inputs[i-4:i,0])
        x_test = np.reshape(x_test ,(7,4,1))
        y_test = model.predict(x_test)
        y_test = sc.inverse_transform(y_test)
        ab = 0
        for i in range(0,7):
            ab = ab + y_test[i]
        ab = ab/7
            
        return render_template('dashboard.html', c1 = l1[a-1], a1= int(y_test[0]),a2= int(y_test[1]),a3= int(y_test[2]),a4= int(y_test[3]),a5= int(y_test[4]),a6= int(y_test[5]),a7= int(y_test[6]),a8= int(ab))
    
    
if __name__ =='__main__':  
        app.run(debug = False)  
    
