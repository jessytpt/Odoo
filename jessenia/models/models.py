# -*- coding: utf-8 -*-

from odoo import models, fields, api

class atabla(models.Model):
     _name = 'jessenia.atabla'

     name = fields.Char(string="Nombre")
     age = fields.Integer(string="Edad")
     promedio = fields.Float(string="Promedio")
     tablab = fields.Many2one('jessenia.btabla',string="tabla B")

class btabla(models.Model):
     _name='jessenia.btabla'

     name = fields.Char(string="Provincia")
     province = fields.Selection([('a','Ambato'),('b','Baños'),('c','Pelileo')],'Ciudades')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
