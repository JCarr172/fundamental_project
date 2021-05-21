pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
            TEST_DATABASE_URI = credentials('TEST_DATABASE_URI')
            TEST_SECRET = credentials('TEST_SECRET')
        }
        stages{
            stage('Run pytest'){
                steps{
                    script{
                            sh 'bash testing.sh'
                            }
                        }
                    }
        }
}
