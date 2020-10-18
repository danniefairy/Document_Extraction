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
                stage('Run the service') {
                    steps {
                        script{
                            StepName = "${env.STAGE_NAME}"
                            // run the testing script of server part.
                            bat "echo \"Run the testing script of server part\""
                            bat "${PYTHON} server\\app.py"
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
                            // run the testing script of data science part.
                            bat "echo \"Run the testing script of data science part\""
                            bat "${PYTHON} server\\test\\test.py"
                            bat "${PYTHON} -m server.test.t"

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
                    // run the service
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
