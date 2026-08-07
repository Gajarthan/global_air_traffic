# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_08:58:27_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-08-07 08:58:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 08:58:27 UTC

- **174,875** saved flights
- **56,519** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,875** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,104,672.1 tonnes** estimated CO2 emissions
- **122,009,977 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6932 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3458 |
| 4 | IndiGo | 3061 |
| 5 | Southwest Airlines | 2755 |
| 6 | American Airlines | 2735 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2068 |
| 9 | LATAM Airlines | 1616 |
| 10 | Lufthansa | 1577 |
| 11 | AZU | 1545 |
| 12 | WIF | 1466 |
| 13 | Vueling | 1436 |
| 14 | LXJ | 1369 |
| 15 | AXM | 1192 |
| 16 | easyJet | 1190 |
| 17 | Swiss International | 1190 |
| 18 | QLK | 1080 |
| 19 | EJU | 1067 |
| 20 | All Nippon Airways | 1066 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 963 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 927 |
| 25 | GLO | 921 |
| 26 | AEE | 913 |
| 27 | United Airlines | 907 |
| 28 | Air France | 895 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150419 |
| 2 | 🇪🇸 ES | 11169 |
| 3 | 🇧🇷 BR | 9948 |
| 4 | 🇦🇺 AU | 9931 |
| 5 | 🇮🇳 IN | 9595 |
| 6 | 🇨🇦 CA | 9566 |
| 7 | 🇮🇹 IT | 9020 |
| 8 | 🇩🇪 DE | 8662 |
| 9 | 🇬🇧 GB | 8088 |
| 10 | 🇯🇵 JP | 7054 |
| 11 | 🇫🇷 FR | 6930 |
| 12 | 🇨🇴 CO | 6423 |
| 13 | 🇬🇷 GR | 5085 |
| 14 | 🇲🇽 MX | 5003 |
| 15 | 🇨🇭 CH | 4622 |
| 16 | 🇳🇴 NO | 4555 |
| 17 | 🇹🇷 TR | 4303 |
| 18 | 🇲🇾 MY | 3110 |
| 19 | 🇵🇱 PL | 2915 |
| 20 | 🇿🇦 ZA | 2828 |
| 21 | 🇹🇭 TH | 2588 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2318 |
| 24 | 🇬🇹 GT | 2227 |
| 25 | 🇰🇷 KR | 2197 |
| 26 | 🇲🇦 MA | 1755 |
| 27 | 🇭🇷 HR | 1696 |
| 28 | 🇲🇪 ME | 1598 |
| 29 | 🇳🇱 NL | 1574 |
| 30 | 🇲🇴 MO | 1505 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3606 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2201 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2133 |
| 6 | Harry Reid International Airport |  | US | 2089 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1900 |
| 8 | Zurich Airport |  | CH | 1850 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1829 |
| 10 | La Aurora Airport |  | GT | 1714 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1543 |
| 16 | Macau International Airport |  | MO | 1505 |
| 17 | Congonhas Airport |  | BR | 1439 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1365 |
| 20 | Madrid Barajas International Airport |  | ES | 1360 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1234 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1232 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1187 |
| 26 | Charles de Gaulle International Airport |  | FR | 1183 |
| 27 | Kuala Lumpur International Airport |  | MY | 1172 |
| 28 | Bengaluru International Airport |  | IN | 1141 |
| 29 | Ninoy Aquino International Airport |  | PH | 1090 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1079 |
| 32 | Barcelona International Airport |  | ES | 1032 |
| 33 | Daniel K Inouye International Airport |  | US | 1009 |
| 34 | Seattle-Tacoma International Airport |  | US | 1007 |
| 35 | Calgary International Airport |  | CA | 992 |
| 36 | Reno/Tahoe International Airport |  | US | 991 |
| 37 | Viracopos International Airport |  | BR | 990 |
| 38 | Oslo Gardermoen Airport |  | NO | 974 |
| 39 | Tenerife Norte Airport |  | ES | 964 |
| 40 | Amsterdam Airport Schiphol |  | NL | 948 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 402 | 1h 8m | 770 km | 5,340.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 322 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 264 | 44m | 241 km | 1,096.6 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 240 | 1h 48m | 1,423 km | 5,890.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 229 | 20m | 250 km | 989.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 208 | 19m | 144 km | 517.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 196 | 24m | 218 km | 738.4 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 190 | 43m | 452 km | 1,480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-07 08:44 UTC | 2026-08-07 08:58 UTC | 13m |
| MVE4AX | MVE | Riga International Airport (EVRA) | Riga International Airport (EVRA) | 2026-08-07 08:14 UTC | 2026-08-07 08:56 UTC | 42m |
| SERCE31 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-08-07 08:34 UTC | 2026-08-07 08:45 UTC | 11m |
| N4585S |  | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-08-07 08:13 UTC | 2026-08-07 08:44 UTC | 30m |
| PNC1A | PNC | London Biggin Hill Airport (EGKB) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-07 06:53 UTC | 2026-08-07 08:41 UTC | 1h 47m |
| ADY371 | ADY | Abu Dhabi International Airport (OMAA) | Erzincan Airport (LTCD) | 2026-08-07 05:29 UTC | 2026-08-07 08:32 UTC | 3h 3m |
| DEEAX | DEE | Frankfurt-Egelsbach Airport (EDFE) | Siegerland Airport (EDGS) | 2026-08-07 07:50 UTC | 2026-08-07 08:24 UTC | 34m |
| CFH3 | CFH | RAAF Base Richmond (YSRI) | Sydney Bankstown Airport (YSBK) | 2026-08-07 08:01 UTC | 2026-08-07 08:15 UTC | 13m |
| FDR893 | FDR | O. R. Tambo International Airport (FAOR) | Rooiberg Airport (FARO) | 2026-08-07 07:51 UTC | 2026-08-07 08:14 UTC | 23m |
| SEH3JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-08-07 07:47 UTC | 2026-08-07 08:14 UTC | 26m |
| FD291 |  | Benalla Airport (YBLA) | Kyneton Airport (YKTN) | 2026-08-07 07:39 UTC | 2026-08-07 08:13 UTC | 34m |
| KLM1787 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Hannover Airport (EDDV) | 2026-08-07 07:35 UTC | 2026-08-07 08:13 UTC | 37m |
| AXM6318 | AXM | Kuala Lumpur International Airport (WMKK) | Penang International Airport (WMKP) | 2026-08-07 07:42 UTC | 2026-08-07 08:11 UTC | 29m |
| HBXTP | HBX | Wangen-Lachen Airport (LSPV) | Muenster Aero Airport (LSPU) | 2026-08-07 07:42 UTC | 2026-08-07 08:10 UTC | 28m |
| ZSTWF | ZST | O. R. Tambo International Airport (FAOR) | Thabazimbi Airport (FATI) | 2026-08-07 07:42 UTC | 2026-08-07 08:09 UTC | 26m |
| OAL040 | OAL | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-08-07 07:38 UTC | 2026-08-07 08:09 UTC | 30m |
| EZY12DP | easyJet | Glasgow International Airport (EGPF) | Francisco de Sá Carneiro Airport (LPPR) | 2026-08-07 05:40 UTC | 2026-08-07 08:08 UTC | 2h 27m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-07 07:16 UTC | 2026-08-07 08:05 UTC | 49m |
| N378TP |  | Paris-Le Bourget Airport (LFPB) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-07 06:58 UTC | 2026-08-07 08:03 UTC | 1h 4m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-07 07:42 UTC | 2026-08-07 08:02 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
