SHELL=/bin/bash

all: download_data 
	# process_*

clean: clean_processed clean_raw

prepare_processed:
	mkdir -p processed

clean_processed:
	# rm -rf processed/<module>

clean_raw:
	# rm -rf raw/<module>*

clean_data:
	rm -rf raw

download_data:
	mkdir -p raw
	download_buildings
	# curl -L "<url>" -o raw/<module>.zip
	# unzip raw/<module>.zip -d raw/<module>


download_buildings:
	mkdir -p raw/buildings
	curl -L "http://egis3.lacounty.gov/dataportal/wp-content/uploads/2012/11/lariac_buildings_2008.zip" -o raw/buildings/buildings.zip
	unzip raw/buildings/buildings.zip -d raw/buildings/


process_council_districts: prepare_processed
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/councildistricts/councildistricts.shp raw/councildistricts/LA_City_Council_Districts_2012.shp

# Use ogrinfo to get all district numbers, pipe them to ogr2ogr and split the
# shapefile using district numbers
split_council_districts:
	ogrinfo -ro -al -geom=NO -fields=YES -sql "SELECT DISTRICT FROM councildistricts" -q processed/councildistricts/councildistricts.shp | \
		sed '/^$$/d' | sed '/OGR/d' | sed '/Layer/d' | sed 's/\s*DISTRICT.*= //' | sort -n | \
		xargs -I{} ogr2ogr -overwrite -where "DISTRICT = '{}'" processed/councildistricts/split processed/councildistricts councildistricts -nln council_district_{}


process_buildings: prepare_processed
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/buildings/buildings.shp raw/buildings/lariac_buildings_2008.shp

clip_buildings_to_council_districts:
	mkdir -p processed/buildings/split
	ogrinfo -ro -al -geom=NO -fields=YES -sql "SELECT DISTRICT FROM councildistricts" -q processed/councildistricts/councildistricts.shp | \
		sed '/^\$$/d' | sed '/OGR/d' | sed '/Layer/d' | sed 's/\s*DISTRICT.*= //' | sort -n | \
		xargs -I{} ogr2ogr -overwrite -clipsrc processed/councildistricts/split/council_district_{}.shp processed/buildings/split/council_district_{}.shp processed/buildings/buildings.shp

push_buildings:
	tar czvf processed/buildings/buildings_split.tar.gz processed/buildings/split/*
	scp processed/buildings/buildings_split.tar.gz la:~/webapps/laopenacres/data/ladata/

load_buildings:
	ogrinfo -ro -al -geom=NO -fields=YES -sql "SELECT DISTRICT FROM councildistricts" -q processed/councildistricts/councildistricts.shp | \
		sed '/^\$$/d' | sed '/OGR/d' | sed '/Layer/d' | sed 's/\s*DISTRICT.*= //' | sort -n | \
		xargs -I{} django-admin.py loadladata buildings --council_district={}


process_parcels: prepare_processed
	mkdir -p processed/parcels
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/parcels/parcels.shp raw/parcels/parcels.shp

clip_parcels_to_council_districts:
	mkdir -p processed/parcels/split
	ogrinfo -ro -al -geom=NO -fields=YES -sql "SELECT DISTRICT FROM councildistricts" -q processed/councildistricts/councildistricts.shp | \
		sed '/^\$$/d' | sed '/OGR/d' | sed '/Layer/d' | sed 's/\s*DISTRICT.*= //' | sort -n | \
		xargs -I{} ogr2ogr -overwrite -clipsrc processed/councildistricts/split/council_district_{}.shp processed/parcels/split/council_district_{}.shp processed/parcels/parcels.shp

push_parcels:
	tar czvf processed/parcels/parcels_split.tar.gz processed/parcels/split/*
	scp processed/parcels/parcels_split.tar.gz la:~/webapps/laopenacres/data/ladata/

load_parcels:
	ogrinfo -ro -al -geom=NO -fields=YES -sql "SELECT DISTRICT FROM councildistricts" -q processed/councildistricts/councildistricts.shp | \
		sed '/^\$$/d' | sed '/OGR/d' | sed '/Layer/d' | sed 's/\s*DISTRICT.*= //' | sort -n | \
		xargs -I{} django-admin.py loadladata parcels --council_district={}


process_localroll: prepare_processed
	mkdir -p processed/localroll
	mdb-export raw/localroll/LocalRollA.mdb LocalRollA > processed/localroll/LocalRollA.csv

push_localroll:
	ssh la "mkdir -p ~/webapps/laopenacres/data/ladata/processed/localroll/"
	scp processed/localroll/LocalRollA.csv la:~/webapps/laopenacres/data/ladata/processed/localroll/LocalRollA.csv


process_protectedareas: prepare_processed
	mkdir -p processed/protectedareas
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/protectedareas/protectedareas.shp raw/protectedareas/CPAD_2013b_Units.shp
	ogr2ogr -overwrite -clipsrc processed/cityboundary/cityboundary.shp processed/protectedareas/protectedareas_clipped.shp processed/protectedareas/protectedareas.shp

push_protectedareas:
	tar czvf processed/protectedareas/protectedareas_clipped.tar.gz processed/protectedareas/protectedareas_clipped.*
	scp processed/protectedareas/protectedareas_clipped.tar.gz la:~/webapps/laopenacres/data/ladata/
