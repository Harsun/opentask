#!/bin/bash

gcloud functions deploy network_list --runtime python37 --trigger-http --allow-unauthenticated
