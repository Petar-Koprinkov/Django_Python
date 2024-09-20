from datetime import datetime

from django.shortcuts import render

# Create your views here.


def index(request):
    name = request.GET.get('name', '')

    return render(request, 'forum/base.html', {'name': name})


def dashboard(request):
    context = {
        "books": [
            {
                "title": "Under the yoke",
                "author": "Ivan Vazov",
                "content": "Under the Yoke, subtitled A Novel About the Life of the Bulgarians on the Eve of Liberation or A Romance of Bulgarian Liberty is a historical novel by Bulgarian author Ivan Vazov written from 1887 to 1888 and published in parts between 1889 and 1890 in a magazine The Collection of Folk Tales and in a single book in 1894.[2][3] It is set in a small town in Central Bulgaria during the months leading up to the April Uprising in 1876 and is the most famous piece of classic Bulgarian literature. Under the Yoke has been translated into more than 30 languages. The English translation was made in 1894 by William Morfill and published by the London publishing house William Heinemann.",
                "created_at": datetime.now(),
            },
            {
                "title": "Mowers",
                "author": "Elin Pelin",
                "content": "He was born in the village of Bailovo, in Sofia District. He completed his primary education, but not his secondary education. Studying to become a teacher, he taught for a year in 1895 in his native village. He went to Sofia some time after that, and from 1898 to 1900 returned to live in Bailovo. He was first published in 1901, and the respect it earned him in literary circles encouraged him to go to Sofia in 1903, where he worked as a librarian at the Sofia University library and national library of Bulgaria from 1904. From 1922 he was a curator of the Ivan Vazov museum. His name was derived from a Bulgarian folksong. He spent 1904–05 in France, and made trips to Italy and Russia in 1906 and 1913. Most of his life was spent in Sofia.",
                "created_at": datetime.now(),
            },
            {
                "title": "Saying Goodbye",
                "author": "Hristo Botev",
                "content": "Hristo Botev, born Hristo Botyov Petkov was a Bulgarian revolutionary and poet. Botev is considered by Bulgarians to be a symbolic historical figure and national hero. His poetry is a prime example of the literature of the Bulgarian National Revival, though he is considered to be ahead of his contemporaries in his political, philosophical, and aesthetic views.",
                "created_at": datetime.now(),
            },
        ]
    }
    return render(request, 'forum/dashboard.html', context)
