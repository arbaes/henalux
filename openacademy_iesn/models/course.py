# -*- coding: utf-8 -*-
import random

from odoo import models,fields


class Course(models.Model):
    _inherit = 'openacademy.course'

    # example of computed fields
    stupid_example = fields.Char(string="This course is", compute="_compute_stupid")

    def _compute_stupid(self):
        kinds_of_stupid = ["stupid", "ignorant", "dense", "brainless", "mindless", "foolish",
                           "dull-witted", "witless", "slow", "dunce-like", "simple-minded",
                           "empty-headed", "vacuous", "vapid", "half-witted", "idiotic",
                           "moronic", "imbecilic", "imbecile", "obtuse", "informalthick",
                           "thick as two short planks", "dim", "dumb", "dopey", "dozy",
                           "cretinous", "birdbrained", "pea-brained", "wooden-headed", "fat-headed"]
        for course in self:
            course.stupid_example = random.choice(kinds_of_stupid)
