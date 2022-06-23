from copy import copy
from odoo import fields, models, api

class Property(models.Model):
	_name = "estate.property"
	_description = "A test description for the test model 'Property'."


	name = fields.Char("Property", translate=True, required=True)
	description = fields.Text(translate=True)
	postcode = fields.Char("Postcode", translate=True)
	date_availability = fields.Date(copy=False, default=lambda self : fields.Date.add(fields.Datetime.today(), months=3))
	expected_price = fields.Float(digits=(12,2), required=True)
	selling_price = fields.Float(digits=(12,2), readonly=True, copy=False)
	bedrooms = fields.Integer(default=2)
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection([('north', 'North'),('south', 'South'),('east', 'East'),('west', 'West')])
	active = fields.Boolean(default=True)
	state = fields.Selection([('new', 'New'), ('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], required=True, copy=False, default='new')
	property_type_id = fields.Many2one("estate.property.type", string="Property Type")
	buyer_id = fields.Many2one("res.partner", copy=False)
	salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
	tag_ids = fields.Many2many("estate.property.tag", string="Tags")
	offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
	total_area = fields.Integer(compute="_compute_total_area")
	best_price = fields.Float(compute="_get_max_price")



	@api.depends("offer_ids.price")
	def _get_max_price(self):
		for record in self:
			if len(record.offer_ids) > 0:
				record.best_price = max(record.offer_ids.mapped('price'))
			else:
				record.best_price = 0


	@api.depends("living_area", "garden_area")
	def _compute_total_area(self):
		for record in self:
			record.total_area = record.living_area + record.garden_area
