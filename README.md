* The project consists of two repositories: one for [infrastructure](https://github.com/nbglink/DevOpsUpskill-FinalProject-Infra.git) and another for the [application](https://github.com/nbglink/DevOpsUpskill-FinalProject.git). The infrastructure repository is responsible for creating the underlying infrastructure that the application will run on. It uses Terraform modules to provision resources in AWS, specifically an Elastic Kubernetes Service (EKS) cluster. EKS is a managed Kubernetes service that makes it easy to run and scale containerized applications.

* Once the EKS cluster is up and running, the infrastructure repository installs ArgoCD on the cluster. ArgoCD is a GitOps tool that allows you to define the desired state of your infrastructure and applications in Git, and continuously monitors for drift between the actual and desired state. ArgoCD automatically reconciles any discrepancies it finds, ensuring that the system stays in the desired state.

* The ArgoCD installation and the Jenkins pipeline for it are run using a multibranch pipeline. Multibranch pipeline is a Jenkins feature that allows to automatically create a pipeline for each branch in the source code repository. This way Jenkins can handle multiple branches and automatically build and test the code in each of them.

* The application repository uses the same approach as the infrastructure repository, but with the addition of building the app, creating a Docker image, and pushing it to DockerHub. This way, you have a containerized version of the application that can be easily deployed to the EKS cluster using ArgoCD.

* ArgoCD is also used in the application repository to monitor for changes and automatically update the system to match the desired state.

* By using GitOps practices in both the infrastructure and application repositories, project ensures that the desired state of the system is always in sync with the actual state of the system, and that deployments are made more efficiently and reliably.
