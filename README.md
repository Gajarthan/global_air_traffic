# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_15:57:34_UTC-green)

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

**Latest saved flight:** 2026-06-10 15:57:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-10 15:57:34 UTC

- **107,548** saved flights
- **37,697** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,548** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,314,397.4 tonnes** estimated CO2 emissions
- **76,196,951 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4423 |
| 2 | SkyWest Airlines | 4035 |
| 3 | IndiGo | 2136 |
| 4 | EJA | 2074 |
| 5 | American Airlines | 1712 |
| 6 | Southwest Airlines | 1618 |
| 7 | ENY | 1345 |
| 8 | Delta Air Lines | 1277 |
| 9 | Lufthansa | 1230 |
| 10 | Vueling | 985 |
| 11 | LATAM Airlines | 956 |
| 12 | WIF | 944 |
| 13 | AXM | 914 |
| 14 | AZU | 875 |
| 15 | LXJ | 810 |
| 16 | Swiss International | 782 |
| 17 | All Nippon Airways | 747 |
| 18 | Alaska Airlines | 739 |
| 19 | QLK | 714 |
| 20 | easyJet | 693 |
| 21 | EJU | 686 |
| 22 | Cathay Pacific | 645 |
| 23 | AEE | 613 |
| 24 | VIV | 613 |
| 25 | Air France | 608 |
| 26 | United Airlines | 594 |
| 27 | MXY | 579 |
| 28 | CXK | 568 |
| 29 | AXB | 530 |
| 30 | Japan Airlines | 530 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90479 |
| 2 | 🇪🇸 ES | 7384 |
| 3 | 🇮🇳 IN | 6727 |
| 4 | 🇦🇺 AU | 6430 |
| 5 | 🇧🇷 BR | 5933 |
| 6 | 🇩🇪 DE | 5772 |
| 7 | 🇮🇹 IT | 5761 |
| 8 | 🇨🇦 CA | 5630 |
| 9 | 🇯🇵 JP | 4900 |
| 10 | 🇬🇧 GB | 4571 |
| 11 | 🇫🇷 FR | 4280 |
| 12 | 🇨🇴 CO | 3726 |
| 13 | 🇲🇽 MX | 3217 |
| 14 | 🇬🇷 GR | 3051 |
| 15 | 🇳🇴 NO | 2974 |
| 16 | 🇨🇭 CH | 2738 |
| 17 | 🇲🇾 MY | 2343 |
| 18 | 🇹🇷 TR | 2093 |
| 19 | 🇿🇦 ZA | 1845 |
| 20 | 🇰🇷 KR | 1786 |
| 21 | 🇳🇿 NZ | 1783 |
| 22 | 🇹🇭 TH | 1764 |
| 23 | 🇵🇱 PL | 1756 |
| 24 | 🇵🇭 PH | 1572 |
| 25 | 🇬🇹 GT | 1550 |
| 26 | 🇲🇦 MA | 1186 |
| 27 | 🇲🇴 MO | 1125 |
| 28 | 🇳🇱 NL | 1057 |
| 29 | 🇲🇪 ME | 1035 |
| 30 | 🇭🇷 HR | 936 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2323 |
| 2 | Denver International Airport |  | US | 1823 |
| 3 | Tokyo International Airport |  | JP | 1623 |
| 4 | Indira Gandhi International Airport |  | IN | 1460 |
| 5 | Harry Reid International Airport |  | US | 1371 |
| 6 | Guaymaral Airport |  | CO | 1369 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1348 |
| 8 | Zurich Airport |  | CH | 1219 |
| 9 | Frankfurt am Main International Airport |  | DE | 1213 |
| 10 | La Aurora Airport |  | GT | 1192 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1159 |
| 12 | El Dorado International Airport |  | CO | 1130 |
| 13 | Macau International Airport |  | MO | 1125 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1080 |
| 15 | Chicago O'Hare International Airport |  | US | 1075 |
| 16 | Madrid Barajas International Airport |  | ES | 936 |
| 17 | Capua Airport |  | IT | 922 |
| 18 | Kuala Lumpur International Airport |  | MY | 918 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 917 |
| 20 | Salt Lake City International Airport |  | US | 914 |
| 21 | Charlotte/Douglas International Airport |  | US | 832 |
| 22 | Congonhas Airport |  | BR | 821 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 815 |
| 24 | Bengaluru International Airport |  | IN | 813 |
| 25 | Charles de Gaulle International Airport |  | FR | 812 |
| 26 | Malpensa International Airport |  | IT | 797 |
| 27 | Daniel K Inouye International Airport |  | US | 727 |
| 28 | Ninoy Aquino International Airport |  | PH | 721 |
| 29 | Tenerife Norte Airport |  | ES | 721 |
| 30 | Barcelona International Airport |  | ES | 704 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 700 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 697 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 697 |
| 34 | Amsterdam Airport Schiphol |  | NL | 653 |
| 35 | Don Mueang International Airport |  | TH | 646 |
| 36 | Vitoria/Foronda Airport |  | ES | 642 |
| 37 | Calgary International Airport |  | CA | 633 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 617 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 610 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 567 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 395 | 21m | 244 km | 1,663.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 285 | 24m | 225 km | 1,105.7 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 282 | 1h 7m | 706 km | 3,433.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 262 | 1h 25m | 910 km | 4,111.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 249 | 1h 10m | 770 km | 3,307.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 215 | 26m | 275 km | 1,018.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 207 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 158 | 22m | 55 km | 150.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 157 | 27m | 215 km | 581.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 147 | 13m | - | - |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 129 | 44m | 241 km | 535.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 126 | 1h 43m | 1,423 km | 3,092.2 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 121 | 1h 18m | 961 km | 2,005.6 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXC87 | LXC | Tarbes-Lourdes-Pyrenees Airport (LFBT) | Tarbes-Lourdes-Pyrenees Airport (LFBT) | 2026-06-10 14:08 UTC | 2026-06-10 15:57 UTC | 1h 49m |
| N20058 |  | Port Bucyrus/Crawford County Airport (K17G) | Port Bucyrus/Crawford County Airport (K17G) | 2026-06-10 15:46 UTC | 2026-06-10 15:56 UTC | 10m |
| SGA2500 | SGA | Eleftherios Venizelos International Airport (LGAV) | Macau International Airport (VMMC) | 2026-06-10 01:03 UTC | 2026-06-10 15:55 UTC | 14h 51m |
| PROTX | PRO | Eurico de Aguiar Salles Airport (SBVT) | Guarapari Airport (SNGA) | 2026-06-10 15:21 UTC | 2026-06-10 15:54 UTC | 32m |
| N1753S |  | Braunschweig Wolfsburg Airport (EDVE) | Hodenhagen Airport (EDVH) | 2026-06-10 15:10 UTC | 2026-06-10 15:50 UTC | 40m |
| FFL1210 | FFL | The Eastern Iowa Airport (KCID) | Mid-Way Regional Airport (KJWY) | 2026-06-10 14:03 UTC | 2026-06-10 15:49 UTC | 1h 46m |
| XABNT | XAB | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-06-10 15:27 UTC | 2026-06-10 15:48 UTC | 21m |
| N491LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-10 14:49 UTC | 2026-06-10 15:45 UTC | 56m |
| BEAK91 | BEA | Maverick County Memorial International Airport (K5T9) | Maverick County Memorial International Airport (K5T9) | 2026-06-10 15:28 UTC | 2026-06-10 15:45 UTC | 17m |
| CXK191 | CXK | Camarillo Airport (KCMA) | Camarillo Airport (KCMA) | 2026-06-10 15:24 UTC | 2026-06-10 15:40 UTC | 15m |
| N4463J |  | WI71 (WI71) | Burlington Municipal Airport (KBUU) | 2026-06-10 15:24 UTC | 2026-06-10 15:38 UTC | 14m |
| N71UM |  | 14ME (14ME) | Bangor International Airport (KBGR) | 2026-06-10 15:27 UTC | 2026-06-10 15:38 UTC | 10m |
| OOJWB | OOJ | Southend Airport (EGMC) | Rotterdam Airport (EHRD) | 2026-06-10 14:53 UTC | 2026-06-10 15:37 UTC | 43m |
| N58LC |  | Mc Clellan-Palomar Airport (KCRQ) | Buchanan Field (KCCR) | 2026-06-10 14:29 UTC | 2026-06-10 15:35 UTC | 1h 5m |
| ITY160 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Brussels Airport (EBBR) | 2026-06-10 13:51 UTC | 2026-06-10 15:35 UTC | 1h 43m |
| N177BD |  | Roberts Field (KRDM) | Prineville Airport (KS39) | 2026-06-10 15:03 UTC | 2026-06-10 15:35 UTC | 31m |
| N157U |  | Logan-Cache Airport (KLGU) | Skypark Airport (KBTF) | 2026-06-10 14:59 UTC | 2026-06-10 15:34 UTC | 34m |
| DIFLE | DIF | Harle Airport (EDXP) | Wangerooge Airport (EDWG) | 2026-06-10 15:29 UTC | 2026-06-10 15:32 UTC | 3m |
| HZAL65 | HZA | Ras Tanura Airport (OERT) | Ras Tanura Airport (OERT) | 2026-06-10 15:31 UTC | 2026-06-10 15:32 UTC | 0m |
| N91GF |  | Santa Fe Regional Airport (KSAF) | Santa Fe Regional Airport (KSAF) | 2026-06-10 14:47 UTC | 2026-06-10 15:30 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
