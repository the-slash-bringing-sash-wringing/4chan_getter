import basc_py4chan as chan
import re

def get_finder(url):
    board=chan.board(url.split('/')[3])
    thread = board.get_thread(url.split('/')[5])
    posts= thread.all_posts
    output = []
    for x in posts:
        if str(x.post_id)[-1:] == str(x.post_id)[-2:-1] or str(x.post_id)[-2:]=='94':
            if re.search('>>(.*)\n', x.text_comment) != None:
                output.append([f'POST: {x.post_id} {x.text_comment}',[[f'REPLIED_TO: {post.post_id}', post.text_comment] for post in posts if post.post_id == int(re.search('>>(.*)\n', x.text_comment).group(1))]])
    return output
