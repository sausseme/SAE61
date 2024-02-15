docker run --rm -d \
	-p 3307:3306\
	-v vol-sql-demo:/var/lib/mysql \
	--name sae51-sql \
	--env MYSQL_ROOT_PASSWORD=foo \
	--network net-tp4 \
	--mount type=bind,source=/home/user/SAE51,target=/srv/csv \
	mysql:8.0 --local-infile=1 --secure-file-priv=''