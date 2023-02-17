from wtforms import Form, DateField, BooleanField, StringField, PasswordField, validators
from wtforms import TextField
from wtforms.fields.html5 import TelField
#from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    username= StringField()
    #last_name= CharField(max_length=50, blank=True, null=True)
    #phone= CharField(max_length=12,blank=True, null=True)
    # mobile= CharField(max_length=12, blank=False, null=False)
    #email= EmailField(default=None, max_length=20, blank=False, null=False)
    #company= CharField(max_length=12, blank=True, null=True)
    #date= DateField(default=date.today)
    #notes= TextField(blank=True, null=True)