# 🐳 Containerized Microservices on AWS ECS Fargate

A production-ready microservices setup deployed on **AWS ECS Fargate**, fronted by an **Application Load Balancer (ALB)**, and containerized with **Docker**.  
The project demonstrates how to host multiple Flask-based microservices (User & Product) behind a single load balancer.

---

## 🏗️ Architecture Overview

![Architecture Diagram](./docs/architecture-diagram.png)

### Components
- **User Service** – Flask app running on port `5000`
- **Product Service** – Flask app running on port `5001`
- **Application Load Balancer** – Routes:
  - `/users*` → `tg-users`
  - `/products*` → `tg-products`
- **AWS ECS Fargate** – Serverless container compute service
- **Amazon CloudWatch** – Logs & metrics for containers

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|----------|
| **AWS ECS Fargate** | Container orchestration |
| **AWS ALB** | Routing to target groups |
| **Docker** | Containerization |
| **Flask** | Python microservice framework |
| **CloudWatch** | Monitoring & logging |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/ManvendraSinghShekhawat/containerized-microservices.git
cd containerized-microservices




🚀 **Deployment Guide (Manual AWS Setup)**

**Step 1 — Create ECS Cluster**

Launch Type: Fargate

Name: microservices-cluster

**Step 2 — Create Target Groups**
Name	Target Type	Port	Health Check Path
tg-users	IP	5000	/health
tg-products	IP	5001	/health


**Step 3 — Create Application Load Balancer**

Scheme: Internet-facing

Protocol: HTTP (80)

Add both subnets in default VPC

Allow inbound port 80

Set default target group = tg-users

Then, under Listeners → Edit rules, add:

/users → Forward to tg-users

/products → Forward to tg-products

**Step 4 — Create ECS Services**

For each microservice:

Task Definition: respective one (user or product)

Launch Type: Fargate

Load Balancer: select ALB created above

Listener Port: 80

Target Group: corresponding one

**Step 5 — Verify**

Visit your ALB DNS URL:

http://<ALB-DNS>/users

http://<ALB-DNS>/products



🧩 **Directory Overview**

containerized-microservices/
├── user-service/          # Flask app for users
├── product-service/       # Flask app for products
├── ecs/                   # ECS & ALB setup files
├── docs/                  # Documentation & diagrams
└── docker-compose.yml     # Local testing setup

🧪 **Local Testing**

To test health endpoints:

curl http://localhost:5000/health
curl http://localhost:5001/health

👨‍💻 **Author**

Manvendra Singh Shekhawat
📧 manvendrasinghshekhawat324@gmail.com
