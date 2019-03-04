from app.models import Comment, User,Blog
from app import db
import unittest
class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'James', password = 'banana', email = 'james12@gmail.com')
        self.new_blog = Blog(id = 123, blog_title = 'Blog', blog_content = 'Blog content',category = 'general')

    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_blog.blog_title,'Blog')
        self.assertEquals(self.new_blog.blog_content,'Blog content')
        self.assertEquals(self.new_blog.category,"success")

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        pitch = Blog.get_blog(123)
        self.assertTrue(blog is not None)
