# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_12:54:18_UTC-green)

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

**Latest saved flight:** 2026-07-23 12:54:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 12:54:18 UTC

- **145,365** saved flights
- **48,648** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **145,365** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,742,032.2 tonnes** estimated CO2 emissions
- **100,987,371 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5897 |
| 2 | SkyWest Airlines | 5317 |
| 3 | EJA | 2863 |
| 4 | IndiGo | 2636 |
| 5 | American Airlines | 2322 |
| 6 | Southwest Airlines | 2196 |
| 7 | ENY | 1808 |
| 8 | Delta Air Lines | 1720 |
| 9 | Lufthansa | 1446 |
| 10 | LATAM Airlines | 1340 |
| 11 | AZU | 1252 |
| 12 | Vueling | 1239 |
| 13 | WIF | 1237 |
| 14 | LXJ | 1117 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1031 |
| 17 | easyJet | 943 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 915 |
| 20 | QLK | 913 |
| 21 | EJU | 890 |
| 22 | VIV | 809 |
| 23 | CXK | 781 |
| 24 | AEE | 770 |
| 25 | JetBlue | 766 |
| 26 | Air France | 765 |
| 27 | MXY | 760 |
| 28 | Cathay Pacific | 758 |
| 29 | United Airlines | 755 |
| 30 | GLO | 746 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125196 |
| 2 | 🇪🇸 ES | 9419 |
| 3 | 🇦🇺 AU | 8338 |
| 4 | 🇮🇳 IN | 8255 |
| 5 | 🇧🇷 BR | 8205 |
| 6 | 🇨🇦 CA | 7725 |
| 7 | 🇮🇹 IT | 7562 |
| 8 | 🇩🇪 DE | 7494 |
| 9 | 🇬🇧 GB | 6626 |
| 10 | 🇯🇵 JP | 6094 |
| 11 | 🇫🇷 FR | 5776 |
| 12 | 🇨🇴 CO | 4751 |
| 13 | 🇲🇽 MX | 4231 |
| 14 | 🇬🇷 GR | 4123 |
| 15 | 🇳🇴 NO | 3874 |
| 16 | 🇨🇭 CH | 3779 |
| 17 | 🇹🇷 TR | 3407 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2450 |
| 20 | 🇿🇦 ZA | 2360 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2140 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1939 |
| 25 | 🇬🇹 GT | 1887 |
| 26 | 🇲🇦 MA | 1505 |
| 27 | 🇲🇪 ME | 1445 |
| 28 | 🇳🇱 NL | 1357 |
| 29 | 🇭🇷 HR | 1324 |
| 30 | 🇲🇴 MO | 1214 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2999 |
| 2 | Denver International Airport |  | US | 2431 |
| 3 | Tokyo International Airport |  | JP | 1959 |
| 4 | Indira Gandhi International Airport |  | IN | 1831 |
| 5 | Harry Reid International Airport |  | US | 1824 |
| 6 | Guaymaral Airport |  | CO | 1777 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1651 |
| 8 | Zurich Airport |  | CH | 1606 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1524 |
| 10 | La Aurora Airport |  | GT | 1462 |
| 11 | Frankfurt am Main International Airport |  | DE | 1394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1371 |
| 13 | Chicago O'Hare International Airport |  | US | 1350 |
| 14 | Salt Lake City International Airport |  | US | 1305 |
| 15 | El Dorado International Airport |  | CO | 1298 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1214 |
| 18 | Capua Airport |  | IT | 1181 |
| 19 | Congonhas Airport |  | BR | 1168 |
| 20 | Madrid Barajas International Airport |  | ES | 1158 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1041 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1017 |
| 26 | Charles de Gaulle International Airport |  | FR | 1010 |
| 27 | Bengaluru International Airport |  | IN | 985 |
| 28 | Malpensa International Airport |  | IT | 938 |
| 29 | Ninoy Aquino International Airport |  | PH | 905 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 890 |
| 31 | Barcelona International Airport |  | ES | 882 |
| 32 | Daniel K Inouye International Airport |  | US | 879 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 866 |
| 34 | Tenerife Norte Airport |  | ES | 832 |
| 35 | Seattle-Tacoma International Airport |  | US | 827 |
| 36 | Viracopos International Airport |  | BR | 826 |
| 37 | Calgary International Airport |  | CA | 825 |
| 38 | Scottsdale Airport |  | US | 823 |
| 39 | Amsterdam Airport Schiphol |  | NL | 817 |
| 40 | Oslo Gardermoen Airport |  | NO | 798 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 749 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 528 | 21m | 244 km | 2,223.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 351 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 261 | 26m | 275 km | 1,236.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 259 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 194 | 1h 46m | 1,423 km | 4,761.1 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N381ES |  | North Perry Airport (KHWO) | Venice Municipal Airport (KVNC) | 2026-07-23 11:32 UTC | 2026-07-23 12:54 UTC | 1h 22m |
| N502SM |  | 2IS4 (2IS4) | 62IA (62IA) | 2026-07-23 11:00 UTC | 2026-07-23 12:54 UTC | 1h 54m |
| HBLAO | HBL | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-07-23 11:53 UTC | 2026-07-23 12:44 UTC | 51m |
| N844MK |  | Trenton Mercer Airport (KTTN) | Newark Liberty International Airport (KEWR) | 2026-07-23 10:48 UTC | 2026-07-23 12:42 UTC | 1h 53m |
| CXK200 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-07-23 12:24 UTC | 2026-07-23 12:39 UTC | 14m |
| LFA542 | LFA | Orlando Sanford International Airport (KSFB) | Marion County Airport (KX35) | 2026-07-23 10:56 UTC | 2026-07-23 12:38 UTC | 1h 41m |
| CFWJP | CFW | Roland (Graham Field) Airport (CKD7) | Roland (Graham Field) Airport (CKD7) | 2026-07-23 10:59 UTC | 2026-07-23 12:35 UTC | 1h 36m |
| SPADE08 | SPA | Hoefen Airport (LOIR) | Laupheim Airport (ETHL) | 2026-07-23 11:49 UTC | 2026-07-23 12:33 UTC | 44m |
| HB2748 |  | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-07-23 11:47 UTC | 2026-07-23 12:32 UTC | 44m |
| WMT2ER | WMT | Baneasa International Airport (LRBS) | Mollis Airport (LSZM) | 2026-07-23 10:09 UTC | 2026-07-23 12:32 UTC | 2h 23m |
| N523AB |  | Erie Municipal Airport (KEIK) | Rocky Mountain Metro Airport (KBJC) | 2026-07-23 11:42 UTC | 2026-07-23 12:30 UTC | 47m |
| HB2206 |  | Muenster Aero Airport (LSPU) | Samedan Airport (LSZS) | 2026-07-23 11:06 UTC | 2026-07-23 12:25 UTC | 1h 18m |
| CXK178 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-23 12:18 UTC | 2026-07-23 12:24 UTC | 6m |
| HB3320 |  | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-07-23 11:52 UTC | 2026-07-23 12:22 UTC | 29m |
| N450LJ |  | MY19 (MY19) | Waskish Municipal Airport (KVWU) | 2026-07-23 11:55 UTC | 2026-07-23 12:22 UTC | 26m |
| HB3291 |  | Muenster Aero Airport (LSPU) | Samedan Airport (LSZS) | 2026-07-23 10:56 UTC | 2026-07-23 12:20 UTC | 1h 23m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-07-23 12:13 UTC | 2026-07-23 12:15 UTC | 2m |
| CPA332 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-07-23 04:07 UTC | 2026-07-23 12:14 UTC | 8h 7m |
| ETD555 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Riyadh Air Base (OERY) | 2026-07-23 10:50 UTC | 2026-07-23 12:13 UTC | 1h 22m |
| EJU653N | EJU | Nice-Cote d'Azur Airport (LFMN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-07-23 10:41 UTC | 2026-07-23 12:11 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
