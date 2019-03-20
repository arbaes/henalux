import base64
import random
import requests

from odoo import models, fields
from odoo.exceptions import UserError

GIPHY_KEY = "wNZ8xtjkJWcfhmoxLLZZPVQ4PjYdBmhb"
GIPHY_ENDPOINT = "http://api.giphy.com/v1/gifs/search"

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # add here a link to a course


    def assign_random_gif(self):
        """
        Fetch a random gif from Giphy and assign it as the task's cover image.

        Hours of the fun for the whole family!
        """
        self.ensure_one()
        # 1. Get a url to a gif from giphy
        # see https://developers.giphy.com/docs/ for the data structure you get in return and en example of the url to call
        pass
        # 2. Store gif in attachment
        # I'll do that part for you, just make sure that gif_url is an URL to a gif file online somewhere (string)
        if 'gif_url' not in locals() and not isinstance(gif_url, str):  # never mind me, just checking if the variable is available
            raise UserError('Implement me!')
        ze_gif = requests.get(gif_url)
        stored_gif = self.env['ir.attachment'].create({
            'name': 'random-gif-task-{}'.format(self.id),
            'datas': base64.b64encode(ze_gif.content),
            'datas_fname': 'random-gif-task-{}.gif'.format(self.id),
            'res_model': self._name,
            'res_id': self.id
        })
        # 3. Link gif to task & set as cover (hint: the field for that is displayed_image_id and it expects an 'ir.attachment' object)
        pass