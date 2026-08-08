# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_13:41:32_UTC-green)

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

**Latest saved flight:** 2026-08-08 13:41:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 13:41:32 UTC

- **178,233** saved flights
- **57,270** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,233** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,142,284.1 tonnes** estimated CO2 emissions
- **124,190,381 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7072 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3508 |
| 4 | IndiGo | 3136 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2773 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2101 |
| 9 | LATAM Airlines | 1651 |
| 10 | Lufthansa | 1594 |
| 11 | AZU | 1585 |
| 12 | WIF | 1491 |
| 13 | Vueling | 1471 |
| 14 | LXJ | 1398 |
| 15 | Swiss International | 1218 |
| 16 | AXM | 1209 |
| 17 | easyJet | 1209 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1088 |
| 20 | EJU | 1085 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 943 |
| 25 | GLO | 940 |
| 26 | AEE | 928 |
| 27 | United Airlines | 919 |
| 28 | Air France | 918 |
| 29 | MXY | 896 |
| 30 | PGT | 882 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152814 |
| 2 | 🇪🇸 ES | 11423 |
| 3 | 🇧🇷 BR | 10165 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9834 |
| 6 | 🇨🇦 CA | 9732 |
| 7 | 🇮🇹 IT | 9227 |
| 8 | 🇩🇪 DE | 8830 |
| 9 | 🇬🇧 GB | 8235 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7086 |
| 12 | 🇨🇴 CO | 6539 |
| 13 | 🇬🇷 GR | 5202 |
| 14 | 🇲🇽 MX | 5097 |
| 15 | 🇨🇭 CH | 4749 |
| 16 | 🇳🇴 NO | 4631 |
| 17 | 🇹🇷 TR | 4475 |
| 18 | 🇲🇾 MY | 3157 |
| 19 | 🇵🇱 PL | 2967 |
| 20 | 🇿🇦 ZA | 2912 |
| 21 | 🇹🇭 TH | 2709 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2274 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1801 |
| 27 | 🇭🇷 HR | 1765 |
| 28 | 🇲🇪 ME | 1623 |
| 29 | 🇳🇱 NL | 1604 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3674 |
| 2 | Denver International Airport |  | US | 2949 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Indira Gandhi International Airport |  | IN | 2189 |
| 5 | Guaymaral Airport |  | CO | 2177 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1925 |
| 8 | Zurich Airport |  | CH | 1895 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1747 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1591 |
| 14 | El Dorado International Airport |  | CO | 1588 |
| 15 | Frankfurt am Main International Airport |  | DE | 1557 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1475 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1429 |
| 19 | Capua Airport |  | IT | 1395 |
| 20 | Madrid Barajas International Airport |  | ES | 1390 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1323 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1259 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1225 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1210 |
| 27 | Kuala Lumpur International Airport |  | MY | 1189 |
| 28 | Bengaluru International Airport |  | IN | 1172 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1103 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1061 |
| 33 | Daniel K Inouye International Airport |  | US | 1026 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1019 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 992 |
| 39 | Tenerife Norte Airport |  | ES | 975 |
| 40 | Amsterdam Airport Schiphol |  | NL | 963 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 656 | 21m | 244 km | 2,762.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 249 | 1h 48m | 1,423 km | 6,110.9 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 226 | 26m | 215 km | 837.0 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 225 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 203 | 24m | 218 km | 764.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BNI5T | BNI | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-08 12:41 UTC | 2026-08-08 13:41 UTC | 1h 0m |
| DFPTF | DFP | Tannheim Airport (EDMT) | Tannheim Airport (EDMT) | 2026-08-08 13:19 UTC | 2026-08-08 13:40 UTC | 20m |
| DFRED | DFR | Leutkirch-Unterzeil Airport (EDNL) | Leutkirch-Unterzeil Airport (EDNL) | 2026-08-08 11:51 UTC | 2026-08-08 13:31 UTC | 1h 40m |
| PRZTU | PRZ | Serra da Capivara Airport (SWKQ) | Fabrica Fortaleza Airport (SJDS) | 2026-08-08 10:38 UTC | 2026-08-08 13:27 UTC | 2h 49m |
| KZR870 | KZR | Istanbul Airport (LTFM) | Astrakhan Airport (URWA) | 2026-08-08 10:50 UTC | 2026-08-08 13:26 UTC | 2h 36m |
| FHIGE | FHI | Uetersen/Heist Airport (EDHE) | Uetersen/Heist Airport (EDHE) | 2026-08-08 13:05 UTC | 2026-08-08 13:21 UTC | 15m |
| BLVG | BLV | Shek Kong Air Base (VHSK) | Shek Kong Air Base (VHSK) | 2026-08-08 13:10 UTC | 2026-08-08 13:21 UTC | 10m |
| N297ME |  | Ocean County Airport (KMJX) | Cape May County Airport (KWWD) | 2026-08-08 12:30 UTC | 2026-08-08 13:20 UTC | 50m |
| N397BC |  | Huntingburg Airport (KHNB) | CO86 (CO86) | 2026-08-08 10:57 UTC | 2026-08-08 13:19 UTC | 2h 21m |
| N611CC |  | Ogden-Hinckley Airport (KOGD) | Flying R Airport (11UT) | 2026-08-08 12:57 UTC | 2026-08-08 13:17 UTC | 20m |
| AAL2435 | American Airlines | Savannah/Hilton Head International Airport (KSAV) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-08 11:10 UTC | 2026-08-08 13:17 UTC | 2h 6m |
| N362PS |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-08 13:04 UTC | 2026-08-08 13:16 UTC | 11m |
| DFROH | DFR | Casale Monferrato Airport (LILM) | Casale Monferrato Airport (LILM) | 2026-08-08 11:28 UTC | 2026-08-08 13:15 UTC | 1h 47m |
| N1947F |  | Melbourne Orlando International Airport (KMLB) | Winter Haven Regional Airport (KGIF) | 2026-08-08 11:57 UTC | 2026-08-08 13:14 UTC | 1h 17m |
| OEKFC | OEK | Stadtlohn-Vreden Airport (EDLS) | Stadtlohn-Vreden Airport (EDLS) | 2026-08-08 12:19 UTC | 2026-08-08 13:13 UTC | 54m |
| OORUN | OOR | Antwerp International Airport (Deurne) (EBAW) | Oostmalle Air Base (EBZR) | 2026-08-08 12:29 UTC | 2026-08-08 13:09 UTC | 39m |
| N529LF |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-08-08 12:31 UTC | 2026-08-08 13:07 UTC | 36m |
| SFG55B | SFG | Olbia / Costa Smeralda Airport (LIEO) | Solenzara (BA 126) Air Base (LFKS) | 2026-08-08 12:52 UTC | 2026-08-08 13:06 UTC | 14m |
| HBKLA | HBK | Lommis Airfield (LSZT) | Bad Ragaz Airport (LSZE) | 2026-08-08 12:26 UTC | 2026-08-08 13:05 UTC | 39m |
| RNA218 | RNA | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-08-08 11:39 UTC | 2026-08-08 13:05 UTC | 1h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
