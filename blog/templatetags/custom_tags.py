from django import template

register = template.Library()


@register.filter
def author_status(obj, user_id):
    return obj.author_status(user_id)
