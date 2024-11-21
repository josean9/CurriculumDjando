# CurriculumDjando

https://github.com/josean9/CurriculumDjando.git

pipenv run python manage.py runserver
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py shell
from blog.models import Post
Post.objects.all()
Post.objects.first()
Post.objects.last()
Post.objects.get(id=1)
post = Post.objects.create(
    title="Otra entrada", content="Texto de prueba")
post
post.entrada
post.title = "Otro título diferente"
post.save()
post.delete()
quit()
