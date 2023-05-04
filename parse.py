import xmltodict
import re


with open('papapiu.WordPress.2023-05-03.xml', encoding="utf-8") as fd:
    doc = xmltodict.parse(fd.read())
print(doc['rss']['channel']['item'][0].keys())


posts = []
for post in doc['rss']['channel']['item']:
    attch = ""
    if 'wp:attachment_url' in post:
        attch = post["wp:attachment_url"]
    pobj = {
        'title': post['title'],
        'date': post['wp:post_date'],
        'description': post['description'],
        'excerpt': post['excerpt:encoded'],
        'content': post['content:encoded'],
        'post_name': post['wp:post_name'],
        'status': post['wp:status'],
        'post_type': post['wp:post_type'],
        'attachment_url': attch,
    }
    posts.append(pobj)

# print(posts)

pages = []
blog_posts = []
attachments = []
for p in posts:
    if p['post_type'] == "post":
        print(p['title'])
        blog_posts.append(p)
    elif p['post_type'] == "page":
        pages.append(p)
    elif  p['post_type'] == "attachment":
        attachments.append(p)

# print(blog_posts)
print(re.sub("(<!--.*?-->)", "", blog_posts[0]['content'], flags=re.DOTALL))