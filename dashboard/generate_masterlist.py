import os
import json
import sys
import urllib
import requests

if __name__ == '__main__':
    from models import Masterlist
else:
    from .models import Masterlist

def create_ml(local=False):
    # Get Test Masterlist

    if local:
        cwd = os.getcwd()
        test_loc = os.path.join(cwd, 'cap_package/CAP/test/test_json.json')

        try:
            with open(test_loc) as testfile:
                masterlist_json = json.load(testfile)
        except:
            print('The expected test file location is missing: "{}"'.format(test_loc))
            sys.exit()
    else:
        github_response = urllib.request.urlopen(r'https://raw.githubusercontent.com/NASA-IMPACT/cdi_master/master/UpdatedMasterList_Aug2021.json')
        masterlist_json = json.load(github_response)

    for dataset in masterlist_json:
        #print(dataset)

        ml_entry = Masterlist(name = dataset["name"],
                            title = dataset["title"],
                            organization = dataset["organization"],
                            catalog_url = dataset["catalog_url"],
                            api_url = dataset["api_url"],
                            cdi_themes = dataset["cdi_themes"],
                            metadata_type = dataset["metadata_type"],
                            geoplatform_id = dataset["geoplatform_id"],
                            status = dataset["status"],
                            datagov_ID = dataset["datagov_ID"])
        print(ml_entry)

        ml_entry.save()