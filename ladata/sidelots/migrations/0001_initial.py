# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SideLot'
        db.create_table(u'sidelots_sidelot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('no', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('cd', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('apn', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('cnt_apn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('intersection', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('land_sqft', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('access', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('zoning', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('tbpg', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('topography', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('source_of_funds', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('est_price_per_sqft_3_08', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('formula_3_08', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('class_c_3_08', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('remarks_by_appraisal', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('field_checked', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('phase', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('synopsis_comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('parcel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parcels.Parcel'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sidelots', ['SideLot'])


    def backwards(self, orm):
        # Deleting model 'SideLot'
        db.delete_table(u'sidelots_sidelot')


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
        },
        u'parcels.parcel': {
            'Meta': {'object_name': 'Parcel'},
            'ain': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'assrdata_m': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'block': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'editorname': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'globalid': ('django.db.models.fields.CharField', [], {'max_length': '38', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_roll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['localroll.LocalRollAEntry']", 'null': 'True', 'blank': 'True'}),
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
        },
        u'sidelots.sidelot': {
            'Meta': {'object_name': 'SideLot'},
            'access': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'apn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cd': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'class_c_3_08': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cnt_apn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_price_per_sqft_3_08': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'field_checked': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'formula_3_08': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intersection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'land_sqft': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'parcel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parcels.Parcel']", 'null': 'True', 'blank': 'True'}),
            'phase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remarks_by_appraisal': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'source_of_funds': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'synopsis_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tbpg': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'topography': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'zoning': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sidelots']