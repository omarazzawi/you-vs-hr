from django.test import TestCase, Client
from django.urls import reverse
from .models import Page, ResourceCategory, Resource

class PageModelTest(TestCase):
    """Test the Page model"""
    
    def setUp(self):
        """Create test page"""
        self.page = Page.objects.create(
            title='About & Policies',
            slug='about-policies',
            content='Test content',
            mission='Test mission',
            guidelines='Test guidelines'
        )
    
    def test_page_creation(self):
        """Test page is created correctly"""
        self.assertEqual(self.page.title, 'About & Policies')
        self.assertEqual(self.page.slug, 'about-policies')
        self.assertTrue(isinstance(self.page, Page))
    
    def test_page_str_method(self):
        """Test string representation"""
        self.assertEqual(str(self.page), 'About & Policies')


class ResourceModelTest(TestCase):
    """Test Resource and ResourceCategory models"""
    
    def setUp(self):
        """Create test category and resource"""
        self.category = ResourceCategory.objects.create(
            name='Job Sites',
            order=1,
            icon='🔍'
        )
        self.resource = Resource.objects.create(
            category=self.category,
            title='Indeed',
            url='https://www.indeed.com',
            description='Job search engine',
            order=1,
            active=True
        )
    
    def test_category_creation(self):
        """Test category is created correctly"""
        self.assertEqual(self.category.name, 'Job Sites')
        self.assertEqual(self.category.icon, '🔍')
    
    def test_resource_creation(self):
        """Test resource is created correctly"""
        self.assertEqual(self.resource.title, 'Indeed')
        self.assertEqual(self.resource.category, self.category)
        self.assertTrue(self.resource.active)
    
    def test_resource_str_method(self):
        """Test resource string representation"""
        expected = f"Indeed (Job Sites)"
        self.assertEqual(str(self.resource), expected)


class AboutPageViewTest(TestCase):
    """Test About page view"""
    
    def setUp(self):
        self.client = Client()
        self.page = Page.objects.create(
            title='About & Policies',
            slug='about-policies',
            mission='Our mission',
            guidelines='Our guidelines'
        )
    
    def test_about_page_loads(self):
        """Test about page is accessible"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
    
    def test_about_page_displays_content(self):
        """Test about page shows page content"""
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'About &amp; Policies')
        self.assertContains(response, 'Our mission')


class ResourcesPageViewTest(TestCase):
    """Test Resources page view"""
    
    def setUp(self):
        self.client = Client()
        self.category = ResourceCategory.objects.create(
            name='Job Sites',
            order=1
        )
        self.active_resource = Resource.objects.create(
            category=self.category,
            title='Indeed',
            url='https://www.indeed.com',
            description='Job search',
            active=True
        )
        self.inactive_resource = Resource.objects.create(
            category=self.category,
            title='Hidden Site',
            url='https://example.com',
            description='Should not appear',
            active=False
        )
    
    def test_resources_page_loads(self):
        """Test resources page is accessible"""
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/resources.html')
    
    def test_resources_page_shows_active_only(self):
        """Test only active resources are displayed"""
        response = self.client.get(reverse('resources'))
        self.assertContains(response, 'Indeed')
        self.assertNotContains(response, 'Hidden Site')
    
    def test_external_links_open_new_tab(self):
        """Test resource links have target blank"""
        response = self.client.get(reverse('resources'))
        self.assertContains(response, 'target="_blank"')
        self.assertContains(response, 'rel="noopener"')