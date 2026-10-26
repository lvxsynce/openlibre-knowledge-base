# Чанк 0516
**Сообщения:** с #211737 по #212054 (всего 300)
**Период:** 2026-08-06T15:01:38 — 2026-08-06T17:04:05

---

<a id="msg_211737"></a>
### [msg_211737](chunk_0516.md#msg_211737) | 2026-08-06T15:01:38 | Вася (в ответ на #211736)
Нельзя им это

<a id="msg_211738"></a>
### [msg_211738](chunk_0516.md#msg_211738) | 2026-08-06T15:01:40 | Kvink⁴² (Алексей) (в ответ на #64360)
Вместе там покумекать

<a id="msg_211739"></a>
### [msg_211739](chunk_0516.md#msg_211739) | 2026-08-06T15:01:44 | Вася (в ответ на #64360)
Оставим это при себе

<a id="msg_211740"></a>
### [msg_211740](chunk_0516.md#msg_211740) | 2026-08-06T15:01:51 | Вася (в ответ на #64360)
Расфорсять и убьют

<a id="msg_211741"></a>
### [msg_211741](chunk_0516.md#msg_211741) | 2026-08-06T15:01:58 | Вася (в ответ на #64360)
Я заебался кастыль подключать

<a id="msg_211742"></a>
### [msg_211742](chunk_0516.md#msg_211742) | 2026-08-06T15:02:03 | Вася (в ответ на #64360)
Он с ошибкой иногда встаёт

<a id="msg_211743"></a>
### [msg_211743](chunk_0516.md#msg_211743) | 2026-08-06T15:02:09 | Вася (в ответ на #64360)
Я честно не хочу больше кастылить

<a id="msg_211744"></a>
### [msg_211744](chunk_0516.md#msg_211744) | 2026-08-06T15:02:12 | Вася (в ответ на #64360)
В пизду все нахуй

<a id="msg_211745"></a>
### [msg_211745](chunk_0516.md#msg_211745) | 2026-08-06T15:02:16 | Вася (в ответ на #64360)
3g слава нахуй

<a id="msg_211746"></a>
### [msg_211746](chunk_0516.md#msg_211746) | 2026-08-06T15:02:51 | Вася (в ответ на #64360)
Ахуено , я неверно то счастлив

<a id="msg_211747"></a>
### [msg_211747](chunk_0516.md#msg_211747) | 2026-08-06T15:02:59 | Вася (в ответ на #64360)
Последний раз я был так счастлив , когда сын родился

<a id="msg_211748"></a>
### [msg_211748](chunk_0516.md#msg_211748) | 2026-08-06T15:03:29 | Вася (в ответ на #64360)
Ахуено

<a id="msg_211749"></a>
### [msg_211749](chunk_0516.md#msg_211749) | 2026-08-06T15:05:46 | Rudi (в ответ на #64360)
Кто Throne юзает, как блять ему настроить чтобы локальные домены mDNS прлходили

<a id="msg_211750"></a>
### [msg_211750](chunk_0516.md#msg_211750) | 2026-08-06T15:05:49 | Rudi (в ответ на #64360)
по типу .local

<a id="msg_211751"></a>
### [msg_211751](chunk_0516.md#msg_211751) | 2026-08-06T15:05:57 | Rudi (в ответ на #64360)
по Ip я сделал

<a id="msg_211752"></a>
### [msg_211752](chunk_0516.md#msg_211752) | 2026-08-06T15:06:00 | Rudi (в ответ на #64360)
а вот домен не хочет

<a id="msg_211753"></a>
### [msg_211753](chunk_0516.md#msg_211753) | 2026-08-06T15:06:09 | Rudi (в ответ на #64360)
dns виноват сука, но я не знаю че не так

<a id="msg_211754"></a>
### [msg_211754](chunk_0516.md#msg_211754) | 2026-08-06T15:07:29 | Rudi (в ответ на #64360)
{
  "default_outbound": "proxy",
  "name": "Routing",
  "rules": [
    {
      "action": "hijack-dns",
      "name": "dns-hijack",
      "protocol": "dns",
      "type": "custom"
    },
    {
      "action": "sniff",
      "inbound": [
        "tun-in",
        "socks-in",
        "http-in"
      ],
      "name": "sniff",
      "type": "custom"
    },
    {
      "action": "route",
      "name": "bittorrent",
      "outbound": "direct",
      "protocol": "bittorrent",
      "type": "custom"
    },
    {
      "action": "route",
      "name": "geoip-ru",
      "outbound": "direct",
      "rule_set": [
        "geoip-ru",
        "geosite-category-gov-ru"
      ],
      "type": "custom"
    },
    {
      "action": "route",
      "domain_suffix": [
        "mesh"
      ],
      "name": "domain_suffix",
      "outbound": "direct",
      "type": "custom"
    },
    {
      "action": "route",
      "ip_cidr": [
        "192.168.0.0/16",
        "10.0.0.0/8",
        "100.64.0.0/10",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "fe80::/10",
        "fc00::/7",
        "100.123.0.0/16",
        "109.69.23.112/32",
        "192.168.200.0/24",
        "10.126.126.0/24"
      ],
      "name": "ip_cidr",
      "outbound": "direct",
      "type": "custom"
    },
    {
      "action": "route",
      "name": "process_name",
      "outbound": "direct",
      "process_name": [
        "easytier-core.exe",
        "easytier-cli.exe",
        "easytier-gui.exe",
        "qBittorrent.exe",
        "transmission-daemon",
        "transmission-qt",
        "uTorrent.exe",
        "BitTorrent.exe",
        "Deluge.exe"
      ],
      "type": "custom"
    }
  ],
  "v": 1
}

<a id="msg_211755"></a>
### [msg_211755](chunk_0516.md#msg_211755) | 2026-08-06T15:08:20 | Rudi (в ответ на #64360)
ну тут не .local надо а .mesh

<a id="msg_211756"></a>
### [msg_211756](chunk_0516.md#msg_211756) | 2026-08-06T15:24:25 | Артём Добринец (в ответ на #211754)
Нужно использовать правила для dns https://sing-box.sagernet.org/configuration/dns/rule/#structure

<a id="msg_211757"></a>
### [msg_211757](chunk_0516.md#msg_211757) | 2026-08-06T15:28:10 | Артём Добринец (в ответ на #64360)
Есть ещё такое пояснение от разработчика
You usually do not need an explicit mdns server in addition to a Local server: the local server already routes queries for *.local. and IPv4/IPv6 link-local reverse zones via mDNS on non-Apple platforms and via the system resolver on Apple platforms. Add an explicit mdns server only when you want to reference it from preferred_by or use it standalone.
Вообще на 4pda в теме есть пользователь, который очень хорошо знает всё по sing-box

<a id="msg_211758"></a>
### [msg_211758](chunk_0516.md#msg_211758) | 2026-08-06T15:30:41 | Rudi (в ответ на #64360)
ну mdns конкретно тут с .local

<a id="msg_211759"></a>
### [msg_211759](chunk_0516.md#msg_211759) | 2026-08-06T15:30:42 | Rudi (в ответ на #64360)
работает

<a id="msg_211760"></a>
### [msg_211760](chunk_0516.md#msg_211760) | 2026-08-06T15:30:45 | Rudi (в ответ на #64360)
а у меня .mesh

<a id="msg_211761"></a>
### [msg_211761](chunk_0516.md#msg_211761) | 2026-08-06T15:32:04 | Rudi (в ответ на #64360)
{
    "rules": [
        {
            "action": "route",
            "domain_suffix": [
                ".mesh"
            ],
            "server": "dns-direct"
        }
    ],
    "servers": [
        {
            "tag": "dns-direct",
            "type": "local"
        }
    ]
}

<a id="msg_211762"></a>
### [msg_211762](chunk_0516.md#msg_211762) | 2026-08-06T15:32:09 | Rudi (в ответ на #64360)
вот вродебы так

<a id="msg_211763"></a>
### [msg_211763](chunk_0516.md#msg_211763) | 2026-08-06T15:32:14 | Rudi (в ответ на #64360)
а не фуручит

<a id="msg_211764"></a>
### [msg_211764](chunk_0516.md#msg_211764) | 2026-08-06T15:32:26 | Rudi (в ответ на #64360)
antigravity тоже нихуя не помогает😭

<a id="msg_211765"></a>
### [msg_211765](chunk_0516.md#msg_211765) | 2026-08-06T16:10:59 | Александр (в ответ на #64360)
Как то можно в 3x-ui импортировать подключение с другого сервера? У меня каскад и хотелось бы в подписке видеть 1 прямое подключение

<a id="msg_211766"></a>
### [msg_211766](chunk_0516.md#msg_211766) | 2026-08-06T16:16:23 | - (в ответ на #64360)
Подскажите знающие, настроил cdn, с браузера если по техдомену или cname стучусь через прокси nginx на порт xhttp, в логах видно на самом серве, если с HAPP пингую нихуя не доходит, пинг стоит естественно на get запросах, напрямую на мой домен работает, а вот с HAPP как будто запрос до CDN доходит и дальше не але, че глянуть можно?

<a id="msg_211767"></a>
### [msg_211767](chunk_0516.md#msg_211767) | 2026-08-06T16:17:22 | agent adidas death of taliban (в ответ на #211766)
пользуйся услугами сертифицированного провайдера ООО КЛАСТЕР - vpnnow.space

<a id="msg_211768"></a>
### [msg_211768](chunk_0516.md#msg_211768) | 2026-08-06T16:19:16 | Kvink⁴² (Алексей) (в ответ на #211765)
В Исходящие его добавить,потом правила маршрутизации сделать для него

<a id="msg_211769"></a>
### [msg_211769](chunk_0516.md#msg_211769) | 2026-08-06T16:20:13 | Вася (в ответ на #211766)
Проверь по логам самого cdn где затык и какая ошибка вылетает

<a id="msg_211770"></a>
### [msg_211770](chunk_0516.md#msg_211770) | 2026-08-06T16:20:33 | Вася (в ответ на #211769)
Там понятнее будет

<a id="msg_211771"></a>
### [msg_211771](chunk_0516.md#msg_211771) | 2026-08-06T16:20:45 | Александр (в ответ на #211768)
Не не так. Про маршрутизацию я знаю. Мне бы просто инбаунд напрямую с другого сервера отображать в подписке

<a id="msg_211772"></a>
### [msg_211772](chunk_0516.md#msg_211772) | 2026-08-06T16:21:34 | - (в ответ на #211769)
по логам cdn это где?

<a id="msg_211773"></a>
### [msg_211773](chunk_0516.md#msg_211773) | 2026-08-06T16:21:43 | Kvink⁴² (Алексей) (в ответ на #211771)
Не как,3хуй такого не умеет

<a id="msg_211774"></a>
### [msg_211774](chunk_0516.md#msg_211774) | 2026-08-06T16:21:54 | Вася (в ответ на #211772)
Кто у тебя CDN ?

<a id="msg_211775"></a>
### [msg_211775](chunk_0516.md#msg_211775) | 2026-08-06T16:22:06 | Kvink⁴² (Алексей) (в ответ на #64360)
Завайбкодь

<a id="msg_211776"></a>
### [msg_211776](chunk_0516.md#msg_211776) | 2026-08-06T16:22:08 | - (в ответ на #211774)
timeweb

<a id="msg_211777"></a>
### [msg_211777](chunk_0516.md#msg_211777) | 2026-08-06T16:22:12 | Kvink⁴² (Алексей) (в ответ на #64360)
Будет классно если сделаешь

<a id="msg_211778"></a>
### [msg_211778](chunk_0516.md#msg_211778) | 2026-08-06T16:22:22 | Вася (в ответ на #211776)
А , так по-моему тайм веб отвалился

<a id="msg_211779"></a>
### [msg_211779](chunk_0516.md#msg_211779) | 2026-08-06T16:22:33 | Kvink⁴² (Алексей) (в ответ на #211777)
Или ремнавейв

<a id="msg_211780"></a>
### [msg_211780](chunk_0516.md#msg_211780) | 2026-08-06T16:22:41 | Kvink⁴² (Алексей) (в ответ на #211779)
Там такое можно вродь

<a id="msg_211781"></a>
### [msg_211781](chunk_0516.md#msg_211781) | 2026-08-06T16:22:49 | - (в ответ на #211778)
да нет, гет запрос с браузера то доходит без проблем

<a id="msg_211782"></a>
### [msg_211782](chunk_0516.md#msg_211782) | 2026-08-06T16:23:06 | Вася (в ответ на #211781)
Просто сколько типов в чат пишет , у всех проблема

