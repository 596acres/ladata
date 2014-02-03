from django.db import models


class LocalRollAEntry(models.Model):
    """
    Semi-automated model created using the LocalRollA table in the
    LocalRollA.mdb table in the county assessor's data.
    """
    ain = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='AIN'
    )
    tra = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text='TRA'
    )
    admin_region_no = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        help_text='Admin Region No'
    )
    common_area_ky = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        help_text='Common Area KY'
    )
    yr_sold_to_state = models.IntegerField(
        null=True,
        blank=True,
        help_text='Yr Sold to State'
    )
    recording_date = models.IntegerField(
        null=True,
        blank=True,
        help_text='Recording Date'
    )
    land_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='LAND Value'
    )
    improvement_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='Improvement Value'
    )
    gpp_ky = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        help_text='GPP KY'
    )
    exmpt_claim_type_ky = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        help_text='Exmpt Claim Type KY'
    )
    gpp_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='GPP Value'
    )
    fixture_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='Fixture Value'
    )
    real_est_exmpt_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='Real Est Exmpt Value'
    )
    pp_exmpt_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='PP Exmpt Value'
    )
    fixture_exmpt_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='Fixture Exmpt Value'
    )
    hmownr_exmpt_value = models.IntegerField(
        null=True,
        blank=True,
        help_text='Hmownr Exmpt Value'
    )
    first_owner_assee_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='1st Owner Assee Name'
    )
    first_owner_name_overflow = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='1st Owner Name Overflow'
    )
    second_owner_assee_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='2nd Owner Assee Name '
    )
    special_name_assee = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='Special Name Assee'
    )
    sa_ky = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        help_text='SA KY'
    )
    sa_date_of_last_chng = models.IntegerField(
        null=True,
        blank=True,
        help_text='SA Date of Last Chng'
    )
    sa_postal_city_cde = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text='SA Postal City Cde'
    )
    sa_house_number = models.IntegerField(
        null=True,
        blank=True,
        help_text='SA House Number'
    )
    sa_fraction = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text='SA Fraction'
    )
    sa_direction = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        help_text='SA Direction'
    )
    sa_unit = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        help_text='SA Unit'
    )
    sa_zip_cde = models.IntegerField(
        null=True,
        blank=True,
        help_text='SA ZIP Cde'
    )
    sa_street_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='SA Street Name'
    )
    sa_city_and_state = models.CharField(
        max_length=48,
        null=True,
        blank=True,
        help_text='SA City and State'
    )
    mao_ky = models.CharField(
        max_length=2,
		null=True,
		blank=True,
        help_text='MAO KY'
    )
    mao_date_of_last_chng = models.IntegerField(
        null=True,
        blank=True,
        help_text='MAO Date Of Last Chng'
    )
    mao_postal_city_cde = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text='MAO Postal City Cde'
    )
    ma_house_number = models.IntegerField(
        null=True,
        blank=True,
        help_text='MA House Number'
    )
    ma_fraction = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text='MA Fraction'
    )
    ma_direction = models.CharField(
        max_length=2,
		null=True,
		blank=True,
        help_text='MA Direction'
    )
    ma_unit = models.CharField(
        max_length=16,
		null=True,
		blank=True,
        help_text='MA Unit'
    )
    ma_zip_cde = models.IntegerField(
        null=True,
		blank=True,
        help_text='MA ZIP Cde'
    )
    ma_street_name = models.CharField(
        max_length=64,
		null=True,
		blank=True,
        help_text='MA Street Name'
    )
    ma_city_and_state = models.CharField(
        max_length=48,
		null=True,
		blank=True,
        help_text='MA City and State'
    )
    ldll_narative = models.CharField(
        max_length=80,
		null=True,
		blank=True,
        help_text='LDLL Narative'
    )
    ldll_lot = models.CharField(
        max_length=10,
		null=True,
		blank=True,
        help_text='LDLL Lot'
    )
    ldll_division = models.CharField(
        max_length=10,
		null=True,
		blank=True,
        help_text='LDLL Division'
    )
    ldll_region = models.CharField(
        max_length=6,
		null=True,
		blank=True,
        help_text='LDLL Region'
    )
    ld_line1 = models.CharField(
        max_length=80,
		null=True,
		blank=True,
        help_text='LD Line1'
    )
    ld_line2 = models.CharField(
        max_length=80,
		null=True,
		blank=True,
        help_text='LD Line2'
    )
    ld_line3 = models.CharField(
        max_length=80,
		null=True,
		blank=True,
        help_text='LD Line3'
    )
    ld_line4 = models.CharField(
        max_length=80,
		null=True,
		blank=True,
        help_text='LD Line4'
    )
    ld_line_5 = models.CharField(
        max_length=80,
		null=True,
		blank=True,
        help_text='LD Line 5'
    )
    zoning_code = models.CharField(
        max_length=30,
		null=True,
		blank=True,
        help_text='Zoning Code'
    )
    use_cde = models.CharField(
        max_length=8,
		null=True,
		blank=True,
        help_text='Use Cde'
    )
    effective_yr = models.IntegerField(
        null=True,
		blank=True,
        help_text='Effective Yr'
    )
    yr_built = models.IntegerField(
        null=True,
		blank=True,
        help_text='YR Built'
    )
    built_sq_ft_main = models.IntegerField(
        null=True,
		blank=True,
        help_text='Built SQ FT Main'
    )
