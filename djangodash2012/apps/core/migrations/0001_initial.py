# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Object'
        db.create_table('core_object', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('coord_x', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('coord_y', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('instag_tags', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('google_tags', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('core', ['Object'])

        # Adding model 'Year'
        db.create_table('core_year', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['Year'])

        # Adding model 'Images'
        db.create_table('core_images', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=250)),
            ('object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Object'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Year'])),
        ))
        db.send_create_signal('core', ['Images'])


    def backwards(self, orm):
        # Deleting model 'Object'
        db.delete_table('core_object')

        # Deleting model 'Year'
        db.delete_table('core_year')

        # Deleting model 'Images'
        db.delete_table('core_images')


    models = {
        'core.images': {
            'Meta': {'object_name': 'Images'},
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
        'core.year': {
            'Meta': {'object_name': 'Year'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']