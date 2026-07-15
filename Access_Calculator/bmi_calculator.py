import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.markdown(
    """
    <div style="background: linear-gradient(135deg, #dff7ff, #f4f7ff); padding: 24px; border-radius: 16px;">
        <h1 style="color: #0e4a7f;">Body Mass Index (BMI) Calculator</h1>
        <p style="font-size: 1rem; color: #2d4a6a; margin: 0;">
            Enter your weight in pounds and height in inches to calculate your BMI and see how it relates to standard health categories.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form(key="bmi_form"):
    st.write("### Enter your information")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (pounds)", min_value=0.0, step=0.1, format="%.1f")
    with col2:
        height = st.number_input("Height (inches)", min_value=0.0, step=0.1, format="%.1f")
    submit = st.form_submit_button("Calculate BMI")

if submit:
    if weight <= 0 or height <= 0:
        st.error("Please enter positive values for both weight and height.")
    else:
        bmi = weight / (height * height) * 703
        bmi_value = f"{bmi:.1f}"

        if bmi < 18.5:
            category = "Underweight"
            description = "This BMI is below the healthy range. Consider checking your nutrition and speaking with a healthcare provider."
            result_func = st.warning
        elif bmi < 25:
            category = "Normal weight"
            description = "This BMI is within the healthy range. Keep up your balanced lifestyle."
            result_func = st.success
        elif bmi < 30:
            category = "Overweight"
            description = "This BMI is above the healthy range. A balanced diet and regular exercise may help."
            result_func = st.warning
        else:
            category = "Obesity"
            description = "This BMI is in the obesity range. Consult a healthcare provider for personalized advice."
            result_func = st.error

        st.metric(label="Your BMI", value=bmi_value, delta=category)
        st.markdown(
            f"**What your BMI means:** BMI, or Body Mass Index, is a number that compares your weight and height to estimate whether your body weight is in a healthy range. A BMI of **{bmi_value}** falls into the **{category}** category."
        )
        result_func(description)

        st.markdown(
            """
            ### BMI categories
            - **Underweight:** BMI less than 18.5
            - **Normal weight:** BMI 18.5 to 24.9
            - **Overweight:** BMI 25 to 29.9
            - **Obesity:** BMI 30 or greater

            BMI does not directly measure body fat, but it is a useful screening tool for many people.
            """
        )
        st.caption("Use this app as a general guide only. For medical advice, consult a health professional.")
