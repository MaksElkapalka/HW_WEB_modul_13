from django.forms import (
    CharField,
    ModelChoiceField,
    ModelForm,
    Select,
    Textarea,
    TextInput,
)

from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(
        max_length=60,
        min_length=3,
        widget=TextInput(attrs={"class": "form-control "}),
    )
    born_date = CharField(
        max_length=60,
        min_length=6,
        widget=TextInput(attrs={"class": "form-control "}),
    )
    born_location = CharField(
        max_length=150,
        widget=TextInput(attrs={"class": "form-control "}),
    )
    description = CharField(
        widget=Textarea(attrs={"class": "form-control "}),
    )

    class Meta:
        model = Author
        fields = ("fullname", "born_date", "born_location", "description")


class TagForm(ModelForm):
    name = CharField(
        max_length=40,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Tag
        fields = ("name",)


class QuoteForm(ModelForm):
    quote = CharField(
        min_length=30,
        widget=Textarea(attrs={"class": "form-control"}),
    )
    tags = CharField(
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    author = ModelChoiceField(
        queryset=Author.objects.all(),
        widget=Select(attrs={"class": "form-control"}),
        to_field_name="fullname",
    )

    class Meta:
        model = Quote
        fields = ("quote", "tags", "author")