<a id="msg_211783"></a>
### [msg_211783](chunk_0516.md#msg_211783) | 2026-08-06T16:23:11 | Kvink⁴² (Алексей) (в ответ на #211781)
А к самому впн то подключается? работает?

<a id="msg_211784"></a>
### [msg_211784](chunk_0516.md#msg_211784) | 2026-08-06T16:23:11 | Вася (в ответ на #64360)
Что на тайм веб не работает

<a id="msg_211785"></a>
### [msg_211785](chunk_0516.md#msg_211785) | 2026-08-06T16:23:27 | - (в ответ на #211783)
да если напрямую к домену своему без проблем

<a id="msg_211787"></a>
### [msg_211787](chunk_0516.md#msg_211787) | 2026-08-06T16:23:51 | - (в ответ на #211784)
у них была ошибка 403 что кеширует CDN их

<a id="msg_211788"></a>
### [msg_211788](chunk_0516.md#msg_211788) | 2026-08-06T16:24:00 | Вася (в ответ на #211787)
Так

<a id="msg_211789"></a>
### [msg_211789](chunk_0516.md#msg_211789) | 2026-08-06T16:24:03 | Александр (в ответ на #211773)
Анлаки. Пробовал через ноды делать но каким то хуем стерлась бд на другом серваке, пришлось из бекапа доставать

<a id="msg_211790"></a>
### [msg_211790](chunk_0516.md#msg_211790) | 2026-08-06T16:24:15 | Вася (в ответ на #64360)
Не я сегодня просто листал чат , тут было типо 8 у которых не работает тайм веб

<a id="msg_211791"></a>
### [msg_211791](chunk_0516.md#msg_211791) | 2026-08-06T16:24:18 | Вася (в ответ на #64360)
Или просто отвалился

<a id="msg_211792"></a>
### [msg_211792](chunk_0516.md#msg_211792) | 2026-08-06T16:24:30 | Вася (в ответ на #211790)
Мб просто строже сделали политику

<a id="msg_211793"></a>
### [msg_211793](chunk_0516.md#msg_211793) | 2026-08-06T16:24:40 | Вася (в ответ на #64360)
Вот и все падает

<a id="msg_211794"></a>
### [msg_211794](chunk_0516.md#msg_211794) | 2026-08-06T16:24:45 | Вася (в ответ на #64360)
Поиграйся с конфигом

<a id="msg_211795"></a>
### [msg_211795](chunk_0516.md#msg_211795) | 2026-08-06T16:24:46 | Kvink⁴² (Алексей) (в ответ на #64360)
Раскур ТФ бесплатно

<a id="msg_211797"></a>
### [msg_211797](chunk_0516.md#msg_211797) | 2026-08-06T16:26:02 | Kvink⁴² (Алексей) (в ответ на #211795)
Кто турбофлейр раскуртвает,присылайте способы маскировки для конфига xray

<a id="msg_211799"></a>
### [msg_211799](chunk_0516.md#msg_211799) | 2026-08-06T16:26:24 | Kvink⁴² (Алексей) (в ответ на #211797)
Хочу сделать универсальный

<a id="msg_211800"></a>
### [msg_211800](chunk_0516.md#msg_211800) | 2026-08-06T16:27:01 | Kvink⁴² (Алексей) (в ответ на #211799)
И тогда уже в открытый доступ выпущу скрипт на автораскур

<a id="msg_211801"></a>
### [msg_211801](chunk_0516.md#msg_211801) | 2026-08-06T16:27:59 | Rudi (в ответ на #64360)
ебать я думал это скам параша чтобы всякие лохи добавляли туда сервера и им ip банили потом

<a id="msg_211802"></a>
### [msg_211802](chunk_0516.md#msg_211802) | 2026-08-06T16:28:06 | Rudi (в ответ на #64360)
ЗФЩЫАШФЩЫЗВШАЗЩФЫВША

<a id="msg_211803"></a>
### [msg_211803](chunk_0516.md#msg_211803) | 2026-08-06T16:28:10 | Rudi (в ответ на #64360)
ну это моя шизотеория

<a id="msg_211804"></a>
### [msg_211804](chunk_0516.md#msg_211804) | 2026-08-06T16:28:12 | Rudi (в ответ на #64360)
та тот момент

<a id="msg_211805"></a>
### [msg_211805](chunk_0516.md#msg_211805) | 2026-08-06T16:28:12 | Kvink⁴² (Алексей) (в ответ на #211801)
Это факты

<a id="msg_211806"></a>
### [msg_211806](chunk_0516.md#msg_211806) | 2026-08-06T16:28:17 | agent adidas death of taliban (в ответ на #64360)
автораскур это когда ты качаешь один sh файлик с жидхаба, а он тебе и xray накатывает и раскур прописывает в config.json + nginx, и ключи выдаёт 🥰

<a id="msg_211807"></a>
### [msg_211807](chunk_0516.md#msg_211807) | 2026-08-06T16:28:21 | Kvink⁴² (Алексей) (в ответ на #64360)
Ну тут два типа забанились

<a id="msg_211808"></a>
### [msg_211808](chunk_0516.md#msg_211808) | 2026-08-06T16:28:40 | Kvink⁴² (Алексей) (в ответ на #211806)
Да,ток у меня там caddy

<a id="msg_211809"></a>
### [msg_211809](chunk_0516.md#msg_211809) | 2026-08-06T16:28:43 | Rudi (в ответ на #211805)
ну типо там все слишком просто, еще и БЕСПЛАТНО

<a id="msg_211810"></a>
### [msg_211810](chunk_0516.md#msg_211810) | 2026-08-06T16:28:48 | Rudi (в ответ на #64360)
а значит дело пахнет писюнами

<a id="msg_211811"></a>
### [msg_211811](chunk_0516.md#msg_211811) | 2026-08-06T16:29:04 | Kvink⁴² (Алексей) (в ответ на #211809)
Ну бля,я конфиг xray 2 дня перебирал

<a id="msg_211812"></a>
### [msg_211812](chunk_0516.md#msg_211812) | 2026-08-06T16:29:09 | Kvink⁴² (Алексей) (в ответ на #64360)
Чтоб заработал

<a id="msg_211813"></a>
### [msg_211813](chunk_0516.md#msg_211813) | 2026-08-06T16:29:17 | agent adidas death of taliban (в ответ на #211808)
ну какая разница главное чтобы ворк

<a id="msg_211814"></a>
### [msg_211814](chunk_0516.md#msg_211814) | 2026-08-06T16:29:18 | Rudi (в ответ на #64360)
ну я имаю в виду по сравнению с уебандексом

<a id="msg_211815"></a>
### [msg_211815](chunk_0516.md#msg_211815) | 2026-08-06T16:29:22 | Вася (в ответ на #211810)
Соберут патерны разошлют всем CDN и все

<a id="msg_211816"></a>
### [msg_211816](chunk_0516.md#msg_211816) | 2026-08-06T16:29:23 | Rudi (в ответ на #64360)
и сх cdn

<a id="msg_211817"></a>
### [msg_211817](chunk_0516.md#msg_211817) | 2026-08-06T16:29:24 | Kvink⁴² (Алексей) (в ответ на #64360)
Потому что в гайде у Артема он не правильный

<a id="msg_211818"></a>
### [msg_211818](chunk_0516.md#msg_211818) | 2026-08-06T16:29:33 | agent adidas death of taliban (в ответ на #64360)
го пацаны автораскур замутим

<a id="msg_211819"></a>
### [msg_211819](chunk_0516.md#msg_211819) | 2026-08-06T16:29:39 | agent adidas death of taliban (в ответ на #64360)
чтобы лишить комммерсов их прибылей

<a id="msg_211820"></a>
### [msg_211820](chunk_0516.md#msg_211820) | 2026-08-06T16:29:44 | Rudi (в ответ на #64360)
sni: max.ru ?

<a id="msg_211821"></a>
### [msg_211821](chunk_0516.md#msg_211821) | 2026-08-06T16:29:49 | Вася (в ответ на #211819)
Ух какой злой

<a id="msg_211823"></a>
### [msg_211823](chunk_0516.md#msg_211823) | 2026-08-06T16:29:54 | Вася (в ответ на #64360)
Без него никак

<a id="msg_211824"></a>
### [msg_211824](chunk_0516.md#msg_211824) | 2026-08-06T16:29:57 | Вася (в ответ на #64360)
Ну прям вообще никак

<a id="msg_211825"></a>
### [msg_211825](chunk_0516.md#msg_211825) | 2026-08-06T16:29:59 | agent adidas death of taliban (в ответ на #211820)
SNI любого ресурса который к сдн подключен

<a id="msg_211826"></a>
### [msg_211826](chunk_0516.md#msg_211826) | 2026-08-06T16:29:59 | Kvink⁴² (Алексей) (в ответ на #211815)
Вот я и хочу универсальный сделать

<a id="msg_211827"></a>
### [msg_211827](chunk_0516.md#msg_211827) | 2026-08-06T16:30:05 | agent adidas death of taliban (в ответ на #64360)
для турбы там айпишники нужно сканить

<a id="msg_211828"></a>
### [msg_211828](chunk_0516.md#msg_211828) | 2026-08-06T16:30:08 | Вася (в ответ на #211826)
Что бы все патерны собрали ?)

<a id="msg_211829"></a>
### [msg_211829](chunk_0516.md#msg_211829) | 2026-08-06T16:30:11 | Kvink⁴² (Алексей) (в ответ на #211826)
Path у меня уже сам генерится

<a id="msg_211830"></a>
### [msg_211830](chunk_0516.md#msg_211830) | 2026-08-06T16:30:19 | agent adidas death of taliban (в ответ на #211827)
https://hackertarget.com/reverse-ip-lookup/ вот здесь

<a id="msg_211831"></a>
### [msg_211831](chunk_0516.md#msg_211831) | 2026-08-06T16:30:23 | Вася (в ответ на #211829)
Прогрес

<a id="msg_211832"></a>
### [msg_211832](chunk_0516.md#msg_211832) | 2026-08-06T16:30:26 | agent adidas death of taliban (в ответ на #64360)
вбивай свой ип и смотри кто на него ходит из легитимных

<a id="msg_211833"></a>
### [msg_211833](chunk_0516.md#msg_211833) | 2026-08-06T16:30:33 | Kvink⁴² (Алексей) (в ответ на #211828)
Ну так не соберут если каждый уникальный будет

<a id="msg_211834"></a>
### [msg_211834](chunk_0516.md#msg_211834) | 2026-08-06T16:30:40 | agent adidas death of taliban (в ответ на #64360)
SNI ставишь какой правильнее, а host оставляешь свой

<a id="msg_211835"></a>
### [msg_211835](chunk_0516.md#msg_211835) | 2026-08-06T16:30:41 | Вася (в ответ на #211833)
Ну если каждый уникальный будет

<a id="msg_211836"></a>
### [msg_211836](chunk_0516.md#msg_211836) | 2026-08-06T16:30:43 | Вася (в ответ на #64360)
То четко

<a id="msg_211837"></a>
### [msg_211837](chunk_0516.md#msg_211837) | 2026-08-06T16:30:58 | Вася (в ответ на #211834)
Главное не забыть sni max.ru

<a id="msg_211838"></a>
### [msg_211838](chunk_0516.md#msg_211838) | 2026-08-06T16:31:01 | Вася (в ответ на #64360)
Иначе никак сука

<a id="msg_211839"></a>
### [msg_211839](chunk_0516.md#msg_211839) | 2026-08-06T16:31:08 | Rudi (в ответ на #64360)
вы все на панелях или вы тру щит бои вайбкодинг департмент инфинити токенс мод?

<a id="msg_211840"></a>
### [msg_211840](chunk_0516.md#msg_211840) | 2026-08-06T16:31:10 | agent adidas death of taliban (в ответ на #211837)
да ебанутый, макс не подключен к сдн

<a id="msg_211841"></a>
### [msg_211841](chunk_0516.md#msg_211841) | 2026-08-06T16:31:13 | agent adidas death of taliban (в ответ на #64360)
не разрезолвит

<a id="msg_211842"></a>
### [msg_211842](chunk_0516.md#msg_211842) | 2026-08-06T16:31:19 | Вася (в ответ на #211840)
Да блять , я угораю ебаный рот

<a id="msg_211843"></a>
### [msg_211843](chunk_0516.md#msg_211843) | 2026-08-06T16:31:27 | Kvink⁴² (Алексей) (в ответ на #211827)
Зачем

<a id="msg_211845"></a>
### [msg_211845](chunk_0516.md#msg_211845) | 2026-08-06T16:31:47 | agent adidas death of taliban (в ответ на #211843)
чтобы выставить sni условного газпрёма или спёрбанка

