# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.happs'
        db.add_column(u'hedonometer_book', 'happs',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Book.length'
        db.add_column(u'hedonometer_book', 'length',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.happs'
        db.delete_column(u'hedonometer_book', 'happs')

        # Deleting field 'Book.length'
        db.delete_column(u'hedonometer_book', 'length')


    models = {
        u'hedonometer.book': {
            'Meta': {'ordering': "('author',)", 'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'happs': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hedonometer.event': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Event'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'longer': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'shorter': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wiki': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'x': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'y': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['hedonometer']