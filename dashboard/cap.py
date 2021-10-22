from CAP import CAP

if __name__ == '__main__':
    from models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist
else:
    from .models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist 

def run_cap():
	
	# Run Cap Program #
    print('hello')
    '''
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


    '''

    




run_cap()
