import streamlit as st
import requests
from requests.exceptions import ConnectionError

ip_api = "127.0.0.1"
port_api = "5000"

st.title("Car Price Prediction")

st.write("Enter the car details:")

symboling = st.selectbox("Symboling", [-3, -2, -1, 0, 1, 2, 3], index=3)
wheelbase = st.number_input("Wheelbase", value=104.3, step=0.1)
carlength = st.number_input("Car Length", value=178.5, step=0.1)
carwidth = st.number_input("Car Width", value=69.5, step=0.1)
carheight = st.number_input("Car Height", value=57.9, step=0.1)
curbweight = st.number_input("Curb Weight", value=2850, step=10)
enginesize = st.number_input("Engine Size", value=122, step=1)
boreratio = st.number_input("Bore Ratio", value=3.31, step=0.01)
stroke = st.number_input("Stroke", value=3.54, step=0.01)
compressionratio = st.number_input("Compression Ratio", value=10.0, step=0.1)
horsepower = st.number_input("Horsepower", value=120, step=1)
peakrpm = st.number_input("Peak RPM", value=6000, step=100)
citympg = st.number_input("City MPG", value=26, step=1)
highwaympg = st.number_input("Highway MPG", value=36, step=1)

CarName = st.text_input("Car Name", value="ford focus")
fueltype = st.selectbox("Fuel Type", ["gas", "diesel", "electric"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.selectbox("Door Number", ["two", "four"])
carbody = st.selectbox("Car Body", ["sedan", "hatchback", "suv", "wagon", "hardtop", "convertible"])
drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "awd"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])
enginetype = st.selectbox("Engine Type", ["ohc", "ohcf", "ohcv", "dohc", "dohcv", "rotor", "electric"])
cylindernumber = st.selectbox("Cylinder Number", ["two", "three", "four", "five", "six", "eight", "twelve", "motor"])
fuelsystem = st.selectbox("Fuel System", ["mpfi", "2bbl", "4bbl", "idi", "mfi", "spdi", "1bbl", "electric"])

if st.button("Predict Price"):
    data = {
        "symboling": symboling,
        "CarName": CarName,
        "fueltype": fueltype,
        "aspiration": aspiration,
        "doornumber": doornumber,
        "carbody": carbody,
        "drivewheel": drivewheel,
        "enginelocation": enginelocation,
        "wheelbase": wheelbase,
        "carlength": carlength,
        "carwidth": carwidth,
        "carheight": carheight,
        "curbweight": curbweight,
        "enginetype": enginetype,
        "cylindernumber": cylindernumber,
        "enginesize": enginesize,
        "fuelsystem": fuelsystem,
        "boreratio": boreratio,
        "stroke": stroke,
        "compressionratio": compressionratio,
        "horsepower": horsepower,
        "peakrpm": peakrpm,
        "citympg": citympg,
        "highwaympg": highwaympg
    }

    try:
        response = requests.post(f"http://{ip_api}:{port_api}/get_predict", json=data)

        if response.status_code == 200:
            prediction = response.json()["prediction"][0]
            st.success(f"Predicted Price: ${prediction:,.2f}")
        else:
            st.error(f"Request failed with status code {response.status_code}")
    except ConnectionError:
        st.error("Failed to connect to the server. Make sure the API is running.")