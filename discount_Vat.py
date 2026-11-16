import streamlit as st
st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
st.divider()
price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0 , value=0.0)
discount = st.number_input("กรอกส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0)
discountTotal = price * (discount/100)
addedVat = discountTotal * 0.07
finalTotal = discountTotal - addedVat
st.divider()
st.write(f"• ส่วนลด ({discount}%): -{discount:.2f} บาท")
st.write(f"• ราคาหลังหักส่วนลด: {discountTotal:.2f} บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{addedVat:.2f} บาท")
st.header(f"• ราคาสุทธิที่ต้องจ่าย: **{finalTotal:.2f}** บาท")
st.divider()
st.write("นายภูมิยศ ชีพประกิต เลขที่ 28  ม.4/5")
