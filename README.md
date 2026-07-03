# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_08:04:21_UTC-green)

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

**Latest saved flight:** 2026-07-03 08:04:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 08:04:21 UTC

- **126,999** saved flights
- **43,338** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **126,999** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,533,004.1 tonnes** estimated CO2 emissions
- **88,869,805 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5144 |
| 2 | SkyWest Airlines | 4692 |
| 3 | EJA | 2499 |
| 4 | IndiGo | 2398 |
| 5 | American Airlines | 1951 |
| 6 | Southwest Airlines | 1904 |
| 7 | ENY | 1594 |
| 8 | Delta Air Lines | 1512 |
| 9 | Lufthansa | 1352 |
| 10 | LATAM Airlines | 1153 |
| 11 | Vueling | 1125 |
| 12 | WIF | 1119 |
| 13 | AZU | 1072 |
| 14 | AXM | 1002 |
| 15 | LXJ | 990 |
| 16 | Swiss International | 882 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 825 |
| 19 | easyJet | 811 |
| 20 | QLK | 803 |
| 21 | EJU | 785 |
| 22 | Cathay Pacific | 706 |
| 23 | VIV | 697 |
| 24 | AEE | 695 |
| 25 | Air France | 693 |
| 26 | CXK | 681 |
| 27 | United Airlines | 674 |
| 28 | MXY | 660 |
| 29 | JetBlue | 652 |
| 30 | GLO | 639 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108647 |
| 2 | 🇪🇸 ES | 8463 |
| 3 | 🇮🇳 IN | 7525 |
| 4 | 🇦🇺 AU | 7441 |
| 5 | 🇧🇷 BR | 7090 |
| 6 | 🇩🇪 DE | 6695 |
| 7 | 🇨🇦 CA | 6677 |
| 8 | 🇮🇹 IT | 6659 |
| 9 | 🇬🇧 GB | 5600 |
| 10 | 🇯🇵 JP | 5563 |
| 11 | 🇫🇷 FR | 5012 |
| 12 | 🇨🇴 CO | 4046 |
| 13 | 🇲🇽 MX | 3686 |
| 14 | 🇬🇷 GR | 3604 |
| 15 | 🇳🇴 NO | 3469 |
| 16 | 🇨🇭 CH | 3230 |
| 17 | 🇹🇷 TR | 2687 |
| 18 | 🇲🇾 MY | 2595 |
| 19 | 🇿🇦 ZA | 2093 |
| 20 | 🇵🇱 PL | 2073 |
| 21 | 🇳🇿 NZ | 2057 |
| 22 | 🇹🇭 TH | 1978 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1743 |
| 26 | 🇲🇦 MA | 1359 |
| 27 | 🇲🇪 ME | 1255 |
| 28 | 🇳🇱 NL | 1196 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1098 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2655 |
| 2 | Denver International Airport |  | US | 2141 |
| 3 | Tokyo International Airport |  | JP | 1834 |
| 4 | Indira Gandhi International Airport |  | IN | 1656 |
| 5 | Harry Reid International Airport |  | US | 1589 |
| 6 | Guaymaral Airport |  | CO | 1533 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1508 |
| 8 | Zurich Airport |  | CH | 1395 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1351 |
| 10 | La Aurora Airport |  | GT | 1347 |
| 11 | Frankfurt am Main International Airport |  | DE | 1306 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1244 |
| 13 | Chicago O'Hare International Airport |  | US | 1227 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1121 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1052 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1045 |
| 20 | Madrid Barajas International Airport |  | ES | 1043 |
| 21 | Kuala Lumpur International Airport |  | MY | 1009 |
| 22 | Congonhas Airport |  | BR | 996 |
| 23 | Charlotte/Douglas International Airport |  | US | 952 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 924 |
| 26 | Bengaluru International Airport |  | IN | 910 |
| 27 | Malpensa International Airport |  | IT | 869 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 848 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 807 |
| 31 | Barcelona International Airport |  | ES | 792 |
| 32 | Tenerife Norte Airport |  | ES | 776 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 770 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 745 |
| 35 | Calgary International Airport |  | CA | 741 |
| 36 | Scottsdale Airport |  | US | 736 |
| 37 | Seattle-Tacoma International Airport |  | US | 734 |
| 38 | Vitoria/Foronda Airport |  | ES | 727 |
| 39 | Viracopos International Airport |  | BR | 723 |
| 40 | Amsterdam Airport Schiphol |  | NL | 722 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 639 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 462 | 21m | 244 km | 1,945.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 318 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 308 | 1h 10m | 770 km | 4,091.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 177 | 44m | 241 km | 735.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 163 | 1h 45m | 1,423 km | 4,000.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 152 | 30m | 49 km | 128.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 148 | 1h 1m | 695 km | 1,774.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 147 | 1h 17m | 961 km | 2,436.6 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BPO305 | BPO | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-07-03 07:31 UTC | 2026-07-03 08:04 UTC | 32m |
| SERCE31 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-07-03 07:21 UTC | 2026-07-03 07:59 UTC | 37m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-07-02 20:55 UTC | 2026-07-03 07:58 UTC | 11h 2m |
| N257EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-03 05:17 UTC | 2026-07-03 07:57 UTC | 2h 39m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-03 07:01 UTC | 2026-07-03 07:52 UTC | 50m |
| N45UH |  | Skypark Airport (KBTF) | Salt Lake City International Airport (KSLC) | 2026-07-03 07:43 UTC | 2026-07-03 07:51 UTC | 8m |
| CCA109 | Air China | Beijing Capital International Airport (ZBAA) | Zhuhai Airport (ZGSD) | 2026-07-03 05:05 UTC | 2026-07-03 07:51 UTC | 2h 45m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-07-03 07:46 UTC | 2026-07-03 07:50 UTC | 3m |
| MBE04 | MBE | Chalgrove Airport (EGLJ) | Belfast International Airport (EGAA) | 2026-07-03 06:21 UTC | 2026-07-03 07:47 UTC | 1h 26m |
| CSZ9102 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Guangzhou Baiyun International Airport (ZGGG) | 2026-07-02 23:53 UTC | 2026-07-03 07:46 UTC | 7h 53m |
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | Zurich Airport (LSZH) | 2026-07-03 06:13 UTC | 2026-07-03 07:45 UTC | 1h 31m |
| N486LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-03 04:55 UTC | 2026-07-03 07:43 UTC | 2h 48m |
| WIF1DK | WIF | Sogndal Airport (ENSG) | Sandane Airport Anda (ENSD) | 2026-07-03 07:22 UTC | 2026-07-03 07:38 UTC | 15m |
| MYP955 | MYP | Mandalay International Airport (VYMD) | Pinlebu Airport (VYPL) | 2026-07-03 06:50 UTC | 2026-07-03 07:33 UTC | 42m |
| ABY136 | ABY | Hamad International Airport (OTHH) | Sirri Island Airport (OIBS) | 2026-07-03 07:07 UTC | 2026-07-03 07:32 UTC | 24m |
| SXEGN | SXE | Amigdhaleon Airport (LGKM) | Olimboi Airport (LG56) | 2026-07-03 04:58 UTC | 2026-07-03 07:31 UTC | 2h 33m |
| OKEUD22 | OKE | Medlanky Airport (LKCM) | Krizanov Airport (LKKA) | 2026-07-03 06:51 UTC | 2026-07-03 07:30 UTC | 38m |
| UBA503 | UBA | Yangon International Airport (VYYY) | Tilin Airport (VYHN) | 2026-07-03 05:55 UTC | 2026-07-03 07:28 UTC | 1h 33m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Zhuhai Airport (ZGSD) | 2026-07-02 20:40 UTC | 2026-07-03 07:28 UTC | 10h 48m |
| N981BB |  | Kenai Municipal Airport (PAEN) | AK04 (AK04) | 2026-07-03 06:47 UTC | 2026-07-03 07:28 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
