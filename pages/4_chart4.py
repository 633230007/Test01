import pandas as pd
import streamlit as st

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier         
from sklearn.naive_bayes import GaussianNB              
from sklearn.neighbors import KNeighborsClassifier       

from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score    # Import measure performance function
from sklearn.metrics import classification_report, confusion_matrix


st.title("Student Stress Factors")
st.header("Student Stress Factors")

df=pd.read_csv('./data/Factors1.csv')
st.write(df.head(10))

x = df.iloc[:, :-1]  # ยกเว้นคอลัมน์สุดท้าย
y = df.iloc[:, -1]   # คอลัมน์สุดท้ายเป็น target

st.line_chart(df)
#st.line_chart(df, x="Kindly Rate your Sleep Quality", y=["How would you rate your stress levels"], color=["Student Stress Factors"])

#st.line_chart(df, x="Kindly Rate your Sleep Quality", "How many times a week do you suffer headaches", "How would you rate you academic performance", "how would you rate your study load", "How many times a week you practice extracurricular activities"  y=["How would you rate your stress levels", "Student Stress Factors"], color=["#FF0000", "#0000FF"])


#x = df[["Sleep Quality", "headaches", "academic performance", "study load", "extracurricular activities"]]
#y = df["stress levels"]


#pf = PolynomialFeatures(degree=3)
#x_poly = pf.fit_transform(x)

#x=df.iloc[:, 0:8]
#y=y = df['class']

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3,random_state=1)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

DTmodel = DecisionTreeClassifier(criterion='gini')
DTmodel.fit(x_train, y_train)

x1 = st.number_input("กรุณาป้อนข้อมูล Sleep Quality:")
x2 = st.number_input("กรุณาป้อนข้อมูล headaches:")
x3 = st.number_input("กรุณาป้อนข้อมูล academic performance:")
x4 = st.number_input("กรุณาป้อนข้อมูล study load:")
x5 = st.number_input("กรุณาป้อนข้อมูล extracurricular activities:")
x6 = st.number_input("กรุณาป้อนข้อมูล stress levels:")

if st.button("พยากรณ์ข้อมูล"):
    x_input = [[x1, x2, x3, x4, x5, x6]]
    y_predict = DTmodel.predict(x_input)
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")
