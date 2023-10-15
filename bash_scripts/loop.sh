while read line; do  
	echo $line
	az acr repository delete -n taconvsummary.azurecr.io --repository  $line -y
done < output2.txt