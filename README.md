# YOU VS HR

**🌐Live Application on Heroku** 
Access the platform here: [you-vs-hr](https://you-vs-hr-f560f6ced83c.herokuapp.com/)  

**GitHub**
[you-vs-hr](https://github.com/omarazzawi/you-vs-hr)  

**Project Board:**
[View Project Progress](https://github.com/users/omarazzawi/projects/11)

## Introduction

You VS HR is a Django-based web platform built for job seekers to share and analyze their experiences with recruiters, HR departments, and hiring processes. By providing a transparent space for candidates to document their recruitment journeys, the platform helps job seekers identify red flags and make informed decisions about potential employers. Unlike traditional employee review sites, we focus exclusively on the candidate experience during the hiring process.

## Features

### Current Features  

- **Story Sharing**: Share your recruitment experiences
- **Comment System**: Discuss and validate others' experiences
- **User Authentication**: Secure user registration and login
- **Dynamic Pages**: Editable About & Policies page
- **Admin Interface**: Full content management system

### Permission System

- **Edit Stories/Comments**: Available with author's permission
- **Delete Stories/Comments**: Authors can delete their own content
- **User Roles**: Registered users with appropriate permissions

## Technology Stack

- **Backend**: Django 5.2.8
- **Python Version**: 3.12.10
- **git version** 2.49.0.windows.1
- **Database**:  PostgreSQL (production)
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Django Allauth

## Testing  

  - ### Bug Fixes 
  
    #### Virtual Environment Conflicts
    - **Issue:** Multiple Python virtual environments installed causing version conflicts and path issues
    - **Problem:** Having several virtual environments (my_env_312, venv, env) created confusion about which environment was active and led to package dependency conflicts
    - **Solution:**
     - Removed all existing virtual environments except the current working environment (my_env_312)
     - Standardized on a single virtual environment for the project
     - Verified active environment using `my_env_312\Scripts\Activate` and `pip list` to confirm correct packages  
    
    #### Heroku Bad Request (400) Error
    - **Issue:** Application returning "Bad Request (400)" on Heroku deployment
    - **Problem:** Incorrect ALLOWED_HOSTS configuration in Django settings:```python
        ALLOWED_HOSTS = ['.herokuapp',  # ❌ Missing .com
                     '.127.0.0.1',] # ❌ Extra dot at beginning
    - **Solution**
    ALLOWED_HOSTS = ['.herokuapp.com',  # ✅ Correct domain
                     '127.0.0.1',]      # ✅ Correct localhost
    #### Environment Configuration Error
    - **Issue:** Environment variables not loading due to incorrect file namingconflicts and path issues
    - **Problem:** Environment configuration file named evn.py instead of correct env.py
    - **Solution:**
     - Renamed file from evn.py to env.py 
     - Verified environment variables are properly loaded
    #### Django Admin Prepopulated Fields Error
    - **Issue:** System check error preventing server startup
    - **Problem:** Incorrect field name in StoryAdmin prepopulated_fields:
    prepopulated_fields = {'slg': ('title',)}  # ❌ 'slg' field doesn't exist
    - **Solution:**
    Corrected field name to match actual model field:
    prepopulated_fields = {'slug': ('title',)}  # ✅ 'slug' field exists
    ### User Object Attribute Error
    - **Issue:** AttributeError when adding comments in Django admin
    - **Problem:** Code referencing 'useranme' attribute that doesn't exist:
    ❌ Typo in attribute name 'useranme'  # Missing 'e' in 'username'
    - **Solution:**
    Corrected attribute name to 'username'.
    ### Card Layout Alignment Issue
    - **Issue:** "Read More" buttons not aligned across cards with varying content heights
    - **Problem:** Inconsistent button positioning due to different content lengths in cards
    - **Solution:** Applied Flexbox layout with auto margin:
           ```css 
               .card-body {
                display: flex;
                flex-direction: column;
                min-height: 250px;
                }
                .card-text {
                flex-grow: 1;
                }  
                .card-body .btn {
                margin-top: auto;
               align-self: flex-start;
             }.

    #### Django application failing to start 
    - **Issue:** Django application failing to start due to import error
    - **Problem:**ImportError: cannot import name 'login_required' from 'django.contrib.auth' - incorrect import path for the login_required decorato
    - **Solution:**
     Fixed import in views.py:
     from django.contrib.auth.decorators import login_required  # ✅ Correct 
    #### StoryForm NameError
    - **Issue:** NameError: name 'StoryForm' is not defined when accessing /story/create/
    - **Problem:**StoryForm class not imported in views.py, causing NameError when trying to use it in story creation view
    - **Solution:**
     Added import in views.py:
     from .forms import StoryForm  # ✅ Import the missing form
    
    #### Django Auth Redirect Issue
    - **Issue:** Page not found (404) when accessing protected routes, Django looking for /accounts/login/ instead of /login/
    - **Problem:** Django's default authentication system redirects to /accounts/login/ but our login URL is at /login/
    - **Solution:**
      Add to settings.py:
      LOGIN_URL = '/login/'  # ✅ Tell Django to use our custom login URL
      LOGIN_REDIRECT_URL = '/'  # ✅ Redirect after successful login
      LOGOUT_REDIRECT_URL = '/'  # ✅ Redirect after logout
   
     #### CSS Specificity Fix for Button Positioning
    - **Issue:**  Absolute positioning applied to all buttons causing layout issues site-wide
    - **Problem:** CSS rule position: absolute; was affecting all buttons, not just the "Read More" buttons in story cards
    - **Solution:** Only apply absolute positioning to "Read More" buttons on story 
       .card-body .btn-primary {
        position: absolute;
        bottom: 15px;
        left: 15px;
       }
    #### Template Syntax Error
    - **Issue:** TemplateSyntaxError with invalid block tag  
    - **Problem:** Mismatched template tags - using 'endfor' inside an 'if' block:
    django
        {% if condition %}
    {% for item in items %}
        {{ item }}
    {% endfor %}  < 'endfor' inside 'if' block 
    {% endif %}
    - **Solution**
     {% if condition %}
     {% for item in items %}
        {{ item }}
     {% endfor %}
     {% endif %}  < ✅ Properly closed 'if' block 


## Deployment (Heroku)
### Prerequisites

- A Heroku account

- A linked GitHub repository containing this project

- Required environment variables (not committed to the repo)

- GitHub connected to Heroku

##### 1. Create a New Heroku App

- Log in to your Heroku Dashboard.

- Click New → Create new app.

- Enter a unique app name and select your region.

- Click Create app.

##### 2. Connect the App to GitHub

- In your Heroku app, go to the Deploy tab.

- Under Deployment method, choose GitHub.

- Search for your repository (e.g., you-vs-hr) and click Connect.

#### 3. Set Your Config Vars

Go to Settings → Config Vars and add the following environment variables:

  Key = Value 
- DATABASE_URL = xxxxx
- DISABLE_COLLECTSTATIC =	1 
- SECRET_KEY	= xxxxxx

#### 4. Deploy the Application

- In the Deploy tab, scroll to Manual deploy.

- Select the branch you want to deploy (typically main).

- Click Deploy Branch.

- Wait for the build to finish.

- Click Open App to launch your deployed application.


## Credits

- **Django 5 By Example** [Django 5 By Example](https://www.amazon.se/-/en/Antonio-Mel%C3%A9/dp/1805125451)
- **My mentor Spencer Barriball** - Project guidance, validation advice. 
- **Code-Institute Django Reference Guide** - Project foundation
- **Abdelrahman Gamal** Django tutorial | كورس دجانجو | ما هو الدجانجو؟
- **AI - clude** - Comment editing, function descriptions, and documentation assistance
- **AI - DeepSeek** - Functionality explanations, comment editing, and README file editing
- **Assessment Insights: PP4: What our Assessors Wish You Knew**[LucyRCode-Institut] (https://events.codeinstitute.net/events/details/code-institute-events-hub-presents-assessment-insights-pp4-what-our-assessors-wish-you-knew/)
- **draw.io** - Diagrams and visual representations