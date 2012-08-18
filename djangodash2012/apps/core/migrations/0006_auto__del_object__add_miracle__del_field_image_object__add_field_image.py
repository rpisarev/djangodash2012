# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Object'
        db.delete_table('core_object')

        # Adding model 'Miracle'
        db.create_table('core_miracle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('coord_x', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('coord_y', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('instag_tags', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('google_tags', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250)),
        ))
        db.send_create_signal('core', ['Miracle'])

        # Deleting field 'Image.object'
        db.delete_column('core_image', 'object_id')

        # Adding field 'Image.miracle'
        db.add_column('core_image', 'miracle',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Miracle']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Object'
        db.create_table('core_object', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250)),
            ('coord_y', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('coord_x', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('instag_tags', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('google_tags', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Object'])

        # Deleting model 'Miracle'
        db.delete_table('core_miracle')

        # Adding field 'Image.object'
        db.add_column('core_image', 'object',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Object']),
                      keep_default=False)

        # Deleting field 'Image.miracle'
        db.delete_column('core_image', 'miracle_id')


    models = {
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miracle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Miracle']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'source': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Year']"})
        },
        'core.miracle': {
            'Meta': {'object_name': 'Miracle'},
            'coord_x': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'coord_y': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'google_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instag_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250'})
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