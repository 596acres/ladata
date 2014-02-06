# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CommunityPlanArea'
        db.create_table(u'communityplanareas_communityplanarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cpa_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name_alf', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('shape_len', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'communityplanareas', ['CommunityPlanArea'])


    def backwards(self, orm):
        # Deleting model 'CommunityPlanArea'
        db.delete_table(u'communityplanareas_communityplanarea')


    models = {
        u'communityplanareas.communityplanarea': {
            'Meta': {'object_name': 'CommunityPlanArea'},
            'cpa_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_alf': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['communityplanareas']