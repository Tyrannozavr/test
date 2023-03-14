from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic import *
from .models import *
from django.core.paginator import Paginator




# СТРАНИЦА - ГЛАВНАЯ
def home(request):
    context = {
        'title': PageHome.objects.get(pk=1),
        'description': PageHome.objects.get(pk=1),
        'header_h1': PageHome.objects.get(pk=1),
        'home': PageHome.objects.all(),
        'material': BlockMaterialPageHome.objects.select_related().all(),
        'guarantees': BlockGuaranteesPageHome.objects.all(),
        'reviews': BlockReviewsPageHome.objects.all(),
        'process': BlockProcessPageHome.objects.all(),
        'list_catalysts': BlockListCatalystsPageHome.objects.all(),
        'faq': BlockFaqPageHome.objects.all(),
    }
    return render(request, 'main/home.html', context=context)






class PageCatalogMeta:
    def get_catalog_meta(self):
        context = {
            'title': PageCatalog.objects.get(pk=1),
            'description': PageCatalog.objects.get(pk=1),
            'header_h1': PageCatalog.objects.get(pk=1),
            'content': PageCatalog.objects.get(pk=1),
        }
        return context



from time import time
# СТРАНИЦА - КАТАЛОГ
class CatalogListView(PageCatalogMeta, ListView):
    model = Catalysts
    template_name = 'main/catalog.html'
    context = 'context'
    extra_context = {'now': time()}
# class CatalogView(PageCatalogMeta, View):

#     def get(self, request):
#         title = PageCatalog.objects.get(pk=1)
#         description = PageCatalog.objects.get(pk=1)
#         #header_h1 = PageCatalog.objects.get(pk=1)
#         content = PageCatalog.objects.get(pk=1)
#         catalysts = Catalysts.objects.all()
#         return render(request, 'main/catalog.html', {
#             'title': title,
#             'description': description,
#             #'header_h1': header_h1,
#             'content': content,
#             'catalog_list': catalysts
#             })
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page'] = PageCatalog.objects.all()
    #     return context










# КАТАЛИЗАТОР
def show_catalyst(request, catalyst_slug):
    catalyst = get_object_or_404('Catalysts', slug=catalyst_slug)
    context = {
        'catalyst': catalyst,
    }

    return render(request, 'main/product.html', context=context)




# СТРАНИЦА - КАЛЬКУЛЯТОР
def calculator(request):
    context = {
        'title': PageCalculator.objects.get(pk=1),
        'description': PageCalculator.objects.get(pk=1),
        'header_h1': PageCalculator.objects.get(pk=1),
        'calculator': PageCalculator.objects.all(),
    }
    return render(request, 'main/calculator.html', context=context)



# СТРАНИЦА - БИРЖА
def stock(request):
    context = {
        'title': PageStock.objects.get(pk=1),
        'description': PageStock.objects.get(pk=1),
        'header_h1': PageStock.objects.get(pk=1),
        'stock': PageStock.objects.all(),
        'online': OnlinePrice.objects.all(),
        'fixprice': FixPrice.objects.all(),
    }
    return render(request, 'main/stock.html', context=context)



# СТРАНИЦА - ЦЕНЫ
def price(request):
    context = {
        'title': PagePrice.objects.get(pk=1),
        'description': PagePrice.objects.get(pk=1),
        'header_h1': PagePrice.objects.get(pk=1),
        'content': PagePrice.objects.get(pk=1),
        'pricetable': PriceTable.objects.all(), 
    }
    return render(request, 'main/price.html', context=context)


# СТРАНИЦА - БЛОГ
def blog(request):
    blog_list = Article.objects.all()
    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': PageBlog.objects.get(pk=1),
        'description': PageBlog.objects.get(pk=1),
        'header_h1': PageBlog.objects.get(pk=1),
        'page_obj': page_obj,
    }
    return render(request, 'main/blog.html', context=context)




# СТАТЬЯ
def show_post(request, post_slug):
    post = get_object_or_404(Article, slug=post_slug)
    post.description = {
        'description': post.description,
    }
    context = {
        'post': post,
        'title': post.title,
        'description': post.description,
    }
    return render(request, 'main/article.html', context=context)



# СТРАНИЦА - КОНТАКТЫ
def contacts(request):
    context = {
        'title': PageContacts.objects.get(pk=1),
        'description': PageContacts.objects.get(pk=1),
        'header_h1': PageContacts.objects.get(pk=1),
        'city': City.objects.all(),
    }
    return render(request, 'main/contacts.html', context=context)




# СТРАНИЦА 404
def pageNotFound(request, exception):
  return HttpResponseNotFound('<h1>Страница не найдена - 404</h1>')


# брэнды для поиска
def brand_list(request):
    brands = BrandAuto.objects.all().values_list('brand')
    brands = [i[0] for i in brands]
    # print(brands, type(brands))
    return JsonResponse({'list': brands})
