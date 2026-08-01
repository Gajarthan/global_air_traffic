# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_15:14:37_UTC-green)

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

**Latest saved flight:** 2026-08-01 15:14:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 15:14:37 UTC

- **164,644** saved flights
- **54,110** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,644** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,979,010.0 tonnes** estimated CO2 emissions
- **114,725,217 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6579 |
| 2 | SkyWest Airlines | 5984 |
| 3 | EJA | 3259 |
| 4 | IndiGo | 2900 |
| 5 | American Airlines | 2592 |
| 6 | Southwest Airlines | 2582 |
| 7 | ENY | 2042 |
| 8 | Delta Air Lines | 1961 |
| 9 | LATAM Airlines | 1536 |
| 10 | Lufthansa | 1534 |
| 11 | AZU | 1447 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1362 |
| 14 | LXJ | 1277 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1129 |
| 17 | easyJet | 1080 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1009 |
| 21 | EJU | 1006 |
| 22 | VIV | 908 |
| 23 | CXK | 882 |
| 24 | Cathay Pacific | 874 |
| 25 | United Airlines | 866 |
| 26 | AEE | 863 |
| 27 | GLO | 863 |
| 28 | Air France | 851 |
| 29 | MXY | 850 |
| 30 | JetBlue | 838 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 142046 |
| 2 | 🇪🇸 ES | 10544 |
| 3 | 🇧🇷 BR | 9394 |
| 4 | 🇦🇺 AU | 9257 |
| 5 | 🇮🇳 IN | 9104 |
| 6 | 🇨🇦 CA | 8951 |
| 7 | 🇮🇹 IT | 8501 |
| 8 | 🇩🇪 DE | 8250 |
| 9 | 🇬🇧 GB | 7583 |
| 10 | 🇯🇵 JP | 6657 |
| 11 | 🇫🇷 FR | 6529 |
| 12 | 🇨🇴 CO | 5908 |
| 13 | 🇬🇷 GR | 4743 |
| 14 | 🇲🇽 MX | 4707 |
| 15 | 🇳🇴 NO | 4338 |
| 16 | 🇨🇭 CH | 4337 |
| 17 | 🇹🇷 TR | 3945 |
| 18 | 🇲🇾 MY | 2967 |
| 19 | 🇵🇱 PL | 2795 |
| 20 | 🇿🇦 ZA | 2687 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2368 |
| 23 | 🇵🇭 PH | 2172 |
| 24 | 🇰🇷 KR | 2132 |
| 25 | 🇬🇹 GT | 2125 |
| 26 | 🇲🇦 MA | 1661 |
| 27 | 🇭🇷 HR | 1554 |
| 28 | 🇲🇪 ME | 1542 |
| 29 | 🇳🇱 NL | 1495 |
| 30 | 🇲🇴 MO | 1393 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3355 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2073 |
| 5 | Indira Gandhi International Airport |  | IN | 2016 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1813 |
| 8 | Zurich Airport |  | CH | 1754 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1728 |
| 10 | La Aurora Airport |  | GT | 1645 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1524 |
| 12 | El Dorado International Airport |  | CO | 1508 |
| 13 | Frankfurt am Main International Airport |  | DE | 1491 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1479 |
| 16 | Macau International Airport |  | MO | 1393 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1379 |
| 18 | Congonhas Airport |  | BR | 1361 |
| 19 | Madrid Barajas International Airport |  | ES | 1299 |
| 20 | Capua Airport |  | IT | 1289 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1164 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Charles de Gaulle International Airport |  | FR | 1124 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1092 |
| 28 | Bengaluru International Airport |  | IN | 1080 |
| 29 | Ninoy Aquino International Airport |  | PH | 1021 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1008 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1006 |
| 32 | Barcelona International Airport |  | ES | 975 |
| 33 | Daniel K Inouye International Airport |  | US | 960 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 935 |
| 37 | Tenerife Norte Airport |  | ES | 919 |
| 38 | Oslo Gardermoen Airport |  | NO | 918 |
| 39 | Scottsdale Airport |  | US | 917 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 865 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 598 | 21m | 244 km | 2,518.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 394 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 307 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 250 | 22m | 55 km | 237.6 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 213 | 20m | 250 km | 920.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 196 | 1h 15m | 961 km | 3,248.8 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 194 | 19m | 144 km | 482.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 184 | 1h 39m | 1,156 km | 3,670.7 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3251G |  | Grimes Field (KI74) | Toledo Executive Airport (KTDZ) | 2026-08-01 14:41 UTC | 2026-08-01 15:14 UTC | 33m |
| RVP303 | RVP | Ponte de Sôr Airport (LPSO) | Vila Real Airport (LPVR) | 2026-08-01 14:03 UTC | 2026-08-01 15:12 UTC | 1h 9m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-08-01 14:53 UTC | 2026-08-01 15:12 UTC | 19m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-01 14:49 UTC | 2026-08-01 15:08 UTC | 19m |
| EURO11 | EUR | Tinker Afb Airport (KTIK) | 29TA (29TA) | 2026-08-01 14:50 UTC | 2026-08-01 15:06 UTC | 16m |
| N116UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-01 14:40 UTC | 2026-08-01 14:57 UTC | 17m |
| N208JW |  | Danielson Airport (KLZD) | Danielson Airport (KLZD) | 2026-08-01 14:41 UTC | 2026-08-01 14:52 UTC | 10m |
| N850FP |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-01 14:37 UTC | 2026-08-01 14:52 UTC | 15m |
| DERMJ | DER | Elz Airport (EDFY) | Detmold Airport (EDLJ) | 2026-08-01 13:56 UTC | 2026-08-01 14:51 UTC | 55m |
| SWA4741 | Southwest Airlines | Flying Eagle Ranch Airport (65TX) | Dallas Love Field (KDAL) | 2026-08-01 13:38 UTC | 2026-08-01 14:48 UTC | 1h 9m |
| N20AW |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-01 14:15 UTC | 2026-08-01 14:47 UTC | 32m |
| OKA2884 | OKA | Tianjin Binhai International Airport (ZBTJ) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-01 14:09 UTC | 2026-08-01 14:47 UTC | 37m |
| RYR49RT | Ryanair | M. R. Stefanik Airport (LZIB) | Palma De Mallorca Airport (LEPA) | 2026-08-01 12:36 UTC | 2026-08-01 14:46 UTC | 2h 10m |
| CFUDF | CFU | Beiseker Airport (CFV2) | Beiseker Airport (CFV2) | 2026-08-01 14:27 UTC | 2026-08-01 14:43 UTC | 16m |
| CHH408 | CHH | Edinburgh Airport (EGPH) | Ukhta Airport (UUYH) | 2026-08-01 11:29 UTC | 2026-08-01 14:41 UTC | 3h 12m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-08-01 14:24 UTC | 2026-08-01 14:39 UTC | 15m |
| VAR486 | VAR | Gila Bend Municipal Airport (KE63) | Gila Bend Municipal Airport (KE63) | 2026-08-01 14:36 UTC | 2026-08-01 14:38 UTC | 2m |
| 4XCNL |  | Ben Gurion International Airport (LLBG) | Isparta Airport (LTBM) | 2026-08-01 13:26 UTC | 2026-08-01 14:37 UTC | 1h 10m |
| EM415 |  | Ataturk International Airport (LTBA) | Ataturk International Airport (LTBA) | 2026-08-01 14:19 UTC | 2026-08-01 14:36 UTC | 17m |
| N750SD |  | Wysocki Field (CT15) | Wysocki Field (CT15) | 2026-08-01 14:15 UTC | 2026-08-01 14:36 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
