#-*- encoding=UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here

class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_user')
    title = models.CharField('title', max_length=100)
    text = models.TextField('post')
    pub_date = models.DateTimeField('date published')
    image = models.ImageField('image',upload_to='blog', blank=True)
    # return title
    def get_title(self):
	return self.title
    # get 200 symbol description saving words
    def get_description(self):
        if len(self.text) < 201:
            return self.text
        else:
            cut = self.text[:201]
            while cut[len(cut)-1]!=' ':
                cut = cut[:len(cut)-1]
            return cut[:len(cut)-1]
    # show fulltext if text length > 200
    def show_full_text(self):
        showText = True if len(self.text) > 200 else False
        return showText
    # get text
    def get_text(self):
        return self.text
    # return pub_date
    def get_pub_date(self):
	return self.pub_date.strftime("%a, %d %b %Y")
    def __unicode__(self):
	return self.title
	
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body))

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("dbe.blog.views.post", args=[pk]))