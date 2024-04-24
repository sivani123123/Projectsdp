from django.shortcuts import render, get_object_or_404, redirect
from .models import Prediction
from .forms import PredictionForm


def prediction_list(request):
    predictions = Prediction.objects.all()
    return render(request, 'crud_app/prediction_list.html', {'predictions': predictions})


def prediction_detail(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    return render(request, 'astrology/prediction_detail.html', {'prediction': prediction})


def prediction_create(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save()
            return redirect('astrology:prediction_detail', pk=prediction.pk)
    else:
        form = PredictionForm()
    return render(request, 'astrology/prediction_form.html', {'form': form})


def prediction_edit(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    if request.method == 'POST':
        form = PredictionForm(request.POST, instance=prediction)
        if form.is_valid():
            prediction = form.save()
            return redirect('astrology:prediction_detail', pk=prediction.pk)
    else:
        form = PredictionForm(instance=prediction)
    return render(request, 'astrology/prediction_form.html', {'form': form})


def prediction_delete(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    if request.method == 'POST':
        prediction.delete()
        return redirect('astrology:prediction_list')
    return render(request, 'astrology/prediction_confirm_delete.html', {'prediction': prediction})
