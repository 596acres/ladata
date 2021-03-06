# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocalRollAEntry'
        db.create_table(u'localroll_localrollaentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ain', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tra', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('admin_region_no', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('common_area_ky', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('yr_sold_to_state', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('recording_date', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('land_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('improvement_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gpp_ky', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('exmpt_claim_type_ky', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('gpp_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fixture_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('real_est_exmpt_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pp_exmpt_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fixture_exmpt_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hmownr_exmpt_value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('first_owner_assee_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('first_owner_name_overflow', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('second_owner_assee_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('special_name_assee', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('sa_ky', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('sa_date_of_last_chng', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sa_postal_city_cde', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('sa_house_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sa_fraction', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('sa_direction', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('sa_unit', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('sa_zip_cde', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sa_street_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('sa_city_and_state', self.gf('django.db.models.fields.CharField')(max_length=48, null=True, blank=True)),
            ('mao_ky', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('mao_date_of_last_chng', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mao_postal_city_cde', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('ma_house_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ma_fraction', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('ma_direction', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('ma_unit', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('ma_zip_cde', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ma_street_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('ma_city_and_state', self.gf('django.db.models.fields.CharField')(max_length=48, null=True, blank=True)),
            ('ldll_narative', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('ldll_lot', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('ldll_division', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('ldll_region', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('ld_line1', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('ld_line2', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('ld_line3', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('ld_line4', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('ld_line_5', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('zoning_code', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('use_cde', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('effective_yr', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('yr_built', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('built_sq_ft_main', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'localroll', ['LocalRollAEntry'])


    def backwards(self, orm):
        # Deleting model 'LocalRollAEntry'
        db.delete_table(u'localroll_localrollaentry')


    models = {
        u'localroll.localrollaentry': {
            'Meta': {'object_name': 'LocalRollAEntry'},
            'admin_region_no': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'ain': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'built_sq_ft_main': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'common_area_ky': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'effective_yr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exmpt_claim_type_ky': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'first_owner_assee_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'first_owner_name_overflow': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'fixture_exmpt_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fixture_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gpp_ky': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'gpp_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hmownr_exmpt_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improvement_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'land_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ld_line1': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ld_line2': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ld_line3': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ld_line4': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ld_line_5': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ldll_division': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ldll_lot': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ldll_narative': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'ldll_region': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'ma_city_and_state': ('django.db.models.fields.CharField', [], {'max_length': '48', 'null': 'True', 'blank': 'True'}),
            'ma_direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'ma_fraction': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'ma_house_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ma_street_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'ma_unit': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'ma_zip_cde': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mao_date_of_last_chng': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mao_ky': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'mao_postal_city_cde': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'pp_exmpt_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'real_est_exmpt_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recording_date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sa_city_and_state': ('django.db.models.fields.CharField', [], {'max_length': '48', 'null': 'True', 'blank': 'True'}),
            'sa_date_of_last_chng': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sa_direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sa_fraction': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'sa_house_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sa_ky': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sa_postal_city_cde': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'sa_street_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'sa_unit': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'sa_zip_cde': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'second_owner_assee_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'special_name_assee': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'tra': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'use_cde': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'yr_built': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yr_sold_to_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zoning_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['localroll']