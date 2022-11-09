import pandas as pd
from django.core.management.base import BaseCommand, CommandError


python manage.py seed_data
--file "/home/keith/Data/Omimgenemap2.txt"
--type 'omin_gene_map'
--data_version 'version-1.0'
class Command(BaseCommand):
    help = "Seed data for a given source"

    def add_arguments(self, parser):
        parser.add_argument("--file", type=str, required=True)
        parser.add_argument(
            "--type",
            type=str,
            choices=[
                "BRCA1_variants"
            ],
            required=True,
        )
        parser.add_arguments("--data_version", type=str, required=True)

    def handle(self, *args, **options):
        if options["type"] == "BRAC1_variants":
            self.stdout.write(self.style.SUCCESS("Importing BRCA1 "
                                                 "variant data "))
            _process_brca1_variants_list(options["file"])


variant_list_file = '/home/keith/Data/IT_Adv_Biofx_app/BRCA1 spreadsheet(2).txt
def _process_brca1_variant_list(variant_list_file):
    # Read in the variant list file
    variant_dataframe = pd.read_csv(variant_list_file, on_bad_lines='skip',
                                    sep='\t', lineterminator='\n', header=None )
    # Create a pandas data frame
    variant_dataframe = pd.DataFrame(variant_dataframe)
    # Replace the null values with specified values
    variant_dataframe.fillna('', inplace=True)
    # Store contents of variant_data
    new_header = variant_dataframe.iloc[0]
    variant_dataframe = variant_dataframe[1:]
    variant_dataframe.columns = new_header
    print(variant_dataframe)

