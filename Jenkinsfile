// comment
pipeline {
 agent any
 stages {
        stage('Checkout-github'){
               steps{
		git poll: true, url: 'git@github.com:nemerdiaz/test-jenkins.git'
               }
        }
        stage('Create-VirtualEnv') {
            steps {
				sh '''
					#bash -c "Error"
					bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate"
				'''
            }
        }
        stage('Install-Requirements') {
            steps {
            	sh '''
            		bash -c "source ${WORKSPACE}/entorno_virtual/bin/activate && ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/entorno_virtual/bin/pip install -r requirements.txt"
                '''
            }
        }   
        stage('Test') {
            steps {
            	sh '''
            		bash -c "source ${WORKSPACE}/entorno_virtual/bin/activate &&  cd src && ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/entorno_virtual/bin/pytest && cd .."
                '''
            }
        }  
        stage('Run') {
            steps {
            	sh '''
            		bash -c "source entorno_virtual/bin/activate ; ${WORKSPACE}/entorno_virtual/bin/python src/main.py &"
                '''
            }
        } 
  }
}
