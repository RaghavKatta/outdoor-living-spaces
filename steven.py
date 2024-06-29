import streamlit as st

st.title("Price Calculator for Outdoor Living Spaces")

area = st.number_input("Enter the area")

#Units converted to in^2
units = {
    "Square millimeters (mm²)": 0.0015500031,  # 1 mm² = 0.0015500031 in²
    "Square centimeters (cm²)": 0.15500031,    # 1 cm² = 0.15500031 in²
    "Square meters (m²)": 1550.0031,           # 1 m² = 1550.0031 in²
    "Square kilometers (km²)": 1550003100.0,   # 1 km² = 1.55e9 in²
    "Square inches (in²)": 1,                  # 1 in² = 1 in²
    "Square feet (ft²)": 144,                  # 1 ft² = 144 in²
    "Square yards (yd²)": 1296,                # 1 yd² = 1296 in²
    "Acres (ac)": 6272640,                     # 1 ac = 6,272,640 in²
    "Hectares (ha)": 15500031.0                # 1 ha = 15,500,031 in²
}

selected_unit = st.selectbox("Select Unit:", units)

#example materials, need to change the units and check accuracy
materials_prices = {
    "Steel": 0.50,        # per kilogram
    "Aluminum": 1.20,     # per kilogram
    "Copper": 6.50,       # per kilogram
    "Concrete": 0.10,     # per kilogram
    "Wood": 0.15,         # per kilogram
    "Glass": 0.20,        # per square meter
    "Brick": 0.50,        # per piece
    "PVC": 1.00,          # per kilogram
    "Rubber": 2.00,       # per kilogram
    "Sand": 0.05,         # per kilogram
    "Gravel": 0.03,       # per kilogram
    "Asphalt": 0.25,      # per kilogram
    "Plaster": 0.15,      # per kilogram
    "Ceramic Tile": 2.50, # per square meter
    "Paint": 3.00,        # per liter
    "Insulation": 0.30,   # per square meter
    "Fiber Glass": 1.50,  # per kilogram
    "Clay": 0.20,         # per kilogram
    "Bamboo": 0.10,       # per kilogram
    "Carbon Fiber": 25.00 # per kilogram
}

selected_material = st.selectbox("Select a material:", list(materials_prices.keys()))

if st.button("Calculate Price"):
    price = area * units[selected_unit] * materials_prices[selected_material]
    st.title(f"Price is : $ {price:.2f}")