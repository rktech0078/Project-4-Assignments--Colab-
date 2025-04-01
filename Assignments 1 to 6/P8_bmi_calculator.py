import streamlit as st

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    
    st.title("BMI CALCULATOR")
    
    weight = st.slider("Weight (kg):", min_value=1, max_value=200, value=50)
    height = st.slider("Height (m):", min_value=1, max_value=200, value=50)
    
    if st.button("Calculate", use_container_width=True):
        bmi = bmi_calculator(weight, height)
        st.write(f"### Your BMI is: {bmi}")
        
        if bmi < 18.5:
            st.warning("🔹 You are underweight. Consider a balanced diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a normal weight. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight. Consider exercising regularly.")
        else:
            st.error("🚨 You are obese. Consult a healthcare provider.")
        
if __name__ == '__main__':
    main()