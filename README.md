# Visão Computacional: Detecção de Sonolência

## Sobre o Projeto
Este projeto tem como objetivo estudar e implementar técnicas de visão computacional para detecção de sonolência através do reconhecimento facial e ocular. Inicialmente, utilizamos o Haar Cascade para aprender sobre a técnica mais básica de detecção de rostos. Posteriormente, aplicamos o Dlib para uma abordagem mais refinada, capaz de identificar o rosto, os olhos e determinar se estão fechados.

Caso os olhos sejam detectados como fechados por um período de tempo significativo, um Arduino será acionado para ativar um buzzer, alertando sobre a possibilidade de que a pessoa tenha adormecido.

## Como Funciona o Haar Cascade
O Haar Cascade é um algoritmo baseado em aprendizado de máquina para a detecção de objetos, incluindo rostos e olhos. Ele utiliza uma abordagem de cascata para filtrar regiões de interesse na imagem, reduzindo a carga computacional. O processo envolve:

1. **Extração de Características**: Através de filtros Haar (diferenças de intensidade entre regiões da imagem).
2. **Treinamento em um Conjunto de Dados**: O classificador é treinado com milhares de amostras positivas (contendo rostos) e negativas (sem rostos).
3. **Aplicando a Cascata**: As regiões são processadas em estágios, onde regiões que falham em um estágio são descartadas imediatamente, tornando a detecção eficiente.

## Como Funciona o Dlib
O Dlib é uma biblioteca de aprendizado de máquina que fornece um detector de faces baseado em Histogramas de Gradientes Orientados (HOG) e redes neurais profundas. Para este projeto, utilizamos o detector de marcos faciais do Dlib para:

1. **Identificar o Rosto**: Detecta a posição do rosto na imagem. A detecção ocorre a partir de um arquivo que gera 68 landmarks no rosto identificado, possibilitanto o reconhecimento de expressões.
2. **Localizar os Olhos**: Usando marcos faciais, podemos obter a posição exata dos olhos.
3. **Verificar se os Olhos Estão Fechados**: Calculando a Razão de Aspecto do Olho (EAR - Eye Aspect Ratio). Se o valor do EAR for abaixo de um limite por um tempo contínuo, assumimos que os olhos estão fechados.
   
## Acionamento do Arduino
Quando o sistema detecta que a pessoa pode ter adormecido, enviamos um sinal via porta serial para um Arduino, que aciona um buzzer para alertar a pessoa.

## Como Executar o Projeto
1. Instale as dependências necessárias:
```bash
pip install opencv-python dlib numpy serial scipy.spatial
```
2. Execute o script principal para iniciar a detecção.
```bash
python face_detected_dlib.py
```
3. Conecte o Arduino via USB para receber os sinais de alerta.


