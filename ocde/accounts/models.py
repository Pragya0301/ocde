# imports
from django.db import models
from django.contrib.auth.models import User

"""! @brief Defines the app models."""
##
# @file models.py
#
# @brief Defines the app models.
#
# @section description_models Description
# Defines the django models for User, Folder, File and Code.
#
# @section notes_models Notes
# - Contains four code language choices : Python, C++, Java and Bash \n
# - Comments are Doxygen compatible.
#
# @section todo_sensors TODO
# - None.
#
# @section author_sensors Author(s)
# - Created by Pragya Baran and Purvi Poonia.

LANG_CHOICES = [
    ('Python','Python'),
    ('C++','C++'),
    ('Java','Java'),
    ('Bash','Bash')
]

class Folder(models.Model):
    """! Class representing folder.
    Defines Owner, Name, Language of folder and Date of creation of the folder."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    language = models.CharField(max_length=10, choices=LANG_CHOICES, default="c++")
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("text"),)
    def __str__(self):
        return self.text

class Submission(models.Model):
    """A class to represent the code submission object.
    Defines Folder , Name, Code, CLI arguments given with code, Input for stdin and Date of creation of the file.
    """
    file_name = models.CharField(max_length=200)
    code = models.TextField()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    CLI = models.BooleanField(default=False)
    CLI_args = models.TextField(blank=True)  #Check out if these have to limited in size, this represents the user input/testcases
    stdin = models.TextField(blank=True)  #Check out if these have to limited in size, this represents the user input/testcases
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'files'
        unique_together = (("file_name"),)
	

class Code(models.Model):
    """A class to represent the code submission object w/o saving option.
    Defines Code, Language, CLI arguments given with code and Input for stdin.
    """
    code = models.TextField()
    stdin = models.TextField(blank=True)  #Check out if these have to limited in size, this represents the user input/testcases
    language = models.CharField(max_length = 10, choices=LANG_CHOICES)
    CLI = models.BooleanField(default=False)
    CLI_args = models.TextField(blank=True)  #Check out if these have to limited in size, this represents the user input/testcases

