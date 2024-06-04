from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm, QuoteForm
from .models import Author, Quote, Tag


# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    padinator = Paginator(list(quotes), per_page)
    quotes_on_page = padinator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = AuthorForm()
    return render(request, "quotes/add_author.html", context={"form": form})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_data = form.cleaned_data["quote"]
            author_id = form.cleaned_data["author"]
            tag_names = form.cleaned_data["tags"].split(",")

            author = Author.objects.get(fullname=author_id)

            tags = []
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name.strip())
                tags.append(tag)

            quote = Quote.objects.create(quote=quote_data, author=author)
            quote.tags.set(tags)

            return redirect("/")
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", context={"form": form})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "quotes/author_detail.html", context={"author": author})


def quotes_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    return render(
        request, "quotes/quotes_by_tag.html", context={"quotes": quotes, "tag": tag}
    )


@login_required
def delete_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        quote.delete()
        return redirect("/")
    return render(request, "quotes/quote_delete.html", {"quote": quote})


@login_required
def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect("/")
    return render(request, "quotes/author_delete.html", {"author": author})
