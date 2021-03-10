import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'


if __name__ == '__main__':
    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: The project slug ({}) is not a valid Python'.format(module_name)
              'module name. Please do not use a - and use _ instead')

        # Exit to cancel project
        sys.exit(1)
