import pandas as pd
import xmltodict
from django.core.management.base import BaseCommand, CommandError
from tqdm import tqdm
import lxml.etree as et
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Q
from django.db import models
import web


class Command(BaseCommand):
    help = "Seed data for a given source"

    def add_arguments(self, parser):
        parser.add_argument("--file", type=str, required=True)
        parser.add_argument(
            "--type",
            type=str,
            choices=[
                "variants_list"
            ],
            required=True,
        )
        parser.add_arguments( type=str, required=True)

    def handle(self, *args, **options):
        if options["type"] == "variants_list":
            self.stdout.write(self.style.SUCCESS("Importing variant data "))
            _parse_txt(options["file"])


variant_file_path = '/home/keith/Data/IT_Adv_Biofx_app/braca1_spreadsheet.txt'


def _parse_txt(variant_list_file):
    """ Parse txt file"""
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
    return variant_dataframe


variant_database = _parse_txt(variant_file_path)

def _upload_txt(variant_df):
    for index in variant_df.index:
        model_entry, created = \
            web.models.patient_identifier.objects.update_or_create(
                g_nomenclature=variant_df['g_nomenclature'][index],
                variant_protein=variant_df['variant_protein'][index],
                c_nomenclature=variant_df['c_nomenclature'][index],
            )
        model_entry.save()




def _upload_txt(variant_df):
    for index in variant_df.index:
        model_entry, created = \
            web.models.patient_identifier.objects.update_or_create(
                forename=variant_df['forename'][index],
                surname=variant_df['surname'][index],
                age=variant_df['age'][index],
                proband=variant_df['proband'][index],
                affected_relatives=variant_df['affected_relatives'][index],
                Stage=variant_df['Stage'][index],
                sequencer=variant_df['sequencer'][index],
                g_nomenclature=variant_df['g_nomenclature'][index],
                pathogenecity_code=variant_df['pathogenecity_code'][index],
                evidence_codes=variant_df['evidence_codes'][index]
        )
        model_entry.save()



_upload_txt(variant_database)



# Sanity check !!!
# print(full_name)
# print(forename)
# print(surname)
# print(forename_list)
# print(surname_list)
# print(variant_dataframe)
