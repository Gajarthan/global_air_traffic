# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_07:30:47_UTC-green)

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

**Latest saved flight:** 2026-07-13 07:30:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 07:30:47 UTC

- **139,768** saved flights
- **47,070** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **139,768** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,678,337.3 tonnes** estimated CO2 emissions
- **97,294,916 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5694 |
| 2 | SkyWest Airlines | 5120 |
| 3 | EJA | 2755 |
| 4 | IndiGo | 2565 |
| 5 | American Airlines | 2213 |
| 6 | Southwest Airlines | 2104 |
| 7 | ENY | 1743 |
| 8 | Delta Air Lines | 1656 |
| 9 | Lufthansa | 1424 |
| 10 | LATAM Airlines | 1284 |
| 11 | Vueling | 1209 |
| 12 | WIF | 1203 |
| 13 | AZU | 1201 |
| 14 | LXJ | 1072 |
| 15 | AXM | 1046 |
| 16 | Swiss International | 994 |
| 17 | easyJet | 911 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 881 |
| 20 | QLK | 877 |
| 21 | EJU | 863 |
| 22 | VIV | 772 |
| 23 | AEE | 752 |
| 24 | Air France | 750 |
| 25 | CXK | 750 |
| 26 | JetBlue | 735 |
| 27 | United Airlines | 731 |
| 28 | Cathay Pacific | 729 |
| 29 | MXY | 726 |
| 30 | GLO | 715 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 120065 |
| 2 | 🇪🇸 ES | 9179 |
| 3 | 🇮🇳 IN | 8035 |
| 4 | 🇦🇺 AU | 8004 |
| 5 | 🇧🇷 BR | 7884 |
| 6 | 🇨🇦 CA | 7330 |
| 7 | 🇮🇹 IT | 7306 |
| 8 | 🇩🇪 DE | 7296 |
| 9 | 🇬🇧 GB | 6351 |
| 10 | 🇯🇵 JP | 5884 |
| 11 | 🇫🇷 FR | 5566 |
| 12 | 🇨🇴 CO | 4421 |
| 13 | 🇲🇽 MX | 4057 |
| 14 | 🇬🇷 GR | 3981 |
| 15 | 🇳🇴 NO | 3763 |
| 16 | 🇨🇭 CH | 3627 |
| 17 | 🇹🇷 TR | 3283 |
| 18 | 🇲🇾 MY | 2722 |
| 19 | 🇵🇱 PL | 2339 |
| 20 | 🇿🇦 ZA | 2286 |
| 21 | 🇳🇿 NZ | 2142 |
| 22 | 🇹🇭 TH | 2109 |
| 23 | 🇰🇷 KR | 2012 |
| 24 | 🇵🇭 PH | 1906 |
| 25 | 🇬🇹 GT | 1848 |
| 26 | 🇲🇦 MA | 1465 |
| 27 | 🇲🇪 ME | 1386 |
| 28 | 🇳🇱 NL | 1316 |
| 29 | 🇭🇷 HR | 1263 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2887 |
| 2 | Denver International Airport |  | US | 2341 |
| 3 | Tokyo International Airport |  | JP | 1908 |
| 4 | Indira Gandhi International Airport |  | IN | 1778 |
| 5 | Harry Reid International Airport |  | US | 1744 |
| 6 | Guaymaral Airport |  | CO | 1701 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1612 |
| 8 | Zurich Airport |  | CH | 1554 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1466 |
| 10 | La Aurora Airport |  | GT | 1428 |
| 11 | Frankfurt am Main International Airport |  | DE | 1374 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1335 |
| 13 | Chicago O'Hare International Airport |  | US | 1316 |
| 14 | Salt Lake City International Airport |  | US | 1244 |
| 15 | El Dorado International Airport |  | CO | 1240 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1199 |
| 17 | Macau International Airport |  | MO | 1188 |
| 18 | Capua Airport |  | IT | 1147 |
| 19 | Madrid Barajas International Airport |  | ES | 1139 |
| 20 | Congonhas Airport |  | BR | 1122 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1120 |
| 22 | Kuala Lumpur International Airport |  | MY | 1054 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1011 |
| 25 | Charles de Gaulle International Airport |  | FR | 993 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 968 |
| 27 | Bengaluru International Airport |  | IN | 962 |
| 28 | Malpensa International Airport |  | IT | 909 |
| 29 | Ninoy Aquino International Airport |  | PH | 889 |
| 30 | Daniel K Inouye International Airport |  | US | 857 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 854 |
| 32 | Barcelona International Airport |  | ES | 853 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 820 |
| 34 | Tenerife Norte Airport |  | ES | 816 |
| 35 | Calgary International Airport |  | CA | 804 |
| 36 | Viracopos International Airport |  | BR | 798 |
| 37 | Seattle-Tacoma International Airport |  | US | 796 |
| 38 | Scottsdale Airport |  | US | 793 |
| 39 | Amsterdam Airport Schiphol |  | NL | 790 |
| 40 | Vitoria/Foronda Airport |  | ES | 779 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 717 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 507 | 21m | 244 km | 2,134.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 332 | 1h 9m | 770 km | 4,410.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 185 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 170 | 31m | 369 km | 1,082.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 158 | 1h 38m | 1,156 km | 3,152.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 154 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VALK03 | VAL | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-07-13 05:51 UTC | 2026-07-13 07:30 UTC | 1h 39m |
| WIF1X | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-07-13 07:04 UTC | 2026-07-13 07:16 UTC | 11m |
| 9MMIN |  | Senai International Airport (WMKJ) | Senai International Airport (WMKJ) | 2026-07-13 06:42 UTC | 2026-07-13 07:14 UTC | 32m |
| H2UPB |  | Larnaca International Airport (LCLK) | RAF Akrotiri (LCRA) | 2026-07-13 06:49 UTC | 2026-07-13 07:09 UTC | 20m |
| N501JM |  | Provo Municipal Airport (KPVU) | Rosebud Airport (NM29) | 2026-07-13 05:20 UTC | 2026-07-13 07:05 UTC | 1h 44m |
| EAG4BX | EAG | George Best Belfast City Airport (EGAC) | Birmingham International Airport (EGBB) | 2026-07-13 06:04 UTC | 2026-07-13 07:04 UTC | 59m |
| N95VB |  | Cardiff International Airport (EGFF) | Bournemouth Airport (EGHH) | 2026-07-13 06:39 UTC | 2026-07-13 07:02 UTC | 23m |
| EWG1 | EWG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-07-13 06:13 UTC | 2026-07-13 06:59 UTC | 45m |
| HBZUO | HBZ | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-07-13 06:43 UTC | 2026-07-13 06:55 UTC | 11m |
| FD603 |  | Perth Jandakot Airport (YPJT) | Corrigin Airport (YCIG) | 2026-07-13 06:22 UTC | 2026-07-13 06:49 UTC | 27m |
| NOZ4PD | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-13 06:16 UTC | 2026-07-13 06:46 UTC | 30m |
| FD243 |  | Sydney Kingsford Smith International Airport (YSSY) | Walgett Airport (YWLG) | 2026-07-13 05:27 UTC | 2026-07-13 06:46 UTC | 1h 19m |
| PY8001 |  | Perth International Airport (YPPH) | Busselton Regional Airport (YBLN) | 2026-07-13 06:16 UTC | 2026-07-13 06:46 UTC | 29m |
| VLG3QU | Vueling | Barcelona International Airport (LEBL) | Leon Airport (LELN) | 2026-07-13 05:45 UTC | 2026-07-13 06:45 UTC | 1h 0m |
| EZY67PB | easyJet | Belfast International Airport (EGAA) | Liverpool John Lennon Airport (EGGP) | 2026-07-13 06:10 UTC | 2026-07-13 06:42 UTC | 32m |
| MMA212 | MMA | Yangon International Airport (VYYY) | Heho Airport (VYHH) | 2026-07-13 06:13 UTC | 2026-07-13 06:42 UTC | 29m |
| EIN2XC | Aer Lingus | Dublin Airport (EIDW) | Birmingham International Airport (EGBB) | 2026-07-13 06:01 UTC | 2026-07-13 06:42 UTC | 40m |
| N90JX |  | Roswell Air Center Airport (KROW) | Roswell Air Center Airport (KROW) | 2026-07-13 06:41 UTC | 2026-07-13 06:41 UTC | 0m |
| RYR78YR | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Pantelleria Airport (LICG) | 2026-07-13 06:09 UTC | 2026-07-13 06:38 UTC | 29m |
| FJLTA | FJL | Alès Cevennes Airport (LFMS) | Uzes Airport (LFNU) | 2026-07-13 06:24 UTC | 2026-07-13 06:37 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
