import pandas as pd

def tag_spreadsheet_formatting(tag_spreadsheet):
    ## formats template tag spreadsheet into boolean TF values
    dictionary_list = []
    df = pd.read_csv(tag_spreadsheet)
    df = df.fillna('False')
    for i in range(len(df)):
        new_dict = {}
        for header in df.columns.values:
            if header == 'Creative':
                new_dict[header] = df[header][i]
            elif str(df[header][i]) == '1.0':
                new_dict[header] = "True"
            else:
                new_dict[header] = "False"
        dictionary_list.append(new_dict)
    output_dataframe = pd.DataFrame(dictionary_list)
    return output_dataframe

            
    

def fix_tag_headers(df):
    # creates a tag header naming convention
    new_columns = df.columns.values
    i = 0
    for column in df:
        if str(df[column][1]) == 'True' or str(df[column][1]) == 'False':
            new_columns[i] = "Tag: " + column
        i+=1
    return new_columns

def create_rows(df, tag_list):
    dictionary_list = []

    for tag in tag_list:
        for i in range(len(df[tag])):
            new_dict = {}
            # allows filtering for a single record as many to many relationship will cause multiple records!
            if tag == tag_list[0]:
                new_dict['Deduplicate Data Filter'] = 'Filter'
            else:
                new_dict['Deduplicate Data Filter'] = 'No Filter'
            if str(df[tag][i]) == 'True':
                new_dict['Tag'] = tag
                new_dict['Creative'] = df['Creative'][i]
                new_dict['in_out'] = 'in'
                dictionary_list.append(new_dict)
            elif str(df[tag][i]) == 'False':
                new_dict['Tag'] = tag
                new_dict['Creative'] = df['Creative'][i]
                new_dict['in_out'] = 'out'
                dictionary_list.append(new_dict)
    output_dataframe = pd.DataFrame(dictionary_list)
    return output_dataframe


    

def main():
    infile = input("Tag tracker filename: ") + '.csv'
    formatted_infile = tag_spreadsheet_formatting(infile)
    formatted_infile.columns = fix_tag_headers(formatted_infile)
    formatted_infile = formatted_infile.reindex(sorted(formatted_infile.columns), axis=1)
    tag_list = formatted_infile.columns[1:]
    output_df = create_rows(formatted_infile, tag_list)
    outfile = (input('Name of film: ').replace(" ", "_") + '_tags.csv').lower()
    output_df.to_csv(outfile)
    print('it worked!')


main()
