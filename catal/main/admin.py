from django.contrib import admin
from .models import *

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# РЕДАКТОР В АДМИНКЕ
class PagePriceAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент' , widget=CKEditorUploadingWidget())
    class Meta:
        model = PagePrice
        fields = '__all__'



# СТРАНИЦА - ГЛАВНАЯ #################################
@admin.register(PageHome)
class PageHomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'main_offer')
    list_display_links = ('title', 'description', 'main_offer')

# БЛОК - ПРИНИМАЕМ НА УТИЛИЗАЦИЮ
@admin.register(BlockMaterialPageHome)
class BlockMaterialPageHomeAdmin(admin.ModelAdmin):
    list_display = ('material_title', 'material_price', 'material_text')
    list_display_links = ('material_title', 'material_price', 'material_text')

# БЛОК - ГАРАНТИИ
@admin.register(BlockGuaranteesPageHome)
class BlockGuaranteesPageHomeAdmin(admin.ModelAdmin):
    list_display = ('guarantees_title', 'guarantees_text')
    list_display_links = ('guarantees_title', 'guarantees_text')

# БЛОК - ОТЗЫВЫ
@admin.register(BlockReviewsPageHome)
class BlockReviewsPageHomeAdmin(admin.ModelAdmin):
    list_display = ('review_name', 'review_date', 'review_text')
    list_display_links = ('review_name', 'review_date', 'review_text')

# БЛОК - ПРОЦЕСС СДАЧИ КАТАЛИЗАТОРА
@admin.register(BlockProcessPageHome)
class BlockProcessPageHomeAdmin(admin.ModelAdmin):
    list_display = ('process_title', 'process_step')
    list_display_links = ('process_title', 'process_step')

# БЛОК - КАТАЛИЗАТОРЫ ПО МАРКАМ
@admin.register(BlockListCatalystsPageHome)
class BlockListCatalystsPageHomeAdmin(admin.ModelAdmin):
    list_display = ('list_brand', 'list_price')
    list_display_links = ('list_brand', 'list_price')
    search_fields = ('list_brand',)
    
# БЛОК - ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ
@admin.register(BlockFaqPageHome)
class BlockFaqPageHomeAdmin(admin.ModelAdmin):
    list_display = ('faq_question', 'faq_answer')
    list_display_links = ('faq_question', 'faq_answer')




# СТРАНИЦА - КАТАЛОГ #################################

# РЕДАКТОР В АДМИНКЕ ДЛЯ КАТАЛОГА
class PageCatalogAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент' , widget=CKEditorUploadingWidget())
    class Meta:
        model = PageCatalog
        fields = '__all__'

@admin.register(PageCatalog)
class PageCatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'header_h1')
    list_display_links = ('title', 'description', 'header_h1')
    form = PageCatalogAdminForm

# КАТАЛИЗАТОР
@admin.register(Catalysts)
class CatalystsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year_release', 'type_motor', 'engine_volume')
    list_display_links = ('brand', 'model')
    list_filter = ('brand','model')
    search_fields = ('brand','model',)
    prepopulated_fields = {"slug": ("header_h1",)}
    save_as = True




# СТРАНИЦА - КАЛЬКУЛЯТОР #############################

# РЕДАКТОР В АДМИНКЕ ДЛЯ СТАТЬИ
class PageCalculatorAdminForm(forms.ModelForm):
    content = forms.CharField(label='Основной контент' , widget=CKEditorUploadingWidget())
    class Meta:
        model = PageCalculator
        fields = '__all__'

@admin.register(PageCalculator)
class PageCalculatorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    form = PageCalculatorAdminForm




# СТРАНИЦА - БИРЖА ###################################
@admin.register(PageStock)
class PageStockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')

# ONLINE КОТИРОВКИ
@admin.register(OnlinePrice)
class OnlinePriceAdmin(admin.ModelAdmin):
    list_display = ('update', 'pt_price_bid', 'pd_price_bid', 'rh_price_bid')
    fieldsets = (
        (None, {
            'fields': (('update'),)
        }),
        ('Платина', {
            'classes': (('collapse'),),
            'fields': (('pt_price_bid', 'pt_price_ask', 'pt_change', 'pt_change_num'),)
        }),
        ('Палладий', {
            'classes': (('collapse'),),
            'fields': (('pd_price_bid', 'pd_price_ask', 'pd_change', 'pd_change_num'),)
        }),
        ('Родий', {
            'classes': (('collapse'),),
            'fields': (('rh_price_bid', 'rh_price_ask', 'rh_change', 'rh_change_num'),)
        }),
    )

# FIX КОТИРОВКИ
@admin.register(FixPrice)
class FixPriceAdmin(admin.ModelAdmin):
    list_display = ('fix_today_date', 'fix_1_date', 'fix_2_date')




# СТРАНИЦА - ЦЕНЫ ####################################
@admin.register(PagePrice)
class PagePriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')
    form = PagePriceAdminForm

# ТАБЛИЦА ЦЕН
@admin.register(PriceTable)
class PriceTableAdmin(admin.ModelAdmin):
    list_display = ('auto', 'price')
    list_display_links = ('auto', 'price')
    save_as = True




# СТРАНИЦА - БЛОГ ####################################
@admin.register(PageBlog)
class PageBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')

# РЕДАКТОР В АДМИНКЕ ДЛЯ СТАТЬИ
class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(label='Содержание статьи' , widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

# СТАТЬЯ
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'header', 'date', 'published')
    list_display_links = ('title', 'description', 'header')
    search_fields = ('header',)
    list_editable = ('published',)
    list_filter = ('date', 'published')
    prepopulated_fields = {"slug": ("header",)}
    form = ArticleAdminForm
    save_as = True




# СТРАНИЦА - КОНТАКТЫ ################################
@admin.register(PageContacts)
class PageContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')

# ГОРОД
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('office', 'city_name', 'manager_name', 'phone', 'get_image')
    list_display_links = ('office', 'city_name', 'manager_name', 'phone')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.manager_photo.url} width="50" height="50"')
    
    get_image.short_description = 'Фото'



admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'AUTOKAT_GROUP'