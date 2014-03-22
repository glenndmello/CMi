#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.split(__file__)[0], '../../')))
sys.path.append(os.path.abspath(os.path.join(os.path.split(__file__)[0], '..')))

args = ['CMi/manage.py', 'runserver', '0.0.0.0:8000', '--noreload']

if __name__ == "__main__":
    import sys
    sys.stderr = sys.stdout
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMi.settings")
    
    print 'path:', sys.path

    from CMi import migrate
    migrate()

    from django.core.management import execute_from_command_line

    execute_from_command_line(args)
