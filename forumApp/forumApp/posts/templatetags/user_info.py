from django import template

register = template.Library()


@register.inclusion_tag(filename='forum/include/user_info.html', takes_context=True)
def user_info(context):
    print(context)
    print(context.request.user.username)
    if context.request.user.is_authenticated:
        return {
            'username': context.request.user,
        }
    return {
        'username': 'Anonymous',
    }

