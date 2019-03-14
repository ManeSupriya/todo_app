from django import forms
from . import models

class newtask(forms.ModelForm):
	class Meta:
		model = models.Schedule
		fields = ['title','start_time','end_time']

