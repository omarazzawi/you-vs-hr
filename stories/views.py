from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, StoryForm, CommentForm
from .models import Story, Comment


def index(request):
    """Display the homepage with all stories."""
    stories = Story.objects.all()
    return render(request, 'stories/index.html', {'stories': stories})


def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Account created successfully! Welcome to You VS HR.'
            )
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'stories/register.html', {'form': form})


def user_login(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('index')
    else:
        form = AuthenticationForm()

    # Add form control class to all fields
    for field in form.fields:
        form.fields[field].widget.attrs.update({'class': 'form-control'})

    return render(request, 'stories/login.html', {'form': form})


def user_logout(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')


def story_detail(request, slug):
    """Display individual story with all approved comments."""
    story = get_object_or_404(Story, slug=slug)
    comments = story.comments.filter(approved=True).order_by('-created_at')

    # Handle comment submission
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.approved = False  # Requires admin approval
            comment.save()
            messages.success(
                request,
                'Your comment has been submitted and is awaiting approval.'
            )
            return redirect('story_detail', slug=story.slug)
    else:
        comment_form = CommentForm()

    context = {
        'story': story,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'stories/story_detail.html', context)


@login_required
def create_story(request):
    """Create a new story (logged-in users only)."""
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            messages.success(
                request, 'Your story has been published successfully!'
            )
            return redirect('story_detail', slug=story.slug)
    else:
        form = StoryForm()

    return render(request, 'stories/create_story.html', {'form': form})


@login_required
def edit_story(request, slug):
    """Edit an existing story (author only)."""
    story = get_object_or_404(Story, slug=slug)

    # Check if user is the author
    if request.user != story.author:
        messages.error(request, 'You can only edit your own stories.')
        return redirect('story_detail', slug=story.slug)

    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your story has been updated successfully!'
            )
            return redirect('story_detail', slug=story.slug)
    else:
        form = StoryForm(instance=story)

    context = {
        'form': form,
        'story': story,
        'editing': True,
    }
    return render(request, 'stories/edit_story.html', context)


@login_required
def delete_story(request, slug):
    """Delete a story (author only)."""
    story = get_object_or_404(Story, slug=slug)

    # Check if user is the author
    if request.user != story.author:
        messages.error(request, 'You can only delete your own stories.')
        return redirect('story_detail', slug=story.slug)

    if request.method == 'POST':
        story_title = story.title
        story.delete()  # This also deletes all associated comments (cascade)
        messages.success(request, f'Story "{story_title}" has been deleted.')
        return redirect('index')

    return render(request, 'stories/delete_story.html', {'story': story})


@login_required
def edit_comment(request, comment_id):
    """Edit a comment (author only)."""
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if user is the comment author
    if request.user != comment.author:
        messages.error(request, 'You can only edit your own comments.')
        return redirect('story_detail', slug=comment.story.slug)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            updated_comment = form.save(commit=False)
            updated_comment.approved = False  # Reset to pending after edit
            updated_comment.save()
            messages.success(
                request,
                'Your comment has been updated and is awaiting approval.'
            )
            return redirect('story_detail', slug=comment.story.slug)
    else:
        form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
        'story': comment.story,
    }
    return render(request, 'stories/edit_comment.html', context)


@login_required
def delete_comment(request, comment_id):
    """Delete a comment (author only)."""
    comment = get_object_or_404(Comment, id=comment_id)
    story_slug = comment.story.slug

    # Check if user is the comment author
    if request.user != comment.author:
        messages.error(request, 'You can only delete your own comments.')
        return redirect('story_detail', slug=story_slug)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('story_detail', slug=story_slug)

    return render(request, 'stories/delete_comment.html', {'comment': comment})
