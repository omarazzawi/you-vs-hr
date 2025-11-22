# YOU VS HR

A Django-based platform for job seekers to share and read real experiences with recruiters, HR departments, and hiring processes.

![You VS HR Homepage](/docs/images/youVsHr.png)

**🌐 Live Application:** [you-vs-hr.herokuapp.com](https://you-vs-hr-f560f6ced83c.herokuapp.com/)  
**📁 GitHub Repository:** [github.com/omarazzawi/you-vs-hr](https://github.com/omarazzawi/you-vs-hr)  
**📋 Project Board:** [View Agile Board](https://github.com/users/omarazzawi/projects/11)

---

## Table of Contents

- [Introduction](#introduction)
- [Project digram](#project-digram)
- [Project Structure](#project-structure)
- [Color Palette](#color-palette)
- [Agile Methodology](#agile-methodology)
- [User Stories](#user-stories)
- [Features](#features)
- [Custom Model Implementation](#custom-model-implementation)
- [Technology Stack](#technology-stack)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Introduction

You VS HR is a transparency platform built exclusively for job seekers to document their experiences during the recruitment process. Unlike traditional employee review sites like Glassdoor that focus on current employees, You VS HR gives voice to candidates who faced unprofessional treatment, ghosting, false promises, or toxic behavior from recruiters and HR departments.

### Project Goals

- Provide a safe space for job seekers to share recruitment experiences
- Help candidates identify red flags before accepting job offers
- Create transparency in hiring processes
- Build a community of informed job seekers

### Target Audience

- Job seekers researching companies before applying
- Candidates who experienced unprofessional recruitment practices
- HR professionals seeking to improve their hiring processes

---

## Project digram
![You VS HR digram](/docs/images/projectDigram.png)   


## Color Palette

![Color Palette](/docs/images/colorPalette.png)


## Project Structure  
![Project Structure](/docs/images/projectStructure.png)

## Agile Methodology

This project was developed using Agile methodologies with GitHub Projects as the project management tool.

### MoSCoW Prioritization

User stories were prioritized using the MoSCoW method:

- **Must Have**: Core functionality essential for MVP (e.g., user authentication, story creation, comment approval)
- **Should Have**: Important features that enhance user experience (e.g., edit/delete functionality)
- **Could Have**: Nice-to-have features for future iterations (e.g., comment flagging system - moved to Won't Have)
- **Won't Have**: Features explicitly out of scope for this iteration

### Development Process

The project was developed iteratively with continuous integration and testing. Features were implemented in order of priority, with Must Have features completed first, followed by Should Have and Could Have features.

### GitHub Project Board

All user stories were tracked as GitHub Issues and managed through a Kanban board with columns:
- **To Do**: Ready for development
- **In Progress**: Currently being worked on
- **Done**: Completed and tested
- 

[View the complete project board](https://github.com/users/omarazzawi/projects/11)

### Agile Reflection

During development, the comment flagging features (User Stories #14) were deprioritized to "Won't Have" to ensure robust implementation of the core comment approval system within the project timeline. This demonstrates real-world Agile scope management and iterative development principles.

All 13 user stories were successfully completed and tested, representing 100% completion of the committed scope for this iteration.

---

## User Stories

### Epic: User Authentication

**#1 - Account Registration**
> As a user, I can register an account so that I can post my workplace stories

**Acceptance Criteria:**
- Registration form validates username (unique, 3+ characters)
- Registration form validates email format
- Registration form validates password (8+ characters)
- Successful registration auto-logs in user and redirects to homepage

**#2 - User Login/Logout**
> As a user, I can login and logout so that I can access my account securely

**Acceptance Criteria:**
- Login form accepts valid credentials
- Invalid credentials show error message
- Logout button visible when logged in
- Navigation shows different options based on auth status

### Epic: Story Management

**#3 - Create Story**
> As a logged-in user, I can submit a new story with title and content so that I can share my experience

**Acceptance Criteria:**
- Create story form only accessible to logged-in users
- Title field max 200 characters
- Content field is large text area
- Story appears on homepage immediately after creation
- Slug auto-generates from title

**#5 - View All Stories**
> As a visitor, I can see a list of all stories on the homepage so that I can browse experiences

**Acceptance Criteria:**
- Homepage displays all stories in responsive grid (3→2→1 columns)
- Each story card shows title, preview, author, and date
- Stories ordered by newest first
- Clicking story opens detail page

**#6 - View Story Details**
> As a visitor, I can view individual story details so that I can read the full story and comments

**Acceptance Criteria:**
- Full story content displayed
- All approved comments shown below story
- Page accessible without login
- Back button returns to homepage

**#7 - Edit Story**
> As a story author, I can edit my own stories so that I can fix mistakes

**Acceptance Criteria:**
- Edit button only visible to story author
- Edit form pre-populated with current content
- Permission check prevents unauthorized edits
- Timestamp shows "last edited" date

**#8 - Delete Story**
> As a story author, I can delete my own stories so that I can remove content

**Acceptance Criteria:**
- Delete button only visible to story author
- Confirmation modal prevents accidental deletion
- Deleting story also deletes associated comments (cascade)
- Redirects to homepage with success message

### Epic: Comment System (Custom Model Feature)

**#9 - Add Comment**
> As a logged-in user, I can comment on stories so that I can share my thoughts

**Acceptance Criteria:**
- Comment form only visible to logged-in users
- Successful submission shows "awaiting approval" message
- Comment does NOT appear immediately (requires approval)
- User redirected to story detail after submission

**#10 - Admin Approve Comments** ⭐ *CUSTOM MODEL FEATURE*
> As an admin, I can approve comments so that only appropriate content is visible

**Acceptance Criteria:**
- Admin panel shows all comments with approval status
- Admin can filter by approved vs pending
- Bulk approval action available
- Approved comments immediately visible on site
- Unapproved comments hidden from regular users

**#11 - Edit/Delete Comments**
> As a comment author, I can edit or delete my own comments so that I can manage my content

**Acceptance Criteria:**
- Edit/delete buttons only visible to comment author
- Edited comments require re-approval
- Delete requires confirmation
- Permission checks prevent unauthorized actions

### Epic: User Experience

**#15 - Responsive Design**
> As a visitor, I can view the site on any device so that I have a good experience

**Acceptance Criteria:**
- Homepage grid adapts to screen size
- Navigation collapses to hamburger menu on mobile
- Forms usable on mobile devices
- Text readable without zooming
- Buttons touch-friendly (44px minimum)

### Epic: Static Pages

**#16 - About & Policies Page**
> As a visitor, I can view the About & Policy page so that I understand the site's purpose and rules

**Acceptance Criteria:**
- Page displays information about You VS HR's mission
- Page explains community guidelines
- Page includes privacy policy
- Page includes terms of use
- Content is editable via admin panel
- Page is accessible from navigation menu
- Page is responsive on all devices

**#17 - Resources Page**
> As a visitor, I can view a page with useful links and resources so that I can access job search platforms, career advice, and professional development tools

**Acceptance Criteria:**
- Page displays categorized resource links
- Links include job search platforms
- Links include career advice YouTube channels
- Content is editable via admin panel
- External links open in new tabs
- Page is accessible from navigation menu
- Page is responsive on all devices

### Won't Have (Future Iterations)

**#13 - User Flag Comments**
> As a user, I can flag inappropriate comments so that moderators can review them

**#14 - Admin Review Flagged Comments**
> As an admin, I can review flagged comments so that I can maintain content quality

*Both flagging features deprioritized to focus on core approval system. Can be implemented in future sprints based on user feedback.*

---

## Features

### Current Features

#### User Authentication
- Secure user registration with validation
- Login/logout functionality
- Password requirements enforced
- Welcome messages on login
- Navigation adapts based on auth status

#### Story Management (Full CRUD)
- **Create**: Logged-in users can post recruitment stories
- **Read**: Anyone can view all stories and details
- **Update**: Authors can edit their own stories
- **Delete**: Authors can delete with confirmation

#### Comment System with Moderation ⭐
- Users can comment on any story
- **Custom Approval Workflow**: Comments require admin approval before appearing
- Admin panel with bulk approval actions
- Authors can edit/delete their own comments
- Edited comments require re-approval for quality control

#### Static Pages
- **About & Policies**: Editable via admin (mission, guidelines, privacy, terms)
- **Resources**: Categorized helpful links (job sites, YouTube channels, tools)

#### Admin Interface
- Full content management system
- Custom admin actions for comment approval
- Bulk operations for efficiency
- Resource category management

#### Responsive Design
- Mobile-first approach using Bootstrap 5
- Hamburger navigation on mobile devices
- Flexible grid layout (3 columns → 2 → 1)
- Touch-friendly buttons and forms

### Future Features (Roadmap)

- Comment flagging system for community moderation
- User profiles with activity history
- Story categories and tags
- Search functionality
- Email notifications for comment approvals
- Company/recruiter mention tagging

---

## Custom Model Implementation

### Comment Approval System ⭐

The **Comment model with approval workflow** is the original custom model created specifically for this project. This feature is not present in the Code Institute walkthrough projects and demonstrates advanced Django model design.

#### Model Structure

```python
class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # CUSTOM FEATURE: Approval workflow
    approved = models.BooleanField(
        default=False,
        help_text="Admin must approve before comment is visible"
    )
```

#### Why This is Custom

1. **Content Moderation**: Unlike standard comment systems, all comments require admin approval before appearing on the site
2. **Re-approval on Edit**: When users edit comments, they return to pending status for quality control
3. **Bulk Admin Actions**: Custom admin interface with one-click approval for multiple comments
4. **User Feedback**: Clear messaging system informs users their comment is "awaiting approval"

#### Implementation Details

**Admin Interface** (`admin.py`):
```python
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'story', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        count = queryset.update(approved=True)
        self.message_user(request, f"{count} comment(s) approved.")
```

**View Logic** (`views.py`):
```python
# Only show approved comments to regular users
comments = story.comments.filter(approved=True).order_by('-created_at')

# New comments default to unapproved
comment.approved = False
comment.save()
messages.success(request, 'Your comment is awaiting approval.')
```

#### Benefits of This Approach

- **Quality Control**: Prevents spam and inappropriate content
- **Community Safety**: Maintains a respectful environment
- **Scalability**: Admin can efficiently moderate as community grows
- **User Trust**: Clear process builds confidence in platform integrity

---

## Technology Stack

### Backend
- **Django 5.2.8**: Web framework
- **Python 3.12.10**: Programming language
- **PostgreSQL**: Production database
- **dj-database-url**: Database configuration
- **psycopg2**: PostgreSQL adapter

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling
- **Bootstrap 5.3.0**: Responsive framework
- **JavaScript**: Interactive elements (via Bootstrap)

### Deployment
- **Heroku**: Cloud platform
- **Gunicorn 20.1.0**: WSGI server
- **WhiteNoise**: Static file serving

### Development Tools
- **Git 2.49.0**: Version control
- **GitHub**: Repository hosting and project management
- **VS Code**: Code editor

### Dependencies

```txt
asgiref==3.10.0
dj-database-url==0.5.0
Django==5.2.8
gunicorn==20.1.0
psycopg2==2.9.11
sqlparse==0.5.3
tzdata==2025.2
whitenoise==6.11.0
```

---

## Database Schema

### Entity Relationship Diagram

```
User (Django built-in)
  ├─ has many Stories
  └─ has many Comments

Story
  ├─ belongs to User (author)
  ├─ has many Comments
  ├─ has slug (unique, auto-generated)
  └─ has timestamps (created_at, updated_at)

Comment ⭐ CUSTOM MODEL
  ├─ belongs to Story
  ├─ belongs to User (author)
  ├─ has approved (Boolean) ← CUSTOM FIELD
  └─ has timestamps (created_at, updated_at)

Page
  ├─ has slug (unique)
  ├─ has content sections (mission, guidelines, privacy, terms)
  └─ editable via admin

ResourceCategory
  ├─ has many Resources
  ├─ has order (for display sorting)
  └─ has icon (emoji/symbol)

Resource
  ├─ belongs to ResourceCategory
  ├─ has URL (external link)
  ├─ has active status (Boolean)
  └─ has order (within category)
```

### Model Details

**Story Model**
- `title`: CharField (max 200, unique slug generation)
- `slug`: SlugField (SEO-friendly URLs)
- `content`: TextField (user's recruitment experience)
- `author`: ForeignKey to User
- `created_at/updated_at`: Auto timestamps

**Comment Model** ⭐
- `story`: ForeignKey to Story (cascade delete)
- `author`: ForeignKey to User
- `content`: TextField
- `approved`: BooleanField (default=False) ← **CUSTOM FEATURE**
- `created_at/updated_at`: Auto timestamps

**Page Model**
- `title/slug`: CharField/SlugField
- `content`: TextField (general content)
- `mission/guidelines/privacy_policy/terms_of_use`: TextField (structured sections)

**ResourceCategory Model**
- `name`: CharField (unique)
- `order`: IntegerField (display sorting)
- `icon`: CharField (emoji representation)

**Resource Model**
- `category`: ForeignKey to ResourceCategory
- `title/url/description`: CharField/URLField/TextField
- `order`: IntegerField (within category)
- `active`: BooleanField (show/hide control)

---

## Testing

### Manual Testing

#### User Authentication

| Test Case | Steps | Expected Result | Actual Result | Pass/Fail |
|-----------|-------|-----------------|---------------|-----------|
| Register new account | 1. Navigate to /register/<br>2. Fill form with valid data<br>3. Submit | Account created, auto-login, redirect to homepage, success message | As expected | ✅ Pass |
| Register with existing username | 1. Try to register with taken username | Error message displayed, form not submitted | As expected | ✅ Pass |
| Login with valid credentials | 1. Navigate to /login/<br>2. Enter correct username/password<br>3. Submit | Logged in, redirected to homepage, welcome message | As expected | ✅ Pass |
| Login with invalid credentials | 1. Enter wrong password<br>2. Submit | Error message, remain on login page | As expected | ✅ Pass |
| Logout | 1. Click logout link | Logged out, redirected to homepage, confirmation message | As expected | ✅ Pass |

#### Story Management

| Test Case | Steps | Expected Result | Actual Result | Pass/Fail |
|-----------|-------|-----------------|---------------|-----------|
| View all stories (logged out) | 1. Visit homepage | All stories displayed in grid, no edit/delete buttons | As expected | ✅ Pass |
| View story detail | 1. Click "Read More" on story card | Full story content, approved comments visible | As expected | ✅ Pass |
| Create story (not logged in) | 1. Try to access /story/create/ | Redirected to login page | As expected | ✅ Pass |
| Create story (logged in) | 1. Login<br>2. Click "Share Story"<br>3. Fill form<br>4. Submit | Story created, redirected to detail page, success message | As expected | ✅ Pass |
| Edit own story | 1. View own story<br>2. Click "Edit Story"<br>3. Modify content<br>4. Submit | Story updated, "edited" timestamp shown, success message | As expected | ✅ Pass |
| Try to edit other's story | 1. Manually navigate to /story/{slug}/edit/ for another user's story | Error message, redirected away | As expected | ✅ Pass |
| Delete own story | 1. Click "Delete Story"<br>2. Confirm deletion | Story and comments deleted, redirected to homepage, success message | As expected | ✅ Pass |
| Delete with cancel | 1. Click "Delete Story"<br>2. Click "Cancel" | Returned to story, no deletion | As expected | ✅ Pass |

#### Comment System (Custom Feature)

| Test Case | Steps | Expected Result | Actual Result | Pass/Fail |
|-----------|-------|-----------------|---------------|-----------|
| View comments (visitor) | 1. View story detail page | Only approved comments visible | As expected | ✅ Pass |
| Add comment (not logged in) | 1. View story detail | Comment form hidden, login prompt shown | As expected | ✅ Pass |
| Add comment (logged in) | 1. Login<br>2. Fill comment form<br>3. Submit | "Awaiting approval" message, comment NOT visible yet | As expected | ✅ Pass |
| Admin approve comment | 1. Login as admin<br>2. Go to Comments<br>3. Select comment<br>4. Choose "Approve" action<br>5. Click Go | Comment approved, immediately visible on site | As expected | ✅ Pass |
| Admin bulk approve | 1. Select multiple comments<br>2. Approve all at once | All comments approved, success message with count | As expected | ✅ Pass |
| Edit own comment | 1. Click "Edit" on own comment<br>2. Modify text<br>3. Submit | Comment updated, returns to "pending approval" status | As expected | ✅ Pass |
| Delete own comment | 1. Click "Delete"<br>2. Confirm | Comment deleted, success message | As expected | ✅ Pass |
| Try to edit other's comment | 1. Manually navigate to /comment/{id}/edit/ for another user | Error message, redirected | As expected | ✅ Pass |

#### Responsive Design

| Test Case | Device/Size | Expected Result | Actual Result | Pass/Fail |
|-----------|------------|-----------------|---------------|-----------|
| Homepage grid - Desktop (1920px) | Desktop browser at full width | 3 story cards per row | As expected | ✅ Pass |
| Homepage grid - Tablet (768px) | Browser resized to tablet size | 3 story cards per row | As expected | ✅ Pass |
| Homepage grid - Mobile (375px) | Browser resized to mobile size | 1 story card per row | As expected | ✅ Pass |
| Navigation - Desktop | Full-width browser | All nav links visible in horizontal row | As expected | ✅ Pass |
| Navigation - Mobile  Tablet | Mobile & Tablet-sized browser | Hamburger menu, collapsible nav | As expected | ✅ Pass |
| Footer - All sizes | Various screen sizes | Footer visible at bottom, not covering content | As expected | ✅ Pass |

#### Admin Interface

| Test Case | Steps | Expected Result | Actual Result | Pass/Fail |
|-----------|-------|-----------------|---------------|-----------|
| Access admin panel | 1. Navigate to /admin/<br>2. Login as superuser | Admin dashboard visible with all models | As expected | ✅ Pass |
| Edit About page content | 1. Go to Pages<br>2. Edit "About & Policies"<br>3. Modify mission text<br>4. Save | Changes immediately visible on /about/ | As expected | ✅ Pass |
| Add new resource | 1. Go to Resources<br>2. Add resource<br>3. Fill URL, description, category<br>4. Save | Resource appears on /resources/ page | As expected | ✅ Pass |
| Deactivate resource | 1. Edit resource<br>2. Uncheck "Active"<br>3. Save | Resource hidden from /resources/ page | As expected | ✅ Pass |
| Manage resource categories | 1. Add new category<br>2. Set order and icon | Category appears in correct order with icon | As expected | ✅ Pass |

### Bug Fixes

##### Don't make my mistake!

Before I even started, the biggest mistake I made in this project: **I built the CSS before I finished the project** and that impacted everything. I had to delete and rebuild the CSS many times.


#### 1. Virtual Environment Conflicts
- **Issue**: Multiple Python virtual environments causing version conflicts
- **Problem**: Having several environments (my_env_312, venv, env) created confusion
- **Solution**: Removed all except active environment, standardized on my_env_312

#### 2. Heroku Bad Request (400) Error
- **Issue**: Application returning "Bad Request (400)" on Heroku
- **Problem**: Incorrect ALLOWED_HOSTS configuration
```python
# ❌ Incorrect
ALLOWED_HOSTS = ['.herokuapp', '.127.0.0.1']

# ✅ Correct
ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']
```

#### 3. Environment Configuration Error
- **Issue**: Environment variables not loading
- **Problem**: File named `evn.py` instead of `env.py`
- **Solution**: Renamed file to correct name

#### 4. Django Admin Prepopulated Fields Error
- **Issue**: System check error preventing server startup
- **Problem**: Incorrect field name in StoryAdmin
```python
# ❌ Incorrect
prepopulated_fields = {'slg': ('title',)}

# ✅ Correct
prepopulated_fields = {'slug': ('title',)}
```

#### 5. User Object Attribute Error
- **Issue**: AttributeError when adding comments
- **Problem**: Typo in attribute name
```python
# ❌ Incorrect
comment.author.useranme

# ✅ Correct
comment.author.username
```

#### 6. Card Layout Alignment Issue
- **Issue**: "Read More" buttons not aligned across cards
- **Problem**: Varying content heights causing inconsistent positioning
- **Solution**: Applied Flexbox with auto margin
```css
.card-body {
    display: flex;
    flex-direction:column;
}
```

#### 7. Django Import Error
- **Issue**: ImportError for login_required decorator
- **Problem**: Incorrect import path
```python
# ❌ Incorrect
from django.contrib.auth import login_required

# ✅ Correct
from django.contrib.auth.decorators import login_required
```

#### 8. StoryForm NameError
- **Issue**: NameError when accessing /story/create/
- **Problem**: Form not imported in views.py
- **Solution**: Added `from .forms import StoryForm`

#### 9. Django Auth Redirect Issue
- **Issue**: 404 error when accessing protected routes
- **Problem**: Django looking for /accounts/login/ instead of /login/
- **Solution**: Added to settings.py:
```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

#### 10. CSS Specificity Issue
- **Issue**: Absolute positioning affecting all buttons
- **Problem**: Rule applied too broadly
- **Solution**: Made selector more specific
```css
/* Only apply to story card buttons */
.card-body > .btn-sm {
    position: absolute;
    bottom: 15px;
    left: 15px;
}
```

#### 11. Template Syntax Error
- **Issue**: TemplateSyntaxError with mismatched tags
- **Problem**: Using 'endfor' inside 'if' block incorrectly
- **Solution**: Properly closed all template tags

#### 12.

### Validation

#### HTML Validation
The errors were caused by missing id attributes on the help text elements.  

**Solution** Add id attributes to the help text divs:
  - Username help text
  - Password help text
  - Password confirmation 
  - ```id="{{ field.id_for_label }}_helptext"```  

 ![htmlValidatorRegistration](/docs/images/htmlValidatorRegistration.png)

#### CSS Validation
- No Error founded
#### Python PEP8 Compliance
- All clear, no errors found
  ![PEP8](/docs/images/PEP8CI.png)
  

#### Accessibility


---

## Deployment

### Prerequisites

- Heroku account
- GitHub repository
- PostgreSQL database

### Environment Variables

Create an `env.py` file (NOT committed to Git) with:

```python
import os

os.environ.setdefault("DATABASE_URL", "your-postgresql-url")
os.environ.setdefault("SECRET_KEY", "your-secret-key")
os.environ.setdefault("DEBUG", "True")  # False for production
```

### Heroku Deployment Steps

1. **Create Heroku App**
   ```bash
   heroku create you-vs-hr
   ```

2. **Set Config Vars in Heroku Dashboard**
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `SECRET_KEY`: Django secret key
   - `DISABLE_COLLECTSTATIC`: 1 (initially)

3. **Connect GitHub Repository**
   - In Heroku Dashboard → Deploy tab
   - Select GitHub as deployment method
   - Search for and connect repository

4. **Deploy**
   - Choose branch (main)
   - Click "Deploy Branch"
   - Wait for build to complete

5. **Run Migrations**
   ```bash
   heroku run python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   heroku run python manage.py createsuperuser
   ```

7. **Collect Static Files**
   ```bash
   heroku run python manage.py collectstatic --noinput
   ```

### Local Development Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/omarazzawi/you-vs-hr.git
   cd you-vs-hr
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv my_env_312
   my_env_312\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**
   - Create `env.py` with your DATABASE_URL
   - Run migrations:
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access Application**
   - Open browser to http://127.0.0.1:8000/
   - Admin panel at http://127.0.0.1:8000/admin/


8. **PostgreSQL database hosting**

## Credits

#### Book
- **Django 5 By Example** [Django 5 By Example](https://www.amazon.se/-/en/Antonio-Mel%C3%A9/dp/1805125451)

#### YouTube channels
- **Abdelrahman Gamal** [Abdelrahman Gamal](https://www.youtube.com/watch?v=UPFKAG9rYOE) 
- **Django Crash Course – Python Web Framework** [freeCodeCamp.org](https://www.youtube.com/@freecodecamp)
- **Django Tutorial for Beginners | Full Course** [Telusko](https://www.youtube.com/watch?v=OTmQOjsl0eg)  
    

#### AI Assistance

- **Claude AI (Anthropic)**
  - Code review and optimization suggestions
  - Documentation assistance
  
- **DeepSeek AI**
  - Function explanations
  - Comment editing
  - README structure improvements

*Note: All AI-generated code was reviewed, tested, and customized to meet project requirements.*


- **draw.io** - Diagrams and visual representations

### Mentorship & Support

- **Spencer Barriball** - Code Institute Mentor
  - Project guidance and validation advice
  - Code review and best practices
  - Error handling
  - Recommended books

- **Code-Institute Django Reference Guide** 
  - Project foundation
- **Assessment Insights: PP4: What our Assessors Wish You Knew**  [LucyRush Code-Institut](https://events.codeinstitute.net/events/details/code-institute-events-hub-presents-assessment-insights-pp4-what-our-assessors-wish-you-knew/)

## Author

**Omar Al-Azzawi**  
Full Stack Developer Student
[GitHub](https://github.com/omarazzawi) | [LinkedIn](https://www.linkedin.com/in/omar-alazzawi/) 

---




*Last Updated: November 2025*
*Django 5.2.8 | Python 3.12,10 | Bootstrap 5*



