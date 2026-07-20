# 🚀 Automated GCP Web App & CI/CD Pipeline

Welcome to my GCP automated application repository! This project contains a production-ready Flask web app, containerized with Docker, and deployed via a fully automated CI/CD pipeline on Google Cloud Platform.
## 🌐 Live Demo
🔗 [View My Live Web App](https://my-automated-web-app-700385388090.me-central1.run.app) 

---

## 🏗️ Architecture Overview

This project layout demonstrates a complete modern DevOps and Cloud architecture:
1. **Frontend/Backend:** Python Flask Application.
2. **Containerization:** Dockerfile configured for production-ready web servers using `gunicorn`.
3. **Source Control:** GitHub repository integrated with GCP.
4. **CI/CD Automation:** Google Cloud Build automates building and pushing artifacts on every `git push`.
5. **Container Registry:** Google Artifact Registry securely stores built Docker images.
6. **Serverless Deployment:** Google Cloud Run scales and hosts the containerized application globally.

---

## 🛠️ Tech Stack & Skills Demonstrated

* **Cloud Provider:** Google Cloud Platform (GCP)
* **Compute / Serverless:** Google Cloud Run
* **CI/CD / Automation:** Google Cloud Build (`cloudbuild.yaml`)
* **Containerization:** Docker, Google Artifact Registry
* **Backend Framework:** Python Flask, Gunicorn
* **Version Control:** Git & GitHub

---

## 🚀 How the CI/CD Pipeline Works (Automation)

Every time code is pushed to the `main` branch, the following automated steps occur via Google Cloud Build:

1. **Step 0 (Build):** Cloud Build pulls the latest code and executes `docker build` based on the local `Dockerfile`.
2. **Step 1 (Push):** The newly created image is tagged and securely pushed to Google Artifact Registry.
3. **Step 2 (Deploy):** The pipeline triggers `gcloud run deploy`, rolling out the updated version to Cloud Run with zero downtime.

---

## 💻 How to Run Locally

If you wish to clone this repository and run the application locally:

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/ahmad-mor/gcp-automated-app.git](https://github.com/ahmad-mor/gcp-automated-app.git)
   cd gcp-automated-app