<a id="msg_211846"></a>
### [msg_211846](chunk_0516.md#msg_211846) | 2026-08-06T16:31:52 | Kvink⁴² (Алексей) (в ответ на #211839)
Ну на впс в Европе для ЧС 3хуй

<a id="msg_211847"></a>
### [msg_211847](chunk_0516.md#msg_211847) | 2026-08-06T16:32:11 | Kvink⁴² (Алексей) (в ответ на #211846)
А на ру серваке который к цдн xray прост

<a id="msg_211849"></a>
### [msg_211849](chunk_0516.md#msg_211849) | 2026-08-06T16:32:39 | Rudi (в ответ на #64360)
я pasarguard раскурил пока вроде норм (после ремны ощущение отсутствия всякого ненужного говна успокаивает)

<a id="msg_211850"></a>
### [msg_211850](chunk_0516.md#msg_211850) | 2026-08-06T16:32:54 | Вася (в ответ на #211849)
Это пока что

<a id="msg_211851"></a>
### [msg_211851](chunk_0516.md#msg_211851) | 2026-08-06T16:33:02 | Вася (в ответ на #64360)
Скоро всех нахуй на CDN банить будут

<a id="msg_211852"></a>
### [msg_211852](chunk_0516.md#msg_211852) | 2026-08-06T16:33:13 | Rudi (в ответ на #64360)
я не знаю

<a id="msg_211853"></a>
### [msg_211853](chunk_0516.md#msg_211853) | 2026-08-06T16:33:15 | Rudi (в ответ на #64360)
нахуя на них

<a id="msg_211854"></a>
### [msg_211854](chunk_0516.md#msg_211854) | 2026-08-06T16:33:17 | Вася (в ответ на #64360)
Я вам клянусь нахуй

<a id="msg_211855"></a>
### [msg_211855](chunk_0516.md#msg_211855) | 2026-08-06T16:33:17 | Rudi (в ответ на #64360)
сидят ваще

<a id="msg_211856"></a>
### [msg_211856](chunk_0516.md#msg_211856) | 2026-08-06T16:33:25 | Вася (в ответ на #211854)
Там скоро будет пиздец

<a id="msg_211857"></a>
### [msg_211857](chunk_0516.md#msg_211857) | 2026-08-06T16:34:01 | Вася (в ответ на #64360)
Скоро все будем сидеть и плакать

<a id="msg_211858"></a>
### [msg_211858](chunk_0516.md#msg_211858) | 2026-08-06T16:34:07 | Вася (в ответ на #64360)
Жизнь жестока

<a id="msg_211859"></a>
### [msg_211859](chunk_0516.md#msg_211859) | 2026-08-06T16:34:19 | Вася (в ответ на #64360)
Все способы перебанят

<a id="msg_211860"></a>
### [msg_211860](chunk_0516.md#msg_211860) | 2026-08-06T16:34:27 | Вася (в ответ на #64360)
Будем плакать

<a id="msg_211861"></a>
### [msg_211861](chunk_0516.md#msg_211861) | 2026-08-06T16:34:45 | Rudi (в ответ на #64360)
мосты на границе с казахстаном

<a id="msg_211862"></a>
### [msg_211862](chunk_0516.md#msg_211862) | 2026-08-06T16:34:45 | Kvink⁴² (Алексей) (в ответ на #211830)
No DNS A records found

<a id="msg_211863"></a>
### [msg_211863](chunk_0516.md#msg_211863) | 2026-08-06T16:34:55 | Kvink⁴² (Алексей) (в ответ на #211862)
Я свой айпи прост кому то дал

<a id="msg_211864"></a>
### [msg_211864](chunk_0516.md#msg_211864) | 2026-08-06T16:35:02 | Kvink⁴² (Алексей) (в ответ на #211863)
Чтоб взломали впс

<a id="msg_211865"></a>
### [msg_211865](chunk_0516.md#msg_211865) | 2026-08-06T16:35:36 | Александр (в ответ на #211848)
Бля чел 1000 благодарностей, все сработало. Хотя и мой костыльный способ по тогу сработал

<a id="msg_211866"></a>
### [msg_211866](chunk_0516.md#msg_211866) | 2026-08-06T16:35:48 | agent adidas death of taliban (в ответ на #211862)
по другому ищи

<a id="msg_211867"></a>
### [msg_211867](chunk_0516.md#msg_211867) | 2026-08-06T16:35:51 | Kvink⁴² (Алексей) (в ответ на #211865)
Рил

<a id="msg_211868"></a>
### [msg_211868](chunk_0516.md#msg_211868) | 2026-08-06T16:35:56 | Kvink⁴² (Алексей) (в ответ на #211867)
Такое есть?

<a id="msg_211869"></a>
### [msg_211869](chunk_0516.md#msg_211869) | 2026-08-06T16:35:58 | Kvink⁴² (Алексей) (в ответ на #64360)
Ахуй

<a id="msg_211870"></a>
### [msg_211870](chunk_0516.md#msg_211870) | 2026-08-06T16:36:36 | Вася (в ответ на #211861)
Обязательно

<a id="msg_211871"></a>
### [msg_211871](chunk_0516.md#msg_211871) | 2026-08-06T16:36:58 | Kvink⁴² (Алексей) (в ответ на #211866)
Ура cdnozon.ru

<a id="msg_211872"></a>
### [msg_211872](chunk_0516.md#msg_211872) | 2026-08-06T16:37:34 | agent adidas death of taliban (в ответ на #211871)
egrnotchet.com
egrpru.com
geokupol.com
wmexchange24.com
ulan-u.de
clowteh.fun
voxme.fun
onpay24.net
harmonymeditation.online
pulse24.online
runafinance.online
ruprava.online
st4nt3rs.online
anime-view.org
smetly.pro
anywhereusb.ru
catsvideo.ru
cuberbug.ru
rst1.cuberbug.ru
diarybydrozdova.ru
enot64.ru
expresswc.ru
gidar.ru
glowstone.ru
lakont.ru
leadbureau.ru
mostbio.ru
mqlab.ru
www.optdom52.ru
paseka5.ru
pdcloud.ru
pixelique.ru
prigovor.ru
rayconnection.ru
www.rayconnection.ru
shablontech.ru
www.shablontech.ru
sitimweb.ru
wikitropes.ru
anadyr.site
shaaa.space
lexa.su
nuko.top
radioboom.vip
xn--80aag4afk.xn--p1acf
440880.xyz
xcheapi.xyz

вот ещё

