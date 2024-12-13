import streamlit as st

st.title("Grades")

# Input fields for project, internal, and external marks
pro = st.number_input('Enter project marks:', min_value=0, step=1)
inte = st.number_input('Enter internal marks:', min_value=0, step=1)
ext = st.number_input('Enter external marks:', min_value=0, step=1)

if st.button("Grade"):
   if pro > 50 and inte > 50 and ext > 50:
       total = ((70 / 100) * pro) + ((10 / 100) * inte) + ((20 / 100) * ext)
       st.write(f'Total: {total}')

       if total > 90:
           st.write('Grade: A')
       elif total > 80:
           st.write('Grade: B')
       else:
           st.write('Grade: C')
   else:
       if pro < 50:
           st.write('Failed in Project')
       if inte < 50:
           st.write('Failed in Internal')
       if ext < 50:
           st.write('Failed in External')
