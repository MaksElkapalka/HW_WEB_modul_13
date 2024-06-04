from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
)


# Create your models here.
class Author(Model):
    fullname = CharField(max_length=60)
    born_date = CharField(max_length=60)
    born_location = CharField(max_length=150)
    description = TextField()

    def __str__(self):
        return self.fullname


class Tag(Model):
    name = CharField(max_length=40, null=False, unique=True)

    def __str__(self):
        return self.name


class Quote(Model):
    quote = TextField()
    tags = ManyToManyField(Tag)
    author = ForeignKey(Author, on_delete=CASCADE, default=None, null=True)
