import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='my-api-key-here') 

# Create a main page
st.title("Foot Traffic Intelligence: Optimize Visits and Empower Businesses")
st.write("Upload your foot traffic data to get insights (for a consumer or a business)")

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to provide summary of the where the place is located, what times and days are the busiest \
                    and when do you recommend the user to visit to avoid peak times.\
                    Also include a summary for the place owners to prepare accordingly for rush times by giving suggestions \
                    for resource allocations."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_input("Enter the name of a place you want to visit: ") 
    
    submitted = st.form_submit_button("Generate Insights")
    
    if submitted:
        st.write(get_completion(prompt))