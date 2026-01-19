# evaluacion_desempeno/models/evaluacion_desempeno.py
from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
 _name = 'evaluacion.desempeno'
 _description = 'Evaluación de desempeño'
 title = fields.Char(string='Título de la evaluación', required=True)
 employee_evaluated = fields.Many2one('hr.employee', string='Empleado evaluado',required=True)
 comments = fields.Text(string='Comentarios del evaluador')
 deadline = fields.Date(string='Fecha de evaluación')
 state = fields.Selection([
 ('pending', 'Pendiente'),
 ('in_progress', 'En Proceso'),
 ('done', 'Finalizado'),
 ], string='Estado', default='pending')
 score = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ],string='Puntuación')