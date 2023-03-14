from django.db import models
from django.urls import reverse




# СТРАНИЦА - ГЛАВНАЯ #########################################################
class PageHome(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    main_offer = models.CharField(max_length=255, help_text='Максимум 255 символов', verbose_name='Уникальное торговое предложение')
    main_suboffer = models.TextField(max_length=400, help_text='Максимум 400 символов', verbose_name='Три главных преимущества')
    material_h2 = models.CharField(max_length=300, blank=True, help_text='Максимум 300 символов', verbose_name='Заголовок блока - Принимаемые катализаторы')
    guarantees_h2 = models.CharField(max_length=300, blank=True, help_text='Максимум 300 символов', verbose_name='Заголовок блока - Гарантии')
    about_h2 = models.CharField(max_length=255, help_text='Максимум 255 символов', verbose_name='Заголовок блока - О компании')
    about_image = models.ImageField(upload_to='media/home', verbose_name='Изображение для блока - О компании')
    about_text = models.TextField(max_length=2000, help_text='Максимум 2000 символов', verbose_name='Информация о компании')
    gallery_image_1 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 1 для блока - Галерея')
    gallery_image_2 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 2 для блока - Галерея')
    gallery_image_3 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 3 для блока - Галерея')
    gallery_image_4 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 4 для блока - Галерея')
    gallery_image_5 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 5 для блока - Галерея')
    gallery_image_6 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 6 для блока - Галерея')
    gallery_image_7 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 7 для блока - Галерея')
    gallery_image_8 = models.ImageField(upload_to='media/home/gallery', verbose_name='Изображение 8 для блока - Галерея')
    advantages_title_1 = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Заголовок преимущества 1')
    advantages_text_1 = models.TextField(max_length=500, help_text='Максимум 500 символов', verbose_name='Текст преимущества 1')
    advantages_title_2 = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Заголовок преимущества 2')
    advantages_text_2 = models.TextField(max_length=500, help_text='Максимум 500 символов', verbose_name='Текст преимущества 2')
    advantages_title_3 = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Заголовок преимущества 3')
    advantages_text_3 = models.TextField(max_length=500, help_text='Максимум 500 символов', verbose_name='Текст преимущества 3')
    advantages_title_4 = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Заголовок преимущества 4')
    advantages_text_4 = models.TextField(max_length=500, help_text='Максимум 500 символов', verbose_name='Текст преимущества 4')
    seo_h2 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок SEO текста')
    seo_video = models.URLField(max_length=250, help_text='Ссылка с youtube', verbose_name='Ссылка на видео')
    seo_text = models.TextField(max_length=3000, help_text='Максимум 3000 символов', verbose_name='SEO текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница - Главная'
        verbose_name_plural = 'Страница - Главная'

# БЛОК - ПРИНИМАЕМ НА УТИЛИЗАЦИЮ
class BlockMaterialPageHome(models.Model):
    material_title = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Тип катализатора')
    material_price = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Диапазон цен катализатора')
    material_text = models.CharField(max_length=255, help_text='Максимум 255 символов', verbose_name='Краткое описание')
    material_css = models.CharField(max_length=20, blank=True, help_text='Максимум 20 символов', verbose_name='Класс CSS')

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'Главная - материалы'

# БЛОК - ГАРАНТИИ
class BlockGuaranteesPageHome(models.Model):
    guarantees_title = models.CharField(max_length=50, help_text='Максимум 50 символов', verbose_name='Гарантия')
    guarantees_text = models.CharField(max_length=255, help_text='Максимум 255 символов', verbose_name='Краткое описание гарантии')
    guarantees_css = models.CharField(max_length=25, blank=True, help_text='Максимум 25 символов', verbose_name='Класс CSS для иконки')

    class Meta:
        verbose_name = 'гарантию'
        verbose_name_plural = 'Главная - гарантии'

# БЛОК - ОТЗЫВЫ
class BlockReviewsPageHome(models.Model):
    review_image = models.ImageField(upload_to='media/home/reviews', verbose_name='Аватарка клиента')
    review_name = models.CharField(max_length=70, help_text='Максимум 70 символов', verbose_name='ФИО клиента')
    review_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата отзыва')
    review_text = models.TextField(max_length=500, help_text='Максимум 500 символов', verbose_name='Текст отзыва')
    review_link = models.URLField(max_length=255, blank=True, help_text='Максимум 255 символов', verbose_name='Ссылка на отзыв на Яндексе или Авито')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Главная - отзывы'

# БЛОК - ПРОЦЕСС СДАЧИ КАТАЛИЗАТОРА
class BlockProcessPageHome(models.Model):
    process_title = models.CharField(max_length=100, help_text='Максимум 100 символов', verbose_name='Заголовок процесса')
    process_step = models.CharField(max_length=3, help_text='Например 1/4', verbose_name='Номер шага')
    process_text = models.TextField(max_length=700, help_text='Максимум 700 символов', verbose_name='Текст процесса')
    process_image = models.ImageField(upload_to='media/home/process', blank=True, verbose_name='Изображение процесса')
    process_css = models.CharField(max_length=20, blank=True, help_text='Например work__img-1,2,3 и т.д.', verbose_name='Класс CSS')

    class Meta:
        verbose_name = 'процесс'
        verbose_name_plural = 'Главная - процесс'
        ordering = ['id']

# БЛОК - КАТАЛИЗАТОРЫ ПО МАРКАМ
class BlockListCatalystsPageHome(models.Model):
    list_image = models.ImageField(upload_to='media/home/list', verbose_name='Логотип марки')
    list_alt_image = models.CharField(max_length=20, blank=True, help_text='Максимум 50 символов', verbose_name='Тег alt для логотипа')
    list_brand = models.CharField(max_length=20, help_text='Максимум 50 символов', verbose_name='Наименование марки')
    list_price = models.CharField(max_length=40, help_text='Максимум 40 символов', verbose_name='Диапазон цен')
    list_link = models.CharField(max_length=50, blank=True, verbose_name='Ссылка на страницу марки')

    class Meta:
        verbose_name = 'марку авто'
        verbose_name_plural = 'Главная - марки авто'

# БЛОК - ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ
class BlockFaqPageHome(models.Model):
    faq_question = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Вопрос')
    faq_answer = models.TextField(max_length=1000, help_text='Максимум 1000 символов', verbose_name='Ответ')

    class Meta:
        verbose_name = 'ответ на вопрос'
        verbose_name_plural = 'Главная - FAQ'


    

# СТРАНИЦА - КАТАЛОГ #########################################################
class PageCatalog(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')
    content = models.TextField(max_length=3500, help_text='Максимум 3500 символов', verbose_name='Контент')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница - Каталог'
        verbose_name_plural = 'Страница - Каталог'

# ТИПЫ ДВИГАТЕЛЕЙ
class TypeOfMotor(models.Model):
    type_motor = models.CharField(max_length=20, verbose_name='Тип двигателя')

    def __str__(self):
        return self.type_motor

# ВИДЫ ОБЪЕМОВ ДВИГАТЕЛЕЙ
class EngineVolume(models.Model):
    volume = models.FloatField(verbose_name='Объем двигателя')

    # def __str__(self):
    #     return self.volume

# ГОДА ВЫПУСКА
class YearRelease(models.Model):
    year = models.CharField(max_length=4, verbose_name='Год выпуска')

    def __str__(self):
        return self.year

# МАРКИ АВТО
class BrandAuto(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Производитель')

    def __str__(self):
        return self.brand

# МОДЕЛИ АВТО
class ModelAuto(models.Model):
    mark = models.ForeignKey('BrandAuto', null=True, on_delete=models.PROTECT)
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return self.model
    

# КАТАЛИЗАТОР
class Catalysts(models.Model):
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')
    image_1 = models.ImageField(upload_to='media/catalog', blank=True, verbose_name='Фото катализатора 1')
    image_2 = models.ImageField(upload_to='media/catalog', blank=True, verbose_name='Фото катализатора 2')
    image_3 = models.ImageField(upload_to='media/catalog', blank=True, verbose_name='Фото катализатора 3')
    image_4 = models.ImageField(upload_to='media/catalog', blank=True, verbose_name='Фото катализатора 4')
    brand = models.ForeignKey('BrandAuto', on_delete=models.PROTECT, help_text='Выберите из списка', verbose_name='Марка авто')
    model = models.ForeignKey('ModelAuto', on_delete=models.PROTECT, help_text='Выберите из списка', verbose_name='Модель авто')
    year_release = models.ForeignKey('YearRelease', on_delete=models.PROTECT, help_text='Выберите из списка', verbose_name='Год выпуска авто')
    COUNTRY_ORIGIN = (
        ('jp', 'Япония'),
        ('us', 'Америка'),
        ('ch', 'Китай'),
        ('ko', 'Корея'),
        ('gb', 'Англия'),
        ('it', 'Италия'),
        ('de', 'Германия'),
        ('fr', 'Франция'),
        ('cz', 'Швеция'),
        ('sw', 'Чехия'),
        ('sp', 'Испания'),
        ('ro', 'Румыния'),
        ('rf', 'Россия'),
    )
    country = models.CharField(max_length=2, choices=COUNTRY_ORIGIN, blank=True, default='rf', verbose_name='Страна производитель')
    type_motor = models.ForeignKey('TypeOfMotor', on_delete=models.PROTECT, help_text='Выберите из списка', verbose_name='Тип двигателя')
    engine_volume = models.ForeignKey('EngineVolume', on_delete=models.PROTECT, help_text='Выберите из списка', verbose_name='Объем двигателя')
    TYPE_OF_TRANSPORT = (
        ('cr', 'легковое авто'),
        ('tr', 'грузовое авто'),
    )
    type_transport = models.CharField(max_length=2, choices=TYPE_OF_TRANSPORT, blank=True, default='cr', verbose_name='Тип автомобиля')
    weight = models.FloatField(blank=True, help_text='Указывать в граммах', verbose_name='Вес катализатора')
    quantity_pt = models.FloatField(blank=True, help_text='Указывать в граммах', verbose_name='Содержание платины')
    quantity_pd = models.FloatField(blank=True, help_text='Указывать в граммах', verbose_name='Содержание палладия')
    quantity_rh = models.FloatField(blank=True, help_text='Указывать в граммах', verbose_name='Содержание родия')
    update = models.ForeignKey('FixPrice', on_delete=models.PROTECT, null=True, help_text='Автообновление', verbose_name='Дата обновления')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена катализатора на сегодня')
    chart_price = models.TextField(max_length=3000, help_text='Не редактировать', verbose_name='Код графика изменения цены')
    content = models.TextField(max_length=3000, help_text='Максимум 3000 символов', verbose_name='Описание катализатора')
    
    def get_absolute_url(self):
        return reverse('catalyst', kwargs={'catalyst_slug': self.slug})
    
    class Meta:
        verbose_name = 'катализатор'
        verbose_name_plural = 'Катализаторы'




# СТРАНИЦА - КАЛЬКУЛЯТОР #####################################################
class PageCalculator(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')
    sub_content = models.TextField(max_length=1000, blank=True, help_text='Максимум 1000 символов', verbose_name='Вспомогательный контент')
    content = models.TextField(max_length=3500, blank=True, help_text='Максимум 3500 символов', verbose_name='Основной контент')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница - Калькулятор'
        verbose_name_plural = 'Страница - Калькулятор'




# СТРАНИЦА - БИРЖА ###########################################################
class PageStock(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')
    online_header = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок для онлайн котировок')
    online_content = models.TextField(max_length=2500, help_text='Максимум 2500 символов', verbose_name='Текст для онлайн котировок')
    fix_header = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок для фиксированных цен')
    fix_content = models.TextField(max_length=2500, help_text='Максимум 2500 символов', verbose_name='Текст для фиксированных цен')
    content = models.TextField(max_length=2500, blank=True, help_text='Максимум 2500 символов', verbose_name='Основной контент')

    def __str__(self):
        return self.header_h1
    
    class Meta:
        verbose_name = 'Страница - Биржа'
        verbose_name_plural = 'Страница - Биржа'

# ONLINE КОТИРОВКИ
class OnlinePrice(models.Model):
    update = models.TimeField(auto_now=False, auto_now_add=False, blank=True, verbose_name='Время обновления')
    pt_price_bid = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Цена Pt Bid USD ounce')
    pt_price_ask = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Цена Pt Ask USD ounce')
    pt_change = models.FloatField(blank=True, null=True, verbose_name='Изменение Pt (процент)')
    pt_change_num = models.FloatField(blank=True, null=True, verbose_name='Изменение Pt (число)')
    pd_price_bid = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Цена Pd Bid USD ounce')
    pd_price_ask = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Цена Pd Ask USD ounce')
    pd_change = models.FloatField(blank=True, null=True, verbose_name='Изменение Pd (процент)')
    pd_change_num = models.FloatField(blank=True, null=True, verbose_name='Изменение Pd (число)')
    rh_price_bid = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Цена Rh Bid USD ounce')
    rh_price_ask = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Цена Rh Ask USD ounce')
    rh_change = models.FloatField(blank=True, null=True, verbose_name='Изменение Rh (процент)')
    rh_change_num = models.FloatField(blank=True, null=True, verbose_name='Изменение Rh (число)')

    class Meta:
        verbose_name = 'Биржа - online котировки'
        verbose_name_plural = 'Биржа - online котировки'

# FIX КОТИРОВКИ
class FixPrice(models.Model):
    fix_today_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, help_text='Автообновление раз в сутки', verbose_name='Дата обновления - сегодня')
    fix_today_pt_usd_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в USD am')
    fix_today_pt_usd_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в USD pm')
    fix_today_pt_rub_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в RUB am')
    fix_today_pt_rub_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в RUB pm')
    fix_today_pd_usd_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в USD am')
    fix_today_pd_usd_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в USD pm')
    fix_today_pd_rub_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в RUB am')
    fix_today_pd_rub_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в RUB pm')
    fix_1_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, help_text='Автообновление раз в сутки', verbose_name='Дата обновления - вчера')
    fix_1_pt_usd_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в USD am')
    fix_1_pt_usd_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в USD pm')
    fix_1_pt_rub_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в RUB am')
    fix_1_pt_rub_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в RUB pm')
    fix_1_pd_usd_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в USD am')
    fix_1_pd_usd_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в USD pm')
    fix_1_pd_rub_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в RUB am')
    fix_1_pd_rub_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в RUB pm')
    fix_2_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, help_text='Автообновление раз в сутки', verbose_name='Дата обновления - позавчера')
    fix_2_pt_usd_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в USD am')
    fix_2_pt_usd_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в USD pm')
    fix_2_pt_rub_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в RUB am')
    fix_2_pt_rub_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pt в RUB pm')
    fix_2_pd_usd_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в USD am')
    fix_2_pd_usd_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в USD pm')
    fix_2_pd_rub_am = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в RUB am')
    fix_2_pd_rub_pm = models.FloatField(blank=True, help_text='Автообновление раз в сутки', verbose_name='Цена Pd в RUB pm')

    class Meta:
        verbose_name = 'Биржа - фиксы'
        verbose_name_plural = 'Биржа - фиксы'
    



# СТРАНИЦА - ЦЕНЫ ############################################################
class PagePrice(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')
    content = models.TextField(max_length=3000, help_text='Максимум 3000 символов', verbose_name='Контент')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница - Цены'
        verbose_name_plural = 'Страница - Цены'

# ТАБЛИЦА ЦЕН
class PriceTable(models.Model):
    auto = models.CharField(max_length=100, verbose_name='Марка и модель авто')
    price = models.CharField(max_length=100, verbose_name='Диапазон цен')

    def __str__(self):
        return self.auto
    
    class Meta:
        verbose_name = 'катализатор от популярного авто'
        verbose_name_plural = 'Катализаторы от популярных авто'




# СТРАНИЦА - БЛОГ ############################################################
class PageBlog(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница - Блог'
        verbose_name_plural = 'Страница - Блог'

# СТАТЬЯ
class Article(models.Model):
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    image = models.ImageField(upload_to='media/blog', verbose_name='Изображение статьи')
    header = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок статьи')
    content = models.TextField(max_length=7000, help_text='Максимум 7000 символов', verbose_name='Содержание статьи')
    date = models.DateField(auto_now=True)
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']




# СТРАНИЦА - КОНТАКТЫ ########################################################
class PageContacts(models.Model):
    title = models.CharField(max_length=150, help_text='Максимум 150 символов', verbose_name='Title')
    description = models.TextField(max_length=350, help_text='Максимум 350 символов', verbose_name='Description')
    header_h1 = models.CharField(max_length=250, help_text='Максимум 250 символов', verbose_name='Заголовок H1')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница - Контакты'
        verbose_name_plural = 'Страница - Контакты'

# ГОРОД
class City(models.Model):
    office = models.CharField(max_length=100, blank=True, help_text='Офис, пункт приема, филиал, головной офис', verbose_name='Тип офиса')
    city_name = models.CharField(max_length=30, help_text='Название города', verbose_name='Город')
    emblem = models.ImageField(upload_to='media/contacts', blank=True, verbose_name='Герб города')
    manager_photo = models.ImageField(upload_to='media/contacts', blank=True, verbose_name='Фото сотрудника')
    manager_post = models.CharField(max_length=50, help_text='Должность сотрудника')
    manager_name = models.CharField(max_length=50, help_text='Имя сотрудника')
    manager_phone = models.CharField(max_length=16, help_text='Ссылка, например tel:+79000000000', verbose_name='Телефон сотрудника')
    manager_whatsapp = models.URLField(max_length=100, help_text='Ссылка на WhatsApp', verbose_name='WhatsApp менеджера')
    manager_telegram = models.URLField(max_length=100, help_text='Ссылка на telegram', verbose_name='Telegram менеджера')
    phone = models.CharField(max_length=20, help_text='Максимум 20 символов', verbose_name='Телефон')
    mail = models.EmailField(max_length=200, help_text='Масимум 200 символов', verbose_name='Email')
    work_time = models.CharField(max_length=255, help_text='Максимум 255 символов', verbose_name='Режим работы')
    address = models.TextField(max_length=400, help_text='Максимум 400 символов', verbose_name='Адрес')
    map = models.TextField(max_length=500, blank=True, help_text='Код из конструктора карт Яндекс', verbose_name='Код карты')

    def __str__(self):
        return self.city_name
  
    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'