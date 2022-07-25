# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _

help_texts = {
    'lino_welfare.projects.mathieu.tests.test_chatelet.TestCase' : _("""Miscellaneous tests on an empty database."""),
    'lino_welfare.projects.mathieu.tests.test_chatelet.TestCase.test_cv_obstacle' : _("""Test whether cv.Obstacle.user is correctly set to the requesting
user."""),
    'lino_welfare.projects.mathieu.tests.test_chatelet.TestCase.test_dupable_hidden' : _("""Since dupable_clients is hidden, we can create duplicate partners
without warning."""),
    'lino_welfare.projects.mathieu.tests.test_chatelet.TestCase.test_suggest_cal_guests' : _("""Tests a bugfix in suggest_cal_guests."""),
    'lino_welcht.lib.cv.ClientIsLearning' : _("""Select only clients who are “learning” during the given date.
That is, who have an active Study, Training or
Experience.
Only the start_date is used, end_date has no effect when
this criteria."""),
    'lino_welcht.lib.cv.Proof' : _("""A proof is some document which certifies that a given person
has a given skill."""),
    'lino_welcht.lib.cv.PersonProperty' : _("""Abstract base for Skill, SoftSkill and
Obstacle."""),
    'lino_welcht.lib.cv.Obstacle' : _("""An obstacle is an observed fact or characteristic of a client
which might be reason to not get a given job."""),
    'lino_welcht.lib.cv.Obstacle.type' : _("""A pointer to ObstacleType."""),
    'lino_welcht.lib.cv.Obstacle.user' : _("""The agent who observed this obstacle."""),
    'lino_welcht.lib.cv.Obstacle.detected_date' : _("""The date when the agent observed this obstacle."""),
}
