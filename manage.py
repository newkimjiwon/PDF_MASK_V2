#!/usr/bin/env python
"""장고 명령어의 시작점
내부에서 장고 세팅 모듈을 'pdfuploader.settings'로 지정.
서버 실행 : python manage.py runserver """
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdfuploader.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
