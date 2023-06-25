<h1 align="center"> SaenseSummy</h1>

![license](http://img.shields.io/static/v1?label=license&message=MIT&color=GREEN&style=for-the-badge)

## Descrição do Projeto
 O Processamento de Linguagem Natural (PLN), uma ramificação da IA e da Linguística, foca em fazer com que os computadores entendam e gerem linguagem humana. Isso abrange a compreensão e geração de texto, sendo aplicado em assistentes virtuais, chatbots, tradutores automáticos e sumarizadores de texto. Nesse contexto, o SaenseSummy é uma solução de sumarização de artigos científicos do portal Saense, que tem como objetivo divulgar novidades científicas de forma acessível, contextualizando as descobertas e explorando suas implicações científicas, tecnológicas e sociais.

 A solução SaenseSummy foi desenvolvida em Python, o processo é dividido em duas fases. Na primeira fase, o texto é extraído da postagem do https://saense.com.br/ Saense utilizando uma adaptação biblioteca HandlePage disponível em https://0xdferraz.github.io/Saense-PLN/. Em seguida, o texto extraido, é repassado para o Sumarizador desenvolvido por https://huggingface.co/phpaiola/ptt5-base-summ-cstnews .
