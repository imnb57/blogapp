from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import BlogForm
from .models import Blog
from django.http import Http404

def home(request):
    return render(request, "blog/home.html")

@login_required
def profile(request):
    return render(request, "blog/profile.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "blog/auth/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login after logout

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save the user without committing to the database
            user.set_password(form.cleaned_data["password"])  # Hash the password
            user.save()  # Now save the user with the hashed password
            login(request, user)  # Log the user in
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "blog/auth/registration.html", {"form": form})

@login_required
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blogs/blog_list.html', {'blogs': blogs })

# View to display a single blog
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blogs/blog_detail.html', {'blog': blog})

# View to create a new blog
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # associate the blog with the logged-in user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blogs/blog_form.html', {'form': form})

@login_required
def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)

    # Check if the logged-in user is the owner of the blog post
    if blog.user != request.user:
        raise Http404("You do not have permission to delete this blog post.")

    # If the user is the owner, delete the blog
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')  # Redirect to the blog list page after deleting

    return render(request, 'blog/blogs/blog_confirm_delete.html', {'blog': blog})

# View to edit an existing blog (optional)
@login_required
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.user != request.user:
        return redirect('blog_list')  # Ensure that the user can only edit their own blog

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blogs/blog_form.html', {'form': form})