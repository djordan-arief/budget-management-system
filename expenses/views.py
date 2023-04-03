from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense, Category
from .forms import ExpenseForm

# Create your views here.
@login_required
def index(request):
    all_expenses = Expense.objects.all().filter(owner=request.user)
    return render(request, 'expense/index.html', {'expenses': all_expenses})

@login_required
def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Expense removed')
    return redirect('expenses')

@login_required
def update_expense(request, id):
    expense = get_object_or_404(Expense, pk=id)
    categories = Category.objects.all()

    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {'form': form, 'categories': categories}
        return render(request, 'expenses/update_expense.html', context)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
            messages.success(request, 'Expense updated successfully')
            return redirect('expenses')
        else:
            messages.error(request, 'Please correct the errors below')
            context = {'form': form, 'categories': categories}
            return render(request, 'expense/update-expense.html', context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False) 
            expense.owner = request.user 
            expense.save() 
            messages.success(request, 'Expense added successfully')
            return redirect('expenses')
        else:
            messages.error(request, 'Invalid informations')
    else:
        form = ExpenseForm()
    return render(request, 'expense/add_expense.html', {'form': form})

