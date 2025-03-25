from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Custom manager
class Mymanager(BaseUserManager):
    def create_user(self, email, password=None, firstName=None, lastName=None):
        if not email:
            raise ValueError("The Email is required")

        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

# Custom User model
class User(AbstractBaseUser):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128, blank=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    objects = Mymanager()  # Link custom manager
    USERNAME_FIELD = 'email'  # ✅ Django requires this field
    REQUIRED_FIELDS = ['firstName', 'lastName'] 

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.title
