
# 🍽️ Django Recipe App

This Django-based web application allows users to **register**, **login**, and **add/update/delete** their favorite recipes. A simple CRUD-based system for culinary creativity! 🥘✨

---
## Demo Video



https://github.com/user-attachments/assets/eec5e802-3968-4a16-8b03-e6f2e21dc585




## 🗂️ Project Features

- User Authentication (Register/Login)
- Recipe Submission (with image upload)
- Recipe Search
- Update/Delete Recipe functionality
- CSRF protection enabled
- Bootstrap styled forms and layout

---

## 📁 HTML Template Overview

### 🔐 `login.html`

- Extends: `base.html`
- Method: `POST`
- Fields:
  - Username
  - Password
- Features:
  - CSRF protection
  - Message rendering
  - Link to registration

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  <input type="text" name="username" />
  <input type="password" name="password" />
  <button type="submit">Submit</button>
</form>
```

---

### 📝 `register.html`

- Extends: `base.html`
- Method: `POST`
- Fields:
  - First name
  - Last name
  - Username
  - Password
- Features:
  - CSRF protection
  - Message rendering
  - Link to login page

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  <input type="text" name="first_name" />
  <input type="text" name="last_name" />
  <input type="text" name="username" />
  <input type="password" name="password" />
</form>
```

---

### 🍲 `recepies.html`

- Extends: `base.html`
- Method: `POST`
- Fields:
  - Recipe Name
  - Recipe Description
  - Recipe Image
- Features:
  - CSRF protection
  - Form to add recipes
  - Search bar
  - Table listing all recipes
  - Buttons for Update/Delete

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  <input name="receipe_name" />
  <textarea name="receipe_description"></textarea>
  <input type="file" name="receipe_image" />
</form>
```

---

### ♻️ `update_recepies.html`

- Extends: `base.html`
- Method: `POST`
- Fields (Pre-filled):
  - Recipe Name
  - Recipe Description
  - Recipe Image
- Features:
  - CSRF protection
  - Update existing recipe details

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  <input name="receipe_name" value="{{recepie.receipe_name}}" />
  <textarea name="receipe_description">{{recepie.receipe_description}}</textarea>
</form>
```

---

## 🛠️ Query Snippets

### Search Recipes
```python
# views.py
search_query = request.GET.get("search")
receipes = Receipe.objects.filter(receipe_name__icontains=search_query)
```

### Add Recipe
```python
if request.method == "POST":
    receipe = Receipe.objects.create(
        receipe_name=request.POST.get("receipe_name"),
        receipe_description=request.POST.get("receipe_description"),
        receipe_image=request.FILES.get("receipe_image")
    )
```

### Update Recipe
```python
if request.method == "POST":
    receipe.receipe_name = request.POST.get("receipe_name")
    receipe.receipe_description = request.POST.get("receipe_description")
    if request.FILES.get("receipe_image"):
        receipe.receipe_image = request.FILES.get("receipe_image")
    receipe.save()
```

---

## 🧾 Requirements

Make sure to install Django and configure the media directory for file uploads:

```bash
pip install django
```

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 📌 Notes

- All templates extend from `base.html` (not included here).
- The form includes CSRF tokens for security.
- Uploaded images are served from `/media/`.

Happy Coding! 🎉
