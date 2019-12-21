# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Control(models.Model):
    name = models.CharField(max_length=225)  # name of the control

    # choices for types of controls
    Primitive = 'Primitive'
    CORPSE = 'CORPSE'
    Gaussian = 'Gaussian'
    CinBB = 'CinBB'
    CinSK = 'CinSK'
    type_choices = [
        (Primitive, 'Primitive'),
        (CORPSE, 'CORPSE'),
        (Gaussian, 'Gaussian'),
        (CinBB, 'CinBB'),
        (CinSK, 'CinSK')
    ]
    type = models.CharField(max_length=10, choices=type_choices, default=Primitive)  # type of control

    maximum_rabi_rate = models.FloatField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]  # validation between 1 and 100
    )

    polar_angle = models.FloatField(
        validators=[MaxValueValidator(1), MinValueValidator(0)]  # validation between 0 and 1
    )

