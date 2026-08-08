# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_15:47:37_UTC-green)

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

**Latest saved flight:** 2026-08-08 15:47:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 15:47:37 UTC

- **178,608** saved flights
- **57,360** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,608** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,146,315.0 tonnes** estimated CO2 emissions
- **124,424,060 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7091 |
| 2 | SkyWest Airlines | 6502 |
| 3 | EJA | 3515 |
| 4 | IndiGo | 3140 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2775 |
| 7 | ENY | 2218 |
| 8 | Delta Air Lines | 2107 |
| 9 | LATAM Airlines | 1661 |
| 10 | Lufthansa | 1597 |
| 11 | AZU | 1593 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1474 |
| 14 | LXJ | 1398 |
| 15 | Swiss International | 1223 |
| 16 | easyJet | 1212 |
| 17 | AXM | 1210 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1088 |
| 20 | EJU | 1087 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 981 |
| 23 | GLO | 950 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 943 |
| 26 | AEE | 929 |
| 27 | Air France | 920 |
| 28 | United Airlines | 919 |
| 29 | MXY | 897 |
| 30 | PGT | 883 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 153056 |
| 2 | 🇪🇸 ES | 11454 |
| 3 | 🇧🇷 BR | 10225 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9843 |
| 6 | 🇨🇦 CA | 9747 |
| 7 | 🇮🇹 IT | 9244 |
| 8 | 🇩🇪 DE | 8854 |
| 9 | 🇬🇧 GB | 8259 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7119 |
| 12 | 🇨🇴 CO | 6574 |
| 13 | 🇬🇷 GR | 5212 |
| 14 | 🇲🇽 MX | 5109 |
| 15 | 🇨🇭 CH | 4770 |
| 16 | 🇳🇴 NO | 4637 |
| 17 | 🇹🇷 TR | 4501 |
| 18 | 🇲🇾 MY | 3159 |
| 19 | 🇵🇱 PL | 2980 |
| 20 | 🇿🇦 ZA | 2916 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2281 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1806 |
| 27 | 🇭🇷 HR | 1772 |
| 28 | 🇲🇪 ME | 1628 |
| 29 | 🇳🇱 NL | 1608 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3679 |
| 2 | Denver International Airport |  | US | 2951 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Indira Gandhi International Airport |  | IN | 2189 |
| 5 | Guaymaral Airport |  | CO | 2186 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1928 |
| 8 | Zurich Airport |  | CH | 1903 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1856 |
| 10 | La Aurora Airport |  | GT | 1752 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1604 |
| 13 | Salt Lake City International Airport |  | US | 1593 |
| 14 | El Dorado International Airport |  | CO | 1589 |
| 15 | Frankfurt am Main International Airport |  | DE | 1561 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1484 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1431 |
| 19 | Capua Airport |  | IT | 1399 |
| 20 | Madrid Barajas International Airport |  | ES | 1397 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1328 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1269 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1226 |
| 25 | Charlotte/Douglas International Airport |  | US | 1215 |
| 26 | Charles de Gaulle International Airport |  | FR | 1212 |
| 27 | Kuala Lumpur International Airport |  | MY | 1190 |
| 28 | Bengaluru International Airport |  | IN | 1174 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1105 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1061 |
| 33 | Daniel K Inouye International Airport |  | US | 1026 |
| 34 | Viracopos International Airport |  | BR | 1025 |
| 35 | Seattle-Tacoma International Airport |  | US | 1025 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 993 |
| 39 | Tenerife Norte Airport |  | ES | 976 |
| 40 | Amsterdam Airport Schiphol |  | NL | 966 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 902 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 656 | 21m | 244 km | 2,762.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 415 | 9m | - | - |
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
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 17 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 230 | 8m | - | - |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 214 | 1h 15m | 961 km | 3,547.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 204 | 24m | 218 km | 768.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 15:14 UTC | 2026-08-08 15:47 UTC | 32m |
| N35CV |  | Wings Field (KLOM) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-08 14:40 UTC | 2026-08-08 15:45 UTC | 1h 4m |
| GGWMB | GGW | Turweston Airport (EGBT) | Turweston Airport (EGBT) | 2026-08-08 15:16 UTC | 2026-08-08 15:34 UTC | 18m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-08 15:18 UTC | 2026-08-08 15:34 UTC | 16m |
| N250MC |  | Oakland Southwest Airport (KY47) | Jackson County/Reynolds Field (KJXN) | 2026-08-08 14:46 UTC | 2026-08-08 15:34 UTC | 47m |
| N3221B |  | Dallas Love Field (KDAL) | Telluride Regional Airport (KTEX) | 2026-08-08 13:48 UTC | 2026-08-08 15:25 UTC | 1h 37m |
| N996TA |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-08 15:01 UTC | 2026-08-08 15:25 UTC | 24m |
| N58AC |  | Lindbergh's Landing Airport (FA35) | Miami Executive Airport (KTMB) | 2026-08-08 15:21 UTC | 2026-08-08 15:24 UTC | 3m |
| N94505 |  | 54OK (54OK) | Eagle Creek Airport (51OK) | 2026-08-08 15:03 UTC | 2026-08-08 15:21 UTC | 18m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | Grenoble Le Versoud Airport (LFLG) | 2026-08-08 15:12 UTC | 2026-08-08 15:21 UTC | 8m |
| N97075 |  | KU42 (KU42) | UT99 (UT99) | 2026-08-08 14:51 UTC | 2026-08-08 15:19 UTC | 28m |
| N595DD |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-08-08 14:56 UTC | 2026-08-08 15:19 UTC | 22m |
| N527TD |  | Livermore Municipal Airport (KLVK) | Lake Tahoe Airport (KTVL) | 2026-08-08 14:24 UTC | 2026-08-08 15:18 UTC | 53m |
| UZB3234 | UZB | Karlovy Vary International Airport (LKKV) | Bezymyanka Airfield (UWWG) | 2026-08-08 12:22 UTC | 2026-08-08 15:17 UTC | 2h 54m |
| CAP4302 | CAP | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-08-08 14:54 UTC | 2026-08-08 15:13 UTC | 19m |
| CAP2682 | CAP | Millard Airport (KMLE) | Scribner State Airport (KSCB) | 2026-08-08 14:42 UTC | 2026-08-08 15:11 UTC | 29m |
| EFY7850 | EFY | Enrique Olaya Herrera Airport (SKMD) | Berastegui Airport (SKBR) | 2026-08-08 14:27 UTC | 2026-08-08 15:10 UTC | 43m |
| N61622 |  | Blue Grass Airport (KLEX) | Lebanon Springfield/George Hoerter Field (K6I2) | 2026-08-08 14:15 UTC | 2026-08-08 15:10 UTC | 54m |
| N665KA |  | Henderson Executive Airport (KHND) | Santa Barbara Municipal Airport (KSBA) | 2026-08-08 13:28 UTC | 2026-08-08 15:09 UTC | 1h 41m |
| HK5220 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-08 14:41 UTC | 2026-08-08 15:09 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