<a id="msg_211873"></a>
### [msg_211873](chunk_0516.md#msg_211873) | 2026-08-06T16:38:20 | Kvink⁴² (Алексей) (в ответ на #64360)
lexa.su не открывается:(((((

<a id="msg_211874"></a>
### [msg_211874](chunk_0516.md#msg_211874) | 2026-08-06T16:39:22 | Вася (в ответ на #64360)
Бля прикол на .ru отдают 504

<a id="msg_211875"></a>
### [msg_211875](chunk_0516.md#msg_211875) | 2026-08-06T16:39:29 | Вася (в ответ на #64360)
А на всех остальных просто не открывается

<a id="msg_211876"></a>
### [msg_211876](chunk_0516.md#msg_211876) | 2026-08-06T16:39:31 | Вася (в ответ на #64360)
Прикольно

<a id="msg_211877"></a>
### [msg_211877](chunk_0516.md#msg_211877) | 2026-08-06T16:39:34 | Kvink⁴² (Алексей) (в ответ на #211873)
pupok.space тоже не открывается

<a id="msg_211878"></a>
### [msg_211878](chunk_0516.md#msg_211878) | 2026-08-06T16:40:26 | Kvink⁴² (Алексей) (в ответ на #64360)
rap-battles.ru

<a id="msg_211879"></a>
### [msg_211879](chunk_0516.md#msg_211879) | 2026-08-06T16:40:29 | Kvink⁴² (Алексей) (в ответ на #64360)
Открылся

<a id="msg_211880"></a>
### [msg_211880](chunk_0516.md#msg_211880) | 2026-08-06T16:41:36 | agent adidas death of taliban (в ответ на #64360)
cdn-v2.soulteam.academy,81.222.127.189
thor.stage.cdn.ru.buddy.ai,81.222.127.189
files.cloft.ai,81.222.127.189
cdn.freezio.app,81.222.127.189
cdn.korpu.app,81.222.127.189
cdn.sweely.app,81.222.127.189
ac22.sowhee.art,81.222.127.189
cdn.athome.asia,81.222.127.189
plain.dagestancousine.biz,81.222.127.190
cdn1.chikiriki.club,81.222.127.189
cdn2.acdamate.com,81.222.127.189
upcd.appnestflowed.com,81.222.127.189
upcd.appsoftcore.com,81.222.127.189
fam-test-cdn.beauit.com,81.222.127.189
docs.biosvyaz.com,81.222.127.189
app-cdn.blythecollection.com,81.222.127.189
cdn.caroroom.com,81.222.127.189
cdn-ru.casinist.com,81.222.127.189
files-ru.casinist.com,81.222.127.189
static-ru.casinist.com,81.222.127.189
upcd.cloudsoftcore.com,81.222.127.189
cdn.coinsgem.com,81.222.127.189
ru.match3-static.eidoloncorp.com,81.222.127.189
ru.tapaway-static.eidoloncorp.com,81.222.127.189
content.ermine-games.com,81.222.127.189
media.futwebapp.com,81.222.127.189
ru-cdn.fylio.com,81.222.127.189
static.gamegamerhive.com,81.222.127.189
upcd.gameplayfoundry.com,81.222.127.189
img.geliophoto.com,81.222.127.189
cdn.getmeetb.com,81.222.127.189
cdn-test.hakaga.com,81.222.127.189
cdn-ru.hgplinko.com,81.222.127.189
ru.cdn.hgplinko.com,81.222.127.189
apk-kz.impcdn.com,81.222.127.190
static-s.kinorium.com,81.222.127.189
stone.loadbolder.com,81.222.127.189
www.lumerasys.com,81.222.127.189
marchelas.com,81.222.127.189
cdn.marchelas.com,81.222.127.189
cdn-ru.mergecakegame.com,81.222.127.189
my.muzzeless.com,81.222.127.190
cdn-ru.myranchgame.com,81.222.127.189
cdn-proxied-sl.oxidesurvival.com,81.222.127.157
cdn.pariexpert.com,81.222.127.189
media.cdn.planx3d.com,81.222.127.189
upcd.playmodeongame.com,81.222.127.189
cdn.ploadbara.com,81.222.127.189
e.ploadbara.com,81.222.127.189
cdn.postnikovmd.com,81.222.127.189
upcd.programcraftsoft.com,81.222.127.189
upcd.programgridtech.com,81.222.127.189
cdn-stage.quietsapa.com,81.222.127.189
media-cdn.restik.com,81.222.127.189
upcd.softnesbpro.com,81.222.127.189
cdn-ru.solitairepuzzle.com,81.222.127.189
cdn.sprosivracha.com,81.222.127.189
cdn2.static-jpt.com,81.222.127.189
wwcdn.sugargames.com,81.222.127.189
cdn.totdom.com,81.222.127.189
upcd.virtualvictorygame.com,81.222.127.189
cdn-cdp.webskyx.com,81.222.127.189
docs.wikkeo.com,81.222.127.189
cdn.wirenboard.com,81.222.127.189
41t.dev,81.222.127.189
labs.41t.dev,81.222.127.189
cdn.develop.efood.dev,81.222.127.189
news-img.gismeteo.dev,81.222.127.189
cdn.try.fit,81.222.127.189
ru.cdn.mergeville.games,81.222.127.189
cdn-s-gsb.tortuga.games,81.222.127.189
media1.webproject.group,81.222.127.189
atriaasean.info,81.222.127.189
alexeev.life,81.222.127.189
alxv.life,81.222.127.189
dwltr.life,81.222.127.189
cdn-media.lookport.live,81.222.127.189
cdn.chpu.market,81.222.127.189
rcdn.appcast.pkrt.me,81.222.127.189
supercell.media,81.222.127.189
data.steam.money,81.222.127.189
cdn-nsowp9vxc32z.bosx.net,81.222.127.189
imcdn.cdnpic.net,81.222.127.189
avatars-ru.evercasino.net,81.222.127.189
base-images-ru.evercasino.net,81.222.127.189
gate.minopay.net,81.222.127.189
0270f8d6-6d85-4ae0-bdcf-83520816f01e.selcdn.net,81.222.127.189
05a9db09-4f7c-41c8-b05c-62b90878d1ad.selcdn.net,81.222.127.189
072f0aa9-45e3-414e-9478-ee94d66adf2f.selcdn.net,81.222.127.189
08407298-5abb-4b0c-94d1-adc827e6f886.selcdn.net,81.222.127.189
0a519d2b-2050-4f1c-ab99-c91f84cf7f99.selcdn.net,81.222.127.189
0b635dda-55e5-40a0-8283-d4714f3a2e33.selcdn.net,81.222.127.189
0c18a7eb-4b8a-4c06-ae6f-1b3c681dd08a.selcdn.net,81.222.127.189
0d6dc691-f928-459d-b293-be5dc0a7bcd5.selcdn.net,81.222.127.189
0efd7589-281c-48fc-a2e4-328f9a40a5b5.selcdn.net,81.222.127.190
10b26050-e4f1-4a02-a0a5-88d90cd2b62c.selcdn.net,81.222.127.189
1238b6ae-6e84-45ec-9f24-340a7f591eed.selcdn.net,81.222.127.189
1258877e-1c06-445f-9ad6-ff59408d487b.selcdn.net,81.222.127.189
12bb6ecf-bda5-4c99-816b-12bda79f6bd9.selcdn.net,81.222.127.189
14932901-854b-48e2-984e-8f96abdb9f4f.selcdn.net,81.222.127.189
166ba6ce-eee2-43f1-87a4-b80ece869977.selcdn.net,81.222.127.189
192ebe36-a241-46a9-8e2a-d17d708f4aa1.selcdn.net,81.222.127.189
1d479686-7139-4edf-9c52-fd28ff5a38e4.selcdn.net,81.222.127.190
1da508ff-7506-4642-9676-6066f824ee42.selcdn.net,81.222.127.190
1e01a66e-2c75-4611-bf2f-c385574d4893.selcdn.net,81.222.127.189
1e9cf14c-fc19-4c51-bce0-2cc6e9631ded.selcdn.net,81.222.127.189
1f446cc4-fba3-4b1f-867b-e66bb099b2c4.selcdn.net,81.222.127.189
2024660e-2b96-4b06-895f-4898f6ed61eb.selcdn.net,81.222.127.189
20d21fa4-1e3a-4de3-bafc-b9e26e04f706.selcdn.net,81.222.127.189
21816ae2-324e-44f7-b7b7-d9763c826dee.selcdn.net,81.222.127.189
231106c9-cc61-48d5-b577-6e6ea329cc7b.selcdn.net,81.222.127.189
2367f896-8060-4f3c-ae30-37af2b6999e9.selcdn.net,81.222.127.189
25aa34f8-a6a7-40c2-8c8d-49b7f17fca28.selcdn.net,81.222.127.189
263d01ed-0bc6-477e-9b66-11cc51d022b5.selcdn.net,81.222.127.189
2745aa6d-29b7-45ba-a590-5419725fb3b0.selcdn.net,81.222.127.189
2936c38c-336b-4e7e-843e-6b632e64ee8d.selcdn.net,81.222.127.189
297d148b-a06d-45a6-a634-a7bb4ddb9578.selcdn.net,81.222.127.189
298658ad-dd3d-437c-8d2c-96d5f69a5da6.selcdn.net,81.222.127.189
2a64601a-9f60-4d9b-93cc-e8531bc0f614.selcdn.net,81.222.127.189
2e64d588-8062-4a4f-b598-8c2d27fab44d.selcdn.net,81.222.127.189
2fadd974-279a-4a7e-92cf-301e131c12bc.selcdn.net,81.222.127.189
31039303-6cc3-4ed1-bf41-8f1962eb0936.selcdn.net,81.222.127.189
31c9b804-5aae-42e9-9a45-ede970439cc3.selcdn.net,81.222.127.189
32b3810d-7df3-44a3-8cd9-42d9f617f5fd.selcdn.net,81.222.127.189
32b4d68c-8c43-486e-a289-0276ec7f8768.selcdn.net,81.222.127.189
33e536c6-37bc-4f33-a9f5-faf128990f42.selcdn.net,81.222.127.189
33f2eaf3-2ca9-4ffb-9848-83582f1cd5f2.selcdn.net,81.222.127.189
34b30f75-f100-4984-ab4e-ac8b6054ebae.selcdn.net,81.222.127.189
351d8081-639e-4bf4-8fa8-dd54378fa14a.selcdn.net,81.222.127.189
356a4132-2079-4314-a7c2-ea800031a00e.selcdn.net,81.222.127.189
357346c5-ba53-48b8-8f1d-1ea1c32218d0.selcdn.net,81.222.127.189
3615ff58-44b0-4276-a579-3208d42d8034.selcdn.net,81.222.127.189
36edb97c-8a49-41cb-91aa-c5bee839b1a8.selcdn.net,81.222.127.189
37098036-e704-4f1d-9785-f585fecc29f0.selcdn.net,81.222.127.189
377eed5e-c491-4c37-b6d4-6102d49c544f.selcdn.net,81.222.127.189
3783a73a-387b-415a-bebd-d2f5f35aeb81.selcdn.net,81.222.127.189
383da3c5-851f-460a-8be2-540bcd1f56af.selcdn.net,81.222.127.189
3870996b-0ba5-4924-8515-844b7e01e64a.selcdn.net,81.222.127.189
39a58a7f-c0ba-48a3-b229-cb3bcddc144e.selcdn.net,81.222.127.189
39ab0d1c-31b9-481d-bde1-099152505b46.selcdn.net,81.222.127.189
3aac4b8d-0d2b-40a4-949d-d1af5c84d0d2.selcdn.net,81.222.127.189
3b7a104b-2d2e-49f6-b64d-ebfeac889567.selcdn.net,81.222.127.189
3de3f184-b64f-4d41-9ad5-cc9ef6ccaf1e.selcdn.net,81.222.127.189
3deec587-dfbe-4cf3-b5e3-8601434324d1.selcdn.net,81.222.127.189
40319fdf-af09-4121-98a7-6044366b4f33.selcdn.net,81.222.127.189
424c152c-475f-4381-8f51-c357732826c1.selcdn.net,81.222.127.189
427185d2-462f-47e3-8b6b-fef8beb4c26f.selcdn.net,81.222.127.189
427c21ae-dd21-456d-9707-b058438c9886.selcdn.net,81.222.127.189
4377ec53-1d56-40cd-873a-2b1eb6ef7a02.selcdn.net,81.222.127.189
451942ed-9762-4100-9ca2-f0c3f206fe16.selcdn.net,81.222.127.189
455053fb-1245-4be1-8f3f-366f6ac7d12c.selcdn.net,81.222.127.189
4930f2fb-febc-4822-b23b-44acf57e4586.selcdn.net,81.222.127.189
495053f9-ddff-411d-8f42-fe1269ac75bb.selcdn.net,81.222.127.189
4aebd863-43b3-4378-ab6d-426a3191ffbc.selcdn.net,81.222.127.189
4babc48d-4b39-4f51-b42c-82f2295052ef.selcdn.net,81.222.127.189
4fef8a60-ef05-4e1c-950a-13cb9658576d.selcdn.net,81.222.127.189
50dbf3bb-7d53-4f07-be97-6e3e08b9ac3b.selcdn.net,81.222.127.189
53927068-b946-4777-8a28-c9868b298c6d.selcdn.net,81.222.127.189
5422a864-4759-4455-9135-a440a624e97b.selcdn.net,81.222.127.190
572103db-6f81-4536-9124-0a48eb471532.selcdn.net,81.222.127.189
590f46f3-e5b9-4b84-9439-6214b827dc32.selcdn.net,81.222.127.189
5921bcac-d31b-42bc-a104-b2ae5b06b783.selcdn.net,81.222.127.189
598a0ce8-0919-46ca-bb16-e0976a99aa4f.selcdn.net,81.222.127.189
5a7ca001-f570-4de9-88ac-b3617755bd26.selcdn.net,81.222.127.189
5c46000f-fbfa-4ebe-8a48-fc0bd4abeb83.selcdn.net,81.222.127.189
5db764a2-48fe-403b-8bca-72f6cfead9fd.selcdn.net,81.222.127.189
5eb95a70-d945-4778-a5e0-994fa97e64eb.selcdn.net,81.222.127.189

<a id="msg_211881"></a>
### [msg_211881](chunk_0516.md#msg_211881) | 2026-08-06T16:41:37 | agent adidas death of taliban (в ответ на #64360)
5f2e5dd0-12e5-4287-8400-ab65831445d7.selcdn.net,81.222.127.189
6251637c-5354-4233-be34-525ab9e62e82.selcdn.net,81.222.127.189
64d90572-5c01-4740-9fda-1ac35c1532cf.selcdn.net,81.222.127.189
657ce016-f7a1-4d7a-97d0-d1258f944fd9.selcdn.net,81.222.127.189
66d04b9c-755a-49b5-8d18-c866ced2cb76.selcdn.net,81.222.127.189
687ee1fa-672d-4484-92d4-895427d9fd46.selcdn.net,81.222.127.189
6894b31c-954a-4ff1-b391-3b9f764fb403.selcdn.net,81.222.127.189
6caae5b2-180b-481a-9875-adeeb70ddc3f.selcdn.net,81.222.127.189
6d4e8e21-0667-4863-8ac5-4b076935e69e.selcdn.net,81.222.127.189
6e12bc39-17fd-47b2-9978-d37e343c9711.selcdn.net,81.222.127.189
6e4d8a6f-2de4-4a72-9251-96a23270b6b5.selcdn.net,81.222.127.189
6ef4e6a1-9d49-47ac-bfed-170f67a815cf.selcdn.net,81.222.127.189
704ff876-6109-4de2-b838-b596bdb6a2b3.selcdn.net,81.222.127.189
71c992e6-4c35-4743-91f9-87e1f430f95c.selcdn.net,81.222.127.189
720c7971-715e-49e9-9ae3-b0109d795ce4.selcdn.net,81.222.127.189
72ec245e-7b58-4b71-a948-3c95cd185228.selcdn.net,81.222.127.189
73dcbbea-b593-43af-9bab-b29865404be5.selcdn.net,81.222.127.189
74187a9d-4791-4313-acf1-8e02a7eda689.selcdn.net,81.222.127.189
776d42c5-ed1a-4e86-a1c8-73c7ee9544f5.selcdn.net,81.222.127.189
777abc8f-bb74-4aaf-a335-4215eea31c90.selcdn.net,81.222.127.189
7801f777-e635-4943-a0db-72f1c0919e29.selcdn.net,81.222.127.189
783795fb-3432-4c90-a805-d0b20b3fe2cf.selcdn.net,81.222.127.189
788815b7-f99e-4953-bda4-92c77fb6eb13.selcdn.net,81.222.127.189
79607237-ab50-4703-896f-64eef5bce36c.selcdn.net,81.222.127.189
7a201345-dfa8-477d-9948-67cbe7c67fac.selcdn.net,81.222.127.189
7bd1d942-cc4b-4bf7-be3d-3b881b937f9f.selcdn.net,81.222.127.189
7c7c458d-34ba-4ee1-839e-17f36ac7e868.selcdn.net,81.222.127.189
7cd51606-0d62-4424-b915-bbb1674d83ac.selcdn.net,81.222.127.189
7de646e5-471f-4c1c-900e-0badd71dba65.selcdn.net,81.222.127.189
7df0bc22-b464-492c-afcd-7c889297f562.selcdn.net,81.222.127.189
81a8ea4e-57fd-44d6-b848-cc8273ca4004.selcdn.net,81.222.127.189
84a84821-3c31-4cac-ad37-d043d299ca0b.selcdn.net,81.222.127.189
8571a11f-f37b-4160-b878-f32b540faa27.selcdn.net,81.222.127.189
87859397-eaa6-4a82-a0d6-2da66b63238c.selcdn.net,81.222.127.189
896dbbcc-bf42-4ac2-95a1-edaffb277cb0.selcdn.net,81.222.127.189
8ab2c1af-c36a-4ea1-82b6-1be692f7afd2.selcdn.net,81.222.127.189
8b91a34b-59e5-484a-8bb4-dfe5dc6db7e8.selcdn.net,81.222.127.189
8ea059a4-dc9b-4393-9ee2-9aefc2e3521f.selcdn.net,81.222.127.189
90537cf8-246e-4656-a60a-1934001de2ad.selcdn.net,81.222.127.189
90e10c1d-569c-47e9-9740-4f2610e9d24b.selcdn.net,81.222.127.189
9245fa52-6432-4be6-bce2-4b1bf9747825.selcdn.net,81.222.127.189
9359a633-7f51-47e1-8e54-1e5f1bf0e1e4.selcdn.net,81.222.127.189
9360ffdf-6ae6-45cc-a5bc-1dda548e2242.selcdn.net,81.222.127.189
9408ed25-e83a-4289-97d3-30879faec0c1.selcdn.net,81.222.127.189
957cf8e4-7ae7-407a-b069-a9b50c2ef1d7.selcdn.net,81.222.127.189
98b81c1d-1a06-4b0b-ae48-f4b49a4cf52b.selcdn.net,81.222.127.189
993409ce-a155-4050-a6d0-2c2513a9e541.selcdn.net,81.222.127.189
9b01795f-c552-4d53-90fd-e8ed84489420.selcdn.net,81.222.127.189
9c1e1f7c-faea-489f-aeed-e13acb9d46f2.selcdn.net,81.222.127.189
9e0a7731-0549-4954-b6be-d38356e37ae5.selcdn.net,81.222.127.189
9ff55adf-011a-46af-9d3c-7a8f0807a8e0.selcdn.net,81.222.127.189
a2202a8f-5c84-4dcb-8396-00a8a90bcef5.selcdn.net,81.222.127.189
a32095e6-2461-405c-8ad6-fbd1767e7fba.selcdn.net,81.222.127.189
a3276246-1b21-495f-a41b-7b7cd816c3a2.selcdn.net,81.222.127.189
a46dbbda-a510-4717-b79b-006cdea8372e.selcdn.net,81.222.127.190
a69a0c88-694c-43e0-ae5a-445a7fb87327.selcdn.net,81.222.127.189
a71963fb-5fcb-44fd-b832-0c3bed2441f3.selcdn.net,81.222.127.189
a8e78abd-82e8-40a6-8517-d2528a947a86.selcdn.net,81.222.127.189
a909fed7-55e8-4b74-a93d-d765a7c975c2.selcdn.net,81.222.127.189
ab1ce0c6-8983-47aa-9e6b-3f17e390fc20.selcdn.net,81.222.127.189
ab1eb084-32bb-44b1-93c1-c1a89196d96d.selcdn.net,81.222.127.189
af383fc1-9546-4a84-af96-2f6eca88bef3.selcdn.net,81.222.127.189
af8c54bd-099b-4e75-8e8b-f5ba068eb7b6.selcdn.net,81.222.127.189
b0f811a5-6035-49d6-bf01-82441c3376d2.selcdn.net,81.222.127.189
b55d83c2-c25d-46dd-87f4-faa682e06a05.selcdn.net,81.222.127.189
b5745c65-76e9-4659-a506-b6fa1bbdcc38.selcdn.net,81.222.127.189
b57ad705-9193-45a2-927f-c1634475930a.selcdn.net,81.222.127.189
bb6a332b-2135-41b9-aa0b-eb416a900fbb.selcdn.net,81.222.127.189
bcb14a28-9764-44b9-a3cb-7744b178d13a.selcdn.net,81.222.127.189
bdbe2fe9-9b85-4bda-a82b-ea1e66ef1b91.selcdn.net,81.222.127.189
bdfad70e-2e4d-4343-a92f-030c98529de8.selcdn.net,81.222.127.189
beb7322c-4551-4d2b-8f7c-d5dcdff018a3.selcdn.net,81.222.127.190
bfb79b95-79e5-4d1c-aca6-dff3e3bdf87a.selcdn.net,81.222.127.189
c359c46a-98dc-4fd3-8b3a-fd025ed1382d.selcdn.net,81.222.127.189
c3ac682b-ffb8-4b79-a999-f83c2acdfbba.selcdn.net,81.222.127.189
c5e58c2d-c2b9-4e07-99f9-c0a752bf7532.selcdn.net,81.222.127.189
c684eda0-6a3e-47ba-ae2e-ba7ccb118f00.selcdn.net,81.222.127.189
c71b2c17-4e6f-48ce-a684-0c4eca3b4ddf.selcdn.net,81.222.127.189
c8c017df-4dcd-4ee0-9f78-c431b7747bce.selcdn.net,81.222.127.189
ccbefb67-363a-4ee1-b844-e58c46019043.selcdn.net,81.222.127.189
cefa2aa0-5d81-4efb-b349-8b410fe937a9.selcdn.net,81.222.127.189
d0140abb-0db9-41ce-8be7-a261488de696.selcdn.net,81.222.127.189
d1311fd7-75f0-4659-b9c1-3be22f4c11c5.selcdn.net,81.222.127.189
d15b3af6-c2ea-48a9-80bc-674e60d2ff5f.selcdn.net,81.222.127.189
d1660e22-8562-49d4-826a-237397395cba.selcdn.net,81.222.127.189
d2b1ee6c-196d-4807-9629-d6948a83ca6e.selcdn.net,81.222.127.189
d2ea4a04-f1fa-4c54-b969-0ca0b92ca2fa.selcdn.net,81.222.127.189
d34fbdcb-df7a-4cdb-b024-ced10244bd73.selcdn.net,81.222.127.189
d3775806-f474-44ab-a7d8-500ecbcd7ed5.selcdn.net,81.222.127.189
d5bd1f88-4887-44bd-9ffc-d9d4daaebe9a.selcdn.net,81.222.127.189
d6869ddc-d09d-4628-83a3-541bb2c7cba8.selcdn.net,81.222.127.189
d6d41f06-ad57-4f7a-88ec-0e83ce6a1605.selcdn.net,81.222.127.189
d89700a7-49f7-4ad7-a992-26ce0afa64e2.selcdn.net,81.222.127.189
d897c100-2088-4e85-8abc-bcc2715369a9.selcdn.net,81.222.127.189
d8a6a33f-3369-444b-9b5f-793c13ff0708.selcdn.net,81.222.127.189
dc1e593c-891c-4c3f-a32a-be4011b4d7a6.selcdn.net,81.222.127.189
df11b9ce-4767-4d7c-ba5b-320758779a2c.selcdn.net,81.222.127.189
e036ce69-5007-4914-894f-e9f52c1687bb.selcdn.net,81.222.127.189
e0e2ff7a-27ae-46ac-8c41-7469f1bbb8ca.selcdn.net,81.222.127.189
e276d0bd-5454-4b3a-ab42-aa16f0fe07d7.selcdn.net,81.222.127.189
e367edcb-f9b7-477c-b1db-714b86a507aa.selcdn.net,81.222.127.189
e577938b-4f32-459b-87b4-1cc844018fcc.selcdn.net,81.222.127.189
e5a186bf-16c6-41eb-b40a-387b16039164.selcdn.net,81.222.127.190
e5babf88-c3b9-4f6c-8982-7094d5ef8929.selcdn.net,81.222.127.190
e7a0c530-9de4-4464-a00a-ea338c59a9ac.selcdn.net,81.222.127.189
eaa8c65f-60fc-4fda-9a20-dd16e1751411.selcdn.net,81.222.127.189
eab24eca-865b-4ced-9fd3-8d59ba3fdd50.selcdn.net,81.222.127.189
eb80ee4f-ecf2-4508-a07d-cdfca9bf0c1c.selcdn.net,81.222.127.189
eea1b42c-7481-43e6-af7b-3fd8408daf32.selcdn.net,81.222.127.189
f01b549a-80de-4978-a64a-bba1cc0f4cad.selcdn.net,81.222.127.189
f2cb7884-adb7-4ebc-a4f9-7f8e85b8d2a6.selcdn.net,81.222.127.189
f2e83576-8813-422e-aef8-d32079878b71.selcdn.net,81.222.127.189
f30883ec-62a0-4452-ac37-552c441ee423.selcdn.net,81.222.127.189
f5f765c2-6874-42fe-b7d8-5599d67a8386.selcdn.net,81.222.127.189
f7350f46-5e7a-40b6-8747-d348377e2d72.selcdn.net,81.222.127.189
fc825993-f89d-44a3-9a51-b415f5def48c.selcdn.net,81.222.127.189
fd58dd82-f6e2-4a94-827c-2cdc88b9436e.selcdn.net,81.222.127.189
cdn.siwamusic.net,81.222.127.189
10pa8uz1or.a.trbcdn.net,81.222.127.190
assets-frontend.weeek.net,81.222.127.189
cdn.ezha.online,81.222.127.190
app.gift-foundation.online,81.222.127.189
live.huskyhub.online,81.222.127.190
update.novarf.online,81.222.127.189
store.rf-platform.online,81.222.127.189
dev-api3.truestat.online,81.222.127.189
cdns.tutprosto.online,81.222.127.190
game.vyzhivaliti.online,81.222.127.189
setup.zapis24.online,81.222.127.189
cdn.qleter48t.dpdns.org,81.222.127.190
cdn.32cars.ru,81.222.127.189
cdn.4k-monitors.ru,81.222.127.189
cdn.4k-pc.ru,81.222.127.189
cdn3.adrun.ru,81.222.127.189
advisoraffects.ru,81.222.127.189
cdn.angelbless.ru,81.222.127.189
cdn.anitachess.ru,81.222.127.190
cdn.bcs.ru,81.222.127.189
tile.gis.big3.ru,81.222.127.189
im4.bloha.ru,81.222.127.189

<a id="msg_211882"></a>
### [msg_211882](chunk_0516.md#msg_211882) | 2026-08-06T16:41:38 | agent adidas death of taliban (в ответ на #64360)
cdn.boltapp.ru,81.222.127.189
cdn.bonusplan.ru,81.222.127.189
img-stage.brikx.ru,81.222.127.189
kem.c.bsps.ru,81.222.127.189
krs.c.bsps.ru,81.222.127.189
tsk.c.bsps.ru,81.222.127.189
cartag.ru,81.222.127.189
cdn.chartsgo.ru,81.222.127.189
cdn2.chickenpromo.ru,81.222.127.189
dialectichortic.ru,81.222.127.189
cdn.dialogo.ru,81.222.127.189
cdn3.dimkapupka.ru,81.222.127.190
hls.donee.ru,81.222.127.189
tizer.eiwi.ru,81.222.127.190
videos.eiwi.ru,81.222.127.190
www.elenabadanina.ru,81.222.127.189
vote-cdn.er.ru,81.222.127.189
c.f1news.ru,81.222.127.189
forumcdn.f1news.ru,81.222.127.189
cdn.facee.ru,81.222.127.189
cdn.finolog.ru,81.222.127.189
media.frents.ru,81.222.127.189
cdn-tiles-planet.gdemoideti.ru,81.222.127.189
update.getcompass.ru,81.222.127.189
stage-static-sso.gid-auth.ru,81.222.127.189
portal-static-preprod.gid.ru,81.222.127.189
map.goyland.ru,81.222.127.189
cdn.hisense.ru,81.222.127.189
honestpartners.ru,81.222.127.189
hootsub.hootlakes.ru,81.222.127.189
cs.hotelstartup.ru,81.222.127.189
english.imedia.ru,81.222.127.189
cdn.img-gorod.ru,81.222.127.189
content.img-gorod.ru,81.222.127.189
infuriatedate.ru,81.222.127.189
cdn.instagentbot.ru,81.222.127.189
download.irmodel.ru,81.222.127.189
cdn.jamfind.ru,81.222.127.189
cdn-v2.arzamas.kassy.ru,81.222.127.189
imcdn.klubgidov.ru,81.222.127.189
cdn.kubach.ru,81.222.127.189
cdn.ledyahcollege.ru,81.222.127.189
cdn.legalsound.ru,81.222.127.189
storage.lirs-market.ru,81.222.127.189
sct.liveimg.ru,81.222.127.189
sc.api.megapteka.ru,81.222.127.189
upcd.minecrafttoday.ru,81.222.127.189
cdn.storage.mobifitness.ru,81.222.127.189
imgs4.mrgav.ru,81.222.127.189
cdn.mvk-spb.ru,81.222.127.189
get.net-freedom.ru,81.222.127.189
tr.neurowow.ru,81.222.127.189
staticwebp.next2u.ru,81.222.127.189
cdn.oleksik.ru,81.222.127.189
footballmanager.one-team.ru,81.222.127.189
cdn.demo.onlinepatent.ru,81.222.127.189
cdn.orident.ru,81.222.127.189
cdn.ouglichwatch.ru,81.222.127.189
cdn-assets.padel.ru,81.222.127.189
s02.cdn.pegast.ru,81.222.127.189
st.peopletalk.ru,81.222.127.189
cdn.pericarditis.ru,81.222.127.189
cdn.profile.ru,81.222.127.189
data.profinansy.ru,81.222.127.189
images.psilog.ru,81.222.127.189
cdn-static.randewoo.ru,81.222.127.189
cdn120.randewoo.ru,81.222.127.189
cdn.reid21.ru,81.222.127.189
cdn.rorobux.ru,81.222.127.189
cdn.images.rusgptchat.ru,81.222.127.189
cdn3.rustz.ru,81.222.127.189
cdn.s-stroy.ru,81.222.127.189
sapp.securebrowser.ru,81.222.127.189
server-defence.selectel.ru,81.222.127.189
brcforum.sitkocdn.ru,81.222.127.189
cdn-1.skkmorf.ru,81.222.127.189
slalomraceone.ru,81.222.127.189
cdn.smartphotostudio.ru,81.222.127.189
s3.snob.ru,81.222.127.189
cdn.spacemount.ru,81.222.127.190
cdn.starterapp.ru,81.222.127.189
files.stk-svet.ru,81.222.127.189
cdn.stolichki.ru,81.222.127.189
www.stopptsr.ru,81.222.127.189
cdn.swapa.ru,81.222.127.189
images.techinsider.ru,81.222.127.189
images2.techinsider.ru,81.222.127.189
www.telegram-work.ru,81.222.127.189
selcdn.teslacode.ru,81.222.127.189
cdn.tlock.ru,81.222.127.189
img.tobody.ru,81.222.127.189
cdn.tripster.ru,81.222.127.189
mirror-app.truestats.ru,81.222.127.189
cdn.tsunami-pro.ru,81.222.127.189
appd2.turnip.ru,81.222.127.189
cdn.uss-app.ru,81.222.127.189
cdn3.vedomosti.ru,81.222.127.189
static.vi-tour.ru,81.222.127.189
img.vkusvill.ru,81.222.127.189
api.webhook-relay.ru,81.222.127.190
cdn.comedy.wmpy.ru,81.222.127.189
cdn.x-manga.ru,81.222.127.189
pos.xleb.ru,81.222.127.189
cdn.yapme.ru,81.222.127.189
zucchiniflo.ru,81.222.127.189
brutus.livecup.run,81.222.127.190
dash.yguard.run,81.222.127.189
cdn.tough-dev.school,81.222.127.189
cdn.mbr-static.oneplatform.site,81.222.127.189
www.qwerty.skin,81.222.127.189
de2lte3cdn.kingtrosper.space,81.222.127.190
cdn.sprocket.studio,81.222.127.189
cdn.boda.su,81.222.127.189
warlord.geronimo.su,81.222.127.189
static.minecraft-play.su,81.222.127.189
static.mr.cdn.plankton.su,81.222.127.189
static.posts.su,81.222.127.189
cdn.ab.tech,81.222.127.189
img-auchan.loymax.tech,81.222.127.189
demo-cdn.ttii.tech,81.222.127.190
tenevoy.video,81.222.127.189
www.xn----7sbbatoirxbedjdpifn5x.xn--p1ai,81.222.127.189
www.xn----8sbfwamcgfkefhe0cw8m4b.xn--p1ai,81.222.127.189
video.xn--80abc2ckjcj9h.xn--p1ai,81.222.127.189

<a id="msg_211883"></a>
### [msg_211883](chunk_0516.md#msg_211883) | 2026-08-06T16:42:20 | Kvink⁴² (Алексей) (в ответ на #211879)
clubika.ru

<a id="msg_211884"></a>
### [msg_211884](chunk_0516.md#msg_211884) | 2026-08-06T16:42:27 | Kvink⁴² (Алексей) (в ответ на #64360)
Точно не сайт заглушка

<a id="msg_211885"></a>
### [msg_211885](chunk_0516.md#msg_211885) | 2026-08-06T16:42:31 | agent adidas death of taliban (в ответ на #64360)
aquarin.info,151.236.109.225
cybervoice.io,151.236.109.225
knbm.lol,151.236.109.225
bucks100.net,151.236.109.225
safelogist.net,151.236.109.225
almazik-pro.online,151.236.109.225
fork.almazik-pro.online,151.236.109.225
altaipn.online,151.236.109.225
amirai.online,151.236.109.225
neverlandxztc.online,151.236.109.225
peacocheck.online,151.236.109.225
netpathway.pro,151.236.109.225
0vh.ru,151.236.109.225
alcocalc.ru,151.236.109.225
alekseimakarov.ru,151.236.109.225
businessfront.ru,151.236.109.225
cdnozon.ru,151.236.109.225
clubika.ru,151.236.109.225
corentos.ru,151.236.109.225
deadfinder.ru,151.236.109.225
easygarant.ru,151.236.109.225
ecdnvideo.ru,151.236.109.225
elikoev.ru,151.236.109.225
elit-el.ru,151.236.109.225
www.elit-el.ru,151.236.109.225
gisweather.ru,151.236.109.225
groby-nn.ru,151.236.109.225
hytalerank.ru,151.236.109.225
in7heaven.ru,151.236.109.225
jmishenko.ru,151.236.109.225
m-avito.ru,151.236.109.225
metallik161.ru,151.236.109.225
optdom52.ru,151.236.109.225
partsview.ru,151.236.109.225
rap-battles.ru,151.236.109.225
zbarskaya.ru,151.236.109.225
pupok.space,151.236.109.225
car-calculator.store,151.236.109.225
tvoimaster24.store,151.236.109.225
ympl.store,151.236.109.225
tourstanok.su,151.236.109.225
tred.su,151.236.109.225
getintegrity.tech,151.236.109.225
kbctv.vip,151.236.109.225
xnetwork.vip,151.236.109.225
xn--b1aaryj3a.xn--p1ai,151.236.109.225
xextrapi.xyz,151.236.109.225

<a id="msg_211886"></a>
### [msg_211886](chunk_0516.md#msg_211886) | 2026-08-06T16:43:23 | agent adidas death of taliban (в ответ на #64360)
SNI можно взять m-avito.ru

<a id="msg_211887"></a>
### [msg_211887](chunk_0516.md#msg_211887) | 2026-08-06T16:43:30 | agent adidas death of taliban (в ответ на #64360)
для турбофларовцев

<a id="msg_211888"></a>
### [msg_211888](chunk_0516.md#msg_211888) | 2026-08-06T16:44:35 | Kvink⁴² (Алексей) (в ответ на #211886)
Да,я нашел.Чекаю смешные названия сайтов

<a id="msg_211889"></a>
### [msg_211889](chunk_0516.md#msg_211889) | 2026-08-06T16:47:03 | - (в ответ на #211885)
ахаха

<a id="msg_211890"></a>
### [msg_211890](chunk_0516.md#msg_211890) | 2026-08-06T16:48:24 | Вася (в ответ на #211889)
Вау

<a id="msg_211891"></a>
### [msg_211891](chunk_0516.md#msg_211891) | 2026-08-06T16:48:33 | Вася (в ответ на #64360)
Честно не заглушка

<a id="msg_211892"></a>
### [msg_211892](chunk_0516.md#msg_211892) | 2026-08-06T16:49:24 | Kvink⁴² (Алексей) (в ответ на #64360)
Ну,у меня клауди эйай так называемый сгенерил

<a id="msg_211893"></a>
### [msg_211893](chunk_0516.md#msg_211893) | 2026-08-06T16:49:25 | Александр (в ответ на #64360)
Прикол у меня походу дом.ру стал реалити детектить. Через вайфай не работает а с мобилы ок. Сдн подключения еще робят

<a id="msg_211894"></a>
### [msg_211894](chunk_0516.md#msg_211894) | 2026-08-06T16:49:29 | Kvink⁴² (Алексей) (в ответ на #64360)
И норм

<a id="msg_211895"></a>
### [msg_211895](chunk_0516.md#msg_211895) | 2026-08-06T16:49:41 | Kvink⁴² (Алексей) (в ответ на #211893)
Транспорт какой?

<a id="msg_211896"></a>
### [msg_211896](chunk_0516.md#msg_211896) | 2026-08-06T16:49:47 | Kvink⁴² (Алексей) (в ответ на #64360)
Tcp?

<a id="msg_211897"></a>
### [msg_211897](chunk_0516.md#msg_211897) | 2026-08-06T16:50:01 | Kvink⁴² (Алексей) (в ответ на #211892)
kvink.space

<a id="msg_211899"></a>
### [msg_211899](chunk_0516.md#msg_211899) | 2026-08-06T16:50:35 | Вася (в ответ на #211897)
Hello world!!!
Я Квинк. Изучаю программирование и компьютерные сети.

// О себе
Студент, интересуюсь сетевыми технологиями: маршрутизация, протоколы, администрирование серверов. Параллельно изучаю программирование — пишу, ломаю, чиню.

Этот сайт — что-то вроде цифрового блокнота. Со временем здесь появится больше заметок, конспектов и мелких проектов.

// Чем занимаюсь
Сетевые протоколы
Linux / администрирование серверов
Python
Bash
Основы кибербезопасности
Учусь по книгам и практике
// Последнее
сейчас
разбираю модель OSI на практике, а не по учебнику
готово
настроил свой первый сервер с нуля
в планах
подтянуть программирование сетевых утилит
// Проект
Пишу и веду VPSRC — можно посмотреть исходники и звёздануть на GitHub.

VPSRC на GitHub
// Связь
Если хочешь обсудить сети, код или что-то смежное — пиши.

<a id="msg_211900"></a>
### [msg_211900](chunk_0516.md#msg_211900) | 2026-08-06T16:51:01 | Kvink⁴² (Алексей) (в ответ на #211898)
xhttp делай

<a id="msg_211902"></a>
### [msg_211902](chunk_0516.md#msg_211902) | 2026-08-06T16:51:10 | Kvink⁴² (Алексей) (в ответ на #211899)
Ну топова же

<a id="msg_211903"></a>
### [msg_211903](chunk_0516.md#msg_211903) | 2026-08-06T16:51:13 | Вася (в ответ на #211901)
Я бы купил

<a id="msg_211905"></a>
### [msg_211905](chunk_0516.md#msg_211905) | 2026-08-06T16:51:26 | Kvink⁴² (Алексей) (в ответ на #64360)
Я ему сказал что я студент и изчую программирование

<a id="msg_211906"></a>
### [msg_211906](chunk_0516.md#msg_211906) | 2026-08-06T16:51:27 | Вася (в ответ на #211902)
Я теперь понял откуда сотни таких страниц находил

<a id="msg_211907"></a>
### [msg_211907](chunk_0516.md#msg_211907) | 2026-08-06T16:51:31 | Kvink⁴² (Алексей) (в ответ на #64360)
И он такое выслал

<a id="msg_211908"></a>
### [msg_211908](chunk_0516.md#msg_211908) | 2026-08-06T16:51:32 | Вася (в ответ на #64360)
Меня наталкивает на мысль

<a id="msg_211909"></a>
### [msg_211909](chunk_0516.md#msg_211909) | 2026-08-06T16:51:36 | Вася (в ответ на #64360)
Что все генерирует ИИ

<a id="msg_211910"></a>
### [msg_211910](chunk_0516.md#msg_211910) | 2026-08-06T16:51:41 | Вася (в ответ на #211904)
Ебать

<a id="msg_211911"></a>
### [msg_211911](chunk_0516.md#msg_211911) | 2026-08-06T16:51:54 | Kvink⁴² (Алексей) (в ответ на #211907)
А ну проект свой дал VPSRC

<a id="msg_211912"></a>
### [msg_211912](chunk_0516.md#msg_211912) | 2026-08-06T16:51:57 | Вася (в ответ на #211904)
Я готов заплатить за них сколько скажешь

<a id="msg_211913"></a>
### [msg_211913](chunk_0516.md#msg_211913) | 2026-08-06T16:52:09 | Вася (в ответ на #211911)
Жёстко

<a id="msg_211914"></a>
### [msg_211914](chunk_0516.md#msg_211914) | 2026-08-06T16:52:18 | Вася (в ответ на #64360)
Я вообще блять учусь щас на левой темп

<a id="msg_211915"></a>
### [msg_211915](chunk_0516.md#msg_211915) | 2026-08-06T16:52:22 | Вася (в ответ на #64360)
Теме

<a id="msg_211916"></a>
### [msg_211916](chunk_0516.md#msg_211916) | 2026-08-06T16:52:30 | Вася (в ответ на #64360)
Которая даже близко не связано с тем , чем я занимаюсь

<a id="msg_211917"></a>
### [msg_211917](chunk_0516.md#msg_211917) | 2026-08-06T16:52:38 | Вася (в ответ на #64360)
Я просто по фану учусь щас ахахахха

<a id="msg_211918"></a>
### [msg_211918](chunk_0516.md#msg_211918) | 2026-08-06T16:53:14 | Kvink⁴² (Алексей) (в ответ на #64360)
Я вообще хочу музыку писать и стать крутым артистом

<a id="msg_211919"></a>
### [msg_211919](chunk_0516.md#msg_211919) | 2026-08-06T16:53:17 | Айла (в ответ на #64360)
я просто хуйней страдаю

<a id="msg_211920"></a>
### [msg_211920](chunk_0516.md#msg_211920) | 2026-08-06T16:53:24 | Айла (в ответ на #64360)
я еще ногти крашу на ногах

<a id="msg_211921"></a>
### [msg_211921](chunk_0516.md#msg_211921) | 2026-08-06T16:53:26 | Айла (в ответ на #64360)
ну нормально короче

<a id="msg_211922"></a>
### [msg_211922](chunk_0516.md#msg_211922) | 2026-08-06T16:53:27 | Вася (в ответ на #211918)
Все чего то хотят

<a id="msg_211923"></a>
### [msg_211923](chunk_0516.md#msg_211923) | 2026-08-06T16:53:30 | Kvink⁴² (Алексей) (в ответ на #64360)
Медкид темный принц скрилекс Маликов

<a id="msg_211924"></a>
### [msg_211924](chunk_0516.md#msg_211924) | 2026-08-06T16:53:36 | Вася (в ответ на #211920)
Фоточку жду.

<a id="msg_211925"></a>
### [msg_211925](chunk_0516.md#msg_211925) | 2026-08-06T16:53:38 | Айла (в ответ на #211918)
я хочу сдохнуть

<a id="msg_211926"></a>
### [msg_211926](chunk_0516.md#msg_211926) | 2026-08-06T16:53:44 | Вася (в ответ на #211923)
Ты им песни писал

<a id="msg_211927"></a>
### [msg_211927](chunk_0516.md#msg_211927) | 2026-08-06T16:53:51 | Kvink⁴² (Алексей) (в ответ на #211926)
Сто проц

<a id="msg_211928"></a>
### [msg_211928](chunk_0516.md#msg_211928) | 2026-08-06T16:53:57 | Вася (в ответ на #211927)
Просто бос

<a id="msg_211929"></a>
### [msg_211929](chunk_0516.md#msg_211929) | 2026-08-06T16:54:02 | agent adidas death of taliban (в ответ на #211925)
ленка, это ты?

<a id="msg_211931"></a>
### [msg_211931](chunk_0516.md#msg_211931) | 2026-08-06T16:54:06 | Kvink⁴² (Алексей) (в ответ на #64360)
У меня есть смертельный файл

<a id="msg_211933"></a>
### [msg_211933](chunk_0516.md#msg_211933) | 2026-08-06T16:54:15 | Вася (в ответ на #211931)
Петобомба ?

<a id="msg_211934"></a>
### [msg_211934](chunk_0516.md#msg_211934) | 2026-08-06T16:54:24 | Kvink⁴² (Алексей) (в ответ на #211930)
Ресурс чекер

<a id="msg_211935"></a>
### [msg_211935](chunk_0516.md#msg_211935) | 2026-08-06T16:54:32 | Kvink⁴² (Алексей) (в ответ на #211933)
Дисс на ркн

<a id="msg_211936"></a>
### [msg_211936](chunk_0516.md#msg_211936) | 2026-08-06T16:54:40 | Kvink⁴² (Алексей) (в ответ на #64360)
Записанный на вайбе в час ночи

<a id="msg_211937"></a>
### [msg_211937](chunk_0516.md#msg_211937) | 2026-08-06T16:54:43 | Вася (в ответ на #64360)
Бля я помню как пиздюка заебашил петобомбой

<a id="msg_211938"></a>
### [msg_211938](chunk_0516.md#msg_211938) | 2026-08-06T16:54:48 | Вася (в ответ на #64360)
Он так плакал

<a id="msg_211939"></a>
### [msg_211939](chunk_0516.md#msg_211939) | 2026-08-06T16:54:53 | Вася (в ответ на #64360)
Я ему скинул это как читы на Майн

<a id="msg_211940"></a>
### [msg_211940](chunk_0516.md#msg_211940) | 2026-08-06T16:54:54 | agent adidas death of taliban (в ответ на #211932)
поцарапай уже а

<a id="msg_211941"></a>
### [msg_211941](chunk_0516.md#msg_211941) | 2026-08-06T16:54:58 | Айла (в ответ на #211940)
да как

<a id="msg_211942"></a>
### [msg_211942](chunk_0516.md#msg_211942) | 2026-08-06T16:55:03 | Вася (в ответ на #64360)
Он начал открывать через 7зип

<a id="msg_211943"></a>
### [msg_211943](chunk_0516.md#msg_211943) | 2026-08-06T16:55:05 | Айла (в ответ на #64360)
ты в очке мира я тоже

<a id="msg_211944"></a>
### [msg_211944](chunk_0516.md#msg_211944) | 2026-08-06T16:55:07 | Вася (в ответ на #64360)
И ПК умер

<a id="msg_211945"></a>
### [msg_211945](chunk_0516.md#msg_211945) | 2026-08-06T16:55:08 | Айла (в ответ на #64360)
там без вариантов

<a id="msg_211946"></a>
### [msg_211946](chunk_0516.md#msg_211946) | 2026-08-06T16:55:09 | agent adidas death of taliban (в ответ на #64360)
и брови себе нарисуй

<a id="msg_211947"></a>
### [msg_211947](chunk_0516.md#msg_211947) | 2026-08-06T16:55:09 | Вася (в ответ на #64360)
Точнее ссд

<a id="msg_211948"></a>
### [msg_211948](chunk_0516.md#msg_211948) | 2026-08-06T16:55:15 | Айла (в ответ на #211946)
планирую

<a id="msg_211949"></a>
### [msg_211949](chunk_0516.md#msg_211949) | 2026-08-06T16:55:18 | Айла (в ответ на #64360)
бабок пока нет

<a id="msg_211950"></a>
### [msg_211950](chunk_0516.md#msg_211950) | 2026-08-06T16:55:19 | agent adidas death of taliban (в ответ на #211943)
я не в очке я вообще не в рф)

<a id="msg_211951"></a>
### [msg_211951](chunk_0516.md#msg_211951) | 2026-08-06T16:55:23 | Kvink⁴² (Алексей) (в ответ на #211947)
F

<a id="msg_211952"></a>
### [msg_211952](chunk_0516.md#msg_211952) | 2026-08-06T16:55:27 | agent adidas death of taliban (в ответ на #211949)
на карандаш?

<a id="msg_211953"></a>
### [msg_211953](chunk_0516.md#msg_211953) | 2026-08-06T16:55:33 | Вася (в ответ на #211951)
Ну а нахуя ему были читы на Майн

<a id="msg_211954"></a>
### [msg_211954](chunk_0516.md#msg_211954) | 2026-08-06T16:55:34 | Айла (в ответ на #211950)
любая точка мира это очко если ты не президент

<a id="msg_211955"></a>
### [msg_211955](chunk_0516.md#msg_211955) | 2026-08-06T16:55:35 | Вася (в ответ на #64360)
Это плохо

<a id="msg_211956"></a>
### [msg_211956](chunk_0516.md#msg_211956) | 2026-08-06T16:55:44 | Вася (в ответ на #64360)
А архив на 2 петобайта тема

<a id="msg_211957"></a>
### [msg_211957](chunk_0516.md#msg_211957) | 2026-08-06T16:55:44 | Kvink⁴² (Алексей) (в ответ на #211955)
Я играл когда был мелки

<a id="msg_211958"></a>
### [msg_211958](chunk_0516.md#msg_211958) | 2026-08-06T16:55:51 | Вася (в ответ на #211957)
Грустно

<a id="msg_211959"></a>
### [msg_211959](chunk_0516.md#msg_211959) | 2026-08-06T16:55:53 | Вася (в ответ на #64360)
Читы плохо

<a id="msg_211960"></a>
### [msg_211960](chunk_0516.md#msg_211960) | 2026-08-06T16:55:54 | agent adidas death of taliban (в ответ на #211954)
звучит как нытьё нереализованного инфантила

<a id="msg_211961"></a>
### [msg_211961](chunk_0516.md#msg_211961) | 2026-08-06T16:55:56 | Kvink⁴² (Алексей) (в ответ на #211959)
Копатель онлайн

<a id="msg_211962"></a>
### [msg_211962](chunk_0516.md#msg_211962) | 2026-08-06T16:55:59 | Kvink⁴² (Алексей) (в ответ на #64360)
Тоже было

<a id="msg_211963"></a>
### [msg_211963](chunk_0516.md#msg_211963) | 2026-08-06T16:56:03 | Вася (в ответ на #211961)
Ох ебать

<a id="msg_211964"></a>
### [msg_211964](chunk_0516.md#msg_211964) | 2026-08-06T16:56:13 | Kvink⁴² (Алексей) (в ответ на #64360)
Кубезумие 2

<a id="msg_211965"></a>
### [msg_211965](chunk_0516.md#msg_211965) | 2026-08-06T16:56:14 | Вася (в ответ на #64360)
Боюсь такое вспоминать

<a id="msg_211966"></a>
### [msg_211966](chunk_0516.md#msg_211966) | 2026-08-06T16:56:16 | Айла (в ответ на #211960)
мне просто дегрейдить нравится

<a id="msg_211967"></a>
### [msg_211967](chunk_0516.md#msg_211967) | 2026-08-06T16:56:19 | Айла (в ответ на #64360)
норм тема

<a id="msg_211968"></a>
### [msg_211968](chunk_0516.md#msg_211968) | 2026-08-06T16:56:30 | Айла (в ответ на #211952)
на такое е

<a id="msg_211969"></a>
### [msg_211969](chunk_0516.md#msg_211969) | 2026-08-06T16:56:31 | Вася (в ответ на #211954)
Не соглашусь

<a id="msg_211970"></a>
### [msg_211970](chunk_0516.md#msg_211970) | 2026-08-06T16:56:39 | agent adidas death of taliban (в ответ на #211968)
так купи и нарисуй чо ты

<a id="msg_211971"></a>
### [msg_211971](chunk_0516.md#msg_211971) | 2026-08-06T16:56:53 | agent adidas death of taliban (в ответ на #64360)
был бы ты тёлкой я бы тебя ракОм сделал

<a id="msg_211972"></a>
### [msg_211972](chunk_0516.md#msg_211972) | 2026-08-06T16:56:58 | Kvink⁴² (Алексей) (в ответ на #211966)
Зарегайся на сайте egirl

<a id="msg_211973"></a>
### [msg_211973](chunk_0516.md#msg_211973) | 2026-08-06T16:56:59 | Вася (в ответ на #64360)
В моем городе единая Россия фонарик поставила , так что можно считать что я уже не жопе мира , но асфальта пока нету и еда в магаз стоит космические бабки

<a id="msg_211974"></a>
### [msg_211974](chunk_0516.md#msg_211974) | 2026-08-06T16:57:03 | Kvink⁴² (Алексей) (в ответ на #211972)
И грей гоев

<a id="msg_211975"></a>
### [msg_211975](chunk_0516.md#msg_211975) | 2026-08-06T16:57:05 | Айла (в ответ на #64360)
мне кажется там и так ты бы раком

<a id="msg_211976"></a>
### [msg_211976](chunk_0516.md#msg_211976) | 2026-08-06T16:57:25 | agent adidas death of taliban (в ответ на #211975)
тебе кажется

<a id="msg_211978"></a>
### [msg_211978](chunk_0516.md#msg_211978) | 2026-08-06T16:57:50 | Вася (в ответ на #211977)
Эх

<a id="msg_211979"></a>
### [msg_211979](chunk_0516.md#msg_211979) | 2026-08-06T16:58:09 | Вася (в ответ на #64360)
Бля слышь

<a id="msg_211980"></a>
### [msg_211980](chunk_0516.md#msg_211980) | 2026-08-06T16:58:13 | Айла (в ответ на #211976)
значит будет так

<a id="msg_211981"></a>
### [msg_211981](chunk_0516.md#msg_211981) | 2026-08-06T16:58:21 | Вася (в ответ на #211980)
Я тебе щас 2 бакса могу кинуть ты рисуешь брови и снимаешь кружок ?

<a id="msg_211982"></a>
### [msg_211982](chunk_0516.md#msg_211982) | 2026-08-06T16:58:26 | agent adidas death of taliban (в ответ на #211980)
ракОм

<a id="msg_211983"></a>
### [msg_211983](chunk_0516.md#msg_211983) | 2026-08-06T16:58:27 | Вася (в ответ на #211981)
Купишь себе хуйню эту

<a id="msg_211984"></a>
### [msg_211984](chunk_0516.md#msg_211984) | 2026-08-06T16:58:29 | Вася (в ответ на #64360)
Для бровей

<a id="msg_211985"></a>
### [msg_211985](chunk_0516.md#msg_211985) | 2026-08-06T16:58:32 | agent adidas death of taliban (в ответ на #211981)
я ваще 10 скину

<a id="msg_211986"></a>
### [msg_211986](chunk_0516.md#msg_211986) | 2026-08-06T16:58:38 | Айла (в ответ на #64360)
уф

<a id="msg_211987"></a>
### [msg_211987](chunk_0516.md#msg_211987) | 2026-08-06T16:58:43 | Вася (в ответ на #64360)
Бля давайте собираем ему деньги

<a id="msg_211988"></a>
### [msg_211988](chunk_0516.md#msg_211988) | 2026-08-06T16:58:46 | Вася (в ответ на #64360)
На брови

<a id="msg_211989"></a>
### [msg_211989](chunk_0516.md#msg_211989) | 2026-08-06T16:58:48 | Kvink⁴² (Алексей) (в ответ на #211986)
Делай

<a id="msg_211990"></a>
### [msg_211990](chunk_0516.md#msg_211990) | 2026-08-06T16:58:57 | Вася (в ответ на #64360)
АХАХАХАХ

<a id="msg_211991"></a>
### [msg_211991](chunk_0516.md#msg_211991) | 2026-08-06T16:59:02 | Kvink⁴² (Алексей) (в ответ на #64360)
Косплей на астрольфо потом

<a id="msg_211992"></a>
### [msg_211992](chunk_0516.md#msg_211992) | 2026-08-06T16:59:11 | Kvink⁴² (Алексей) (в ответ на #64360)
Или на феликса

<a id="msg_211994"></a>
### [msg_211994](chunk_0516.md#msg_211994) | 2026-08-06T16:59:32 | Вася (в ответ на #64360)
Жду такой косплей от него

<a id="msg_211995"></a>
### [msg_211995](chunk_0516.md#msg_211995) | 2026-08-06T16:59:34 | Айла (в ответ на #211985)
уф

<a id="msg_211996"></a>
### [msg_211996](chunk_0516.md#msg_211996) | 2026-08-06T16:59:43 | Айла (в ответ на #211994)
ну кста с моими волосами мб

<a id="msg_211997"></a>
### [msg_211997](chunk_0516.md#msg_211997) | 2026-08-06T16:59:46 | Вася (в ответ на #211996)
Сколько тебе за него закинуть

<a id="msg_211998"></a>
### [msg_211998](chunk_0516.md#msg_211998) | 2026-08-06T16:59:52 | Айла (в ответ на #64360)
ебу

<a id="msg_211999"></a>
### [msg_211999](chunk_0516.md#msg_211999) | 2026-08-06T16:59:54 | Kvink⁴² (Алексей) (в ответ на #64360)
Я готов скинуть 4.2 рубля

<a id="msg_212000"></a>
### [msg_212000](chunk_0516.md#msg_212000) | 2026-08-06T17:00:02 | Вася (в ответ на #211998)
2.20 бакса погнали ?

<a id="msg_212001"></a>
### [msg_212001](chunk_0516.md#msg_212001) | 2026-08-06T17:00:04 | Айла (в ответ на #211999)
вселенная выслала сильнейших

<a id="msg_212002"></a>
### [msg_212002](chunk_0516.md#msg_212002) | 2026-08-06T17:00:05 | Вася (в ответ на #64360)
АХАХХАХА

<a id="msg_212003"></a>
### [msg_212003](chunk_0516.md#msg_212003) | 2026-08-06T17:00:08 | Kvink⁴² (Алексей) (в ответ на #211999)
Из своего бюджета

<a id="msg_212004"></a>
### [msg_212004](chunk_0516.md#msg_212004) | 2026-08-06T17:00:19 | Вася (в ответ на #212000)
Ну ладно , 2.25

<a id="msg_212005"></a>
### [msg_212005](chunk_0516.md#msg_212005) | 2026-08-06T17:00:35 | Айла (в ответ на #64360)
ну в целом хватит на хост

<a id="msg_212006"></a>
### [msg_212006](chunk_0516.md#msg_212006) | 2026-08-06T17:00:36 | Айла (в ответ на #64360)
нормально

<a id="msg_212008"></a>
### [msg_212008](chunk_0516.md#msg_212008) | 2026-08-06T17:00:46 | Вася (в ответ на #212005)
Пробковый ?

<a id="msg_212009"></a>
### [msg_212009](chunk_0516.md#msg_212009) | 2026-08-06T17:00:55 | Айла (в ответ на #64360)
ну вы тут суммы кидаете

<a id="msg_212010"></a>
### [msg_212010](chunk_0516.md#msg_212010) | 2026-08-06T17:00:59 | Айла (в ответ на #64360)
я хуй знает

<a id="msg_212011"></a>
### [msg_212011](chunk_0516.md#msg_212011) | 2026-08-06T17:01:08 | Kvink⁴² (Алексей) (в ответ на #212007)
А хуй знает,я поставил и оно работает

<a id="msg_212012"></a>
### [msg_212012](chunk_0516.md#msg_212012) | 2026-08-06T17:01:13 | Kvink⁴² (Алексей) (в ответ на #64360)
На клиенте

<a id="msg_212013"></a>
### [msg_212013](chunk_0516.md#msg_212013) | 2026-08-06T17:01:28 | Вася (в ответ на #212009)
Кидай адресс , тебе все необходимое отправлю

<a id="msg_212014"></a>
### [msg_212014](chunk_0516.md#msg_212014) | 2026-08-06T17:01:42 | Айла (в ответ на #64360)
ща скачаю исходус

<a id="msg_212015"></a>
### [msg_212015](chunk_0516.md#msg_212015) | 2026-08-06T17:01:45 | Kvink⁴² (Алексей) (в ответ на #212007)
Сни Авито,http хост твой домен

<a id="msg_212016"></a>
### [msg_212016](chunk_0516.md#msg_212016) | 2026-08-06T17:01:53 | Вася (в ответ на #212013)
Авито доставкой ?

<a id="msg_212019"></a>
### [msg_212019](chunk_0516.md#msg_212019) | 2026-08-06T17:02:15 | agent adidas death of taliban (в ответ на #211995)
gogo

<a id="msg_212020"></a>
### [msg_212020](chunk_0516.md#msg_212020) | 2026-08-06T17:02:18 | Айла (в ответ на #212014)
кейк воллет вроде норм но он хуйня ебаная которая лагает как сука даже на 4060

<a id="msg_212021"></a>
### [msg_212021](chunk_0516.md#msg_212021) | 2026-08-06T17:02:30 | Вася (в ответ на #212020)
Иссходус

<a id="msg_212022"></a>
### [msg_212022](chunk_0516.md#msg_212022) | 2026-08-06T17:02:32 | agent adidas death of taliban (в ответ на #212017)
Зелепутін 🟩 🇺🇦 ПЕРЕМОГА

<a id="msg_212023"></a>
### [msg_212023](chunk_0516.md#msg_212023) | 2026-08-06T17:02:34 | Вася (в ответ на #212021)
На 4060

<a id="msg_212024"></a>
### [msg_212024](chunk_0516.md#msg_212024) | 2026-08-06T17:02:35 | Айла (в ответ на #212021)
ну так

<a id="msg_212026"></a>
### [msg_212026](chunk_0516.md#msg_212026) | 2026-08-06T17:02:44 | Айла (в ответ на #212023)
ну блять оно на проце да

<a id="msg_212027"></a>
### [msg_212027](chunk_0516.md#msg_212027) | 2026-08-06T17:02:46 | Айла (в ответ на #64360)
сне похуй

<a id="msg_212028"></a>
### [msg_212028](chunk_0516.md#msg_212028) | 2026-08-06T17:02:46 | agent adidas death of taliban (в ответ на #212025)
15 травня

<a id="msg_212029"></a>
### [msg_212029](chunk_0516.md#msg_212029) | 2026-08-06T17:02:49 | Вася (в ответ на #212026)
Друг , я иссходус прошел на встройки от ноута 2012 года )

<a id="msg_212030"></a>
### [msg_212030](chunk_0516.md#msg_212030) | 2026-08-06T17:02:50 | agent adidas death of taliban (в ответ на #64360)
пиріжки вишневі

<a id="msg_212032"></a>
### [msg_212032](chunk_0516.md#msg_212032) | 2026-08-06T17:03:02 | Айла (в ответ на #212029)
я не про метро

<a id="msg_212033"></a>
### [msg_212033](chunk_0516.md#msg_212033) | 2026-08-06T17:03:04 | Вася (в ответ на #212029)
На средних в 20 ФПС

<a id="msg_212034"></a>
### [msg_212034](chunk_0516.md#msg_212034) | 2026-08-06T17:03:06 | Айла (в ответ на #64360)
а кошелек exodus

<a id="msg_212035"></a>
### [msg_212035](chunk_0516.md#msg_212035) | 2026-08-06T17:03:07 | Вася (в ответ на #212032)
А жаль

<a id="msg_212036"></a>
### [msg_212036](chunk_0516.md#msg_212036) | 2026-08-06T17:03:11 | agent adidas death of taliban (в ответ на #212031)
репу для дпі

<a id="msg_212037"></a>
### [msg_212037](chunk_0516.md#msg_212037) | 2026-08-06T17:03:15 | Вася (в ответ на #212034)
Не не , я про обычный адресс

<a id="msg_212038"></a>
### [msg_212038](chunk_0516.md#msg_212038) | 2026-08-06T17:03:18 | Вася (в ответ на #64360)
Не крипто кошелек говорил

<a id="msg_212039"></a>
### [msg_212039](chunk_0516.md#msg_212039) | 2026-08-06T17:03:21 | Айла (в ответ на #212033)
у меня ща встройка на ноуте как гтх 960

<a id="msg_212040"></a>
### [msg_212040](chunk_0516.md#msg_212040) | 2026-08-06T17:03:23 | Вася (в ответ на #64360)
Все что тебе надо у меня есть

<a id="msg_212041"></a>
### [msg_212041](chunk_0516.md#msg_212041) | 2026-08-06T17:03:24 | Айла (в ответ на #64360)
в целом норм

<a id="msg_212042"></a>
### [msg_212042](chunk_0516.md#msg_212042) | 2026-08-06T17:03:29 | Вася (в ответ на #212039)
Ебать

<a id="msg_212043"></a>
### [msg_212043](chunk_0516.md#msg_212043) | 2026-08-06T17:03:33 | Kvink⁴² (Алексей) (в ответ на #212035)
Я на Нинтендо свитч купил ласт лайт и 2033 редукс

<a id="msg_212044"></a>
### [msg_212044](chunk_0516.md#msg_212044) | 2026-08-06T17:03:41 | Вася (в ответ на #212043)
Я все это прошел

<a id="msg_212045"></a>
### [msg_212045](chunk_0516.md#msg_212045) | 2026-08-06T17:03:47 | Kvink⁴² (Алексей) (в ответ на #212043)
И прошел ласт лайн

<a id="msg_212046"></a>
### [msg_212046](chunk_0516.md#msg_212046) | 2026-08-06T17:03:48 | Айла (в ответ на #212039)
я на ней 360фпс рендеры в фхд в майнкрафте высрал

<a id="msg_212047"></a>
### [msg_212047](chunk_0516.md#msg_212047) | 2026-08-06T17:03:49 | Вася (в ответ на #64360)
Я вообще все в свое жизни прошел

<a id="msg_212048"></a>
### [msg_212048](chunk_0516.md#msg_212048) | 2026-08-06T17:03:50 | Айла (в ответ на #64360)
на встройке

<a id="msg_212049"></a>
### [msg_212049](chunk_0516.md#msg_212049) | 2026-08-06T17:03:52 | Kvink⁴² (Алексей) (в ответ на #64360)
А 2033 не

<a id="msg_212050"></a>
### [msg_212050](chunk_0516.md#msg_212050) | 2026-08-06T17:03:53 | Айла (в ответ на #64360)
запись 360фпс

<a id="msg_212051"></a>
### [msg_212051](chunk_0516.md#msg_212051) | 2026-08-06T17:03:55 | Вася (в ответ на #64360)
У меня Стим все игры щас содержит платные

<a id="msg_212052"></a>
### [msg_212052](chunk_0516.md#msg_212052) | 2026-08-06T17:03:57 | Айла (в ответ на #64360)
в 20-30к битрейта

<a id="msg_212053"></a>
### [msg_212053](chunk_0516.md#msg_212053) | 2026-08-06T17:04:03 | Айла (в ответ на #212052)
нет там юольше

<a id="msg_212054"></a>
### [msg_212054](chunk_0516.md#msg_212054) | 2026-08-06T17:04:05 | Айла (в ответ на #64360)
я не помню
