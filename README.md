<p align="center">
Animação em Micropython - Amigo virtual PET <br/>
</p>

<br/>

## :pushpin: Descrição

Nosso projeto consiste em uma animação de um jogo no estilo de "bichinho virtual", tematizado com o mascote do programa PET-SI. O projeto conta com sprites iniciais que poderão ser usados futuramente para um jogo no estilo de "Tamagotchi", contendo uma animação de "stand-by" e uma de dúvida.


<br/>

## :robot: Montagem do dispositivo físico

### Lista de materiais

| Quantidade | Nome | Link para referência |
| --- | --- | --- |
| 1 | ESP32 e cabo USB | https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html |
| 1 | Display OLED SSD1306 | https://www.mercadolivre.com.br/modulo-de-display-oled-096-polegadas-128x64-i2c-spi-ssd1306/p/MLB2094680074?pdp_filters=item_id%3AMLB7623424740&from=gshop&matt_tool=36897333&matt_word=&matt_source=google&matt_campaign_id=24072337389&matt_ad_group_id=201646451751&matt_match_type=&matt_network=g&matt_device=c&matt_creative=818746220522&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735128188&matt_product_id=MLB2094680074-product&matt_product_partition_id=2494360127015&matt_target_id=pla-2494360127015&cq_src=google_ads&cq_cmp=24072337389&cq_net=g&cq_plt=gp&cq_med=pla |
| 1 | Fonte de alimentação - PowerBank | https://www.amazon.com.br/Power-Geonav-10-000mAh-USB-C-espacial/dp/B0CNH9WK1H/ref=asc_df_B0CNH9WK1H?mcid=97951b9a0466376abf732037adb368c7&hvadid=709964502887&hvpos=&hvnetw=g&hvrand=9815242386640242301&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197956&hvtargid=pla-2275983322978&psc=1&hvocijid=9815242386640242301-B0CNH9WK1H-&hvexpln=0&language=pt_BR |

### Lista de conexões

| Componente | Pino da placa |
| --- | --- |
| Display SSD1306 | 21, 22, GND .2 e 3v3|


### Funcionamento dos componentes

#### Display SSD1306

O Display SSD1306 nos permite apresentar informações(Especificação técnica: https://randomnerdtutorials.com/esp32-ssd1306-oled-display-arduino-ide/)


### Circuito

<p align="center">
Figura - Diagrama do circuito<br/>
  <img src="https://github.com/andre-cerca/Pet-virtual/edit/main/Circuito.png" width="400" /><br/>
</p>
Informações importantes sobre o circuito, onde colocá-lo, entre outros.
<br/>

<br/>

## :electric_plug: Funcionamento do sistema

**Não esqueça: adicione um videozinho do sistema funcionando :)**

Liste informações como:
- requisitos do código
- estrutura de arquivos
- qual o objetivo de cada arquivo/pedaço de código
Não precisa ser muito detalhado, apenas o suficiente para que seu código seja entendível!


<br/>

## :busts_in_silhouette: Contribuir no projeto

### Features implementadas

- [x] Identificação da mudança de posição na cadeira *(exemplo de features que já estão funcionando no projeto)*


### Features para incrementar no projeto

- [ ] Possibilidade do usuário configurar o tempo e a temperatura para os alertas *(exemplo de features que as pessoas podem contribuir no projeto)*


