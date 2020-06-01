# from django.http import HttpResponseRedirect
# from django.shortcuts import  render
# from django.urls import reverse
# from django.utils import timezone
from .models import Article
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        """Return the last five published articles."""
        return Article.objects.filter(status=1).order_by('-pub_date')[:5]

def ArticleView(request, slug):
    template_name = 'blog/detail.html'
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter()
    new_comment = None

     # Comment posted   
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'article': article,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

    # def get_queryset(self):
    #     """
    #     Excludes any articles that aren't published yet.
    #     """
    #     return Article.objects.filter(pub_date__lte=timezone.now())

class WhoamiView(generic.TemplateView):
    template_name = 'blog/whoami.html'
