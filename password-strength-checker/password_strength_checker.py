import streamlit as st
import re

# Web Title
st.title("🔐 Password Strength Checker 🔐") 

# Description
st.markdown(""" 
Welcome Dear User!  
**Improve Your Password Strength**  
Ensure your password is secure by checking:
- ✅ Length
- ✅ Upper & Lowercase letters
- ✅ Numbers
- ✅ Special characters
""")

# Input
password = st.text_input("Enter your Password:", type="password")

# Password Strength Checking Function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length checking
    if len(password) >= 8:
        score += 1
    else:    
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase & Lowercase checking
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:    
        feedback.append("Password should include both uppercase and lowercase letters.")

    # Digits Checking
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special Character Checking
    if re.search(r'\W', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    return score, feedback   

# Button
if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔍 Password Strength Result:")

        # Strength Bar
        strength_percentage = (score / 4) * 100

        if score == 4:
            st.success("🟢 ✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("🟡 ⚠️ Moderate Password. Try to meet all criteria for a stronger password.")
        else:
            st.error("🔴 ❌ Weak Password. Improve it using the suggestions below.")

        st.progress(int(strength_percentage))  # Visual bar

        # Feedback Suggestions
        if feedback:
            st.info("💡 Suggestions to improve your password:")
            for tip in feedback:
                st.write(f"- {tip}")
    else:
        st.error("🚨 Please enter a password to check.")

# Footer  
st.markdown("""
---
Made with ❤️ by **Muhammad Raees student of GHS.**
""")
