# imports
from django import forms  #https://youtu.be/6oOHlcHkX2U
from .models import Submission, Folder, Code

"""! @brief Defines the app forms."""
##
# @file forms.py
#
# @brief Defines the app forms.
#
# @section description_forms Description
# Defines the django forms for Folder, File and Code.
#
# @section todo_sensors TODO
# - None.
#
# @section author_sensors Author(s)
# - Created by Pragya Baran and Purvi Poonia.

class SubmissionForm(forms.ModelForm):
    """! Class representing the submission form for file.
    Field are : File name, Code, Command Line Input arguments and Code Output.
    """
    class Meta:
        model = Submission
        fields = [
                  'file_name',
                  'code',
                  
                  'CLI_args',
                  'file_name',
                  'stdin'
                  ]
        widgets = {
        'file_name' : forms.Textarea(attrs={'class': 'form-control InputStyle file', 'id':'filename', 'rows':'2', 'cols': '50'}),
            'code': forms.Textarea(attrs={'class': 'form-control', 'id':'code', 'placeholder':'Write your Code here', 'rows': '16', 'cols':'120'}),
            
            'CLI_args': forms.Textarea(attrs={'rows':'2', 'cols': '50', 'id':'CLI_args'}),
            'stdin': forms.Textarea(attrs={'rows':'2', 'cols': '50', 'id':'stdin'}),
        }

class CodeForm(forms.ModelForm):
    """! Class representing the submission form for code w/o saving it as a file.
    Field are : Code, Language of code, Command Line Input arguments, Input for stdin and Code output.
    """
    class Meta:
        model = Code
        fields = ['code',
                  'language',
                  
                  'stdin',
                  'CLI_args']

        widgets = {
            'code': forms.Textarea(attrs={'class': 'form-control', 'id':'code', 'placeholder':'Write your Code here', 'rows': '16', 'cols':'120'}),
            'language': forms.Select(),
            
            'CLI_args': forms.Textarea(attrs={'rows':'3', 'cols': '50', 'id':'CLI'}),
            'stdin': forms.Textarea(attrs={'rows':'3', 'cols': '50', 'id':'stdin'}),
        }

class FolderForm(forms.ModelForm):
    """! Class representing the form for creating folder.
    Field are : Folder name and Language.
    """
    class Meta:
        model = Folder
        fields = ['text', 'language']
        labels = {'text':'Name'}
        widgets = {
                  'language': forms.Select()}
