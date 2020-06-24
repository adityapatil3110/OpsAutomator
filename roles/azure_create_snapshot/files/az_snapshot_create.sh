#!/bin/bash


echo "COLLECT DISK NAMES"

declare -a DISK_NAME=$(az vm list -g "{{ resource_group }}" --query "[?tags.snapshot=='yes'].storageProfile.dataDisks[].name" -o tsv && az vm list -g "{{ resource_group }}" --query "[?tags.snapshot=='yes'].storageProfile.osDisk[].name" -o tsv)

for entry in "${DISK_NAME[@]}" ;
do 
 echo "$entry"
done

echo "Create snapshots of the listed disks"
Extension="_SNAPSHOT"

for entry in ${DISK_NAME[@]} ;
do
 az snapshot create -g "{{ resource_group }}"  -n "$entry${Extension}" --source "$entry"
done