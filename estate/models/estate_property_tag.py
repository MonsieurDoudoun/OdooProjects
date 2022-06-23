from fnmatch import translate
from pkg_resources import require
from odoo import fields, models

class PropertyTag(models.Model):
    _name = "estate.property.tag"


    name = fields.Char(required=True, translate=True)