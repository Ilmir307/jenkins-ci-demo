pipeline {
    agent any

    stages {
        stage('Сборка') {
            steps {
                // проверка синтаксиса: компиляция в байт-код
                bat 'python -m py_compile app.py test_app.py'
            }
        }
        stage('Тестирование') {
            steps {
                // запуск модульных тестов
                bat 'python -m unittest test_app.py -v'
            }
        }
        stage('Упаковка') {
            steps {
                // упаковка приложения в zip-архив
                bat 'python -c "import shutil; shutil.make_archive(\'app\', \'zip\', \'.\')"'
                archiveArtifacts artifacts: 'app.zip'
            }
        }
        stage('Развёртывание') {
            steps {
                // копирование приложения в каталог тестового сервера
                bat 'xcopy /Y app.py C:\\deploy\\test\\'
            }
        }
    }
    post {
        success { echo 'Пайплайн выполнен успешно' }
        failure { echo 'Пайплайн завершился с ошибкой' }
    }
}
