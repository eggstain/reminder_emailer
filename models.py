#Copyright 2016 Matthew Krohn
#
#This file is part of Reminder Emailer.
#
#Basic Inventory is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from django.db import models
import settings
import datetime

# Create your models here.

class separatedEmployee(models.Model):
    """Some task that needs periodic reminder emails sent"""
    name = models.CharField(max_length=200)
    manager_email = models.CharField(max_length=200)
    set_date = models.DateField('Task Initiated Date')
    def __str__(self):
        return self.name