class Post:
    def __init__(self, account_id, date, likes, dislikes, post_type):
        self.account_id = account_id
        self.date = date
        self.likes = likes
        self.dislikes = dislikes
        self.post_type = post_type

class Account:
    def __init__(self, account_id, account_name):
        self.account_id = account_id
        self.account_name = account_name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)