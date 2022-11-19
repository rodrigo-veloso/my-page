import pandas as pd
import streamlit as st

st.set_page_config(page_title="Python e Ciência de Dados com Rodrigo Veloso", layout="wide")

content, about = st.columns((3,1))

content.header("Procurando por aulas de Python e Ciência de Dados?")
content.markdown(
  """###
  ##### Se você quer: 
  * ##### Se preparar para uma prova/entrevista :pencil:
  * ##### Adquirir novas habilidades de programação e análise :computer: 
  * ##### Solucionar problemas usando Python/Ciência de dados :chart_with_upwards_trend:
  * ##### Consultoria para projetos e carreira :bulb:
  """
)
content.markdown("#### Olá, meu nome é o Rodrigo Veloso, e eu vou te ajudar :smiley:")
about.image("foto.jpeg")
about.markdown("""Sou cientista de dados profissional e mestre em dinâmica dos fluidos computacional pela UFF.
Programo todos os dias desde o início da minha graduação, adoro resolver problemas. Cursei mineração de dados e inteligência artificial na pós graduação de ciência da computação da UFF e desde então migrei totalmente para a área de dados. Iniciei minha carreira profissional em 2021 no Brasil como cientista de dados e hoje moro em Portugal e trabalho como cientista de dados em uma das maiores empresas de telecomunicações de Portugal.
Sou professor particular há mais de 5 anos e amo ensinar.""")
content.markdown(
  """###
  ##### Minhas especialidades são: 
  * ##### Python
  * ##### Ciência de dados/Data Science: Algoritmos e bibliotecas (scikit-learn, pandas, tensorflow, numpy, streamlit, pyspark, etc...)
  * ##### Machine Learning: Classificação, regressão, clusterização, aprendizado por reforço, mineração de dados, etc...
  * ##### Métodos numéricos e algoritmos gerais: Integração, diferenciação, simulações, soluções de sistemas, algoritmos genéticos, heurísticas, etc...
  """
)
content.markdown(
  """###
  #### Quer saber mais sobre as aulas e consultorias? Entre em contato por whatsapp! +351968266283
  """
)
