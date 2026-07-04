# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_15:23:14_UTC-green)

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

**Latest saved flight:** 2026-07-04 15:23:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-04 15:23:14 UTC

- **128,831** saved flights
- **43,876** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,831** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,554,615.0 tonnes** estimated CO2 emissions
- **90,122,611 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5241 |
| 2 | SkyWest Airlines | 4771 |
| 3 | EJA | 2524 |
| 4 | IndiGo | 2423 |
| 5 | American Airlines | 1985 |
| 6 | Southwest Airlines | 1935 |
| 7 | ENY | 1615 |
| 8 | Delta Air Lines | 1536 |
| 9 | Lufthansa | 1359 |
| 10 | LATAM Airlines | 1172 |
| 11 | Vueling | 1141 |
| 12 | WIF | 1133 |
| 13 | AZU | 1095 |
| 14 | AXM | 1003 |
| 15 | LXJ | 999 |
| 16 | Swiss International | 896 |
| 17 | All Nippon Airways | 858 |
| 18 | Alaska Airlines | 831 |
| 19 | easyJet | 823 |
| 20 | QLK | 808 |
| 21 | EJU | 796 |
| 22 | VIV | 711 |
| 23 | Cathay Pacific | 710 |
| 24 | AEE | 703 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 685 |
| 28 | MXY | 672 |
| 29 | JetBlue | 665 |
| 30 | GLO | 653 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110237 |
| 2 | 🇪🇸 ES | 8579 |
| 3 | 🇮🇳 IN | 7600 |
| 4 | 🇦🇺 AU | 7479 |
| 5 | 🇧🇷 BR | 7228 |
| 6 | 🇨🇦 CA | 6785 |
| 7 | 🇩🇪 DE | 6780 |
| 8 | 🇮🇹 IT | 6754 |
| 9 | 🇬🇧 GB | 5718 |
| 10 | 🇯🇵 JP | 5607 |
| 11 | 🇫🇷 FR | 5112 |
| 12 | 🇨🇴 CO | 4074 |
| 13 | 🇲🇽 MX | 3756 |
| 14 | 🇬🇷 GR | 3667 |
| 15 | 🇳🇴 NO | 3517 |
| 16 | 🇨🇭 CH | 3296 |
| 17 | 🇹🇷 TR | 2774 |
| 18 | 🇲🇾 MY | 2603 |
| 19 | 🇿🇦 ZA | 2135 |
| 20 | 🇵🇱 PL | 2115 |
| 21 | 🇳🇿 NZ | 2069 |
| 22 | 🇹🇭 TH | 2001 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1808 |
| 25 | 🇬🇹 GT | 1763 |
| 26 | 🇲🇦 MA | 1380 |
| 27 | 🇲🇪 ME | 1280 |
| 28 | 🇳🇱 NL | 1210 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇭🇷 HR | 1121 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2685 |
| 2 | Denver International Airport |  | US | 2182 |
| 3 | Tokyo International Airport |  | JP | 1848 |
| 4 | Indira Gandhi International Airport |  | IN | 1676 |
| 5 | Harry Reid International Airport |  | US | 1606 |
| 6 | Guaymaral Airport |  | CO | 1561 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1526 |
| 8 | Zurich Airport |  | CH | 1416 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1370 |
| 10 | La Aurora Airport |  | GT | 1363 |
| 11 | Frankfurt am Main International Airport |  | DE | 1314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1256 |
| 13 | Chicago O'Hare International Airport |  | US | 1237 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1147 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1073 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1059 |
| 20 | Madrid Barajas International Airport |  | ES | 1055 |
| 21 | Congonhas Airport |  | BR | 1017 |
| 22 | Kuala Lumpur International Airport |  | MY | 1013 |
| 23 | Charlotte/Douglas International Airport |  | US | 968 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 939 |
| 25 | Charles de Gaulle International Airport |  | FR | 937 |
| 26 | Bengaluru International Airport |  | IN | 919 |
| 27 | Malpensa International Airport |  | IT | 876 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 866 |
| 29 | Ninoy Aquino International Airport |  | PH | 838 |
| 30 | Daniel K Inouye International Airport |  | US | 813 |
| 31 | Barcelona International Airport |  | ES | 803 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 786 |
| 33 | Tenerife Norte Airport |  | ES | 783 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 758 |
| 35 | Calgary International Airport |  | CA | 752 |
| 36 | Vitoria/Foronda Airport |  | ES | 745 |
| 37 | Seattle-Tacoma International Airport |  | US | 743 |
| 38 | Scottsdale Airport |  | US | 742 |
| 39 | Viracopos International Airport |  | BR | 738 |
| 40 | Amsterdam Airport Schiphol |  | NL | 728 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 653 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 466 | 21m | 244 km | 1,962.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 324 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 314 | 1h 10m | 770 km | 4,171.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 246 | 26m | 275 km | 1,165.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 237 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 180 | 44m | 241 km | 747.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 167 | 1h 45m | 1,423 km | 4,098.4 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 152 | 1h 1m | 695 km | 1,822.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 143 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1926U |  | Seldovia Airport (PASO) | Homer Airport (PAHO) | 2026-07-04 15:12 UTC | 2026-07-04 15:23 UTC | 11m |
| FGIBV | FGI | Chambery-Savoie Airport (LFLB) | Chambery-Savoie Airport (LFLB) | 2026-07-04 15:04 UTC | 2026-07-04 15:17 UTC | 13m |
| N634DF |  | Hammonton Municipal Airport (KN81) | Hammonton Municipal Airport (KN81) | 2026-07-04 14:52 UTC | 2026-07-04 15:16 UTC | 24m |
| CFE42A | CFE | London Stansted Airport (EGSS) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-04 13:26 UTC | 2026-07-04 15:13 UTC | 1h 47m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-07-04 14:05 UTC | 2026-07-04 15:06 UTC | 1h 1m |
| VHFNA | VHF | Nea Anchialos Airport (LGBL) | Thessaloniki Macedonia International Airport (LGTS) | 2026-07-04 13:42 UTC | 2026-07-04 15:03 UTC | 1h 21m |
| FFT2060 | FFT | Raleigh-Durham International Airport (KRDU) | Philadelphia International Airport (KPHL) | 2026-07-04 13:47 UTC | 2026-07-04 14:58 UTC | 1h 11m |
| N481W |  | Double Eagle Ii Airport (KAEG) | Ohkay Owingeh Airport (KE14) | 2026-07-04 14:16 UTC | 2026-07-04 14:58 UTC | 41m |
| SPMDM | SPM | Gdańsk Lech Wałęsa Airport (EPGD) | Malbork Military Air Base (EPMB) | 2026-07-04 14:16 UTC | 2026-07-04 14:58 UTC | 41m |
| ECNZM | ECN | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-07-04 14:11 UTC | 2026-07-04 14:52 UTC | 41m |
| N694DA |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-07-04 14:20 UTC | 2026-07-04 14:52 UTC | 31m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-07-04 14:34 UTC | 2026-07-04 14:51 UTC | 17m |
| N87WS |  | Centennial Airport (KAPA) | Rangely Airport (K4V0) | 2026-07-04 14:07 UTC | 2026-07-04 14:49 UTC | 42m |
| N2141Y |  | Sugar Land Regional Airport (KSGR) | Henson Farms Airport (3TS5) | 2026-07-04 14:23 UTC | 2026-07-04 14:47 UTC | 23m |
| SKW5194 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-07-04 13:39 UTC | 2026-07-04 14:43 UTC | 1h 3m |
| SRG851A | SRG | Oban Airport (EGEO) | Glasgow International Airport (EGPF) | 2026-07-04 14:19 UTC | 2026-07-04 14:41 UTC | 21m |
| EPI262 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-07-04 14:20 UTC | 2026-07-04 14:40 UTC | 20m |
| N32KY |  | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-04 13:41 UTC | 2026-07-04 14:40 UTC | 59m |
| ABP812 | ABP | Mikonos Airport (LGMK) | Sparti Airport (LGSP) | 2026-07-04 14:09 UTC | 2026-07-04 14:39 UTC | 29m |
| DLH2JV | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-07-04 13:43 UTC | 2026-07-04 14:35 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
