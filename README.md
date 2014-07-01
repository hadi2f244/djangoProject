djangoProject
=============

We are working on three  part :

* Blog
* Ecommerce
* Courseware

In this project python version is 2.7 and also django version is 1.5.5 we choose this version cause the changes between 1.6 and 1.5 please take look at change logs in [django webpage]( https://www.djangoproject.com/ ) . Upto now Blog part in approximately at the end of developing and it will be finished soon .

Content

* Blog
 - Installation
   - Required
 - Optional
 - Running
   - Localhost
   - Serving on the server

Blog
================

### Installation

* Required

1. Download djangoProject to your computer .
  - ```git clone https://github.com/hadi2f244/djangoProject.git```
2. go to directory .
  - ```cd djangoProject```
3. Install or add django-ckeditor, django-haystack , django-dajaxice, django-dajax to your python path.
  - ``` pip install django=1.5.5 django-ckeditor django-haystack django-dajaxice django-dajax ```
4. Collecting statics files in STATIC_ROOT .
  - ``` python manage.py collect static ```

### Optional

### Running

* Localhost
```python manage.py runserver```
* serving on the server





