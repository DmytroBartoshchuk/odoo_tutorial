# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DietFactsProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("Calories")
    serving_size = fields.Float("Serving Size")
    last_updated = fields.Date("Last updated")
    diet_item = fields.Boolean("Diet item")


class DietFactsResUsersMeal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char('Meal Name')
    meal_date = fields.Datetime('Meal Date')
    item_ids = fields.One2many('res.users.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users', 'Meal User')
    notes = fields.Text('Notes')


class DietFactsResUsersMealItems(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template', 'Menu item')
    servings = fields.Float('Servings')
    notes = fields.Text('Meal item notes')
