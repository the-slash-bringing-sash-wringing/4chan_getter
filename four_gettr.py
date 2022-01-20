import basc_py4chan as chan
from bs4 import BeautifulSoup
import re

def cleanup(string):
    return BeautifulSoup(string, "lxml").text

def get_finder(url):
    board=chan.board(url.split('/')[3])
    thread = board.get_thread(url.split('/')[5])
    posts= thread.all_posts
    output = []
    for x in posts:
        if str(x.post_id)[-1:] == str(x.post_id)[-2:-1] or str(x.post_id)[-2:]=='94' or str(x.post_id)[-2:]==str(x.post_id)[-4:-2]:
            if re.search('href="#p(.*)"', x.comment) != None:
                if re.search('>>\d+', cleanup(x.comment)) != None:
                    rpi = re.match('>>\d+', cleanup(x.comment)).group().replace('>>', "")
                    output.append({f'POST {x.post_id}' : f'{cleanup(x.comment)}', f'REPLIED TO {rpi}' : [f'{cleanup(post.comment)}' for post in posts \
                                    if post.post_id == int(rpi)]})
                else:
                	output.append({f'POST {x.post_id}' : f'{cleanup(x.comment)}'})
    return output
