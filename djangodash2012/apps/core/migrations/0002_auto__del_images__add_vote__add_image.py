# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Images'
        db.delete_table('core_images')

        # Adding model 'Vote'
        db.create_table('core_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=1, decimal_places=0)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Image'])),
        ))
        db.send_create_signal('core', ['Vote'])

        # Adding model 'Image'
        db.create_table('core_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=250)),
            ('object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Object'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Year'])),
        ))
        db.send_create_signal('core', ['Image'])


    def backwards(self, orm):
        # Adding model 'Images'
        db.create_table('core_images', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=250)),
            ('object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Object'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Year'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Images'])

        # Deleting model 'Vote'
        db.delete_table('core_vote')

        # Deleting model 'Image'
        db.delete_table('core_image')


    models = {
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Object']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Year']"})
        },
        'core.object': {
            'Meta': {'object_name': 'Object'},
            'coord_x': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'coord_y': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'google_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instag_tags': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'core.vote': {
            'Meta': {'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Image']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '1', 'decimal_places': '0'})
        },
        'core.year': {
            'Meta': {'object_name': 'Year'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']