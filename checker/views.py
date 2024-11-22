from django.views import generic
from .models import Fileupload
from core.sip4dzip import Sip4dZipChecker
from sip4dzip.settings import MEDIA_ROOT, BASE_DIR

class FileuploadView(generic.CreateView):
    model = Fileupload
    fields = ['filefield']
    success_url = '/checker/result'
    template_name = 'checker/fileupload.html'

class ResultView(generic.ListView):
    model = Fileupload
    template_name = 'checker/result.html'
    context_object_name = 'result_messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file = MEDIA_ROOT / Fileupload.objects.last().filefield.name

        ck = Sip4dZipChecker()
        ck.template_root = BASE_DIR / "core/template"
        ck.Check(file)
        context['result'] = ck.result
        messages = ck.report.split("\n")
        reports = []
        for m in  messages:
            if m.find(u"[ERROR]") != -1:
                reports.append({"message": m, "color": "red"})
            elif m.find(u"[WARN]") != -1:
                reports.append({"message": m, "color": "orange"})
            else:
                reports.append({"message": m, "color": "black"})
        context['reports'] = reports
        return context
    
    
    def check_file(self, file):
        ck = Sip4dZipChecker()
        ck.Check(file)
        return ck.report