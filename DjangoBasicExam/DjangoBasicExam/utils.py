from DjangoBasicExam.authors.models import Author
from DjangoBasicExam.posts.models import Post


def get_profile():
    return Author.objects.first()


def get_latest_post():
    return Post.objects.order_by('-updated_at').first()


def get_all_posts():
    return Post.objects.all()
