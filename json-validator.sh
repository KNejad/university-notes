#validates all json files
shopt -s globstar
for f in **/*.json
do
 echo "Processing $f"
 jq ".Title" $f
done

