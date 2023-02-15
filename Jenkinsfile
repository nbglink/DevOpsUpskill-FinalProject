#!/usr/bin/env groovy
// CI part
pipeline {
    agent any
    tools {
        maven 'Maven'
    }
    environment {
        VERSION = 'jma-15'
        APPLICATION_NAME = 'demo-app'
        IMAGE_NAME = "nbglink/$env.APPLICATION_NAME:$env.VERSION"
    }
    stages {
        stage('Replace Docker image name') {
            steps {
                sh "python ./scripts/replacevars.py $env.IMAGE_NAME $env.APPLICATION_NAME $env.VERSION"
            }
            post {
                success {
                    slackSend color: 'good', message: "Build SUCCESS: Variables has been replaced successfully."
                }
                failure {
                    slackSend color: 'danger', message: "Build FAILURE: Failed to replace variables."
                }
            }
        }
        stage('build app') {
            steps {
               script {
                  echo "$env.IMAGE_NAME"
                  echo "building the application for branch $BRANCH_NAME"
                  sh 'mvn package'
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
                   withCredentials([usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: "PASS", usernameVariable: "USER")]) {
                       sh "docker build -t $env.IMAGE_NAME ."
                       sh "echo $PASS | docker login -u $USER --password-stdin"
                       sh "docker push $env.IMAGE_NAME"
                   }
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
        stage('Update GIT') {
          steps {
            script {
              catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
                    sh "git add ."
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
        // stage('deploy to ArgoCD') {
        //     steps {
        //         dir("argocd-app-config") {
        //             sh "kubectl apply -f application.yaml"
        //         }
        //     }
        //     post {
        //         success {
        //             slackSend color: 'good', message: "Build SUCCESS: Application has been deployed to ArgoCD successfully."
        //         }
        //         failure {
        //             slackSend color: 'danger', message: "Build FAILURE: Failed to deploy application to ArgoCD."
        //         }
        //     }
        // }
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
