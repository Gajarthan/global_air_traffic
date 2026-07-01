# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_17:45:34_UTC-green)

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

**Latest saved flight:** 2026-07-01 17:45:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-01 17:45:34 UTC

- **125,785** saved flights
- **42,989** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **125,785** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,517,548.9 tonnes** estimated CO2 emissions
- **87,973,852 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5117 |
| 2 | SkyWest Airlines | 4648 |
| 3 | EJA | 2459 |
| 4 | IndiGo | 2390 |
| 5 | American Airlines | 1936 |
| 6 | Southwest Airlines | 1882 |
| 7 | ENY | 1580 |
| 8 | Delta Air Lines | 1501 |
| 9 | Lufthansa | 1347 |
| 10 | LATAM Airlines | 1136 |
| 11 | Vueling | 1119 |
| 12 | WIF | 1111 |
| 13 | AZU | 1061 |
| 14 | AXM | 996 |
| 15 | LXJ | 972 |
| 16 | Swiss International | 878 |
| 17 | All Nippon Airways | 845 |
| 18 | Alaska Airlines | 821 |
| 19 | easyJet | 802 |
| 20 | QLK | 784 |
| 21 | EJU | 781 |
| 22 | Cathay Pacific | 696 |
| 23 | AEE | 694 |
| 24 | VIV | 688 |
| 25 | Air France | 687 |
| 26 | CXK | 673 |
| 27 | United Airlines | 669 |
| 28 | MXY | 654 |
| 29 | JetBlue | 644 |
| 30 | GLO | 633 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 107438 |
| 2 | 🇪🇸 ES | 8419 |
| 3 | 🇮🇳 IN | 7492 |
| 4 | 🇦🇺 AU | 7323 |
| 5 | 🇧🇷 BR | 7008 |
| 6 | 🇩🇪 DE | 6651 |
| 7 | 🇮🇹 IT | 6622 |
| 8 | 🇨🇦 CA | 6615 |
| 9 | 🇬🇧 GB | 5561 |
| 10 | 🇯🇵 JP | 5508 |
| 11 | 🇫🇷 FR | 4974 |
| 12 | 🇨🇴 CO | 4044 |
| 13 | 🇲🇽 MX | 3651 |
| 14 | 🇬🇷 GR | 3592 |
| 15 | 🇳🇴 NO | 3449 |
| 16 | 🇨🇭 CH | 3203 |
| 17 | 🇹🇷 TR | 2652 |
| 18 | 🇲🇾 MY | 2576 |
| 19 | 🇿🇦 ZA | 2080 |
| 20 | 🇵🇱 PL | 2065 |
| 21 | 🇳🇿 NZ | 2027 |
| 22 | 🇹🇭 TH | 1970 |
| 23 | 🇰🇷 KR | 1946 |
| 24 | 🇵🇭 PH | 1778 |
| 25 | 🇬🇹 GT | 1740 |
| 26 | 🇲🇦 MA | 1351 |
| 27 | 🇲🇪 ME | 1248 |
| 28 | 🇳🇱 NL | 1189 |
| 29 | 🇲🇴 MO | 1182 |
| 30 | 🇧🇸 BS | 1090 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2630 |
| 2 | Denver International Airport |  | US | 2115 |
| 3 | Tokyo International Airport |  | JP | 1819 |
| 4 | Indira Gandhi International Airport |  | IN | 1647 |
| 5 | Harry Reid International Airport |  | US | 1569 |
| 6 | Guaymaral Airport |  | CO | 1531 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1506 |
| 8 | Zurich Airport |  | CH | 1391 |
| 9 | La Aurora Airport |  | GT | 1344 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1342 |
| 11 | Frankfurt am Main International Airport |  | DE | 1300 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1231 |
| 13 | Chicago O'Hare International Airport |  | US | 1216 |
| 14 | Macau International Airport |  | MO | 1182 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1106 |
| 17 | Capua Airport |  | IT | 1066 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1046 |
| 19 | Madrid Barajas International Airport |  | ES | 1041 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1023 |
| 21 | Kuala Lumpur International Airport |  | MY | 1003 |
| 22 | Congonhas Airport |  | BR | 980 |
| 23 | Charlotte/Douglas International Airport |  | US | 947 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 920 |
| 25 | Charles de Gaulle International Airport |  | FR | 915 |
| 26 | Bengaluru International Airport |  | IN | 905 |
| 27 | Malpensa International Airport |  | IT | 863 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 838 |
| 29 | Ninoy Aquino International Airport |  | PH | 824 |
| 30 | Daniel K Inouye International Airport |  | US | 803 |
| 31 | Barcelona International Airport |  | ES | 789 |
| 32 | Tenerife Norte Airport |  | ES | 772 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 767 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 734 |
| 36 | Scottsdale Airport |  | US | 728 |
| 37 | Seattle-Tacoma International Airport |  | US | 726 |
| 38 | Vitoria/Foronda Airport |  | ES | 724 |
| 39 | Amsterdam Airport Schiphol |  | NL | 718 |
| 40 | Viracopos International Airport |  | BR | 714 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 638 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 459 | 21m | 244 km | 1,932.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 317 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 302 | 1h 10m | 770 km | 4,011.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 233 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 162 | 1h 45m | 1,423 km | 3,975.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 144 | 1h 17m | 961 km | 2,386.9 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 143 | 30m | 49 km | 120.9 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR167 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-01 17:08 UTC | 2026-07-01 17:45 UTC | 37m |
| GFY164 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-07-01 16:36 UTC | 2026-07-01 17:41 UTC | 1h 4m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-01 16:32 UTC | 2026-07-01 17:39 UTC | 1h 6m |
| TKR107 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-01 17:18 UTC | 2026-07-01 17:37 UTC | 19m |
| LHB2 | LHB | Friedrichshafen Airport (EDNY) | Toulouse-Blagnac Airport (LFBO) | 2026-07-01 16:23 UTC | 2026-07-01 17:36 UTC | 1h 12m |
| CGPGT | CGP | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-07-01 17:14 UTC | 2026-07-01 17:34 UTC | 20m |
| N871ST |  | Tidmore Airport (7PN0) | Philadelphia International Airport (KPHL) | 2026-07-01 17:02 UTC | 2026-07-01 17:34 UTC | 32m |
| BRG621 | BRG | Ambler Airport (PAFM) | Ambler Airport (PAFM) | 2026-07-01 17:25 UTC | 2026-07-01 17:33 UTC | 7m |
| N606U |  | Little 'L' Ranch Airport (TS61) | Eagle Airport (TA51) | 2026-07-01 17:16 UTC | 2026-07-01 17:31 UTC | 15m |
| N40057 |  | Van Nuys Airport (KVNY) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-01 16:00 UTC | 2026-07-01 17:31 UTC | 1h 30m |
| N715HL |  | Ted Stevens Anchorage International Airport (PANC) | Big Creek Airport (AK51) | 2026-07-01 16:53 UTC | 2026-07-01 17:29 UTC | 36m |
| N665PD |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Los Alamitos Army Air Field (KSLI) | 2026-07-01 16:25 UTC | 2026-07-01 17:29 UTC | 1h 3m |
| N312PC |  | Gnoss Field (KDVO) | Santa Barbara Municipal Airport (KSBA) | 2026-07-01 16:17 UTC | 2026-07-01 17:28 UTC | 1h 10m |
| N34BL |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-07-01 16:51 UTC | 2026-07-01 17:28 UTC | 36m |
| TKR103 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-01 16:48 UTC | 2026-07-01 17:27 UTC | 38m |
| N682AC |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-07-01 17:17 UTC | 2026-07-01 17:27 UTC | 10m |
| PGT1158 | PGT | Dublin Airport (EIDW) | Sabiha Gokcen International Airport (LTFJ) | 2026-07-01 13:37 UTC | 2026-07-01 17:26 UTC | 3h 49m |
| BLADE12 | BLA | Grandfield Municipal Airport (K1O1) | Frederick Regional Airport (KFDR) | 2026-07-01 17:00 UTC | 2026-07-01 17:24 UTC | 23m |
| TRA194G | TRA | Palma De Mallorca Airport (LEPA) | Rotterdam Airport (EHRD) | 2026-07-01 15:14 UTC | 2026-07-01 17:24 UTC | 2h 9m |
| AWH28D | AWH | Hannover Airport (EDDV) | Leipzig Halle Airport (EDDP) | 2026-07-01 16:52 UTC | 2026-07-01 17:23 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
