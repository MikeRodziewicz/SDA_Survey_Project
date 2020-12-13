from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString
from surveys.models import Survey, Product
from django.db.models import Avg, Sum, F
from operator import itemgetter
from django.db.models import Count

register = Library()


@register.simple_tag
def product_format(product, short=False):
    if short:
        return f'{product.name}'
    return f'{product.name} ({product.price})'


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value}</p>')


@register.filter
def average_rating(product, rate_number: str):
    if Survey.objects.all().count() == 0:
        return f'No surveys'
    else:
        return round(Survey.objects.filter(product_id=product.id).aggregate(Avg(rate_number))
                    ['rate_' + rate_number[-1] + '__avg'], 1)


@register.filter
def product_full_average(product):
    rating = []
    if Survey.objects.filter(product_id=product.id).count() == 0:
        return f'No surveys'
    else:
        for num in range(5):
            rating.append(average_rating(product, 'rate_' + str(num + 1)))
        return round(sum(rating)/len(rating), 1)


def product_averages(products):
    products = products.annotate(survey_count=Count('survey'), 
                                        avg_rate_1=Avg('survey__rate_1'),
                                        avg_rate_2=Avg('survey__rate_2'),
                                        avg_rate_3=Avg('survey__rate_3'),
                                        avg_rate_4=Avg('survey__rate_4'),
                                        avg_rate_5=Avg('survey__rate_5'),
                                        total_avg = (F('avg_rate_1')+F('avg_rate_2')+F('avg_rate_3')
                                        +F('avg_rate_4')+F('avg_rate_5'))/5).filter(survey_count__gte=1).order_by('-total_avg')
    avarage_rate_list = [(product.name, product.total_avg) for product in products]
    return avarage_rate_list[:5], avarage_rate_list[-5:]


