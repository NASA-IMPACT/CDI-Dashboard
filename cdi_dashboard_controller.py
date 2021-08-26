from flask import Flask, render_template, abort, jsonify, request, redirect, url_for


app = Flask(__name__)



# CDI DASHBOARD HOME PAGE
@app.route("/")
def home():
	return render_template(
		"HOMEPAGE.html"
		)



# METRICS PAGE
@app.route("/metrics")
def metrics():
	return render_template(
		"/metrics/METRICS.html"
		)



# WARNINGS PAGE
@app.route("/warnings")
def warnings():
	return render_template(
		"/warnings/WARNINGS.html"
		)



# WARNINGS INSTANCE PAGE
@app.route("/warnings/<instance>")
def warnings_instance(instance):
	return render_template(
		"/warnings/WARNINGS_INSTANCE.html"
		)



# CLIMATE COLLECTION PAGE
@app.route("/climate-collection")
def climate_collection():
	return render_template(
		"/climate_collection/CLIMATE_COLLECTION.html"
		)



# MASTERLIST PAGE
@app.route("/cdi-masterlist")
def cdi_masterlist():
	return render_template(
		"/cdi_masterlist/CDI_MASTERLIST.html"
		)




# MASTERLIST DOWNLOAD (Route)
@app.route("/cdi-masterlist/download")
def cdi_masterlist_download():
	return render_template(
		"/cdi_masterlist/MASTERLIST_DOWNLOAD.html"
		)




# MASTERLIST QA UPDATES PAGE
@app.route("/cdi-masterlist/qa-updates")
def qa_updates():
	return render_template(
		"/cdi_masterlist/qa_updates/QA_UPDATES.html"
		)



# QA DOWNLOAD ALL (Route)
@app.route("/cdi-masterlist/qa-updates/download-all")
def qa_updates_download_all():
	return render_template(
		"/cdi_masterlist/qa_updates/QA_UPDATES_DOWNLOAD.html"
		)



# QA DOWNLOAD INSTANCE (Route)
@app.route("/cdi-masterlist/qa-updates/download-<instance>")
def qa_updates_download_instance(instance):
	return render_template(
		"/cdi_masterlist/qa_updates/QA_UPDATES_DOWNLOAD_INSTANCE.html"
		)



# RETAG DATASETS PAGE
@app.route("/retag")
def retag():
	return render_template(
		"/retag/RETAG.html"
		)



# RETAG REQUEST DOWNLOAD (Route)
@app.route("/retag/retag-request-download")
def retag_request_download():
	return render_template(
		"/retag/RETAG_REQUEST_DOWNLOAD.html"
		)



##### CHARTS #####

# Datasets by Agency
@app.route("/metrics/agency")
def agency_chart():
	return render_template(
		"/metrics/charts/AGENCY_CHART.html"
		)



# CDI Theme Distrubution
@app.route("/metrics/theme")
def theme_chart():
	return render_template(
		"/metrics/charts/THEME_CHART.html"
		)


# Geospatial vs. Nongeospatial
@app.route("/metrics/metadata-type")
def metadata_type_chart():
	return render_template(
		"/metrics/charts/METADATA_TYPE_CHART.html"
		)


# Tagged vs. No Tag
@app.route("/metrics/climate-tag")
def climate_tag_chart():
	return render_template(
		"/metrics/charts/CLIMATE_TAG_CHART.html"
		)





