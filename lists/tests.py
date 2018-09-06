from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page
from .models import Item


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        frist_item = Item()
        frist_item.text = 'The frist (ever) list item'
        frist_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        frist_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(frist_saved_item.text, 'The frist (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
