// toekn: 
// document_extraction_token = 11582f5a6a13241071f66fcbf3d525e651
pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS') 
    }
    stages {
        stage('[Prepare component]') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"
                    bat "python test.py"
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
        stage('[Deploy and train on stage]') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"
                    bat "echo \"Deploy and train on stage\""
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
        stage('[Validate and test on stage]') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"
                    bat "echo \"Validate and test on stage\""
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
        stage('[Deploy on production]') {
            steps {
                script{
                    StepName = "${env.STAGE_NAME}"
                    bat "echo \"Deploy on production\""
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
