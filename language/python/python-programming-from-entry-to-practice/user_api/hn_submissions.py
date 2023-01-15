# -*- coding: utf-8 -*-

import requests
from operator import itemgetter
import time
from progress.bar import Bar

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'


PAGE_COUNT = 10
bar = Bar('Loading ', max=PAGE_COUNT)
submission_dicts = []
text_content = ''
r = requests.get(url)
submission_ids = r.json()

for submission_id in submission_ids[:PAGE_COUNT]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
    submission_r = requests.get(url)

    # print(type(submission_r.status_code))
    if submission_r.status_code == 200:
        bar.next()
        time.sleep(1)

    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    # print('\nTitle: ', submission_dict['title'])
    # print('Discussion link: ', submission_dict['link'])
    # print('Comments: ', submission_dict['comments'])
    text_content += (
        '\nTitle: '
        + submission_dict['title']
        + '\nDiscussion link: '
        + submission_dict['link']
        + '\nComments: '
        + str(submission_dict['comments'])
        + '\n'
    )

# 结束进度条
bar.finish()

with open('./hn_submissions.txt', 'w', encoding='utf-8') as f:
    f.write(text_content)
