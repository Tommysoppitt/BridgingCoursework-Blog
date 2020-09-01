from django import forms
from .models import Post
from .models import Skill
from .models import Responsibility
from .models import Experience
from .models import Hobby

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('skill', 'detail',)
class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('experience', 'detail',)

class HobbyForm(forms.ModelForm):

    class Meta:
        model = Hobby
        fields = ('hobby', 'detail',)

class ResponsibilityForm(forms.ModelForm):

    class Meta:
        model = Responsibility
        fields = ('responsibility', 'detail',)