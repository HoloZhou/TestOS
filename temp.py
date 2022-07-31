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
age=st.number_input('年龄')
se=st.selectbox('性别',options=('男','女'))
if se=='男':
    sex=1
else:
    sex=0
cp=st.selectbox('心律',options=(0,1,2,3))
trestbps=st.number_input('血压')
chol=st.number_input('晨起血糖')
fbs=st.selectbox('餐后2小时血糖',options=(0,1))
restecg=st.selectbox('手术史',options=(0,1))
thalach=st.number_input('Insert thalach')
exang=st.selectbox('exang',options=(0,1))
oldpeak=st.number_input('Insert oldpeak')
slope=st.selectbox('slope',options=(0,1,2))
ca=st.selectbox('ca',options=(0,1))
thal=st.selectbox('thal',options=(1,2,3))
allfactor=[[age,sex, cp,trestbps,chol,fbs,restecg,thalach,
       exang,oldpeak,slope,ca,thal]]
allfactor=pd.DataFrame(allfactor,columns=['age','sex', 'cp','trestbps','chol','fbs','restecg','thalach',
       'exang','oldpeak','slope','ca','thal'])
#%%
submit=st.button('提交')
if submit:
    wb = openpyxl.load_workbook('工作簿1.xlsx')
    ws = wb.active
    ws_current_row=ws.max_row
    ws.append(allfactor)
    
    wb.save('工作簿1.xlsx')
