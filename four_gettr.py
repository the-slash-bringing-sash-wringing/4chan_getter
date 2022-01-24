import basc_py4chan as chan
from bs4 import BeautifulSoup
import re
import rich

def cleanup(string):
    return BeautifulSoup(string, "lxml").text

def get_finder(url):
    board=chan.board(url.split('/')[3])
    thread = board.get_thread(url.split('/')[5])
    posts= thread.all_posts
    output = []
    for x in posts:
        if str(x.post_id)[-1:] == str(x.post_id)[-2:-1] or str(x.post_id)[-2:]==str(x.post_id)[-4:-2]:
            if re.search('href="#p(.*)"', x.comment) != None:
                if re.search('>>\d+', cleanup(x.comment)) != None:
                    rpi = [x.replace('>>', '') for x in re.findall('>>\d+', cleanup(x.comment))]
                    rich.print({f'POST {x.post_id}' : f'{cleanup(x.comment)}'})
                    for reply_id in rpi:
                        print({'ABOVE_REPLIED_TO': f'{reply_id}', \
                                       'CONTENTS': [cleanup(post.comment) for post in posts \
                                                  if post.post_id==int(reply_id)]})  
                else:
                    rich.print({f'POST {x.post_id}' : f'{cleanup(x.comment)}'})
