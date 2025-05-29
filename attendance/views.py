from django.shortcuts import render
from .forms import AttendanceForm


def calculate_attendance(request):
    result = None
    current_percentage = None  # Define it before use

    if request.method == 'POST':
        form = AttendanceForm(request.POST)

        if form.is_valid():
            total_classes = form.cleaned_data['total_classes']
            classes_attended = form.cleaned_data['classes_attended']
            target_percentage = form.cleaned_data['target_percentage']

            if total_classes > 0:
                current_percentage = (classes_attended / total_classes) * 100

                if current_percentage >= target_percentage:
                    result = f"Your current attendance is {current_percentage:.2f}%. You already meet the target."
                else:
                    required = ((target_percentage * total_classes) - (classes_attended * 100)) / (100 - target_percentage)
                    required = int(required) + (1 if required % 1 > 0 else 0)  # Round up
                    result = f"You need to attend at least {required} more class(es) to reach {target_percentage}% attendance."
            else:
                result = "Total classes must be greater than 0."
    else:
        form = AttendanceForm()

    return render(request, 'attendance/index.html', {'form': form, 'result': result, 'current_percentage': current_percentage})
