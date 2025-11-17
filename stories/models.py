from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Story(models.Model):
    """
    Represents a story or article in the application.

    Attributes:
        title (CharField): The title of the story
        slug (SlugField): URL-friendly version of the title
        content (TextField): The main content of the story
        author (ForeignKey): User who created the story
        created_at (DateTimeField): When the story was created
        updated_at (DateTimeField): When the story was last updated
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadata options for the Story model."""
        verbose_name_plural = "Stories"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate slug from title.
        If no slug is provided, creates a URL-friendly slug from the title
        before saving the instance to the database.
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return string representation of the Story instance.
        Returns:
            str: The story title
        """
        return self.title


class Comment(models.Model):

    """
    Represents a comment on a story.
    Attributes:
        story (ForeignKey): The story this comment belongs to
        author (ForeignKey): User who wrote the comment
        content (TextField): The comment text content
        created_at (DateTimeField): When the comment was created
        updated_at (DateTimeField): When the comment was last updated
        approved (BooleanField): Whether the comment has been approved by admin
    """
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(
        default=False,
        help_text="Admin must approve before comment is visible to users"
    )

    class Meta:
        """Metadata options for the Comment model."""
        ordering = ['-created_at']

    def __str__(self):
        """
        Return string representation of the Comment instance.
        Returns:
            str: Format showing author and associated story
        """
        return f"Comment by {self.author.username} on {self.story.title}"
