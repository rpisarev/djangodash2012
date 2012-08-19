# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Miracle.views_count'
        db.add_column('core_miracle', 'views_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Miracle.views_count'
        db.delete_column('core_miracle', 'views_count')


    models = {
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miracle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Miracle']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '250'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Year']", 'null': 'True', 'blank': 'True'})
        },
        'core.miracle': {
            'Meta': {'object_name': 'Miracle'},
            'coord_x': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'coord_y': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'flickr_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'google_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instag_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'views_count': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.vote': {
            'Meta': {'object_name': 'Vote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Image']"}),
            'user_ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '1', 'decimal_places': '0'})
        },
        'core.year': {
            'Meta': {'object_name': 'Year'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']