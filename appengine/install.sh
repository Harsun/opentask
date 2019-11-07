#!/bin/bash
source ./config
gcloud app create --region=${GCP_REGION} --quiet;
gcloud app deploy --project=${PROJECT_ID} --quiet
