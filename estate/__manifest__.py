{
	'name': "estate",
	'depends': ["base"],
	'description': "Test module - Real Estate App",
	'application': True,
	'installable': True,
	'data': [
		'security/ir.model.access.csv',
		'views/estate_property_views.xml',
		'views/estate_property_type_views.xml',
		'views/estate_property_tag_views.xml',
		'views/estate_menus.xml'
		],

}
