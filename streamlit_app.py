# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
cnx = st.connection("snowflake")
session = cnx.session()
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

# erased on lesson 2
#option = st.selectbox(
#    'What is your favorite fruit?',
#    ('Banana', 'Strawberries', 'Peaches')
#)

#st.write('Your favorite fruite is: ', option)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients'
    , my_dataframe
    , max_selections=5
)

ingredients_string = ''
if ingredients_list:
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    #st.write(ingredients_string)


my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """', '""" + name_on_order + """')"""

#st.write(my_insert_stmt)

time_to_insert = st.button('Submit Order')

if time_to_insert :
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")
