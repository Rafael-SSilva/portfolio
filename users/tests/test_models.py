from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagerTestCase(TestCase):

  def test_create_user(self):
    """Ensure we can create a new user"""
    User = get_user_model()
    user = User.objects.create_user(email='user@email.com', password='password@2022')
    self.assertEqual(user.email, 'user@email.com')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)
  

  def test_create_superuser(self):
    """Ensure we can create a new  superuser"""
    User = get_user_model()
    admin_user = User.objects.create_superuser(email='admin@email.com', password='password@2022')
    self.assertEqual(admin_user.email, 'admin@email.com')
    self.assertTrue(admin_user.is_active)
    self.assertTrue(admin_user.is_staff)
    self.assertTrue(admin_user.is_superuser)