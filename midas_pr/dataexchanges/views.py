# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import MessageForm
from .models import Report


def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'dataexchanges/index.html', {'form': MessageForm()})
