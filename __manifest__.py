# evaluacion_desempeno/__manifest__.py
{
 'name': 'Evaluación de Desempeño',
 'version': '1.0',
 'summary': 'Gestión de las evaluaciones de desempeño',
 'description': 'Este módulo gestiona las evaluaciones de desempeño de los empleados de la empresa',
 'author': 'Cristina Benítez',
 'category': 'Human Resource',
 'website': 'https://tuweb.com',
 'license': 'LGPL-3',
 'depends': ['base','hr'],
 'icon': '/evaluacion_desempeno/static/description/icon53.png',
 'data': [
 'security/ir.model.access.csv', # Control de acceso
 'views/evaluacion_desempeno_views.xml', # Vista del módulo
 ],
 'installable': True,
 'application': True,
}