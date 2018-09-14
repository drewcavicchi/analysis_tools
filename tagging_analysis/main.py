import pandas

number_list = ['10-Second Video Views', '3-Second Video Views',
       'Amount Spent (USD)', 'Clicks (All)',
       'Frequency', 'Impressions',
        'Number of Records',
       'Permalink', 'Post Engagement', 'Reach','Video Average Watch Time',
       'Video Percentage Watched', 'Video Watches at 100%',
       'Video Watches at 25%', 'Video Watches at 50%', 'Video Watches at 75%',
       'Video Watches at 95%','Website Purchases', 'Website Searches']

new_dataframe_columns = ['Tag', 'total_amount_spent', 'total_impressions', 'total_website_purchases', 'total_website_searches',
        'price_per_purchase', 'price_per_search', 'purchase_rate', 'search_rate', 'purchase_per_search']
        # TODO: automate new columns

def fix_tag_headers(df):
    # creates a tag header naming convention
    new_columns = df.columns.values
    i = 0
    for column in df:
        if str(df[column][1]) == 'True' or str(df[column][1]) == 'False':
            new_columns[i] = "Tag: " + column
        i+=1
    return new_columns

def divide_by_zero(num, dom):
    if dom == 0:
        return 0
    else:
        return num/dom


def get_tag_list(df):
    # creates a list of tags
    tag_list = list()
    for column in df:
        if str(df[column][1]) == 'True' or str(df[column][1]) == 'False':
            tag_list.append(column)
    return tag_list

def get_tag_metrics(df, tag_list):
    rows_list = []
    for item in tag_list:
        row_dict = {}
        total_amount_spent = 0
        total_impressions = 0
        total_website_purchases = 0
        total_website_searches = 0
        i = 0
        for i in range(len(df[item])):
            # totals for tag
            if str(df[item][i]) == 'True':          
                total_amount_spent += df['Amount Spent (USD)'][i]
                total_impressions += df['Impressions'][i]
                total_website_purchases += df['Website Purchases'][i]
                total_website_searches += df['Website Searches'][i]
        # metrics for analysis, add to new dataframe
        row_dict['Tag'] = item
        row_dict['total_amount_spent'] = total_amount_spent
        row_dict['total_impressions'] = total_impressions
        row_dict['total_website_purchases'] = total_website_purchases
        row_dict['total_website_searches'] = total_website_searches
        row_dict['price_per_purchase'] = divide_by_zero(total_amount_spent, total_website_purchases)
        row_dict['price_per_search'] = divide_by_zero(total_amount_spent, total_website_searches)
        row_dict['purchase_rate'] = divide_by_zero(total_website_purchases, total_impressions)
        row_dict['search_rate'] = divide_by_zero(total_website_searches, total_impressions)
        row_dict['purchase_per_search'] = divide_by_zero(total_website_searches, total_website_purchases)
        rows_list.append(row_dict)
    output_dataframe = pandas.DataFrame(rows_list)
    return output_dataframe



def main(infile, outfile):
    df = pandas.read_csv(infile)
    df.columns = fix_tag_headers(df)
    tag_list = get_tag_list(df)
    df[number_list] = df[number_list].fillna(0)
    output_df = get_tag_metrics(df, tag_list)
    output_df.to_csv(outfile)



main("tag_data.csv", "output.csv")