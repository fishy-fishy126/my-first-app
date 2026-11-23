import streamlit as st

st.markdown("# :red[🏋️ คำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนํ้าหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื่องต้น")

weight = st.number_input("กรอกนํ้าหนักของคุณ (kg):", min_value = 1.0, value = 1.0)
height = st.number_input("กรอกความสูงของคุณ (cm):", min_value = 1.0, value = 1.0)

if st.button("คำนวนค่า BMI 🎯"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)

  st.write ("---")
  st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

  if bmi < 18.5:
    st.warning("⚠️ คุณมีนํ้าหนักน้อยกว่าเกนฑ์ (ผอม)")
  elif 18.5 <= bmi < 23.0:
    st.success("🎉 คุณมีนํ้าหนักอยู่ในเกนฑ์ปกติ (สุขภาพดี)")
  elif 23.0 <= bmi < 25.0:
    st.info("💡 คุณเรื่มมีนํ้าหนักเกินเกนฑ์ (ท่วม)")
  else
    st.error("🚨 คุณอยู่ในเกนฒ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")
st.divider()
st.write("นาย ภูมิยศ ชีพประกิต ม.4/5 เลขที่ 28")
