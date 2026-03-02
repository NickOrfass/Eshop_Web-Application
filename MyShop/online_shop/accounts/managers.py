from django.contrib.auth.models import BaseUserManager

# Custom user manager class for handling user creation
class UserManager(BaseUserManager):
    
    # Method to create a regular user
    def create_user(self, email, full_name, password=None, **extra_fields):
        # Check if the email is provided
        if not email:
            raise ValueError('Email is required!')
        # Check if the full name is provided
        if not full_name:
            raise ValueError('Full name is required!')
        
        # Create a new user instance with normalized email and full name
        user = self.model(email=self.normalize_email(email), full_name=full_name, **extra_fields)
        # Set the user's password
        user.set_password(password)
        # Save the user to the database
        user.save(using=self._db)
        return user

    # Method to create a superuser
    def create_superuser(self, email, full_name, password=None, **extra_fields):
        # Set default values for is_staff, is_admin, is_manager and is_superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_manager', True)
        extra_fields.setdefault('is_superuser', True)

        # Ensure that is_staff is set to True
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        # Ensure that is_admin is set to True
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        # Ensure that is_manager is set to True
        if extra_fields.get('is_manager') is not True:
            raise ValueError('Superuser must have is_manager=True.')
        # Ensure that is_superuser is set to True
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Create and return the superuser
        return self.create_user(email, full_name, password, **extra_fields)
