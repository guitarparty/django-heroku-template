from django_assets import Bundle, register

js = Bundle(
	'js/jquery-1.8.2.js',
	'js/bootstrap.js',

	filters='yui_js',
	output='../globalstatic/bundles/app.js')

css = Bundle(
    'css/bootstrap.css',
    'css/bootstrap-responsive.css',

    output='../globalstatic/bundles/app.css')


register('js_app', js)
register('css_app', css)