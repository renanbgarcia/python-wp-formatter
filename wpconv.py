import wpparser


data = wpparser.parse("./papapiu.WordPress.2023-05-03.xml")

# print(data['posts'][20])


pages = []
blog_posts = []
attachments = []
for p in data['posts']:
    if p['post_type'] == "post":
        print(p['title'])
        blog_posts.append(p)
    elif p['post_type'] == "page":
        pages.append(p)
    elif  p['post_type'] == "attachment":
        attachments.append(p)

# print(blog_posts)
print(blog_posts[0])