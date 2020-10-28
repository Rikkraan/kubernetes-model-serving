---
# Kubernetes

This repo demonstrates a simple method to serve a machine learning method via kubernetes


## Requirements
Install cli of kubernetes (kubectl https://kubernetes.io/docs/tasks/tools/install-kubectl/) and minikube (https://minikube.sigs.k8s.io/docs/start/)

## How to reproduce
1. To make a simple training Job -> `kubectl apply -f train_job.yaml`
This is a single job that trains a model and saves the model in the `/model` folder

2. To serve the model --> `kubectl apply -f serve_model.yaml` && `minikube service serve_model`
This spins up 2 pods that train and serve the model so that predictions can be made. By default Flask is using port 5000, so these are exposed by the service.
NB. the `minikube service serve_model` is necessary to make the service accesible from your browser
