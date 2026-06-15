# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_22:08:28_UTC-green)

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

**Latest saved flight:** 2026-06-15 22:08:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-15 22:08:28 UTC

- **111,531** saved flights
- **38,889** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **111,531** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,363,203.0 tonnes** estimated CO2 emissions
- **79,026,259 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4602 |
| 2 | SkyWest Airlines | 4173 |
| 3 | IndiGo | 2180 |
| 4 | EJA | 2164 |
| 5 | American Airlines | 1762 |
| 6 | Southwest Airlines | 1667 |
| 7 | ENY | 1387 |
| 8 | Delta Air Lines | 1320 |
| 9 | Lufthansa | 1257 |
| 10 | Vueling | 1023 |
| 11 | WIF | 985 |
| 12 | LATAM Airlines | 982 |
| 13 | AXM | 936 |
| 14 | AZU | 925 |
| 15 | LXJ | 852 |
| 16 | Swiss International | 799 |
| 17 | All Nippon Airways | 774 |
| 18 | Alaska Airlines | 757 |
| 19 | QLK | 731 |
| 20 | easyJet | 720 |
| 21 | EJU | 708 |
| 22 | Cathay Pacific | 659 |
| 23 | AEE | 630 |
| 24 | United Airlines | 623 |
| 25 | VIV | 623 |
| 26 | Air France | 622 |
| 27 | MXY | 594 |
| 28 | CXK | 585 |
| 29 | AXB | 547 |
| 30 | GLO | 546 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93941 |
| 2 | 🇪🇸 ES | 7650 |
| 3 | 🇮🇳 IN | 6871 |
| 4 | 🇦🇺 AU | 6616 |
| 5 | 🇧🇷 BR | 6159 |
| 6 | 🇮🇹 IT | 6004 |
| 7 | 🇩🇪 DE | 5958 |
| 8 | 🇨🇦 CA | 5864 |
| 9 | 🇯🇵 JP | 5035 |
| 10 | 🇬🇧 GB | 4794 |
| 11 | 🇫🇷 FR | 4447 |
| 12 | 🇨🇴 CO | 3787 |
| 13 | 🇲🇽 MX | 3306 |
| 14 | 🇬🇷 GR | 3172 |
| 15 | 🇳🇴 NO | 3081 |
| 16 | 🇨🇭 CH | 2852 |
| 17 | 🇲🇾 MY | 2418 |
| 18 | 🇹🇷 TR | 2220 |
| 19 | 🇿🇦 ZA | 1895 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1836 |
| 22 | 🇳🇿 NZ | 1828 |
| 23 | 🇵🇱 PL | 1827 |
| 24 | 🇵🇭 PH | 1623 |
| 25 | 🇬🇹 GT | 1594 |
| 26 | 🇲🇦 MA | 1228 |
| 27 | 🇲🇴 MO | 1151 |
| 28 | 🇲🇪 ME | 1092 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2378 |
| 2 | Denver International Airport |  | US | 1894 |
| 3 | Tokyo International Airport |  | JP | 1669 |
| 4 | Indira Gandhi International Airport |  | IN | 1493 |
| 5 | Guaymaral Airport |  | CO | 1407 |
| 6 | Harry Reid International Airport |  | US | 1403 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1383 |
| 8 | Zurich Airport |  | CH | 1252 |
| 9 | Frankfurt am Main International Airport |  | DE | 1230 |
| 10 | La Aurora Airport |  | GT | 1226 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1199 |
| 12 | Macau International Airport |  | MO | 1151 |
| 13 | El Dorado International Airport |  | CO | 1140 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1118 |
| 15 | Chicago O'Hare International Airport |  | US | 1109 |
| 16 | Madrid Barajas International Airport |  | ES | 973 |
| 17 | Capua Airport |  | IT | 968 |
| 18 | Salt Lake City International Airport |  | US | 948 |
| 19 | Kuala Lumpur International Airport |  | MY | 941 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 940 |
| 21 | Charlotte/Douglas International Airport |  | US | 857 |
| 22 | Congonhas Airport |  | BR | 857 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 836 |
| 24 | Charles de Gaulle International Airport |  | FR | 834 |
| 25 | Bengaluru International Airport |  | IN | 829 |
| 26 | Malpensa International Airport |  | IT | 812 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 757 |
| 28 | Ninoy Aquino International Airport |  | PH | 749 |
| 29 | Daniel K Inouye International Airport |  | US | 739 |
| 30 | Tenerife Norte Airport |  | ES | 734 |
| 31 | Barcelona International Airport |  | ES | 728 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 728 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 669 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 662 |
| 37 | Calgary International Airport |  | CA | 659 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 642 |
| 39 | Seattle-Tacoma International Airport |  | US | 641 |
| 40 | Viracopos International Airport |  | BR | 632 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 407 | 21m | 244 km | 1,713.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 288 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 262 | 1h 10m | 770 km | 3,480.5 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 224 | 26m | 275 km | 1,061.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 162 | 27m | 215 km | 600.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 160 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 151 | 31m | 369 km | 961.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 143 | 20m | 250 km | 617.7 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 142 | 44m | 241 km | 589.8 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 125 | 1h 17m | 961 km | 2,071.9 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N839DM |  | Torgerson Airport (06MT) | Calgary International Airport (CYYC) | 2026-06-15 21:29 UTC | 2026-06-15 22:08 UTC | 38m |
| NRF | NRF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-06-15 21:32 UTC | 2026-06-15 22:07 UTC | 34m |
| PAT079 | PAT | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-06-15 21:39 UTC | 2026-06-15 22:02 UTC | 23m |
| N79US |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-06-15 21:08 UTC | 2026-06-15 21:58 UTC | 50m |
| N1270K |  | Colonel James Jabara Airport (KAAO) | Salina Regional Airport (KSLN) | 2026-06-15 21:12 UTC | 2026-06-15 21:52 UTC | 40m |
| N468GT |  | Boundary Bay Airport (CZBB) | Boeing Field/King County International Airport (KBFI) | 2026-06-15 21:06 UTC | 2026-06-15 21:52 UTC | 45m |
| N669JW |  | Sanderson Field (KSHN) | Sanderson Field (KSHN) | 2026-06-15 21:31 UTC | 2026-06-15 21:52 UTC | 20m |
| N35683 |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-06-15 21:19 UTC | 2026-06-15 21:51 UTC | 31m |
| CAP4203 | CAP | KWSD (KWSD) | KWSD (KWSD) | 2026-06-15 20:20 UTC | 2026-06-15 21:50 UTC | 1h 29m |
| N7614Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-06-15 21:17 UTC | 2026-06-15 21:49 UTC | 32m |
| N589ME |  | Allegheny County Airport (KAGC) | Dunlea Airpark (PN66) | 2026-06-15 21:31 UTC | 2026-06-15 21:46 UTC | 15m |
| N317CL |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-06-15 21:34 UTC | 2026-06-15 21:46 UTC | 12m |
| N18JA |  | Aurora Municipal Airport (KARR) | Ruder Airport (59IL) | 2026-06-15 21:33 UTC | 2026-06-15 21:44 UTC | 11m |
| DHC99 | DHC | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-06-15 20:55 UTC | 2026-06-15 21:43 UTC | 48m |
| XAMLG | XAM | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-06-15 21:22 UTC | 2026-06-15 21:40 UTC | 18m |
| N6341A |  | Pegasus Airpark (5AZ3) | Eric Marcus Municipal Airport (KP01) | 2026-06-15 20:29 UTC | 2026-06-15 21:40 UTC | 1h 10m |
| DEATH1 | DEA | Rye Field (MS63) | Rye Field (MS63) | 2026-06-15 21:26 UTC | 2026-06-15 21:39 UTC | 13m |
| DEATH2 | DEA | Rye Field (MS63) | Rye Field (MS63) | 2026-06-15 21:27 UTC | 2026-06-15 21:39 UTC | 12m |
| MVK51 | MVK | South St Paul Municipal/Richard E Fleming Field (KSGS) | South St Paul Municipal/Richard E Fleming Field (KSGS) | 2026-06-15 21:26 UTC | 2026-06-15 21:37 UTC | 10m |
| N164S |  | Felts Field (KSFF) | Lewiston/Nez Perce County Airport (KLWS) | 2026-06-15 21:15 UTC | 2026-06-15 21:35 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
