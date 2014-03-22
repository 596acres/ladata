# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ZoningDistrict'
        db.create_table(u'zoning_zoningdistrict', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('simplified_geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('zone_cmplt', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('zone_under', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('shape_len', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('zone_class', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('zone_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'zoning', ['ZoningDistrict'])


    def backwards(self, orm):
        # Deleting model 'ZoningDistrict'
        db.delete_table(u'zoning_zoningdistrict')


    models = {
        u'zoning.zoningdistrict': {
            'Meta': {'object_name': 'ZoningDistrict'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'simplified_geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'zone_class': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'zone_cmplt': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'zone_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zone_under': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['zoning']