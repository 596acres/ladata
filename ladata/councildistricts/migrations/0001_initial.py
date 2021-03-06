# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CouncilDistrict'
        db.create_table(u'councildistricts_councildistrict', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('simplified_geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('cdmember', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('sq_mi', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('shadesym', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('revised', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'councildistricts', ['CouncilDistrict'])


    def backwards(self, orm):
        # Deleting model 'CouncilDistrict'
        db.delete_table(u'councildistricts_councildistrict')


    models = {
        u'councildistricts.councildistrict': {
            'Meta': {'object_name': 'CouncilDistrict'},
            'cdmember': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'revised': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'shadesym': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'simplified_geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'sq_mi': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['councildistricts']