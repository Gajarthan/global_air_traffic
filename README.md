# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_20:06:09_UTC-green)

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

**Latest saved flight:** 2026-06-04 20:06:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-04 20:06:09 UTC

- **102,336** saved flights
- **36,249** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **102,336** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,250,040.9 tonnes** estimated CO2 emissions
- **72,466,137 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4214 |
| 2 | SkyWest Airlines | 3841 |
| 3 | IndiGo | 2045 |
| 4 | EJA | 1961 |
| 5 | American Airlines | 1654 |
| 6 | Southwest Airlines | 1548 |
| 7 | ENY | 1269 |
| 8 | Delta Air Lines | 1202 |
| 9 | Lufthansa | 1189 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 906 |
| 12 | WIF | 901 |
| 13 | AXM | 881 |
| 14 | AZU | 825 |
| 15 | LXJ | 770 |
| 16 | Swiss International | 741 |
| 17 | All Nippon Airways | 720 |
| 18 | Alaska Airlines | 715 |
| 19 | QLK | 685 |
| 20 | easyJet | 666 |
| 21 | EJU | 643 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 595 |
| 24 | VIV | 590 |
| 25 | Air France | 587 |
| 26 | United Airlines | 570 |
| 27 | MXY | 552 |
| 28 | CXK | 549 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 505 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85988 |
| 2 | 🇪🇸 ES | 7064 |
| 3 | 🇮🇳 IN | 6472 |
| 4 | 🇦🇺 AU | 6201 |
| 5 | 🇧🇷 BR | 5612 |
| 6 | 🇩🇪 DE | 5506 |
| 7 | 🇮🇹 IT | 5444 |
| 8 | 🇨🇦 CA | 5314 |
| 9 | 🇯🇵 JP | 4709 |
| 10 | 🇬🇧 GB | 4330 |
| 11 | 🇫🇷 FR | 4062 |
| 12 | 🇨🇴 CO | 3536 |
| 13 | 🇲🇽 MX | 3090 |
| 14 | 🇬🇷 GR | 2913 |
| 15 | 🇳🇴 NO | 2853 |
| 16 | 🇨🇭 CH | 2629 |
| 17 | 🇲🇾 MY | 2246 |
| 18 | 🇹🇷 TR | 1938 |
| 19 | 🇿🇦 ZA | 1776 |
| 20 | 🇳🇿 NZ | 1717 |
| 21 | 🇹🇭 TH | 1695 |
| 22 | 🇰🇷 KR | 1659 |
| 23 | 🇵🇱 PL | 1638 |
| 24 | 🇬🇹 GT | 1506 |
| 25 | 🇵🇭 PH | 1497 |
| 26 | 🇲🇦 MA | 1135 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1015 |
| 29 | 🇲🇪 ME | 968 |
| 30 | 🇭🇷 HR | 902 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2220 |
| 2 | Denver International Airport |  | US | 1753 |
| 3 | Tokyo International Airport |  | JP | 1560 |
| 4 | Indira Gandhi International Airport |  | IN | 1408 |
| 5 | Harry Reid International Airport |  | US | 1309 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1307 |
| 7 | Guaymaral Airport |  | CO | 1284 |
| 8 | Frankfurt am Main International Airport |  | DE | 1189 |
| 9 | Zurich Airport |  | CH | 1169 |
| 10 | La Aurora Airport |  | GT | 1159 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1104 |
| 12 | El Dorado International Airport |  | CO | 1081 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1041 |
| 15 | Chicago O'Hare International Airport |  | US | 1025 |
| 16 | Madrid Barajas International Airport |  | ES | 898 |
| 17 | Kuala Lumpur International Airport |  | MY | 887 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 879 |
| 19 | Salt Lake City International Airport |  | US | 861 |
| 20 | Capua Airport |  | IT | 853 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 794 |
| 22 | Charlotte/Douglas International Airport |  | US | 793 |
| 23 | Congonhas Airport |  | BR | 781 |
| 24 | Charles de Gaulle International Airport |  | FR | 780 |
| 25 | Bengaluru International Airport |  | IN | 773 |
| 26 | Malpensa International Airport |  | IT | 772 |
| 27 | Daniel K Inouye International Airport |  | US | 707 |
| 28 | Tenerife Norte Airport |  | ES | 701 |
| 29 | Ninoy Aquino International Airport |  | PH | 684 |
| 30 | Barcelona International Airport |  | ES | 673 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 666 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 664 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 653 |
| 34 | Amsterdam Airport Schiphol |  | NL | 627 |
| 35 | Don Mueang International Airport |  | TH | 620 |
| 36 | Vitoria/Foronda Airport |  | ES | 620 |
| 37 | Calgary International Airport |  | CA | 602 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 590 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 577 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 530 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 375 | 21m | 244 km | 1,579.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 269 | 24m | 225 km | 1,043.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 247 | 28m | 304 km | 1,294.8 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 215 | 19m | 165 km | 611.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 143 | 27m | 152 km | 373.7 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 137 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 135 | 20m | 250 km | 583.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 133 | 18m | 144 km | 330.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 116 | 44m | 241 km | 481.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3262L |  | Schaumburg Regional Airport (K06C) | Ruder Airport (59IL) | 2026-06-04 19:48 UTC | 2026-06-04 20:06 UTC | 17m |
| N760W |  | Page Field (KFMY) | 92FL (92FL) | 2026-06-04 19:34 UTC | 2026-06-04 20:05 UTC | 31m |
| THY3GL | Turkish Airlines | Batumi International Airport (UGSB) | UKFB (UKFB) | 2026-06-04 19:17 UTC | 2026-06-04 20:04 UTC | 46m |
| VJT271 | VJT | Amsterdam Airport Schiphol (EHAM) | Naypyidaw Airport (VYEL) | 2026-06-04 10:12 UTC | 2026-06-04 20:02 UTC | 9h 49m |
| N4438U |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-06-04 19:24 UTC | 2026-06-04 20:00 UTC | 35m |
| N901CA |  | Round Mountain Ranch Airport (CA09) | Ashland Municipal/Sumner Parker Field (KS03) | 2026-06-04 19:30 UTC | 2026-06-04 19:59 UTC | 29m |
| N745DS |  | KU77 (KU77) | K36U (K36U) | 2026-06-04 19:37 UTC | 2026-06-04 19:57 UTC | 20m |
| BOE118 | BOE | Seattle Paine Field International Airport (KPAE) | Warden Airport (K2S4) | 2026-06-04 17:55 UTC | 2026-06-04 19:50 UTC | 1h 55m |
| VT824 |  | Faa'a International Airport (NTAA) | Arutua Airport (NTGU) | 2026-06-04 18:57 UTC | 2026-06-04 19:49 UTC | 52m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-04 18:44 UTC | 2026-06-04 19:44 UTC | 1h 0m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-04 19:10 UTC | 2026-06-04 19:42 UTC | 31m |
| N570JA |  | Aurora Municipal Airport (KARR) | Ruder Airport (59IL) | 2026-06-04 19:30 UTC | 2026-06-04 19:40 UTC | 10m |
| EVANS13 | EVA Air | Geary Ranch Airport (CO65) | Ak Su Airport (CO61) | 2026-06-04 18:39 UTC | 2026-06-04 19:40 UTC | 1h 0m |
| N619AG |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-06-04 19:10 UTC | 2026-06-04 19:38 UTC | 28m |
| CNS21 | CNS | Mount Holly Airport (SC98) | Savannah/Hilton Head International Airport (KSAV) | 2026-06-04 19:08 UTC | 2026-06-04 19:36 UTC | 28m |
| BLINR77 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-06-04 18:05 UTC | 2026-06-04 19:35 UTC | 1h 29m |
| N2219 |  | 49AZ (49AZ) | Hereford Municipal Airport (KHRX) | 2026-06-04 16:27 UTC | 2026-06-04 19:34 UTC | 3h 7m |
| N840CT |  | Evans Aerodrome (XS39) | River Acres Airport (3AR8) | 2026-06-04 18:29 UTC | 2026-06-04 19:32 UTC | 1h 2m |
| N682AC |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-06-04 19:17 UTC | 2026-06-04 19:31 UTC | 13m |
| LYM3803 | LYM | Greenville Mid-Delta Airport (KGLH) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-06-04 18:26 UTC | 2026-06-04 19:30 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
