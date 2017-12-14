from math import ceil
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from blog.models import Articles, Comments
from blog.forms import NewArticle, NewComment, EditArticle


def list_view(request, page = 1):
    page = int(page) - 1
    ITEMS_ON_PAGE = 10
    firstitem = int(page*ITEMS_ON_PAGE)
    last_item = firstitem+ITEMS_ON_PAGE
    all_items = Articles.objects.all().order_by('-id')
    maxpage = int(ceil(len(all_items)/ITEMS_ON_PAGE) + 1)
    if all_items.count() == 0:
        maxpage += 1
    items = all_items[firstitem:last_item]

    return render(request, 'blog/list_view.html', {
        'articles' : items,
        'title' : 'Kaktys\'s blog',
        'auth': request.user.is_authenticated,
        'username': request.user.username,
        'pages' : list(range(1,maxpage)),
        'cur_page' : page + 1,
        'maxpage' : maxpage - 1,
        'next_page' : page + 2,
        'prev_page' : page,
    })


def delete_view(request,article_id):
    if request.method == 'POST':
        article = get_object_or_404(Articles, id = article_id)
        Articles.objects.filter(id=article.id).delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Bad request')


def create_new_article(request):
    if request.method == 'POST':
        form = NewArticle(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(form)
    else:
        form = NewArticle()

        return render(request, 'blog/create_article.html', {
            'form' : form,
            'title' : 'Создание новой записи',
            'user' : request.user.username,
            'auth': request.user.is_authenticated,
        })


def article_view(request, article_id):
    item = get_object_or_404(Articles, id=article_id)
    comments = Comments.objects.all().filter(article_id=article_id)
    form = NewComment()
    if request.user.is_authenticated: username = request.user.username
    else: username = 'Анонимный пользоатель'

    return render(request, 'blog/article.html',{
        'item' : item,
        'title' : item.name,
        'comments': comments,
        'form' : form,
        'username': username,
        'auth' : request.user.is_authenticated,
    })


def create_new_comment(request, article_id):
    if request.method == 'POST':
        form = NewComment(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            article = get_object_or_404(Articles, id=article_id)
            comment.article_id = article
            if request.user.is_authenticated :
                comment.user = request.user.username
            else:
                comment.user = 'Неизвестный пользователь'
            comment.save()
            return HttpResponseRedirect('/article/' + article_id)


def update_view(request,article_id):
    article = get_object_or_404(Articles, id=article_id)
    if request.method == 'POST':
        form = EditArticle(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            return HttpResponse('Bad request')
    else:
        form = EditArticle(instance=article)
        return render(request, 'blog/edit.html', {
            'form' : form,
            'auth': request.user.is_authenticated,
        })
