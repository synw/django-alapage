## Theming option

Theming option in Alapage is designed to let the website visitors choose a theme for the site. It uses sessions to remember the theme name from the user choice.

A theme is a base template and a css file. 

### Settings

Add `ALAPAGE_USE_THEMES = True` in settings

Set `ALAPAGE_THEMES` tuples with the slug and name of your themes to enable them.

  ```python
ALAPAGE_THEMES = (
                  ('dark','Dark !'),
                  ('light','Light'),
                  )
  ```
  
### Create themes

:one: In your `templates` folder create a `themes` folder. 

In this folder create subfolders for your themes (from the slug you chooses in `ALAPAGE_THEMES`): `dark`, `light` . These two can be found `alapage/templates/themes` for an example.

You can just copy your `base.html` template in these folders and start customizing.

:two: In `static` create a `themes` folder.

In this folder create subfolders for your themes (from the slug you chooses in `ALAPAGE_THEMES`): `dark`, `light` . These two can be found in `alapage/static/themes` for an example

You can extend your base css putting a `screen.css` file in theses folders.

### Make a menu in template for theme choosing

In a template use `current_theme` and `themes`

  ```HTML+Django
 	{% if current_theme %}
		<a href="{% url 'change-theme' theme='default' %}?from={{ request.get_full_path }}" class="btn btn-link">
			Remove theme
		</a>
	{% endif %}
	{% for theme in themes %}
		{% if not theme.0 == current_theme %}
		<a href="{% url 'change-theme' theme=theme.0 %}?from={{ request.get_full_path }}" class="btn btn-link">
			{{ theme.1 }}
		</a>
		{% endif %}
	{% endfor %}  
  ```
  
`current_theme` template variable is a `('theme_slug','Theme name')` tuple

`themes` template variable is a list of `('theme_slug','Theme name')` tuples


