# Minecraft

## Instalar o Java

### Versões 1.12 a 1.17 do Minecraft

#### Debian / Ubuntu

`sudo apt-get install openjdk-8-jre`

### Versões 1.18 e adiante do Minecraft

Baixar o Java e JavaC

`wget https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_linux-x64_bin.tar.gz`

Descomprimir

`tar xvf openjdk-17.0.2_linux-x64_bin.tar.gz`

mover para pasta do Java

`sudo mv jdk-17.0.2/ /usr/java/openjdk/`

Caso não exista a pasta, execute

`sudo mkdir -p /usr/java/openjdk/`

Instalar como executável

`sudo update-alternatives --install /usr/bin/java java /usr/java/openjdk/jdk-17.0.2/bin/java 20 && sudo update-alternatives --install /usr/bin/javac javac /usr/java/openjdk/jdk-17.0.2/bin/javac 20`

## Executar um server com Mods

### Instalar o Forge

Abrir pasta do msm

`cd /opt/msm`

Criar Pasta para organizar múltiplas instalações do Forge

`sudo mkdir forge && cd forge`

Criar Pasta para a versão

`sudo mkdir 1-12-2 && cd 1-12-2`

Baixar o Instalador do Forge da Versão escolhida

`sudo wget https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar`

Instalar o Forge

`sudo java -jar forge-1.12.2-14.23.5.2860-installer.jar --installServer`

Renomear executável do servidor

`sudo mv forge-1.12.2-14.23.5.2860.jar server.jar`

Criar um novo server do MSM

`sudo msm server create nome-do-servidor && cd /opt/msm/servers/nome-do-servidor`

Copiar arquivos necessários para instalação

`sudo rm server.jar && sudo cp -r /opt/msm/forge/1-12-2/* .`

Aceitar EULA

`echo "eula=true" | sudo tee -a eula.txt`

Criar Pasta de Mods, passar todos os mods para essa pasta

`sudo mkdir mods`

Alterar Executável Java

`echo "msm-invocation=/usr/java/openjdk/jdk-1.8/bin/java -Xms{RAM}M -Xmx{RAM}M -jar {JAR} nogui" | sudo tee -a server.properties`

executar servidor

`sudo msm nome-do-servidor start`