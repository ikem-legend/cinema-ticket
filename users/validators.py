from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class PasswordFormatValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})", password):
            raise ValidationError(
                _(
                    "This password must contain at least 1 lowercase, 1 uppercase, 1 number and %(min_length)d characters."
                ),
                code="password_pattern_invalid",
                params={"min_length": self.min_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase, 1 uppercase, 1 number and %(min_length)d characters."
            % {"min_length": self.min_length}
        )
