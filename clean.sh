rm -r MicroBiome/__pycache__
rm -r MicroBiome/migrations
rm db.sqlite3
python manage.py makemigrations MicroBiome
python manage.py migrate
python manage.py su

git clone https://github.com/codemeleon/AMPData

for fl in $(ls /home/app/african_microbiome_portal/AMPData/Corrected/*.csv); do
        echo $fl

        python manage.py upload_data --infile $fl \
                --elo_wiki_file /home/app/african_microbiome_portal/AMPData/fixed/elo_wiki.csv \
                --participant_summary_file /home/app/african_microbiome_portal/AMPData/fixed/project_summary.csv
        break
done
