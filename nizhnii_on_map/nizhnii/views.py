from django.views.generic import TemplateView
from nizhnii import utils


class ShowMap(TemplateView):
    template_name = 'nizhnii/index.html'
    extra_context = {
        'map': utils.get_map()
    }
