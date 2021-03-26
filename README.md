<h1 align="center">Weather Bot</h1>
<h3>Projeto usando Scrapy para fazer crawl no site Climatempo.</h3>
<h4>Bibliotecas externas usadas</h4>
<p>*Scrapy
*Schedule
*MySQL Connector</p>
<h5>Resumo</h5>
<p>Crawler executado de uma em uma hora usando a biblioteca Schedule</p>
<p>Requests feitas para APIs JSON com dados meteorólogicos em tempo real de cidades</p>
<p>Response é então convertida e enviada para uma database MySQL usando a biblioteca MySQL Connector</p>
<p>Duas tabelas são criadas,uma com as cidades e outra com os respectivos dados meteorológicos</p>