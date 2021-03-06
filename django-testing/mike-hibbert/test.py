from fileinput import filename
from django.test import TestCase
from models import Article, get_upload_file_name
from django.utils import timezone
from time import time

from django.shortcuts import reverse

class ArticleTest(TestCase):

    def create_article(self, title="test article", body="Kaza mwendo bila kuchoka"):
        return Article.objects.create(title=title,
                                    body=body,
                                    pub_date=timezone.now(),
                                    likes=0)

    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__unicode__(). a.title)

    def test_get_upload_file_name(self):
        filename = 'Cheese.txt'
        path = "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
        created_path = get_upload_file_name(self, filename)
        self.assertEqual(path, created_path)

    def test_articles_list_view(self):
        a = self.create_article()
        url = reverse('article.views.articles')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(a.title, resp.content)


    def test_article_detail_views(self):
        a = self.create_article()
        url = reverse('article.views.article', args=[a.id])
        resp = self.client.get(url)

        self.assertEqual(reverse('article.views.article', args=[a.id]), a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(a.title, resp.content)
        
