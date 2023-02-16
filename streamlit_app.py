import streamlit as st
from utils import *

# List of bastards
usr_list = ('Andrei', 'Bart', 'Egor', 'Sviat')

# Create csv file if not exists
create_csv()

# Streamlit site configuration
st.set_page_config(page_title='who pays?', page_icon=':money_with_wings:')


# Streamlit application
def main():
    # Save backup files on each run
    backup_csv()

    st.subheader('Input expenses')

    col1, col2 = st.columns([1, 2])
    with col1:
        who_pays = st.selectbox('who pays?', usr_list)
    with col2:
        who_shares = st.multiselect('who shares?', usr_list, usr_list)

    col3, col4, col5 = st.columns([2, 1, 1])
    with col3:
        comment = st.text_input('comment (e.g. groceries, beer, etc.)')
    with col4:
        how_much = st.number_input('how much?', min_value=0, max_value=1000, value=0)
    with col5:
        st.text('press if ready')
        button = st.button('submit expense')

    if button:
        write_input_to_csv(who_pays, who_shares, comment, how_much)

    # Show table
    expenses_table = show_table()
    st.table(expenses_table.style.format({'An.': '{:.2f}', 'Ba.': '{:.2f}', 'Eg.': '{:.2f}', 'Sv.': '{:.2f}'}))

    # Show summary table
    summary_table = show_summary_table()
    st.table(summary_table.style.format({'An.': '{:.0f}', 'Ba.': '{:.0f}', 'Eg.': '{:.0f}', 'Sv.': '{:.0f}'}))

    st.subheader('Delete rows')

    col6, col7, col8 = st.columns(3)
    with col6:
        row_to_delete = st.selectbox('select row', range(0, len(expenses_table.index)))
    with col7:
        st.text('check if sure')
        sure = st.checkbox('are you sure?')
    with col8:
        st.text('press to delete')
        del_button = st.button('delete row')

    if sure and del_button:
        delete_row(row_to_delete)
        st.experimental_rerun()


if __name__ == '__main__':
    main()
