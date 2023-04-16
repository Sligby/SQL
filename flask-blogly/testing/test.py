import unittest
from app import app, db
from models import User

class FlaskTests(unittest.TestCase):
    
    def setUp(self):
        """Set up test app and database"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Clean up database"""
        db.session.remove()
        db.drop_all()

    def test_list_users(self):
        """Test GET /users to ensure all users are displayed"""
        user1 = User(first_name='John', last_name='Doe', image_url='https://example.com/john.jpg')
        user2 = User(first_name='Jane', last_name='Doe', image_url='https://example.com/jane.jpg')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'Jane Doe', response.data)

    def test_add_user(self):
        """Test POST /users/new to ensure new user is added"""
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'image_url': 'https://example.com/john.jpg'
        }
        response = self.app.post('/users/new', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)

    def test_view_user(self):
        """Test GET /users/[user-id] to ensure correct user is displayed"""
        user = User(first_name='John', last_name='Doe', image_url='https://example.com/john.jpg')
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)

    def test_edit_user(self):
        """Test GET /users/[user-id]/edit to ensure edit form is displayed"""
        user = User(first_name='John', last_name='Doe', image_url='https://example.com/john.jpg')
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f'/users/{user.id}/edit')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Edit User', response.data)

    def test_update_user(self):
        """Test POST /users/[user-id]/edit to ensure user is updated"""
        user = User(first_name='John', last_name='Doe', image_url='https://example.com/john.jpg')
        db.session.add(user)
        db.session.commit()

        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'image_url': 'https://example.com/jane.jpg'
        }
        response = self.app.post(f'/users/{user.id}/edit', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane Doe', response.data)

    def test_delete_user(self):
        """Test POST /users/[user-id]/delete to ensure user is deleted"""
        user = User(first_name='John', last_name='Doe', image_url='https://example.com/john.jpg')
        db.session.add(user)
        db.session.commit()

        response = self.app.post(f'/users/{user.id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)