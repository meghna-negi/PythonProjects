#Class to initialize the posts in the blog
class Post:
    def __init__(self,id,title,subtitle,body) -> None:
        self.post_id = id
        self.post_title = title
        self.post_subtitle = subtitle
        self.post_body = body