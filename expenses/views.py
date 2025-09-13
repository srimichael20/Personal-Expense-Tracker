from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

def index(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all().order_by('-date')

    total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    # Category Summary
    category_summary = list(
        expenses.values('category').annotate(total=Sum('amount'))
    )

    # Time Summary
    time_summary = list(
        expenses.values('date').annotate(total=Sum('amount')).order_by('date')
    )

    context = {
        'form': form,
        'expenses': expenses,
        'total_spent': total_spent,
        'category_summary': category_summary,
        'time_summary': time_summary,
    }
    return render(request, 'expenses/index.html', context)
