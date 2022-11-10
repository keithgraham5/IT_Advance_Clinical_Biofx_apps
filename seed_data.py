import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from web import models


# python manage.py seed_data
# --file "/home/keith/Data/Omimgenemap2.txt"
# --type 'omin_gene_map'
# --data_version 'version-1.0'
# class Command(BaseCommand):
#     help = "Seed data for a given source"
#
#     def add_arguments(self, parser):
#         parser.add_argument("--file", type=str, required=True)
#         parser.add_argument(
#             "--type",
#             type=str,
#             choices=[
#                 "BRCA1_variants"
#             ],
#             required=True,
#         )
#         parser.add_arguments("--data_version", type=str, required=True)
#
#     def handle(self, *args, **options):
#         if options["type"] == "BRAC1_variants":
#             self.stdout.write(self.style.SUCCESS("Importing BRCA1 "
#                                                  "variant data "))
#             _process_brca1_variants_list(options["file"])


variant_file_path = '/home/keith/Data/IT_Adv_Biofx_app/BRCA1 spreadsheet(' \
                    '2).txt'

def _process_txt(variant_list_file):


    # Read in the variant list file
    variant_dataframe = pd.read_csv(variant_list_file, on_bad_lines='skip',
                                    sep='\t', lineterminator='\n')
    # Create a pandas data frame
    variant_dataframe = pd.DataFrame(variant_dataframe)
    # Replace the null values with specified values
    variant_dataframe.fillna('', inplace=True)
    variant_dataframe.drop('Unnamed: 10', axis=1, inplace=True)
    # Change header names on dataframe
    variant_dataframe.columns = ['name','age','proband','affected_relatives',
                                 'Stage','tumor','sequencer','c_nomenclature',
                                 'variant_protein','g_nomenclature',
                                 'pathogenecity_code', 'evidence_codes']
    # Create a list of forenames
    forename_list = []
    # Create a list of surnames
    surname_list = []
    # Get full_name from name column
    for i in variant_dataframe.iterrows():
        # Get full name
        full_name = i[1]["name"]
        # Get forename from surname
        forename = full_name.strip().split(" ")[0]
        # Append forename to forename_list
        forename_list.append(forename)
        # Get surname from surname
        surname = full_name.strip().split(" ")[1]
        # Append surname to surname list
        surname_list.append(surname)
    # Add forename column to dataframe populate with forename_list
    variant_dataframe = variant_dataframe.assign(forename=forename_list)
    # Add surname column to the dataframe populate with surname_list
    variant_dataframe = variant_dataframe.assign(surname=surname_list)
    print(variant_dataframe)

    for index in variant_dataframe.index:
        model_entry, created = models.patient_identifier.objects.update_or_create(
            name=variant_dataframe['name'][index],
            age=variant_dataframe['age'][index],
            proband=variant_dataframe['proband'][index],
            affected_relatives=variant_dataframe['affected_relatives'][index],
            Stage=variant_dataframe['Stage'][index],
            sequencer=variant_dataframe['sequencer'][index],
            c_nomenclature=variant_dataframe['c_nomenclature'][index],
            variant_protein=variant_dataframe['variant_protein'][index],
            g_nomenclature=variant_dataframe['g_nomenclature'][index],
            pathogencity_code=variant_dataframe['pathogenecity_code'][index],
            evidenc_codes=variant_dataframe['evidence_codes'][index]
        )
        model_entry.save()


_process_txt(variant_file_path)




# Sanity check !!!
# print(full_name)
# print(forename)
# print(surname)
# print(forename_list)
# print(surname_list)
# print(variant_dataframe)






