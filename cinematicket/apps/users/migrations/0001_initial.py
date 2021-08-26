# Generated by Django 3.2.6 on 2021-08-26 18:43

import cinematicket.apps.users.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Required. 50 letters or fewer",
                        max_length=50,
                        verbose_name="first name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Required. 50 letters or fewer",
                        max_length=50,
                        verbose_name="last name",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with that email already exists."
                        },
                        help_text="Required. Valid email address of 30 letters or fewer",
                        max_length=100,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that phone number already exists."
                        },
                        help_text="Required. Must be max 17 digits in the format: '+999999999'",
                        max_length=17,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                        verbose_name="phone",
                    ),
                ),
                (
                    "user_id",
                    models.UUIDField(
                        help_text="Required. Must be 36 characters",
                        verbose_name="user id",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="date of birth"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(default=False, verbose_name="verified"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "auth_user",
            },
            managers=[
                ("objects", cinematicket.apps.users.models.UserManager()),
            ],
        ),
    ]
