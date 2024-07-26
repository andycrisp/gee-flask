# A Simple Flask app, deployed to Cloud Run that calls Earth Engine without a user login required or without downloading SA keys

This contains a simple flask app. Main.py returns the land cover for a specific hardcoded location for a hard-coded date range when called.

## Set Up project
1. Create and enable project for Earth Engine: https://developers.google.com/earth-engine/cloud/earthengine_cloud_project_setup
2. Create Service Account to call Earth Engine: https://cloud.google.com/iam/docs/service-accounts-create 
3. Give Service Account relevant Earth Engine permissions: https://developers.google.com/earth-engine/cloud/roles_permissions
4. Ensure the Service Account used for Cloud Build (often the default Compute Engine service account has the necessary permissions to deploy)

## Create application 
1. Clone this app. 

## Deploy app
1. Make sure you’re in the folder of the repo E.g. `cd gee-flask`
2. Execute: `gcloud run deploy --source .` 
3. Follow the click throughs… 
4. Once deployed, find your app on the Cloud Run Page, click ‘edit and deploy’ >  ‘security’ and choose your Earth Engine service account. Click deploy. 

## Use App

1. If your app is exposed to internet, you should be able to hit the url generated on your browser. 
2. If it is restricted to authorized access only, you can try the following from your Cloud Shell:
`curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" <URL>`



Code borrowed liberally form: https://colab.sandbox.google.com/github/google/earthengine-community/blob/master/guides/linked/ee-api-colab-setup.ipynb#scrollTo=NMp9Ei9b0XXL