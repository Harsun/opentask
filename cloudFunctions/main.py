import googleapiclient.discovery
import os


def network_list(request):
    region_list = [
        'asia-east1',
        'asia-east2',
        'asia-northeast1',
        'asia-northeast2',
        'asia-south1',
        'asia-southeast1',
        'australia-southeast1',
        'europe-north1',
        'europe-west1',
        'europe-west2',
        'europe-west3',
        'europe-west4',
        'europe-west6',
        'northamerica-northeast1',
        'southamerica-east1',
        'us-central1',
        'us-east1',
        'us-east4',
        'us-west1',
        'us-west2'
    ]

    subnet_list = []
    if request is not None:
        project = os.environ.get(key='GCP_PROJECT', default='variable has not set yet.')
        compute = googleapiclient.discovery.build('compute', 'v1')
        for i in region_list:
            subnet_list.append(compute.subnetworks().list(project=project, region=i).execute())

        return str(subnet_list)