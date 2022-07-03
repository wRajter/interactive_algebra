import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title('Interactive math')

st.write('''
        ## Try multiplication
        Watch how the rectangle's area is reacting
         ''')

first_num = st.sidebar.slider('select first number', 1, 10)
second_num = st.sidebar.slider('select second number', 1, 10)


# XY array
Z = np.arange(1, first_num * second_num + 1)
Z = Z.reshape(first_num, second_num)

fig, ax = plt.subplots(figsize=(5, 5))
# ax.text(0.1, 0.1, 'Test', color='blue',
#         bbox=dict(facecolor='none', edgecolor='blue', pad=10.0))
ax.imshow(Z)
ax.set_aspect('equal')
# ax.set_axis_off()
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel(str(first_num))
ax.set_xlabel(str(second_num))
st.pyplot(fig)
