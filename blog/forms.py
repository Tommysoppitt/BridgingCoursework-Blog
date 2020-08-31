
from django import forms
from .models import Post
from .models import Skill
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('skill', 'detail',)
