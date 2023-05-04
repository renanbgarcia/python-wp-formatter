from blog.models import Post
import json

posts = [
    {
        'title': 'Post 1',
        'date': '2022-05-01',
        'description': 'Description 1',
        'excerpt': 'Excerpt 1',
        'content': 'Content 1',
        'post_name': 'post-1',
        'status': 'published',
        'post_type': '',
        'attachment_url': ''
    },
    {
        'title': 'Post 2',
        'date': '2022-05-02',
        'description': 'Description 2',
        'excerpt': 'Excerpt 2',
        'content': 'Content 2',
        'post_name': 'post-2',
        'status': 'published',
        'post_type': '',
        'attachment_url': ''
    }
]

for post in posts:
    Post.objects.create(
        title=post['title'],
        date=post['date'],
        description=post['description'],
        excerpt=post['excerpt'],
        content=post['content'],
        post_name=post['post_name'],
        status=post['status'],
        post_type=post['post_type'],
        attachment_url=post['attachment_url']
    )