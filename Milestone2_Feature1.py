import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title("Simple Foot Traffic Simulation")

# Introduction text
st.write("""
### Welcome to the simple foot traffic simulation tool.
Use the slider below to simulate foot traffic data and see the real-time chart update.
""")

# Simulated initial data
traffic_data = pd.DataFrame({
    'time': pd.date_range(start='2023-10-27 08:00', periods=10, freq='H'),
    'foot_traffic': np.random.randint(50, 500, 10)
})

# Display the initial chart
st.line_chart(traffic_data.set_index('time'))

# Add a slider for user input to simulate foot traffic
new_traffic = st.slider("Adjust the foot traffic manually", min_value=0, max_value=1000, value=300)

# Update the data with the new slider value
new_time = traffic_data.iloc[-1]['time'] + pd.Timedelta(hours=1)
new_data = pd.DataFrame({'time': [new_time], 'foot_traffic': [new_traffic]})

# Add the new data to the existing traffic data
traffic_data = pd.concat([traffic_data, new_data], ignore_index=True)

# Update and display the new chart with the user's input
st.line_chart(traffic_data.set_index('time'))

# Footer message
st.write("This simple tool allows you to control foot traffic data and see the updated chart in real-time.")

