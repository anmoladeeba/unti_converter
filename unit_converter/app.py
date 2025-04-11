import streamlit as st

def distance_convertor(from_unit,to_unit,value):
     units = {
        "Meters": 1,
        "Kilometers":1000,
        "foot":0.3048,
        "Miles":1609.34,
    }
     result = value * units[from_unit] / units[to_unit]
     return result


def Temperature_convertor(from_unit,to_unit,value):
 if from_unit == "Celsius" and to_unit == "Fahrenheit":
    result = (value * 9/5) + 32

 elif from_unit == "Fahrenheit" and to_unit == "Celsius":
    result = (value - 32) * 5/0
 else :
    result = value
    return result
 
 
 
def weight_convertor(from_unit,to_unit,value):
     units = {
        "Kilograms": 1,
        "Grams":0.001,
        "Pounds":0.453592,
        "Ounces":0.0283495,
    }
     result = value * units[from_unit] / units[to_unit]
     return result


def pressure_convertor(from_unit,to_unit,value):
     units = {
        "Pascals": 1,
        "Hactopascalsa":100,
        "Kilopascals":1000,
        "Bar":100000,
    }
     result = value * units[from_unit] / units[to_unit]
     return result


   

st.title("Unit Converter App")

category = st.selectbox("Select Category",["Distance","Temperature","Weight","Pressure"])

if category == "Distance":
   from_unit = st.selectbox("From",["Meters","Kilometers","foot","Miles"])
   to_unit = st.selectbox("To",["Meters","Kilometers","foot","Miles"])
   value = st.number_input("Enter value")

   if st.button("Convert"):
       result = distance_convertor( from_unit, to_unit, value)
   st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":

   from_unit = st.selectbox("From",["celsius","fahrenheit"])
   to_unit = st.selectbox("To",["celsius","fahrenheit"])
   value = st.number_input("Enter value")

   if st.button("Convert"):
       result = Temperature_convertor( from_unit, to_unit, value)
   st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


elif category == "Weight":

   from_unit = st.selectbox("From",["Kilograms","Grams","Pounds","Ounces"])
   to_unit = st.selectbox("To",["Kilograms","Grams","Pounds","Ounces"])
   value = st.number_input("Enter value")

   if st.button("Convert"):
       result = weight_convertor( from_unit, to_unit, value)
   st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


elif category == "Pressure":

   from_unit = st.selectbox("From",["Pascals","Hactopascalsa","Kilopascals","Bar"])
   to_unit = st.selectbox("To",["Pascals","Hactopascalsa","Kilopascals","Bar"])
   value = st.number_input("Enter value")

   if st.button("Convert"):
       result = pressure_convertor( from_unit, to_unit, value)
   st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

    

    