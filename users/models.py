from django.db import models


class User(models.Model):
    USER_STATUS = (
        ("Active", "Active"),
        ("Pending", "Pending"),
        ("Inactive", "Inactive"),
    )
    first_name = models.CharField(
        max_length=20, help_text="Required. 20 letters or fewer"
    )
    last_name = models.CharField(
        max_length=20, help_text="Required. 20 letters or fewer"
    )
    user_id = models.UUIDField(
        max_length=36, help_text="Required. Must be 36 characters"
    )
    phone = models.CharField(
        max_length=11,
        help_text="Required. Must be 11 numbers",
        error_messages={"unique": "A user with that phone number already exists."},
    )
    email = models.EmailField(
        max_length=30,
        unique=True,
        help_text="Required. Valid email address of 30 letters or fewer",
        error_messages={"unique": "A user with that email already exists."},
    )
    password = models.CharField(
        max_length=100,
        help_text="Required. Valid password must be 8 characters or more",
    )
    dob = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(
        choices=USER_STATUS,
        max_length=10,
        error_messages={"invalid_choice": "Invalid choice"},
    )

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
