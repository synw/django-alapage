# -*- coding: utf-8 -*-

def can_see_page(page, user):
    """
    To avoid queries pass a prefetched related page object: prefetch 'users_only' and/or 'groups_only'
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
    if page.is_reserved_to_groups is True:
        user_is_allowed = False
        for group in user.groups.all():
            if group in page.groups_only.all():
                user_is_allowed = True
                break
        return user_is_allowed
    if page.is_reserved_to_users is True:
        if user in page.users_only.all():
            return True
        else:
            return False
    if page.registration_required:
        if user.is_anonymous():
            return False
    return True