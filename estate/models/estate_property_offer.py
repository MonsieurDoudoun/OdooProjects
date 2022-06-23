from pkg_resources import require
from odoo import fields, models, api
import datetime

class PropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection(copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline")


    @api.depends("create_date", "validity")
    def _compute_deadline(self):
        for record in self:
            if (not(record.create_date)):
                record.create_date = fields.Datetime.now()
            record.date_deadline = fields.Date.add(record.create_date, days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            if (not(record.create_date)):
                record.create_date = fields.Datetime.now()
            record.validity = (record.date_deadline - record.create_date).days