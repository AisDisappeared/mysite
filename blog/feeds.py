from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post


class LatestEntriesFeed(Feed):
    title = "blog latest posts"
    link = "/rss/feed"
    description = "best blog ever"

    def items(self):
        return post.objects.filter(status=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:80]
