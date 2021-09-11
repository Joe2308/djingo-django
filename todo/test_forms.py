from django.test import TestCase
from .forms import ItemForm


# Create your tests here.
class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        # Create instance of form of user that didn't enter name
        form = ItemForm({'name': ""})
        # Check if the error is in form validation
        self.assertFalse(form.is_valid())
        # Check if the error is in the name field
        self.assertIn('name', form.errors.keys())
        # Check if the error is exactly empty field
        # The 0 index tells us the first error in list is field is required
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Test if form is valid only sending a name
        # It should be valid without selecting the done status
        form = ItemForm({'name': "Test Todo Item"})
        self.assertTrue(form.is_valid())
    
    # Test that the only fields 
    # displayed in the form are the name and done fields
    def test_fields_are_explicit_in_form_metaclass(self):
        # create instance of an empty form
        form = ItemForm()
        # Check that the form fields are equal to name and done
        self.assertEqual(form.Meta.fields, ['name', 'done'])