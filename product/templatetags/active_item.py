from django import template

register = template.Library()


def active(url, request):
    '''
    Helper for detection active url in templates

    :param url:
    :param request:
    :return: True or False
    '''
    if url == request.get_full_path():
        return True
    else:
        return False


register.filter('active', active)
