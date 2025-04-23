import streamlit as st
import math

def calculate_body_fat(gender, height, neck, waist, hip=None):
    if gender == 'Male':
        bfp = 86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76
    elif gender == 'Female':
        if hip is None:
            raise ValueError("Hip measurement is required for females.")
        bfp = 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387
    else:
        raise ValueError("Invalid gender input.")
    return round(bfp, 2)

def main():
    st.title("Body Fat Percentage Calculator")
    st.write("Based on the US Navy Body Fat Formula")

    gender = st.selectbox("Gender", options=["Male", "Female"])
    height = st.number_input("Height (in cm):", min_value=50.0, step=0.1)
    neck = st.number_input("Neck circumference (in cm):", min_value=10.0, step=0.1)
    waist = st.number_input("Waist circumference (in cm):", min_value=20.0, step=0.1)

    hip = None
    if gender == "Female":
        hip = st.number_input("Hip circumference (in cm):", min_value=20.0, step=0.1)

    if st.button("Calculate Body Fat %"):
        try:
            bfp = calculate_body_fat(gender, height, neck, waist, hip)
            st.success(f"Estimated Body Fat Percentage: {bfp}%")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
