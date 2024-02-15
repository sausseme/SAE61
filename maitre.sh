./purge.sh

./create_network.sh

if [ $? != 0 ]; then
	echo "echec de lancement du script  create_network.sh"
	exit 666
fi

./run_mysql.sh

if [ $? != 0 ]; then 
        echo "echec de lancement du script  run_mysql.sh"
        exit 666
fi

sleep 30

./filldb.sh

if [ $? != 0 ]; then 
        echo "echec de lancement du script filldb .sh"
	./run_mysql.sh
	./filldb.sh
fi

./launch.sh

if [ $? != 0 ]; then 
        echo "echec de lancement du script  tp4-app.sh"
        exit 666
fi