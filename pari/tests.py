from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Books
from .serializers import BookSerializer
from django.urls import reverse

class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.books_data = {
            'author': 'Alice',
            'year': 1945,
            'title' : 'Rise of Abyss',
            'city' : 'Land of Dawn',
            'publisher': 'HOK: Bang Bang!'
        }
        self.books = Books.objects.create(
            author="mike",
            year=2019,
            title="under the sun",
            city="bandung",
            publisher="gramedia"
        )
    
    def test_create_books(self):
        response = self.client.post(reverse('books'), self.books_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Books.objects.count(), 2)
        self.assertEqual(Books.objects.get(id=2).author, 'Alice')

    def test_get_all_books(self):
        response = self.client.get(reverse('books'))
        book = Books.objects.all()
        serializer_class = BookSerializer(book, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_class.data)

    def test_get_single_book(self):
        response = self.client.get(reverse('books-detail', kwargs={'pk': self.books.id}))
        book = Books.objects.get(id=self.books.id)
        serializer_class = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_class.data)

    def test_update_book(self):
        updated_data = {
            'author': 'J. K. Rowling',
            'year': 2000,
            'title' : 'Harry Potter and the Goblet of Fire',
            'city' : 'United Kingdom',
            'publisher': 'Bloomsbury'
        }
        response = self.client.put(reverse('books-detail', kwargs={'pk': self.books.id}), updated_data, format='json')
        self.books.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.books.author, 'J. K. Rowling')
        self.assertEqual(self.books.year, 2000)
        self.assertEqual(self.books.title, 'Harry Potter and the Goblet of Fire')
        self.assertEqual(self.books.city, 'United Kingdom')
        self.assertEqual(self.books.publisher, 'Bloomsbury')

    def test_delete_book(self):
        response = self.client.delete(reverse('books-detail', kwargs={'pk': self.books.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Books.objects.count(), 0)
