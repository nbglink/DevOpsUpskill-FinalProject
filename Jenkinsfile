#!/usr/bin/env groovy

library identifier: 'jenkins-shared-library@main', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'https://github.com/nbglink/jenkins-shared-library.git',
     credentialsId: 'github-credentials'
    ]
)
// CI part
pipeline {
    agent any
    tools {
        maven 'Maven'
    }
    environment {
        IMAGE_NAME = 'nbglink/demo-app:jma-11'
        APPLICATION_NAME = 'demo-app'
    }
    stages {
        stage('build app') {
            steps {
               script {
                  echo 'building application jar...'
                  buildJar()
               }
            }
            post {
                success {
                    slackSend color: 'good', message: "Build SUCCESS: Application jar has been built successfully."
                }
                failure {
                    slackSend color: 'danger', message: "Build FAILURE: Failed to build application jar."
                }
            }
        }
        stage('build image') {
            steps {
                script {
                   echo 'building docker image...'
                   buildImage(env.IMAGE_NAME)
                   dockerLogin()
                   dockerPush(env.IMAGE_NAME)
                   sh "mkdir --parents ./argocd-app-config/$env.APPLICATION_NAME/ && cp -rf ./target/classes/META-INF/dekorate/kubernetes.yml ./argocd-app-config/$env.APPLICATION_NAME/"
                }
            }
            post {
                success {
                    slackSend color: 'good', message: "Build SUCCESS: Docker image has been built and pushed successfully."
                }
                failure {
                    slackSend color: 'danger', message: "Build FAILURE: Failed to build or push Docker image."
                }
            }
        }
        stage('Replace Docker image name') {
            steps {
                sh "python ./scripts/replaceimagename.py $env.APPLICATION_NAME"
            }
            post {
                success {
                    slackSend color: 'good', message: "Build SUCCESS: Docker image name has been replaced successfully."
                }
                failure {
                    slackSend color: 'danger', message: "Build FAILURE: Failed to replace Docker image name."
                }
            }
        }
        stage('deploy to ArgoCD') {
            steps {
                dir("argocd-app-config") {
                    sh "kubectl apply -f application.yaml"
                }
            }
            post {
                success {
                    slackSend color: 'good', message: "Build SUCCESS: Application has been deployed to ArgoCD successfully."
                }
                failure {
                    slackSend color: 'danger', message: "Build FAILURE: Failed to deploy application to ArgoCD."
                }
            }
        }
        stage('Update GIT') {
          steps {
            script {
              catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
                    sh "git add argocd-app-config/"
                    sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
                    sh "git push https://${GIT_USERNAME}:${encodedPassword}@github.com/${GIT_USERNAME}/DevOpsUpskill-FinalProject.git HEAD:main"
                }
              }
            }
          }
          post {
              success {
                  slackSend color: 'good', message: "Build SUCCESS: Git repository has been updated successfully."
              }
              failure {
                  slackSend color: 'danger', message: "Build FAILURE: Failed to update Git repository."
              }
          }
        }
    }
    post {
        always {
            script {
                def buildStatus = currentBuild.result == 'SUCCESS' ? 'SUCCESS' : 'FAILURE'
                slackSend color: buildStatus == 'SUCCESS' ? 'good' : 'danger', message: "Build ${buildStatus}: ${currentBuild.fullDisplayName} (${env.BUILD_NUMBER})"
            }
        }
        aborted {
            script {
                slackSend color: 'warning', message: "Build ABORTED: ${currentBuild.fullDisplayName} (${env.BUILD_NUMBER})"
            }
        }
    }
}
