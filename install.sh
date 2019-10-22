#!/bin/bash

## Autor: Gabriel Nunes Delfino
## ti.gabrieldelfino@gmail.com
## Github: nunesdelfino

echo "#################################################";
echo "Verificando se há acesso root!";
echo "#################################################";

if [[ $EUID == 0 ]];
  then

    cp ./remakeIproute.py /usr/local/bin/

    cp ./ipmake /usr/local/bin/

    chmod +x /usr/local/bin/ipmake

else
  echo "Por favor execute o script com permissões de super usuário!";
fi
