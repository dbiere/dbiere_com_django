from django.shortcuts import render
from amazon.api import AmazonAPI

from django.conf import settings

from .models import Book, Author

def index(request):
    old_books_start_year = 1992
    current_books = Book.objects.filter(date_finished__isnull=True).order_by('-date_started').prefetch_related('author')
    books = Book.objects.filter(date_finished__year__gt=old_books_start_year).order_by('-date_finished__year', 'title').prefetch_related('author')
    old_books = Book.objects.filter(date_finished__year__lte=old_books_start_year).order_by('title').prefetch_related('author')

    # Get Amazon data, add to current books

    # amazon_asin_list = []
    # amazon_product_list = []

    # TODO - Handle error properly
    # TODO - Remove or replace Amazon API, they cut off access due to low (no) sales volume in early 2019
    # if current_books:
    #     for book in current_books:
    #         amazon_asin_list.append(book.amazon_asin)
    #     amazon = AmazonAPI(settings.AMAZON_KEY, settings.AMAZON_SECRET_KEY, settings.AMAZON_STORE_ID)
    #     amazon_product_list = amazon.lookup_bulk(ItemId=",".join(amazon_asin_list))

    # if len(amazon_product_list) == len(current_books):
    #     for i, product in enumerate(amazon_product_list):
    #         current_books[i].amazon_image_url = product.large_image_url

    '''
    https://docs.aws.amazon.com/AWSECommerceService/latest/DG/TroubleshootingApplications.html

    Note that your account will lose access to Product Advertising API if it has not generated referring sales using PA API in the last 30 days.

    If you are trying to submit requests that exceed the maximum request for your account (TPD limit), or if your access has been revoked you will receive a 503 error message from Product Advertising API.

    If you lose access to Product Advertising API, please see our other product linking tools, such as Site Stripe. You will regain access to Product Advertising API once your account again begins to drive referring sales.
    '''

    # Build context and return

    context = {
        'current_books': current_books,
        'books': books,
        'old_books': old_books,
        'old_books_start_year': old_books_start_year,
    }

    return render(request, 'books/index.html', context)

