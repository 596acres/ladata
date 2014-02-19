# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NeighborhoodCouncil'
        db.create_table(u'neighborhoodcouncils_neighborhoodcouncil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('simplified_geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perimeter', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cname1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cname2', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone2', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail2', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle2', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cname3', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone3', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail3', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle3', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cname4', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone4', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail4', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle4', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cname5', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone5', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail5', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle5', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cname6', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone6', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail6', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle6', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cname7', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cphone7', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('cemail7', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ctitle7', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('waddress', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('oaddr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ocity', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ozip', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('otel', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('ofax', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('dname1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('dphone1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('dname2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dphone2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dwebsite', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('demail', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('dphone', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('oid_field', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nc_id', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('certified', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('newsqmile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'neighborhoodcouncils', ['NeighborhoodCouncil'])


    def backwards(self, orm):
        # Deleting model 'NeighborhoodCouncil'
        db.delete_table(u'neighborhoodcouncils_neighborhoodcouncil')


    models = {
        u'neighborhoodcouncils.neighborhoodcouncil': {
            'Meta': {'object_name': 'NeighborhoodCouncil'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cemail1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cemail2': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cemail3': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cemail4': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cemail5': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cemail6': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cemail7': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'certified': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cname1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cname2': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cname3': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cname4': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cname5': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cname6': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cname7': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone2': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone3': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone4': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone5': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone6': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'cphone7': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle2': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle3': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle4': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle5': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle6': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ctitle7': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'demail': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'dname1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'dname2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dphone': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'dphone1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'dphone2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dwebsite': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'nc_id': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'newsqmile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'oaddr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ocity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ofax': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'oid_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otel': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'ozip': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'perimeter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'simplified_geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'waddress': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['neighborhoodcouncils']