#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ipl.settings")
=======
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project3.settings")
=======
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project2.settings")
>>>>>>> a0d1c0dcac871169bbd0c2d26e116318b78e335a
>>>>>>> cc8fec921e57687fa85f0b4341a52601e30f0687
>>>>>>> b53dca2e558b6b48cde32e7fd927e316fb5e7e86
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
