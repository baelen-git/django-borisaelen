# from django.http import HttpResponseRedirect
# from django.shortcuts import  render
# from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        """Return the last five published articles."""
        return Article.objects.filter(status=1).order_by('-pub_date')[:5]

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """
        Excludes any articles that aren't published yet.
        """
        return Article.objects.filter(pub_date__lte=timezone.now())


class WhoamiView(generic.TemplateView):
    template_name = 'blog/whoami.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
