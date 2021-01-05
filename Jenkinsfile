/*
toekn: 
    document_extraction_token, 11582f5a6a13241071f66fcbf3d525e651
*/
pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS') 
    }
    stages {
        stage('Initialize the variables') {
            // Each stage is made up of steps
            steps{
                script{
                    StepName = "${env.STAGE_NAME}"
                    PYTHON="C:\\Users\\user\\Anaconda3\\python.exe"
                    bat "echo \"sh(script: 'env|sort', returnStdout: true)\""
                }
            }                
        }
        stage('Prepare component') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"
                    // install the dependency if it doesn't exist.
                    bat "echo \"Install the requirements\""
                    bat "${PYTHON} -m pip install -r scripts\\requirements.txt"
                }
            }
            post{
                success{
                    setBuildStatus("Build succeeded", "SUCCESS", "${StepName}");
                }
                failure{
                    setBuildStatus("Build failed", "FAILURE", "${StepName}");
                }
            }
        }
        stage('Deploy and train on stage') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"
                    // run the train script
                    bat "echo \"Pass\""
                }
            }
            post{
                success{
                    setBuildStatus("Build succeeded", "SUCCESS", "${StepName}");
                }
                failure{
                    setBuildStatus("Build failed", "FAILURE", "${StepName}");
                }
            }
        }
        stage('Validate and test on stage') {
           parallel {
                stage('Run the service on stage') {
                    steps {
                        script{
                            StepName = "${env.STAGE_NAME}"
                            try{
                                // run the server on stage.
                                bat "echo \"Run the server on stage\""
                                bat "${PYTHON} server\\app.py"
                            } catch(hudson.AbortException ae){
                                // The process was explicitly killed by somebody wielding the kill program is acceptable
                                // ref: https://wiki.jenkins.io/display/JENKINS/Job+Exit+Status
                                if(ae.getMessage().contains('script returned exit code 15')){
                                   print("error code 15 is acceptable.")
                                } else {
                                    throw ae
                                }
                            }

                        }
                    }
                    post{
                        success{
                            setBuildStatus("Build succeeded", "SUCCESS", "${StepName}");
                        }
                        failure{
                            setBuildStatus("Build failed", "FAILURE", "${StepName}");
                        }
                    }
                }
                stage('Run the test') {
                    steps {
                        script{
                            StepName = "${env.STAGE_NAME}"
                            // check the server is on.
                            bat "echo \"Check the server is on.\""
                            bat "${PYTHON} server\\test\\check.py"

                            // run the testing script of the server part.
                            bat "echo \"Run the testing script of the server part\""
                            bat "${PYTHON} -m unittest server/test/server_test.py"

                            // run the testing script of the ui part.
                            bat "echo \"Run the testing script of the ui part\""
                            bat "${PYTHON} -m unittest server/test/ui_test.py"

                            // stop the running service.
                            bat "echo \"Stop the running service\""
                            bat "${PYTHON} server\\test\\shutdown.py"
                        }
                    }
                    post{
                        success{
                            setBuildStatus("Build succeeded", "SUCCESS", "${StepName}");
                        }
                        failure{
                            setBuildStatus("Build failed", "FAILURE", "${StepName}");
                        }
                    }
                }
            }
        }
        stage('Deploy on production') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"                    
                    // run the server on production.
                    bat "echo \"Be able to start the server with the command: 'python server/app.py'\""
                    branch = "${env.BRANCH_NAME}"
                    if (branch == 'stage') {
                        bat "echo 'I only execute on the stage branch'"
                    } else {
                        bat "echo 'I do not execute on the stage branch'"
                    }
                }
            }
            post{
                success{
                    setBuildStatus("Build succeeded", "SUCCESS", "${StepName}");
                }
                failure{
                    setBuildStatus("Build failed", "FAILURE", "${StepName}");
                }
            }
        }
    }
}

void setBuildStatus(String message, String state, String taskTitle) {
    // Clean up the ansible dir and containers if the pipeline fails.
    if (state=="FAILURE") {
        script{
            bat "echo \"Failure!\""
        }
    }

    // Send the commit status to github.
    step([
        $class: "GitHubCommitStatusSetter",
        reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/danniefairy/Document_Extraction"],
        contextSource: [$class: "ManuallyEnteredCommitContextSource", context: taskTitle],
        errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
        statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
    ]);
}
