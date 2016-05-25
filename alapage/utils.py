# -*- coding: utf-8 -*-


def can_see_page(page, user):
    """
    To avoid queries pass a prefetched related page object: prefetch 'users_only' and 'groups_only'
    """
    if user.is_superuser:
        return True
    if page.superuser_only is True:
        return False
    if page.staff_only is True:
        if user.is_staff:
            return True
        else:
            return False
    reserved_to_groups = page.groups_only.all()
    if len(reserved_to_groups) > 0:
        user_is_allowed = False
        for group in user.groups.all():
            if group in reserved_to_groups:
                user_is_allowed = True
                break
        return user_is_allowed
    reserved_to_users = page.users_only.all()
    if len(reserved_to_users) > 0:
        if user in reserved_to_users:
            return True
        else:
            return False
    return True