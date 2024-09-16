import streamlit as st

# App description
st.title("Eczema Area and Severity Index (EASI) Calculator")
st.write("""
The Eczema Area and Severity Index (EASI) is a tool used by clinicians to measure the extent (area) and severity of eczema. 
This app helps healthcare providers easily calculate the EASI score based on the patient's clinical condition.
""")

# Function to calculate EASI
def calculate_easi(erythema, edema, excoriation, lichenification, area_percentage):
    # Formula for EASI is the sum of scores for each region
    region_score = 0.1 * area_percentage * (erythema + edema + excoriation + lichenification)
    return region_score

# Input for each body region
st.header("Enter severity scores (0-3) for each body region")

with st.expander("Head/Neck"):
    erythema_hn = st.slider('Erythema (Redness)', 0, 3)
    edema_hn = st.slider('Edema/ Papulation (Swelling)', 0, 3)
    excoriation_hn = st.slider('Excoriation (Scratching)', 0, 3)
    lichenification_hn = st.slider('Lichenification (Thickened skin)', 0, 3)
    area_hn = st.slider('Area affected (%)', 0, 100)

with st.expander("Upper Limbs"):
    erythema_ul = st.slider('Erythema (Redness) - Upper limbs', 0, 3)
    edema_ul = st.slider('Edema/ Papulation (Swelling) - Upper limbs', 0, 3)
    excoriation_ul = st.slider('Excoriation (Scratching) - Upper limbs', 0, 3)
    lichenification_ul = st.slider('Lichenification (Thickened skin) - Upper limbs', 0, 3)
    area_ul = st.slider('Area affected (%) - Upper limbs', 0, 100)

with st.expander("Lower Limbs"):
    erythema_ll = st.slider('Erythema (Redness) - Lower limbs', 0, 3)
    edema_ll = st.slider('Edema/ Papulation (Swelling) - Lower limbs', 0, 3)
    excoriation_ll = st.slider('Excoriation (Scratching) - Lower limbs', 0, 3)
    lichenification_ll = st.slider('Lichenification (Thickened skin) - Lower limbs', 0, 3)
    area_ll = st.slider('Area affected (%) - Lower limbs', 0, 100)

with st.expander("Trunk"):
    erythema_trunk = st.slider('Erythema (Redness) - Trunk', 0, 3)
    edema_trunk = st.slider('Edema/ Papulation (Swelling) - Trunk', 0, 3)
    excoriation_trunk = st.slider('Excoriation (Scratching) - Trunk', 0, 3)
    lichenification_trunk = st.slider('Lichenification (Thickened skin) - Trunk', 0, 3)
    area_trunk = st.slider('Area affected (%) - Trunk', 0, 100)

# Calculate EASI score for each region
easi_hn = calculate_easi(erythema_hn, edema_hn, excoriation_hn, lichenification_hn, area_hn)
easi_ul = calculate_easi(erythema_ul, edema_ul, excoriation_ul, lichenification_ul, area_ul)
easi_ll = calculate_easi(erythema_ll, edema_ll, excoriation_ll, lichenification_ll, area_ll)
easi_trunk = calculate_easi(erythema_trunk, edema_trunk, excoriation_trunk, lichenification_trunk, area_trunk)

# Total EASI score
total_easi = easi_hn + easi_ul + easi_ll + easi_trunk

# Display the result
st.subheader(f'Total EASI Score: {total_easi:.2f}')
