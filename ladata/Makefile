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

# process_<module>: prepare_processed
	# ogr2ogr -t_srs EPSG:4326 -overwrite processed/<module>/<module>.shp raw/<module>/<filename>.shp
