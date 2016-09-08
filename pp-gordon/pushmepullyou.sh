case $1 in 
	--push|-ph)
		echo "push scenario"
		rsync --rsh=/usr/bin/ssh --verbose --progress --stats --recursive --times --perms . pp-gordon@r2d2.ifi.uzh.ch:~
		exit 0
	;;
	--pull|-pl)
		echo "pull scenario"
		rsync --rsh=/usr/bin/ssh --verbose --progress --stats --recursive --times --perms pp-gordon@r2d2.ifi.uzh.ch:~ ..
		exit 0
	;;
	--both|-b)
		echo "do both"
		rsync --rsh=/usr/bin/ssh --verbose --progress --stats --recursive --times --perms . pp-gordon@r2d2.ifi.uzh.ch:~	
		rsync --rsh=/usr/bin/ssh --verbose --progress --stats --recursive --times --perms pp-gordon@r2d2.ifi.uzh.ch:~ ..
		exit 0
	;;
	-*)
		echo "You need to specify a tag"
		echo '--push|-ph means push'
		echo '--pull|-pl means pull'
		echo '--both|-b means both'
		exit 1
	;;
esac
	
	echo "You need to specify a tag"
	echo '--push|-ph means push'
	echo '--pull|-pl means pull'
	echo '--both|-b means both'
	exit 1
