Permissions management
======================

Alapage provides page level permissions. Those with the ``can_change_page_permissions`` will be able to manage
them.

Pages access can be limited to:

- Logged in users
- Staff
- Groups
- Users

Note: for the groups and users pages you have to check the checkbox before selecting a group or user (this is
used internaly to avoid making a query when it is not strictly necessary to keep the things as 
fast and light as possible). 