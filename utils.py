import pandas as pd
import shutil
import os
from datetime import datetime


# Create csv file if not exists
def create_csv():
    csv_file = 'csv_table.csv'
    if os.path.exists(csv_file):
        pass
    else:
        # create empty dataframe with the right columns & dtypes
        table = {
            'Name': [],
            'Comment': [],
            'Euros': [],
            'An.': [],
            'Ba.': [],
            'Eg.': [],
            'Sv.': [],
        }
        df = pd.DataFrame.from_dict(table)
        csv_table = df.to_csv(csv_file, sep=',', encoding='utf-8', index=False)
        return csv_table


# Function to store backup files
def backup_csv():
    src_path = 'csv_table.csv'
    dst_path = 'backup/' + datetime.now().strftime("%Y%m%d-%H%M%S") + '_' + src_path
    shutil.copy(src_path, dst_path)


# Write input to csv file
def write_input_to_csv(who_pays, who_shares, comment, how_much):
    if len(who_shares) == 0:
        pass
    elif [who_pays] == who_shares:
        pass
    elif how_much == 0:
        pass
    else:
        n = len(who_shares)
        new_row = {
            'Name': str(who_pays),
            'Comment': str(comment),
            'Euros': int(how_much),
            'An.': int(how_much) / n if 'Andrei' in who_shares else 0,
            'Ba.': int(how_much) / n if 'Bart' in who_shares else 0,
            'Eg.': int(how_much) / n if 'Egor' in who_shares else 0,
            'Sv.': int(how_much) / n if 'Sviat' in who_shares else 0,
        }

        csv_file = 'csv_table.csv'
        df = pd.read_csv(csv_file, sep=',')
        df2 = df.append(new_row, ignore_index=True)
        csv_table = df2.to_csv(csv_file, sep=',', encoding='utf-8', index=False)
        return csv_table


# Show expenses table
def show_table():
    csv_file = 'csv_table.csv'
    table = pd.read_csv(csv_file, sep=',')
    return table


# Show summary table
def show_summary_table():
    csv_file = 'csv_table.csv'
    table = pd.read_csv(csv_file, sep=',')

    an_payed = table.loc[table['Name'] == 'Andrei', 'Euros'].sum()
    an_had_to = table['An.'].sum()
    ba_payed = table.loc[table['Name'] == 'Bart', 'Euros'].sum()
    ba_had_to = table['Ba.'].sum()
    eg_payed = table.loc[table['Name'] == 'Egor', 'Euros'].sum()
    eg_had_to = table['Eg.'].sum()
    sv_payed = table.loc[table['Name'] == 'Sviat', 'Euros'].sum()
    sv_had_to = table['Sv.'].sum()

    new_table = {
        'Summary': ['payed total', 'had to pay', 'gets(+) / gives(-)'],
        'An.': [an_payed, an_had_to, an_payed - an_had_to],
        'Ba.': [ba_payed, ba_had_to, ba_payed - ba_had_to],
        'Eg.': [eg_payed, eg_had_to, eg_payed - eg_had_to],
        'Sv.': [sv_payed, sv_had_to, sv_payed - sv_had_to],
    }

    df = pd.DataFrame.from_dict(new_table)
    return df


# Delete selected rows by one
def delete_row(row_number):
    csv_file = 'csv_table.csv'
    df = pd.read_csv(csv_file, sep=',')
    df2 = df.drop(index=row_number)
    csv_table = df2.to_csv(csv_file, sep=',', encoding='utf-8', index=False)
    return csv_table
