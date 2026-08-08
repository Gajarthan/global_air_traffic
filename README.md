# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_09:36:24_UTC-green)

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

**Latest saved flight:** 2026-08-08 09:36:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 09:36:24 UTC

- **177,778** saved flights
- **57,178** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,778** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,136,405.4 tonnes** estimated CO2 emissions
- **123,849,590 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7043 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3507 |
| 4 | IndiGo | 3120 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1646 |
| 10 | Lufthansa | 1591 |
| 11 | AZU | 1581 |
| 12 | WIF | 1482 |
| 13 | Vueling | 1465 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1210 |
| 16 | AXM | 1205 |
| 17 | easyJet | 1204 |
| 18 | QLK | 1092 |
| 19 | All Nippon Airways | 1083 |
| 20 | EJU | 1083 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 942 |
| 25 | GLO | 939 |
| 26 | AEE | 926 |
| 27 | United Airlines | 917 |
| 28 | Air France | 914 |
| 29 | MXY | 896 |
| 30 | PGT | 879 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152731 |
| 2 | 🇪🇸 ES | 11380 |
| 3 | 🇧🇷 BR | 10138 |
| 4 | 🇦🇺 AU | 10062 |
| 5 | 🇮🇳 IN | 9780 |
| 6 | 🇨🇦 CA | 9727 |
| 7 | 🇮🇹 IT | 9183 |
| 8 | 🇩🇪 DE | 8778 |
| 9 | 🇬🇧 GB | 8189 |
| 10 | 🇯🇵 JP | 7188 |
| 11 | 🇫🇷 FR | 7048 |
| 12 | 🇨🇴 CO | 6526 |
| 13 | 🇬🇷 GR | 5182 |
| 14 | 🇲🇽 MX | 5097 |
| 15 | 🇨🇭 CH | 4707 |
| 16 | 🇳🇴 NO | 4611 |
| 17 | 🇹🇷 TR | 4441 |
| 18 | 🇲🇾 MY | 3144 |
| 19 | 🇵🇱 PL | 2955 |
| 20 | 🇿🇦 ZA | 2886 |
| 21 | 🇹🇭 TH | 2672 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2352 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2226 |
| 26 | 🇲🇦 MA | 1795 |
| 27 | 🇭🇷 HR | 1753 |
| 28 | 🇲🇪 ME | 1614 |
| 29 | 🇳🇱 NL | 1601 |
| 30 | 🇲🇴 MO | 1509 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2948 |
| 3 | Tokyo International Airport |  | JP | 2236 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2175 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1920 |
| 8 | Zurich Airport |  | CH | 1884 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1591 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1554 |
| 16 | Macau International Airport |  | MO | 1509 |
| 17 | Congonhas Airport |  | BR | 1471 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1391 |
| 20 | Madrid Barajas International Airport |  | ES | 1387 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1255 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1246 |
| 24 | Malpensa International Airport |  | IT | 1218 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1205 |
| 27 | Kuala Lumpur International Airport |  | MY | 1184 |
| 28 | Bengaluru International Airport |  | IN | 1164 |
| 29 | Ninoy Aquino International Airport |  | PH | 1106 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1103 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1056 |
| 33 | Daniel K Inouye International Airport |  | US | 1025 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 990 |
| 39 | Tenerife Norte Airport |  | ES | 972 |
| 40 | Amsterdam Airport Schiphol |  | NL | 962 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 655 | 21m | 244 km | 2,758.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 419 | 24m | 225 km | 1,625.5 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 415 | 1h 8m | 770 km | 5,513.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 298 | 27m | 275 km | 1,412.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 293 | 1h 7m | 706 km | 3,567.3 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 246 | 1h 48m | 1,423 km | 6,037.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 227 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 203 | 24m | 218 km | 764.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| G72234 |  | Laredo International Airport (KLRD) | Laredo International Airport (KLRD) | 2026-08-08 09:21 UTC | 2026-08-08 09:36 UTC | 15m |
| DESSC | DES | Friedrichshafen Airport (EDNY) | Friedrichshafen Airport (EDNY) | 2026-08-08 09:01 UTC | 2026-08-08 09:32 UTC | 30m |
| ISR271 | ISR | Ben Gurion International Airport (LLBG) | Stuttgart Airport (EDDS) | 2026-08-08 05:30 UTC | 2026-08-08 09:19 UTC | 3h 48m |
| GBBKB | GBB | Sandtoft Airfield (EGCF) | Leicester Airport (EGBG) | 2026-08-08 08:23 UTC | 2026-08-08 09:14 UTC | 51m |
| CHX1 | CHX | Oberschleisheim Airfield (EDNX) | Oberschleisheim Airfield (EDNX) | 2026-08-08 08:55 UTC | 2026-08-08 09:14 UTC | 19m |
| AFR79NB | Air France | Charles de Gaulle International Airport (LFPG) | Vienna International Airport (LOWW) | 2026-08-08 07:37 UTC | 2026-08-08 09:05 UTC | 1h 28m |
| N685GT |  | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-08-08 08:42 UTC | 2026-08-08 09:03 UTC | 21m |
| G72234 |  | Laredo International Airport (KLRD) | Laredo International Airport (KLRD) | 2026-08-08 07:52 UTC | 2026-08-08 09:03 UTC | 1h 11m |
| EAI51C | EAI | Edinburgh Airport (EGPH) | Dublin Airport (EIDW) | 2026-08-08 07:55 UTC | 2026-08-08 08:57 UTC | 1h 1m |
| CSZ336 | CSZ | Butterworth Airport (WMKB) | Macau International Airport (VMMC) | 2026-08-08 05:28 UTC | 2026-08-08 08:55 UTC | 3h 26m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 08:00 UTC | 2026-08-08 08:51 UTC | 51m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-08 08:39 UTC | 2026-08-08 08:50 UTC | 11m |
| RYR9MP | Ryanair | Birmingham International Airport (EGBB) | Dublin Airport (EIDW) | 2026-08-08 08:05 UTC | 2026-08-08 08:44 UTC | 39m |
| FBY412S | FBY | Burgos Airport (LEBG) | Bilbao Airport (LEBB) | 2026-08-08 08:09 UTC | 2026-08-08 08:43 UTC | 34m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-08 08:23 UTC | 2026-08-08 08:42 UTC | 19m |
| DLH2LX | Lufthansa | Grazzanise Airport (LIRM) | Munich International Airport (EDDM) | 2026-08-08 07:23 UTC | 2026-08-08 08:38 UTC | 1h 14m |
| DEOFF | DEO | Stade Airport (EDHS) | Stade Airport (EDHS) | 2026-08-08 08:15 UTC | 2026-08-08 08:38 UTC | 22m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-08-08 08:21 UTC | 2026-08-08 08:34 UTC | 13m |
| UIA8789 | UIA | Taipei Songshan Airport (RCSS) | Longtan Air Base (RCDI) | 2026-08-08 08:20 UTC | 2026-08-08 08:33 UTC | 12m |
| ROT603W | ROT | Henri Coanda International Airport (LROP) | Caransebes Airport (LRCS) | 2026-08-08 07:43 UTC | 2026-08-08 08:32 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
