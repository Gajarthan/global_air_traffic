# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_10:14:14_UTC-green)

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

**Latest saved flight:** 2026-06-16 10:14:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-16 10:14:14 UTC

- **111,899** saved flights
- **38,988** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **111,899** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,368,088.7 tonnes** estimated CO2 emissions
- **79,309,491 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4612 |
| 2 | SkyWest Airlines | 4185 |
| 3 | IndiGo | 2186 |
| 4 | EJA | 2167 |
| 5 | American Airlines | 1766 |
| 6 | Southwest Airlines | 1672 |
| 7 | ENY | 1395 |
| 8 | Delta Air Lines | 1327 |
| 9 | Lufthansa | 1262 |
| 10 | Vueling | 1025 |
| 11 | WIF | 990 |
| 12 | LATAM Airlines | 985 |
| 13 | AXM | 939 |
| 14 | AZU | 928 |
| 15 | LXJ | 853 |
| 16 | Swiss International | 802 |
| 17 | All Nippon Airways | 780 |
| 18 | Alaska Airlines | 758 |
| 19 | QLK | 734 |
| 20 | easyJet | 722 |
| 21 | EJU | 710 |
| 22 | Cathay Pacific | 664 |
| 23 | AEE | 632 |
| 24 | United Airlines | 625 |
| 25 | Air France | 624 |
| 26 | VIV | 624 |
| 27 | MXY | 596 |
| 28 | CXK | 586 |
| 29 | AXB | 549 |
| 30 | GLO | 547 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 94210 |
| 2 | 🇪🇸 ES | 7672 |
| 3 | 🇮🇳 IN | 6894 |
| 4 | 🇦🇺 AU | 6654 |
| 5 | 🇧🇷 BR | 6173 |
| 6 | 🇮🇹 IT | 6011 |
| 7 | 🇩🇪 DE | 5983 |
| 8 | 🇨🇦 CA | 5878 |
| 9 | 🇯🇵 JP | 5063 |
| 10 | 🇬🇧 GB | 4825 |
| 11 | 🇫🇷 FR | 4455 |
| 12 | 🇨🇴 CO | 3794 |
| 13 | 🇲🇽 MX | 3309 |
| 14 | 🇬🇷 GR | 3183 |
| 15 | 🇳🇴 NO | 3092 |
| 16 | 🇨🇭 CH | 2870 |
| 17 | 🇲🇾 MY | 2429 |
| 18 | 🇹🇷 TR | 2231 |
| 19 | 🇿🇦 ZA | 1903 |
| 20 | 🇰🇷 KR | 1853 |
| 21 | 🇹🇭 TH | 1840 |
| 22 | 🇳🇿 NZ | 1840 |
| 23 | 🇵🇱 PL | 1830 |
| 24 | 🇵🇭 PH | 1631 |
| 25 | 🇬🇹 GT | 1594 |
| 26 | 🇲🇦 MA | 1230 |
| 27 | 🇲🇴 MO | 1159 |
| 28 | 🇲🇪 ME | 1094 |
| 29 | 🇳🇱 NL | 1087 |
| 30 | 🇭🇷 HR | 971 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2387 |
| 2 | Denver International Airport |  | US | 1897 |
| 3 | Tokyo International Airport |  | JP | 1679 |
| 4 | Indira Gandhi International Airport |  | IN | 1499 |
| 5 | Guaymaral Airport |  | CO | 1407 |
| 6 | Harry Reid International Airport |  | US | 1406 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1384 |
| 8 | Zurich Airport |  | CH | 1259 |
| 9 | Frankfurt am Main International Airport |  | DE | 1232 |
| 10 | La Aurora Airport |  | GT | 1226 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1201 |
| 12 | Macau International Airport |  | MO | 1159 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1121 |
| 15 | Chicago O'Hare International Airport |  | US | 1115 |
| 16 | Madrid Barajas International Airport |  | ES | 974 |
| 17 | Capua Airport |  | IT | 970 |
| 18 | Salt Lake City International Airport |  | US | 949 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 942 |
| 20 | Kuala Lumpur International Airport |  | MY | 942 |
| 21 | Charlotte/Douglas International Airport |  | US | 861 |
| 22 | Congonhas Airport |  | BR | 860 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 840 |
| 24 | Charles de Gaulle International Airport |  | FR | 836 |
| 25 | Bengaluru International Airport |  | IN | 833 |
| 26 | Malpensa International Airport |  | IT | 812 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 762 |
| 28 | Ninoy Aquino International Airport |  | PH | 753 |
| 29 | Daniel K Inouye International Airport |  | US | 741 |
| 30 | Tenerife Norte Airport |  | ES | 734 |
| 31 | Barcelona International Airport |  | ES | 729 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 729 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 670 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 663 |
| 37 | Calgary International Airport |  | CA | 659 |
| 38 | Seattle-Tacoma International Airport |  | US | 646 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 644 |
| 40 | Viracopos International Airport |  | BR | 635 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 408 | 21m | 244 km | 1,718.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 298 | 24m | 225 km | 1,156.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 288 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 264 | 1h 10m | 770 km | 3,507.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 224 | 26m | 275 km | 1,061.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 163 | 27m | 215 km | 603.7 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 152 | 31m | 369 km | 967.5 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 149 | 44m | 452 km | 1,161.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 143 | 20m | 250 km | 617.7 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 142 | 44m | 241 km | 589.8 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 125 | 1h 17m | 961 km | 2,071.9 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ETP07 | ETP | MoD Boscombe Down Airport (EGDM) | MoD Boscombe Down Airport (EGDM) | 2026-06-16 09:00 UTC | 2026-06-16 10:14 UTC | 1h 13m |
| SAVER20 | SAV | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-06-16 09:04 UTC | 2026-06-16 10:12 UTC | 1h 8m |
| SYERTN6 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-06-16 09:36 UTC | 2026-06-16 10:11 UTC | 34m |
| DHK011 | DHK | East Midlands Airport (EGNX) | Macau International Airport (VMMC) | 2026-06-15 22:27 UTC | 2026-06-16 10:01 UTC | 11h 33m |
| DHUGO | DHU | Ecuvillens Airport (LSGE) | Raron Airport (LSTA) | 2026-06-16 08:14 UTC | 2026-06-16 10:00 UTC | 1h 46m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-06-15 20:00 UTC | 2026-06-16 09:51 UTC | 13h 51m |
| SGA2561 | SGA | Thessaloniki Macedonia International Airport (LGTS) | Macau International Airport (VMMC) | 2026-06-15 19:21 UTC | 2026-06-16 09:51 UTC | 14h 30m |
| A7GQE |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-06-16 09:04 UTC | 2026-06-16 09:51 UTC | 46m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-16 08:16 UTC | 2026-06-16 09:47 UTC | 1h 31m |
| EWG1 | EWG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-06-16 08:52 UTC | 2026-06-16 09:44 UTC | 51m |
| GSIRT | GSI | Coventry Airport (EGBE) | Coventry Airport (EGBE) | 2026-06-16 09:40 UTC | 2026-06-16 09:41 UTC | 0m |
| HBZWE | HBZ | Zweisimmen Airport (LSTZ) | Meiringen Airport (LSMM) | 2026-06-16 09:12 UTC | 2026-06-16 09:38 UTC | 25m |
| N960JP |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Grant County Airport (KSVC) | 2026-06-16 09:10 UTC | 2026-06-16 09:36 UTC | 26m |
| OKSUU44 | OKS | Vysoke Myto Glider Airport (LKVM) | Letnany Airport (LKLT) | 2026-06-16 09:01 UTC | 2026-06-16 09:34 UTC | 32m |
| RYR1SV | Ryanair | Stockholm-Arlanda Airport (ESSA) | Otocac Airport (LDRO) | 2026-06-16 07:31 UTC | 2026-06-16 09:33 UTC | 2h 2m |
| TRD33 | TRD | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-06-16 09:18 UTC | 2026-06-16 09:33 UTC | 14m |
| TRIDNT11 | TRI | Oaksey Park Airport (EGTW) | DCAE Cosford Airport (EGWC) | 2026-06-16 09:01 UTC | 2026-06-16 09:32 UTC | 30m |
| BHA708 | BHA | Phaplu Airport (VNPL) | Tribhuvan International Airport (VNKT) | 2026-06-16 09:06 UTC | 2026-06-16 09:31 UTC | 25m |
| GCIFY | GCI | Gloucestershire Airport (EGBJ) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-06-16 09:09 UTC | 2026-06-16 09:31 UTC | 21m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-06-16 09:04 UTC | 2026-06-16 09:30 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
