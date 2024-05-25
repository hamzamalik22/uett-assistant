from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .forms import *
from .models import *

# Create your views here.

def generate_pdf(request):
    if request.method == 'POST':
        form = TitlePageForm(request.POST)
        if form.is_valid():
            title_page_data = form.cleaned_data
            unique_filename = f"TitlePage_{title_page_data['title']}_{title_page_data['course']}.pdf"
            html_template = render_to_string('titlepage/title_page.html', {'title_page': title_page_data})
            pdf_file = HTML(string=html_template).write_pdf()
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{unique_filename}"'
            return response
    else:
        form = TitlePageForm()
    return render(request, 'titlepage/title_page_form.html', {'form': form,'title' : 'Title Page'})