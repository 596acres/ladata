# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProtectedArea'
        db.create_table(u'protectedareas_protectedarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agncy_name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('access_typ', self.gf('django.db.models.fields.CharField')(max_length=17, null=True, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('agncy_lev', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('agncy_web', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('layer', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('mng_agncy', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('label_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('own_type', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('unit_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('superunit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('agncy_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mng_ag_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gis_acres', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'protectedareas', ['ProtectedArea'])


    def backwards(self, orm):
        # Deleting model 'ProtectedArea'
        db.delete_table(u'protectedareas_protectedarea')


    models = {
        u'protectedareas.protectedarea': {
            'Meta': {'object_name': 'ProtectedArea'},
            'access_typ': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'agncy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'agncy_lev': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'agncy_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'agncy_web': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'gis_acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'layer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'mng_ag_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mng_agncy': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'own_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'superunit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'unit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['protectedareas']