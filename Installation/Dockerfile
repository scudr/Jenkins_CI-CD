# Utilizar la versión de Soporte a Largo Plazo (LTS) de Jenkins como la imagen base
FROM jenkins/jenkins:lts

# Cambiar al usuario root para realizar operaciones a nivel de sistema
USER root

################# Preparar un entorno de Jenkins que pueda trabajar eficientemente con Docker #################
# Instalar el complemento docker-workflow para habilitar a Jenkins a trabajar con Docker
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt
# Actualizar la lista de paquetes sin imprimir la lista de paquetes (modo silencioso) e instalar paquetes esenciales para la instalación
RUN apt-get update -qq \
    && apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common 
# Este comando descarga la clave GPG del repositorio oficial de Docker y la añade al sistema para verificar la autenticidad de los paquetes Docker.
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# Añadir el repositorio de Docker a la lista de repositorios de software del sistema
# Esto es necesario para poder instalar y actualizar Docker desde el repositorio oficial,
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
# Actualizar nuevamente la lista de paquetes en modo silencioso e instalar una versión específica de Docker CE
RUN apt-get update -qq \
    && apt-get install -y docker-ce docker-ce-cli containerd.io

# Instalar AWS CLI para interactuar con los Servicios Web de Amazon
RUN apt install awscli -y

# Instalar Python3 y pip
RUN apt-get install -y python3 python3-pip

# Instalar el instalador de paquetes de Python3, pip
RUN apt-get install python3-pip -y

# Instalar GnuPG para la gestión de claves y operaciones de seguridad
RUN apt-get install -y gnupg

# Añadir el usuario de jenkins al grupo docker para permitir que Jenkins ejecute comandos de Docker
RUN usermod -aG docker jenkins
