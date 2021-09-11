from django.test import TestCase
from .models import Item


# Create your tests here.
class TestViews(TestCase):

    def test_get_todo_list(self):
        # Set variable for home page
        response = self.client.get("/")
        # test we have a valid http resonse
        self.assertEqual(response.status_code, 200)
        # Check correct template is being used
        self.assertTemplateUsed(response, 'todo/to_list.html')

    def test_get_add_item_page(self):
        # Set variable for add page
        response = self.client.get("/add")
        # test we have a valid http resonse
        self.assertEqual(response.status_code, 200)
        # Check correct template is being used
        self.assertTemplateUsed(response, 'todo/add_item.html')
    
    def test_get_edit_item_page(self):
        # Create variable to access object id
        item = Item.objects.create(name="Test Todo Item")
        # Set variable for edit page including item id in an f string
        response = self.client.get(f"/edit/{item.id}")
        # test we have a valid http resonse
        self.assertEqual(response.status_code, 200)
        # Check correct template is being used
        self.assertTemplateUsed(response, 'todo/edit_item.html')
    
    def test_can_add_item(self):
        #  Test item can be added
        response = self.client.POST("/add", {"name": "Test Added Item"})
        #  If item is added successfully redirect user to home
        self.assertRedirects(response, "/")
    
    def test_can_delete_item(self):
        # Create variable to access object id
        item = Item.objects.create(name="Test Todo Item")
        # Set variable for delete including item id in an f string
        response = self.client.get(f"/delete/{item.id}")
        #   If item is deleted successfully redirect user to home
        self.assertRedirects(response, "/")
        # To make sure item is deleted try to get it from DB
        existing_item = Item.objects.filter(id=item.id)
        # check if deleted item is less  that 0 in DB
        self.assertEqual(len(existing_item), 0)
    
    def test_can_toggle_item(self):
        # Create variable to check object id status id done
        item = Item.objects.create(name="Test Todo Item", done=True)
        # Set variable for delete including item id in an f string
        response = self.client.get(f"/toggle/{item.id}")
        #   If item is deleted successfully redirect user to home
        self.assertRedirects(response, "/")
        # Create variable to check item
        updated_item = Item.objects.get(id=item.id)
        # Check items done status
        self.assertFalse(updated_item.done)
