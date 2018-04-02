# coding:utf-8
from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u"账号")
    password = models.CharField(max_length=200, verbose_name=u"密码")
    phone = models.CharField(max_length=30, verbose_name=u"手机", null=False, default="")
    email = models.EmailField(null=True)
    SEX_CHOICES = (('F', 'Female'), ('M', 'Male'))
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True)
    age = models.SmallIntegerField(default=-1, blank=True)


    def __str__(self):
        return self.username

class User(models.Model):
    """
        Summary of class here.

        Longer class information....
        Longer class information....

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not.
            eggs: An integer count of the eggs we have laid.
        Author: 5stars
        BuildDate:
        Version:0.1
        Date:2017-12-23
        History:
    """
    username = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u"账号")
    password = models.CharField(max_length=200, verbose_name=u"密码")
    phone = models.CharField(max_length=30, verbose_name=u"手机", null=False, default="")
    email = models.EmailField(null=True)
    SEX_CHOICES = (('F', 'Female'), ('M', 'Male'))
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True)
    age = models.SmallIntegerField(default=-1, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        """Fetches rows from a Bigtable.

            Retrieves rows pertaining to the given keys from the Table instance
            represented by big_table.  Silly things may happen if
            other_silly_variable is not None.

            Args:
                big_table: An open Bigtable Table instance.
                keys: A sequence of strings representing the key of each table row
                    to fetch.
                other_silly_variable: Another optional variable, that has a much
                    longer name than the other args, and which does nothing.

            Returns:
                A dict mapping keys to the corresponding table row data
                fetched. Each row is represented as a tuple of strings. For
                example:

                {'Serak': ('Rigel VII', 'Preparer'),
                 'Zim': ('Irk', 'Invader'),
                 'Lrrr': ('Omicron Persei 8', 'Emperor')}

                If a key from the keys argument is missing from the dictionary,
                then that row was not found in the table.

            Raises:
                IOError: An error occurred accessing the bigtable.Table object.
        """
        return self.username



class LzhTest(models.Model):
    username = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u"this is 账号")
    password = models.CharField(max_length=200, verbose_name=u"this is密码")
    phone = models.CharField(max_length=30, verbose_name=u"this is手机", null=False, default="")
    email = models.EmailField(null=True)
    SEX_CHOICES = (('F', 'Female'), ('M', 'Male'))
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True)
    age = models.SmallIntegerField(default=-1, blank=True)


    def __str__(self):
        return self.username
