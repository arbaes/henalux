# Import des librairies standard de Python
import base64
import random
import requests
import logging

# Import des librairies d'Odoo
from odoo import models, fields
from odoo.exceptions import UserError

# Constantes utiles au modèles Odoo de ce fichier
GIPHY_KEY = "wNZ8xtjkJWcfhmoxLLZZPVQ4PjYdBmhb"
GIPHY_ENDPOINT = "http://api.giphy.com/v1/gifs/search"

# Initialisation du logger
_logger = logging.getLogger(__name__)

# Définition d'un Modèle Odoo
class ProjectTask(models.Model):


    # Définition du modèle. Dans ce cas si nous souhaitons modifier le modèle existant 'project.task'
    # Cfr: https://www.odoo.com/documentation/13.0/reference/orm.html#inheritance-and-extension
    _inherit = 'project.task'

    # C'est ici qu'il vous faudra rajouter un "relational field" pour faire un lien 
    # entre une 'project.task et un 'openacademy.course':
    # 'openacademy.course' est défini dans openacademy/models/course.py
    # Cfr: https://www.odoo.com/documentation/13.0/reference/orm.html#fields
    course_id = '???' 


    def assign_random_gif(self):
        """
        Fetch a random gif from Giphy and assign it as the task's cover image.

        Hours of the fun for the whole family!
        """
        self.ensure_one()
        
        # 0. Exemple d'utilisation du logger
        # _logger.info('COUCOU LES LOGS !')

        # 1. Il nous faut faire une requête à l'API de Giphy
        # Allez sur https://developers.giphy.com/docs/api/endpoint/ pour savoir comment la construire.

        try:
            r = requests.get(gif_api_url).json()
        except:
            raise UserError('LIKE HORRIBLY WRONG !')

        # 2. Si vous avez correctement construit votre requête, r['data'] devrait contenir 
        # une réponse de type GIF Objects, parsée comme un dictionnaire python.
        # Cfr: https://developers.giphy.com/docs/api/schema
        # Il vous faut maintenant extraire de ces données un lien direct vers un gif au hasard.
        gif_images_0 = r['data'][0]['images']

        # 3. Une fois l'url obtenue, il faut l'utiliser pour stocker directement le gif dans Odoo.
        # Comme c'est un peu technique, le code ci-dessous a déjà été fait en ce sens.
        if 'gif_url' not in locals() or not isinstance(gif_url, str):
            raise UserError('I cannot store something if it doesnt exist. (Maybe Quantic Odoo can ?)')
        ze_gif = requests.get(gif_url)
        stored_gif = self.env['ir.attachment'].create({
            'name': 'random-gif-task-{}.gif'.format(self.id),
            'datas': base64.b64encode(ze_gif.content),
            'res_model': self._name,
            'res_id': self.id
        })

        # 4. Liez maintenant ce gif à la couverture des vignettes kanban des taches
        # (Indice: le field qui sert à ça s'appelle 'displayed_image_id' et s'attend à recevoir un objet de type 'ir.attachment')
