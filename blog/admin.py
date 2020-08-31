from django.contrib import admin
from .models import Post
from .models import Skill
from .models import Responsibility
from .models import Hobby
from .models import Experience
admin.site.register(Post)
admin.site.register(Skill)
admin.site.register(Responsibility)
admin.site.register(Hobby)
admin.site.register(Experience)