# Função Contínua

## Definição matemática

A função vai ser contínua em x0 se ocorrer:
1) A função estar definida em x0;
2) O limite de x se aproximando de x0 fa função existir;
3) O limite de x se aproximando de x0 da função ser igual a f(x0).

## Gráfico de uma função contínua

![cont](https://github.com/user-attachments/assets/68859654-0c54-4e32-bb1a-d749bfa87132)


## Gráfico de uma função não contínua

![naocont](https://github.com/user-attachments/assets/78960647-823e-4efd-95a1-a0bb40b6bdac)

## Importância

1) Treinamento de Modelos (Backpropagation e Gradientes):
Em redes neurais, a retropropagação (backpropagation) usa derivadas para ajustar os pesos do modelo. Garantir continuidade facilita o ajuste suave dos parâmetros. Um exemplo é usar a função ReLu(Rectified Linear Unit).

2) Interpolação e suavização de dados: é essencial quando queremos prever valores entre pontos conhecidos, garantindo que não haja mudanças bruscas ou inconsistências nos dados.

**Interpolação**: é o processo de estimar valores entre pontos conhecidos. Se tivermos um conjunto de dados discretos, podemos usar uma função contínua para conectar esses pontos de forma suave.

**Suavização de dados**: ocorre quando eliminamos ruídos ou variações abruptas, garantindo que o modelo gere previsões mais estáveis.

**Otimização de funções de custo**: A função de custo mede o quão ruim está o modelo ao fazer previsões. O objetivo do treinamento é minimizar essa função. Se a função for contínua e diferenciável, podemos usar técnicas matemáticas para minimizá-las, como o gradientee descendente, que é um método para reduzir a função de custo. Caso a função de custo não fosse contínua, o gradiente pode ser indefinido ou 0, impedindo a atualização eficiente dos pesos.