# Embarcados
Repositório para tarefas de Sistemas Embarcados dos alunos Gabriel Scarabelli, Bruno Gianesi e Leonardo Masson

Projeto 2: Movimentação ponto a ponto de um eixo de robo reabilitação.

Descrição resumida: Operar um grau de liberdade do robo comunicando-se com o sistema de acionamento ESCON e fazendo a leitura de encorders

Harware Computacional:VIOLA + VF Toradex

Hardware Mecatrônico: Braço robo MOREA - reabilitação de braço

Software Mínimo Adotado: Linux; C




## Projeto dividido em 4 etapas a serem atacadas:

  #### Etapa 1 - Conexão com o driver EPOS
    File EPOSControl -> Biblioteca para controle da EPOS
    File: EPOSControl.h
    Desc: A library for communicating with and configuring EPOS motor controllers
          made by Maxon motors using CAN bus.

  #### Etapa 2 - Movimentação do motor
    //EPOSControl/include/EPOSControl/CANMotorControllerAction.h
    Acionamento de motor com CAN pelo driver EPOS
    File: CANMotorControllerAction.h
    Desc: Represents a very basic action that can be done with a motor
          controller. A motor controller configuration is built up from a number
          of actions.

  #### Etapa 3 - Leitura do Encoder
     File: CANMotorController.h
     Desc: The object that represents an EPOS motor controller on a CAN bus.
           A CANMotorController is configured and controlled using sequences of
           CANMotorControllerActions. 'Configuration' actions are assumed to be a
           persistant list of tasks that should be carried out to configure
           a motor controller.

  #### Etapa 4 - Atualizar posição do motor (Leitura e reenvio)
    File: SDOField.h
    Desc: An object that configures either a read or a write of an SDO field
          from a CAN Open node
