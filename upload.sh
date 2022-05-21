#python manage.py upload_data --infile Data/refined_metadata_2_metadata_refined.csv
#python manage.py upload_data --infile ../Database_bkp/Database/Data/test.csv

for fl in $(ls /home/devil/Documents/Tools/H3A/MicroBiomeDatabase/AMPData/Corrected/*.csv); do
        echo $fl

        python manage.py upload_data --infile $fl \
                --elo_wiki_file /home/devil/Documents/Tools/H3A/MicroBiomeDatabase/AMPData/fixed/elo_wiki.csv \
                --participant_summary_file /home/devil/Documents/Tools/H3A/MicroBiomeDatabase/AMPData/fixed/project_summary.csv
        break
done
#../Database_bkp/Database/Data/mgp12183.csv
#python manage.py upload_data --infile Data/refined_metadata_1_12_03_Main.csv
