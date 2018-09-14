import pandas
from datetime import datetime
import csv

startTime = datetime.now()

useful_columns = ['Tag: 10-20s',
                   '10-Second Video Views',
                   '3-Second Video Views',
                   'Tag: 5-10s',
                   'Ad ID',
                   'Ad Name',
                   'Ad Set ID',
                   'Ad Set Name',
                   'Ad name 2',
                   'Amount Spent (USD)',
                   'Tag: Awkwafina',
                   'Campaign ID',
                   'Campaign Name',
                   'Tag: Character focus',
                   'Clicks (All)',
                   'Tag: Color: Bright/ bold',
                   'Tag: Color: Flat',
                   'Tag: Color: Muted/ antique',
                   'Tag: Color: black and white',
                   'Tag: Comedy',
                   'Tag: Cool Palatte',
                   'Creative',
                   'Tag: Dark',
                   'Tag: Dialogue',
                   'Tag: Eleanor Young',
                   'Tag: Family',
                   'Tag: Food',
                   'Frequency',
                   'Tag: Friend',
                   'Tag: Gif',
                   'Tag: Has Other Text',
                   'Tag: Has Reviews',
                   'Tag: Has subtitles',
                   'Impressions',
                   'Tag: Light',
                   'Tag: Music',
                   'Tag: Nick Young',
                   'Tag: Older female characters featured',
                   'Tag: Older male characters featured',
                   'Permalink',
                   'Post Engagement',
                   'Tag: Rachel Chu',
                   'Reach',
                   'Reporting Ends',
                   'Reporting Starts',
                   'Tag: Riches',
                   'Tag: Romance',
                   'Tag: Rotten Tomatoes',
                   'Tag: Square',
                   'Tag: Still',
                   'Tag: Story focus',
                   'Tag: Talent appears in first 5s',
                   'Tag: Talent names present',
                   'Tag: Title Card Always Present',
                   'Tag: Title Card: End',
                   'Video Average Watch Time',
                   'Video Percentage Watched',
                   'Video Watches at 100%',
                   'Video Watches at 25%',
                   'Video Watches at 50%',
                   'Video Watches at 75%',
                   'Video Watches at 95%',
                   'Tag: Voice-over',
                   'Tag: Warm Palatte',
                   'Website Purchases',
                   'Website Searches',
                   'Tag: Wide',
                   'Tag: Young female characters featured',
                   'Tag: Young male characters featured',
                   'Ad Name 8']

                  
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
    for i in range(10):
        print('working on column {} of {}'.format(i, len(df)))
        for item in tag_list:
            row_dict = {}
            repeat_order = 1
            for header in useful_columns:
                row_dict[header] = df[header][i]
            if str(df[item][i]) == 'True':
                row_dict['in_out'] = 'in'
                row_dict['repeat_order'] = repeat_order
                repeat_order += 1
            if str(df[item][i]) == 'False':
                row_dict['in_out'] = 'out'
                row_dict['repeat_order'] = repeat_order
                repeat_order += 1
            rows_list.append(row_dict)
    print('no memory issue here!')
    return rows_list

def write_rows(dictionary, outfile):
    data = csv.DictReader(dictionary)
    with open(outfile, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile)
        writer.writeheader()
        for line in data:
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
    print('this took: {} seconds to complete'.format(complete_time))


main("TagDataJoinedPython.csv", "output2.csv")
