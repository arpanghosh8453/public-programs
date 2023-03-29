# %%
import requests, time
import datetime

def get_post_details(start_time,end_time,subreddit,use_filter=""):
    url_submission = f"https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size=0&after={start_time}&before={end_time}&q={use_filter}"
    response_submission = requests.get(url_submission)
    url_comment = f"https://api.pushshift.io/reddit/search/comment/?subreddit={subreddit}&size=0&after={start_time}&before={end_time}&q={use_filter}"
    response_comment = requests.get(url_comment)
    
    old_sub_url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size=1&before={start_time}"
    response_old_sub = requests.get(old_sub_url)
    old_sub_data = response_old_sub.json()
    old_sub_count = old_sub_data['data'][0]['subreddit_subscribers']

    new_sub_url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size=1&before={end_time}"
    response_new_sub = requests.get(new_sub_url)
    new_sub_data = response_new_sub.json()
    new_sub_count = new_sub_data['data'][0]['subreddit_subscribers']

    sub_increase_count = new_sub_count-old_sub_count

    if response_submission.status_code == 200 and response_comment.status_code == 200:
        data_submission = response_submission.json()
        data_comment = response_comment.json()
        return {"start_date":datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d'),"end_date":datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d'), "new_submission_count":data_submission['metadata']['es']['hits']['total']['value'], "new_comment_count":data_comment['metadata']['es']['hits']['total']['value'],"new_subscriber_count":sub_increase_count, "total_current_subscribers":new_sub_count}
    else:
        print("Error fetching data from Pushshift API.")
        raise ValueError("Error fetching data from pushapi")

# %%
SUBREDDIT = "unemployment" # replace with the desired subreddit name
INCLUDE_REMOVED = True
OUTPUT_FILE = "C:/Users/thisi/Downloads/reddit_code_out.csv"
start_date = "2020-01-01"  # yyyy-mm-dd format
end_date = "2020-03-01"  # yyyy-mm-dd format
interval_days = 7 # interval days

#current_time = int(datetime.datetime.now().timestamp())
#last_week_time = int((datetime.datetime.now() - datetime.timedelta(days=7)).timestamp())

additional_filter = "" if INCLUDE_REMOVED else "!(%22[removed]%22)"

# %%
start_time = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end_time = datetime.datetime.strptime(end_date, "%Y-%m-%d")
interval = datetime.timedelta(days=interval_days)

timestamps = []
current_time = start_time
while current_time <= (end_time-interval):
    timestamps.append((int(current_time.timestamp()),int((current_time+interval).timestamp())))
    current_time += interval

timestamps.append((int(current_time.timestamp()),int(end_time.timestamp())))

# %%
for timestamp in timestamps:
    while True:
        try:
            result_dict = get_post_details(timestamp[0],timestamp[1],SUBREDDIT,additional_filter)
        except Exception as ERR:
            print(ERR)
            time.sleep(2)
            continue
        break
    output_str = ",".join([result_dict['start_date'], result_dict['end_date'],str(result_dict['new_submission_count']),str(result_dict['new_comment_count']),str(result_dict['new_subscriber_count']),str(result_dict['total_current_subscribers'])])
    with open(OUTPUT_FILE,'a') as out_file:
        out_file.write("\n"+output_str)
    print(result_dict)

# %%
#get_post_details(int(datetime.datetime.strptime("2021-12-01", "%Y-%m-%d").timestamp()),int(datetime.datetime.strptime("2022-11-01", "%Y-%m-%d").timestamp()),SUBREDDIT,additional_filter)




