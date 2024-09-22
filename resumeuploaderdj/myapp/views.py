from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume
from django.views import View
from .models import Candidate

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'myapp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'myapp/home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})

def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == "POST":
        candidate.delete()
        return redirect('home')  # Redirect to home after deletion
    return render(request, 'delete_confirm.html', {'candidate': candidate})
