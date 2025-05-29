from django import forms


class AttendanceForm(forms.Form):
    total_classes = forms.IntegerField(label='Total Classes Conducted')
    classes_attended = forms.IntegerField(label='Total Classes Attended')
    target_percentage = forms.IntegerField(label='Target Attendance Percentage', initial=75)
    
