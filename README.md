# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_17:22:16_UTC-green)

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

**Latest saved flight:** 2026-08-01 17:22:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 17:22:16 UTC

- **165,016** saved flights
- **54,204** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **165,016** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,983,779.7 tonnes** estimated CO2 emissions
- **115,001,723 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6593 |
| 2 | SkyWest Airlines | 5998 |
| 3 | EJA | 3274 |
| 4 | IndiGo | 2908 |
| 5 | American Airlines | 2599 |
| 6 | Southwest Airlines | 2587 |
| 7 | ENY | 2048 |
| 8 | Delta Air Lines | 1965 |
| 9 | LATAM Airlines | 1538 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1449 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1364 |
| 14 | LXJ | 1280 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1132 |
| 17 | easyJet | 1084 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1009 |
| 21 | EJU | 1007 |
| 22 | VIV | 909 |
| 23 | CXK | 884 |
| 24 | Cathay Pacific | 877 |
| 25 | AEE | 866 |
| 26 | GLO | 866 |
| 27 | United Airlines | 866 |
| 28 | Air France | 853 |
| 29 | MXY | 851 |
| 30 | JetBlue | 839 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 142399 |
| 2 | 🇪🇸 ES | 10563 |
| 3 | 🇧🇷 BR | 9413 |
| 4 | 🇦🇺 AU | 9259 |
| 5 | 🇮🇳 IN | 9128 |
| 6 | 🇨🇦 CA | 8958 |
| 7 | 🇮🇹 IT | 8521 |
| 8 | 🇩🇪 DE | 8269 |
| 9 | 🇬🇧 GB | 7592 |
| 10 | 🇯🇵 JP | 6660 |
| 11 | 🇫🇷 FR | 6549 |
| 12 | 🇨🇴 CO | 5939 |
| 13 | 🇬🇷 GR | 4754 |
| 14 | 🇲🇽 MX | 4724 |
| 15 | 🇨🇭 CH | 4345 |
| 16 | 🇳🇴 NO | 4339 |
| 17 | 🇹🇷 TR | 3960 |
| 18 | 🇲🇾 MY | 2967 |
| 19 | 🇵🇱 PL | 2802 |
| 20 | 🇿🇦 ZA | 2691 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2368 |
| 23 | 🇵🇭 PH | 2172 |
| 24 | 🇬🇹 GT | 2137 |
| 25 | 🇰🇷 KR | 2132 |
| 26 | 🇲🇦 MA | 1662 |
| 27 | 🇭🇷 HR | 1560 |
| 28 | 🇲🇪 ME | 1543 |
| 29 | 🇳🇱 NL | 1499 |
| 30 | 🇲🇴 MO | 1402 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3368 |
| 2 | Denver International Airport |  | US | 2733 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2079 |
| 5 | Indira Gandhi International Airport |  | IN | 2020 |
| 6 | Harry Reid International Airport |  | US | 1993 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1814 |
| 8 | Zurich Airport |  | CH | 1757 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1731 |
| 10 | La Aurora Airport |  | GT | 1654 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1527 |
| 12 | El Dorado International Airport |  | CO | 1515 |
| 13 | Frankfurt am Main International Airport |  | DE | 1495 |
| 14 | Chicago O'Hare International Airport |  | US | 1485 |
| 15 | Salt Lake City International Airport |  | US | 1481 |
| 16 | Macau International Airport |  | MO | 1402 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1380 |
| 18 | Congonhas Airport |  | BR | 1364 |
| 19 | Madrid Barajas International Airport |  | ES | 1301 |
| 20 | Capua Airport |  | IT | 1291 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1254 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1166 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1155 |
| 25 | Charles de Gaulle International Airport |  | FR | 1127 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1098 |
| 28 | Bengaluru International Airport |  | IN | 1081 |
| 29 | Ninoy Aquino International Airport |  | PH | 1021 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1010 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1010 |
| 32 | Barcelona International Airport |  | ES | 976 |
| 33 | Daniel K Inouye International Airport |  | US | 961 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 938 |
| 36 | Viracopos International Airport |  | BR | 937 |
| 37 | Scottsdale Airport |  | US | 922 |
| 38 | Tenerife Norte Airport |  | ES | 920 |
| 39 | Oslo Gardermoen Airport |  | NO | 918 |
| 40 | Reno/Tahoe International Airport |  | US | 904 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 599 | 21m | 244 km | 2,522.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 397 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 308 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 250 | 22m | 55 km | 237.6 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 226 | 1h 47m | 1,423 km | 5,546.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 215 | 20m | 250 km | 928.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 197 | 1h 15m | 961 km | 3,265.4 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 194 | 19m | 144 km | 482.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 188 | 50m | 556 km | 1,802.1 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 185 | 1h 38m | 1,156 km | 3,690.7 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LBT731 | LBT | Charles de Gaulle International Airport (LFPG) | Tabarka 7 Novembre Airport (DTKA) | 2026-08-01 15:30 UTC | 2026-08-01 17:22 UTC | 1h 52m |
| N464DA |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-08-01 16:43 UTC | 2026-08-01 17:18 UTC | 35m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-08-01 17:07 UTC | 2026-08-01 17:18 UTC | 11m |
| N15HV |  | Kent Fort Manor Airport (7MD8) | Kent Fort Manor Airport (7MD8) | 2026-08-01 16:11 UTC | 2026-08-01 17:17 UTC | 1h 5m |
| CXK654 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-01 16:16 UTC | 2026-08-01 17:14 UTC | 58m |
| N750SS |  | Pepperell Airport (26MA) | Pepperell Airport (26MA) | 2026-08-01 16:51 UTC | 2026-08-01 17:12 UTC | 20m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-08-01 16:15 UTC | 2026-08-01 17:08 UTC | 53m |
| N74737 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-01 16:33 UTC | 2026-08-01 17:06 UTC | 33m |
| N9380P |  | Anniston Regional Airport (KANB) | Anniston Regional Airport (KANB) | 2026-08-01 16:53 UTC | 2026-08-01 17:06 UTC | 13m |
| N2416Q |  | Skylark Field (KILE) | Skylark Field (KILE) | 2026-08-01 16:50 UTC | 2026-08-01 17:05 UTC | 15m |
| MSR772 | EgyptAir | Geneva Cointrin International Airport (LSGG) | HE42 (HE42) | 2026-08-01 13:38 UTC | 2026-08-01 17:02 UTC | 3h 23m |
| SHOOT69 | SHO | 3TX2 (3TX2) | Homer Municipal Airport (K5F4) | 2026-08-01 16:29 UTC | 2026-08-01 17:00 UTC | 31m |
| N289WW |  | Chandler Municipal Airport (KCHD) | Rimrock Airport (48AZ) | 2026-08-01 16:23 UTC | 2026-08-01 16:59 UTC | 36m |
| KING39 | KIN | Sebastian Municipal Airport (KX26) | Patrick Space Force Base Airport (KCOF) | 2026-08-01 16:31 UTC | 2026-08-01 16:58 UTC | 27m |
| N610EP |  | Fort Worth Meacham International Airport (KFTW) | True Grit South Airport (CO95) | 2026-08-01 15:11 UTC | 2026-08-01 16:56 UTC | 1h 44m |
| CPA501 | Cathay Pacific | Narita International Airport (RJAA) | Chek Lap Kok International Airport (VHHH) | 2026-08-01 13:10 UTC | 2026-08-01 16:54 UTC | 3h 44m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-01 16:36 UTC | 2026-08-01 16:53 UTC | 17m |
| CAN25 | CAN | Lamezia Terme Airport (LICA) | Lamezia Terme Airport (LICA) | 2026-08-01 16:36 UTC | 2026-08-01 16:53 UTC | 16m |
| N12234 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Sacramento Executive Airport (KSAC) | 2026-08-01 15:52 UTC | 2026-08-01 16:49 UTC | 57m |
| BCS516 | BCS | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-08-01 09:06 UTC | 2026-08-01 16:49 UTC | 7h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
