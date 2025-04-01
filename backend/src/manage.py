#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv[1] == "startapp":
        app_path = os.path.join("apps", sys.argv[2])
        os.makedirs(app_path, exist_ok=True)
        sys.argv.append(app_path)
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
