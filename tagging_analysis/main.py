import pandas
from datetime import datetime
import csv
# TODO: automate useful_columns and headers

startTime = datetime.now()

useful_columns = ['10-Second Video Views',
                   '3-Second Video Views',
                   'Ad ID',
                   'Ad Name',
                   'Ad Set ID',
                   'Ad Set Name',
                   'Ad name 2',
                   'Amount Spent (USD)',
                   'Campaign ID',
                   'Campaign Name',
                   'Clicks (All)',
                   'Creative',
                   'Frequency',
                   'Impressions',
                   'Permalink',
                   'Post Engagement',
                   'Reach',
                   'Reporting Ends',
                   'Reporting Starts',
                   'Video Average Watch Time',
                   'Video Percentage Watched',
                   'Video Watches at 100%',
                   'Video Watches at 25%',
                   'Video Watches at 50%',
                   'Video Watches at 75%',
                   'Video Watches at 95%',
                   'Website Purchases',
                   'Website Searches',
                   'Ad Name 8'
                    ]
headers = [
                   '10-Second Video Views',
                   '3-Second Video Views',
                   'Ad ID',
                   'Ad Name',
                   'Ad Set ID',
                   'Ad Set Name',
                   'Ad name 2',
                   'Amount Spent (USD)',
                   'Campaign ID',
                   'Campaign Name',
                   'Clicks (All)',
                   'Creative',
                   'Frequency',
                   'Impressions',
                   'Permalink',
                   'Post Engagement',
                   'Reach',
                   'Reporting Ends',
                   'Reporting Starts',
                   'Video Average Watch Time',
                   'Video Percentage Watched',
                   'Video Watches at 100%',
                   'Video Watches at 25%',
                   'Video Watches at 50%',
                   'Video Watches at 75%',
                   'Video Watches at 95%',
                   'Website Purchases',
                   'Website Searches',
                   'Ad Name 8',
                   'Tag',
                   'in_out',
                   'repeat_order']


                  
def fix_tag_headers(df):
    # creates a tag header naming convention
    new_columns = df.columns.values
    i = 0
    for column in df:
        if str(df[column][1]) == 'True' or str(df[column][1]) == 'False':
            new_columns[i] = "Tag: " + column
        i+=1
    return new_columns


def get_tag_list(df):
    # creates a list of tags
    tag_list = list()
    for column in df:
        if str(df[column][1]) == 'True' or str(df[column][1]) == 'False':
            tag_list.append(column)
    return tag_list


def get_tag_metrics(df, tag_list):
    rows_list = []
    for i in range(len(df)):
        print('working on column {} of {}'.format(i, len(df)))
        repeat_order = 1
        for item in tag_list:
            row_dict = {}

            for header in useful_columns:
                row_dict[header] = df[header][i]
            if str(df[item][i]) == 'True':
                row_dict['in_out'] = 'in'
                row_dict['repeat_order'] = repeat_order
                row_dict['Tag'] = item
                repeat_order += 1
            if str(df[item][i]) == 'False':
                row_dict['in_out'] = 'out'
                row_dict['repeat_order'] = repeat_order
                row_dict['Tag'] = item
                repeat_order += 1
            rows_list.append(row_dict)
    print('no memory issue here!')
    return rows_list

def write_rows(dictionary, outfile):
    with open(outfile, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames = headers)
        writer.writeheader()
        for line in dictionary:
            writer.writerow(line)


def main(infile, outfile):
    df = pandas.read_csv(infile, engine='python')
    print('it worked')
    df.columns = fix_tag_headers(df)
    print('get tag list')
    tag_list = get_tag_list(df)

    dictionary_to_write = get_tag_metrics(df, tag_list)
    write_rows(dictionary_to_write, outfile)
    
    complete_time = datetime.now() - startTime
    print('Time to complete: '+ complete_time)
