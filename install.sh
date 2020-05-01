#!/bin/bash

## Autor: Gabriel Nunes Delfino
## ti.gabrieldelfino@gmail.com
## Github: nunesdelfino

echo "#################################################";
echo "Verificando se há acesso root!";
echo "#################################################";

if [[ $EUID == 0 ]];
  then

    echo "#################################################";
    echo "Acesso root OK!";
    echo "#################################################";

    cp ./rmkip.py /usr/local/bin/

    cp ./ipmake /usr/local/bin/

    chmod 777 /usr/local/bin/ipmake
    chmod 777 /usr/local/bin/rmkip.py


    echo "#################################################";
    echo "          Finalizado!";
    echo "#################################################";

else
  echo "Por favor execute o script com permissões de super usuário!";
fi
