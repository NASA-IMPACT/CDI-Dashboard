import ast
from CAP import CAP

if __name__ == '__main__':
    from models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist
else:
    from .models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist

def run_cap():

    # Get CDI Masterlist from DB
    masterlist = Masterlist.objects.values()
    masterlist_json = list(masterlist) # Converts to list rather then QuerySet

    ## Run CDI Analysis Platform ##
    cap = CAP(masterlist_json)

    cap.ingest_datasets()
    cap.run_qa()
    cap.climate_tag_check()
    cap.not_in_masterlist_check()
    cap.create_cdi_metrics()
    cap.create_warnings_summary()

    all_metrics = cap.export_all()

    ## Create DB Records ##
    cap_instance = add_CAPInstance(all_metrics)

    retag_entries = add_Retags(all_metrics, cap_instance)
    broken_entries = add_BrokenAPI(all_metrics, cap_instance)
    nim_entries = add_NotInMasterlist(all_metrics, cap_instance)
    qa_entries = add_QAUpdates(all_metrics, cap_instance)

    ## Update Masterlist on QA Updates ##

    update_masterlist(cap_instance)

def add_CAPInstance(all_metrics):

    # Grab Metrics from CAP Package
    cdi_metrics = all_metrics["CDI Metrics"]
    warnings_summary = all_metrics["Warnings Summary"]

    masterlist_count = cdi_metrics['cdi_masterlist_count']
    climate_collection_count = cdi_metrics['climate_collection_count']
    broken_urls = warnings_summary['broken_url_count']
    lost_climate_tag = warnings_summary['lost_climate_tag_count']
    not_in_masterlist = warnings_summary['not_in_masterlist_count']
    total_warnings= warnings_summary['total_warnings']

    # Create Record

    capinstance = CAPInstance(masterlist_count = masterlist_count,
                                climate_collection_count = climate_collection_count,
                                broken_urls = broken_urls, 
                                lost_climate_tag = lost_climate_tag, 
                                not_in_masterlist = not_in_masterlist, 
                                total_warnings = total_warnings
                                ) 

    capinstance.save() # Adds Record to Database

    return capinstance

def add_Retags(all_metrics, cap_instance):
    
    retag_json = all_metrics['Retag Datasets']
    retag_entries = []

    for retag in retag_json:

        dg_id = retag["datagov_ID"]
        masterlist_dataset = Masterlist.objects.get(datagov_ID=dg_id)

        retag_entry = Retag(cap_id=cap_instance, datagov_ID=masterlist_dataset)

        retag_entry.save()

        retag_entries.append(retag_entry)

    return retag_entries

def add_BrokenAPI(all_metrics, cap_instance):

    broken_json = all_metrics['Broken API']
    broken_entries = []

    for broken in broken_json:

        dg_id = broken["datagov_ID"]
        masterlist_dataset = Masterlist.objects.get(datagov_ID=dg_id)

        broken_entry = BrokenAPI(cap_id=cap_instance, datagov_ID=masterlist_dataset)

        broken_entry.save()

        broken_entries.append(broken_entry)

        masterlist_dataset.status = 'Not Active'
        masterlist_dataset.save()

    return broken_entries

def add_QAUpdates(all_metrics, cap_instance):
    
    qa_updates_json = all_metrics['QA Updates']
    qa_entries = []

    for qa in qa_updates_json:

        dg_id = qa["datagov_id"]
        masterlist_dataset = Masterlist.objects.get(datagov_ID=dg_id)

        qa_entry = QAUpdates(cap_id = cap_instance,
                            datagov_ID = masterlist_dataset,
                            name = qa['name'],
                            title = qa['title'],
                            organization = qa['organization'],
                            catalog_url = qa['catalog_url'],
                            metadata_type = qa['metadata_type']
                            )
        qa_entry.save()

        qa_entries.append(qa_entry)

    return qa_entries

def add_NotInMasterlist(all_metrics, cap_instance):
    
    notinmasterlist_json = all_metrics['Not in Masterlist']
    nim_entries = []

    for nim in notinmasterlist_json:

        nim_entry = NotInMasterlist(cap_id =cap_instance,
                                    title = nim['title'],
                                    name = nim['name'],
                                    catalog_url = nim['catalog_url'],
                                    api_url = nim['api_url']
                                    )
        nim_entry.save()

        nim_entries.append(nim_entry)

    return nim_entries

def update_masterlist(cap_instance):

    qa_records = QAUpdates.objects.filter(cap_id=cap_instance)

    for qa in qa_records:

        masterlist_obj = qa.datagov_ID

        if qa.name:
            qa_name_dict = ast.literal_eval(qa.name)
            masterlist_obj.name = qa_name_dict['Updated']

        if qa.title:
            qa_title_dict = ast.literal_eval(qa.title)
            masterlist_obj.title = qa_title_dict['Updated']

        if qa.organization:
            qa_org_dict = ast.literal_eval(qa.organization)
            masterlist_obj.organization = qa_org_dict['Updated']

        if qa.catalog_url:
            qa_cat_dict = ast.literal_eval(qa.catalog_url)
            masterlist_obj.catalog_url = qa_cat_dict['Updated']

        if qa.metadata_type:
            qa_meta_dict = ast.literal_eval(qa.metadata_type)
            masterlist_obj.metadata_type = qa_meta_dict['Updated']
        
        masterlist_obj.save()





