# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Miracle.coord_y'
        db.delete_column('core_miracle', 'coord_y')

        # Deleting field 'Miracle.coord_x'
        db.delete_column('core_miracle', 'coord_x')

        # Deleting field 'Miracle.instag_tags'
        db.delete_column('core_miracle', 'instag_tags')

        # Adding field 'Miracle.instagram_tags'
        db.add_column('core_miracle', 'instagram_tags',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Miracle.flickr_tags'
        db.alter_column('core_miracle', 'flickr_tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Miracle.google_tags'
        db.alter_column('core_miracle', 'google_tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Miracle.description'
        db.alter_column('core_miracle', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Adding field 'Miracle.coord_y'
        db.add_column('core_miracle', 'coord_y',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=250),
                      keep_default=False)

        # Adding field 'Miracle.coord_x'
        db.add_column('core_miracle', 'coord_x',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=250),
                      keep_default=False)

        # Adding field 'Miracle.instag_tags'
        db.add_column('core_miracle', 'instag_tags',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=250),
                      keep_default=False)

        # Deleting field 'Miracle.instagram_tags'
        db.delete_column('core_miracle', 'instagram_tags')


        # Changing field 'Miracle.flickr_tags'
        db.alter_column('core_miracle', 'flickr_tags', self.gf('django.db.models.fields.CharField')(default=1, max_length=250))

        # Changing field 'Miracle.google_tags'
        db.alter_column('core_miracle', 'google_tags', self.gf('django.db.models.fields.CharField')(default=1, max_length=250))

        # Changing field 'Miracle.description'
        db.alter_column('core_miracle', 'description', self.gf('django.db.models.fields.TextField')(default=1))

    models = {
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miracle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Miracle']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '250'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Year']", 'null': 'True', 'blank': 'True'})
        },
        'core.miracle': {
            'Meta': {'object_name': 'Miracle'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flickr_tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'google_tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram_tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'views_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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