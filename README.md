# Distributed Chat Application on Kubernetes

This project implements a scalable, real-time messaging system deployed on Google Cloud Platform (GCP) using Flask, MongoDB, and Socket.IO, orchestrated with Kubernetes. It simulates a production-ready architecture with real-time communication, persistent data storage, and dynamic scaling.

## Technologies Used

- Flask – Python-based web server for handling client requests and Socket.IO integration  
- MongoDB – NoSQL database for storing chat history and user data  
- Socket.IO – Enables real-time, bidirectional communication between clients and server  
- Docker – For creating isolated and portable containers  
- Kubernetes (k8s) – Manages containerized deployments, scaling, and fault tolerance  
- Google Cloud Platform (GCP) – Provides the infrastructure (VMs, Kubernetes Engine)

## Architecture Overview

- Web Tier: Flask + Socket.IO running in one or more pods managed by a Deployment  
- Database Tier: MongoDB running as a StatefulSet with PersistentVolumeClaim  
- Services:
  - NodePort for external web access  
  - ClusterIP for internal MongoDB access  
- Load Balancing: NodePort distributes traffic among web pods  
- DNS-Based Service Discovery: Kubernetes services automatically resolve across pods  

## Features

- Real-time messaging via WebSockets
- Persistent message storage using MongoDB
- Multi-node Kubernetes cluster deployment
- Fault tolerance and horizontal pod scaling
- DNS-based service discovery within the cluster

## Deployment Instructions

1. Clone the repository and configure Docker images for the web and database tiers.
2. Deploy MongoDB StatefulSet and Service.
3. Deploy the Flask application using the Deployment and expose it with a NodePort service.
4. Access the chat application via `<NodeIP>:<NodePort>`.

