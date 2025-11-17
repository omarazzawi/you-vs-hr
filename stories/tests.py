from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Story, Comment
from .forms import StoryForm, CommentForm, RegisterForm
# Create your tests here.


class StoryModelTest(TestCase):
    """Test the Story model"""
    
    def setUp(self):
        """Create test user and story"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.story = Story.objects.create(
            title='Test Story',
            content='This is a test story content',
            author=self.user
        )
    
    def test_story_creation(self):
        """Test story is created correctly"""
        self.assertEqual(self.story.title, 'Test Story')
        self.assertEqual(self.story.author, self.user)
        self.assertTrue(isinstance(self.story, Story))
    
    def test_story_slug_generation(self):
        """Test slug is auto-generated from title"""
        self.assertEqual(self.story.slug, 'test-story')
    
    def test_story_str_method(self):
        """Test string representation"""
        self.assertEqual(str(self.story), 'Test Story')


class CommentModelTest(TestCase):
    """Test the Comment model (custom feature)"""
    
    def setUp(self):
        """Create test data"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.story = Story.objects.create(
            title='Test Story',
            content='Test content',
            author=self.user
        )
        self.comment = Comment.objects.create(
            story=self.story,
            author=self.user,
            content='Test comment',
            approved=False
        )
    
    def test_comment_creation(self):
        """Test comment is created correctly"""
        self.assertEqual(self.comment.content, 'Test comment')
        self.assertEqual(self.comment.author, self.user)
        self.assertFalse(self.comment.approved)
    
    def test_comment_default_not_approved(self):
        """Test comments default to unapproved (custom feature)"""
        new_comment = Comment.objects.create(
            story=self.story,
            author=self.user,
            content='Another comment'
        )
        self.assertFalse(new_comment.approved)
    
    def test_comment_str_method(self):
        """Test string representation"""
        expected = f"Comment by {self.user.username} on {self.story.title}"
        self.assertEqual(str(self.comment), expected)


class UserAuthenticationTest(TestCase):
    """Test user authentication views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_register_page_loads(self):
        """Test registration page is accessible"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/register.html')
    
    def test_login_page_loads(self):
        """Test login page is accessible"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/login.html')
    
    def test_user_can_login(self):
        """Test user can login with valid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login


class StoryViewTest(TestCase):
    """Test story views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.story = Story.objects.create(
            title='Test Story',
            content='Test content',
            author=self.user
        )
    
    def test_homepage_loads(self):
        """Test homepage displays stories"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Story')
    
    def test_story_detail_loads(self):
        """Test story detail page"""
        response = self.client.get(
            reverse('story_detail', kwargs={'slug': self.story.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Story')
        self.assertContains(response, 'Test content')
    
    def test_create_story_requires_login(self):
        """Test create story redirects if not logged in"""
        response = self.client.get(reverse('create_story'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_logged_in_user_can_create_story(self):
        """Test logged-in user can access create page"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('create_story'))
        self.assertEqual(response.status_code, 200)


class CommentApprovalTest(TestCase):
    """Test comment approval system (custom feature)"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.story = Story.objects.create(
            title='Test Story',
            content='Test content',
            author=self.user
        )
        self.approved_comment = Comment.objects.create(
            story=self.story,
            author=self.user,
            content='Approved comment',
            approved=True
        )
        self.unapproved_comment = Comment.objects.create(
            story=self.story,
            author=self.user,
            content='Unapproved comment',
            approved=False
        )
    
    def test_only_approved_comments_visible(self):
        """Test unapproved comments don't appear on story page"""
        response = self.client.get(
            reverse('story_detail', kwargs={'slug': self.story.slug})
        )
        self.assertContains(response, 'Approved comment')
        self.assertNotContains(response, 'Unapproved comment')
    
    def test_comment_count_only_approved(self):
        """Test comment count only includes approved comments"""
        response = self.client.get(
            reverse('story_detail', kwargs={'slug': self.story.slug})
        )
        # Should show "Comments (1)" not "Comments (2)"
        self.assertContains(response, 'Comments (1)')


class FormTest(TestCase):
    """Test forms"""
    
    def test_story_form_valid(self):
        """Test story form with valid data"""
        form_data = {
            'title': 'Test Story',
            'content': 'This is test content'
        }
        form = StoryForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_story_form_invalid_no_title(self):
        """Test story form rejects empty title"""
        form_data = {
            'title': '',
            'content': 'This is test content'
        }
        form = StoryForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_comment_form_valid(self):
        """Test comment form with valid data"""
        form_data = {'content': 'Test comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())