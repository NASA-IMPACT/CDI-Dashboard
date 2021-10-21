from cap_package.CAP import CAP
from .models import *

def run_cap():
	
	# Run Cap Program #

	masterlist = ""

	cap = CAP(masterlist)
    cap.ingest_datasets()

    # Run QA
    cap.run_qa()

    # Execute Climate Tag Check
    cap.climate_tag_check()

    # Not in Masterlist Check
    cap.not_in_masterlist_check()

    # Create Metrics
    cap.create_cdi_metrics()
    cap.create_warnings_summary()

    # Gather Metrics
    all_metrics = cap.export_all()

	# and put output in the models/database


	#loop through the retag dictionary:

		#add a record to the retag DB including the data.gov_id and the CAP_id









run_cap()
