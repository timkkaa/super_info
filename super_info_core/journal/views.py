from django.views import View

from django.views.generic import TemplateView

from journal.models import Publication, PublicationComment


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        publication = Publication.objects.all()

        paginator = Paginator(publication, 10)
        page_number = self.riquest.GET['page']
        page_number = self.riquest.GET.get()
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj
        }
        return context


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'


class AboutView(TemplateView):
    template_name = 'contact.html'


def post(request, **kwargs):
    publication_pk = kwargs['pk']

    publication = Publication.objects.get(id=publication_pk)

    commant_text = request.POST['comment_text']

    PublicationComment.objects.create(publication=publication, text=commant_text)
    #        bot.send_message(chat_id=1723863989, text='')
    return request('publication-detail.html', publication_pk),


class CreatePublicationCommentView(View):
    pass
