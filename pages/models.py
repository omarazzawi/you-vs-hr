from django.db import models


class Page(models.Model):
    """Model for static pages with editable content."""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(help_text="Main page content")

    # For About/Policy page sections
    mission = models.TextField(blank=True, help_text="Mission statement")
    guidelines = models.TextField(blank=True, help_text="Community guidelines")
    privacy_policy = models.TextField(blank=True, help_text="Privacy policy")
    terms_of_use = models.TextField(blank=True, help_text="Terms of use")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ResourceCategory(models.Model):
    """Categories for organizing resources."""

    name = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(
        default=0,
        help_text="Display order (lower numbers first)"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional icon/emoji (e.g., 🔍, 📺)"
    )

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Resource Categories"

    def __str__(self):
        return self.name


class Resource(models.Model):
    """Individual resource links."""

    category = models.ForeignKey(
        ResourceCategory,
        on_delete=models.CASCADE,
        related_name='resources'
    )
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    order = models.IntegerField(
        default=0,
        help_text="Display order within category"
    )
    active = models.BooleanField(
        default=True,
        help_text="Show/hide this resource"
    )

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.title} ({self.category.name})"
