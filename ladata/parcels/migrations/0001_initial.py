# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parcel'
        db.create_table(u'parcels_parcel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('assrdata_m', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perimeter', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('phase', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('lot', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('moved', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('tra', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('pcltype', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('subdtype', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('tract', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('usecode', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('udate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('editorname', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('parcel_typ', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('unit_no', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('pm_ref', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('tot_units', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ain', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('globalid', self.gf('django.db.models.fields.CharField')(max_length=38, null=True, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('shape_len', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'parcels', ['Parcel'])


    def backwards(self, orm):
        # Deleting model 'Parcel'
        db.delete_table(u'parcels_parcel')


    models = {
        u'parcels.parcel': {
            'Meta': {'object_name': 'Parcel'},
            'ain': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'assrdata_m': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'block': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'editorname': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'globalid': ('django.db.models.fields.CharField', [], {'max_length': '38', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'moved': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parcel_typ': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pcltype': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'perimeter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'phase': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'pm_ref': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'subdtype': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'tot_units': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tra': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'tract': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'udate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'unit_no': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'usecode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['parcels']