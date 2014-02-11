all: download_data 
	# process_*

clean: clean_processed clean_raw

prepare_processed:
	mkdir -p processed
	# mkdir -p processed/<module>

clean_processed:
	# rm -rf processed/<module>

clean_raw:
	# rm -rf raw/<module>*

clean_data:
	rm -rf raw

download_data:
	mkdir -p raw
	# curl -L "<url>" -o raw/<module>.zip
	# unzip raw/<module>.zip -d raw/<module>


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


process_parcels: prepare_processed
	mkdir -p processed/parcels
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/parcels/parcels.shp raw/parcels/Parcels.shp

clip_parcels_to_council_districts:
	mkdir -p processed/parcels/split
	ogrinfo -ro -al -geom=NO -fields=YES -sql "SELECT DISTRICT FROM councildistricts" -q processed/councildistricts/councildistricts.shp | \
		sed '/^\$$/d' | sed '/OGR/d' | sed '/Layer/d' | sed 's/\s*DISTRICT.*= //' | sort -n | \
		xargs -I{} ogr2ogr -overwrite -clipsrc processed/councildistricts/split/council_district_{}.shp processed/parcels/split/council_district_{}.shp processed/parcels/parcels.shp
