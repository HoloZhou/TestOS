# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import streamlit as st
import os
import pandas as pd
import numpy as np
import openpyxl
#%%
age=str(st.number_input('年龄'))
se=st.selectbox('性别',options=('男','女'))
if se=='男':
    sex=str(1)
else:
    sex=str(0)
cp=str(st.selectbox('心律',options=(0,1,2,3)))
trestbps=str(st.number_input('血压'))
chol=str(st.number_input('晨起血糖'))
fbs=str(st.selectbox('餐后2小时血糖',options=(0,1)))
restecg=str(st.selectbox('手术史',options=(0,1)))
thalach=str(st.number_input('Insert thalach'))
exang=str(st.selectbox('exang',options=(0,1)))
oldpeak=str(st.number_input('Insert oldpeak'))
slope=str(st.selectbox('slope',options=(0,1,2)))
ca=str(st.selectbox('ca',options=(0,1)))
thal=str(st.selectbox('thal',options=(1,2,3)))
allfactor=[age,sex, cp,trestbps,chol,fbs,restecg,thalach,
        exang,oldpeak,slope,ca,thal]
#allfactor=pd.DataFrame(allfactor,columns=['age','sex', 'cp','trestbps','chol','fbs','restecg','thalach',
       #'exang','oldpeak','slope','ca','thal'])
#%%
submit=st.button('提交')

if submit:
    al=",".join(allfactor)+"\n"
    f = open('新建.csv','a')
    f.add_rows(data=al)
   
    f.close()
