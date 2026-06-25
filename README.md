# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_17:42:45_UTC-green)

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

**Latest saved flight:** 2026-06-25 17:42:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-25 17:42:45 UTC

- **120,111** saved flights
- **41,321** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **120,111** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,452,622.9 tonnes** estimated CO2 emissions
- **84,210,022 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4938 |
| 2 | SkyWest Airlines | 4427 |
| 3 | EJA | 2317 |
| 4 | IndiGo | 2309 |
| 5 | American Airlines | 1864 |
| 6 | Southwest Airlines | 1791 |
| 7 | ENY | 1497 |
| 8 | Delta Air Lines | 1420 |
| 9 | Lufthansa | 1317 |
| 10 | Vueling | 1081 |
| 11 | WIF | 1066 |
| 12 | LATAM Airlines | 1063 |
| 13 | AZU | 998 |
| 14 | AXM | 978 |
| 15 | LXJ | 910 |
| 16 | Swiss International | 843 |
| 17 | All Nippon Airways | 820 |
| 18 | Alaska Airlines | 793 |
| 19 | easyJet | 774 |
| 20 | QLK | 768 |
| 21 | EJU | 753 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 670 |
| 24 | Air France | 659 |
| 25 | United Airlines | 657 |
| 26 | VIV | 657 |
| 27 | CXK | 643 |
| 28 | MXY | 630 |
| 29 | AXB | 597 |
| 30 | JetBlue | 594 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 101716 |
| 2 | 🇪🇸 ES | 8165 |
| 3 | 🇮🇳 IN | 7256 |
| 4 | 🇦🇺 AU | 7070 |
| 5 | 🇧🇷 BR | 6602 |
| 6 | 🇩🇪 DE | 6427 |
| 7 | 🇮🇹 IT | 6401 |
| 8 | 🇨🇦 CA | 6316 |
| 9 | 🇯🇵 JP | 5351 |
| 10 | 🇬🇧 GB | 5284 |
| 11 | 🇫🇷 FR | 4784 |
| 12 | 🇨🇴 CO | 4016 |
| 13 | 🇲🇽 MX | 3502 |
| 14 | 🇬🇷 GR | 3433 |
| 15 | 🇳🇴 NO | 3309 |
| 16 | 🇨🇭 CH | 3087 |
| 17 | 🇲🇾 MY | 2539 |
| 18 | 🇹🇷 TR | 2471 |
| 19 | 🇿🇦 ZA | 2021 |
| 20 | 🇵🇱 PL | 1978 |
| 21 | 🇳🇿 NZ | 1942 |
| 22 | 🇹🇭 TH | 1916 |
| 23 | 🇰🇷 KR | 1904 |
| 24 | 🇵🇭 PH | 1721 |
| 25 | 🇬🇹 GT | 1680 |
| 26 | 🇲🇦 MA | 1297 |
| 27 | 🇲🇪 ME | 1198 |
| 28 | 🇲🇴 MO | 1173 |
| 29 | 🇳🇱 NL | 1150 |
| 30 | 🇭🇷 HR | 1039 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2521 |
| 2 | Denver International Airport |  | US | 2012 |
| 3 | Tokyo International Airport |  | JP | 1771 |
| 4 | Indira Gandhi International Airport |  | IN | 1597 |
| 5 | Guaymaral Airport |  | CO | 1506 |
| 6 | Harry Reid International Airport |  | US | 1491 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1459 |
| 8 | Zurich Airport |  | CH | 1339 |
| 9 | La Aurora Airport |  | GT | 1297 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1275 |
| 11 | Frankfurt am Main International Airport |  | DE | 1271 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1188 |
| 13 | Macau International Airport |  | MO | 1173 |
| 14 | El Dorado International Airport |  | CO | 1171 |
| 15 | Chicago O'Hare International Airport |  | US | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1035 |
| 17 | Capua Airport |  | IT | 1035 |
| 18 | Madrid Barajas International Airport |  | ES | 1010 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1001 |
| 20 | Kuala Lumpur International Airport |  | MY | 982 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 929 |
| 22 | Congonhas Airport |  | BR | 923 |
| 23 | Charlotte/Douglas International Airport |  | US | 909 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 890 |
| 25 | Charles de Gaulle International Airport |  | FR | 883 |
| 26 | Bengaluru International Airport |  | IN | 874 |
| 27 | Malpensa International Airport |  | IT | 839 |
| 28 | Ninoy Aquino International Airport |  | PH | 797 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 783 |
| 30 | Daniel K Inouye International Airport |  | US | 774 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 761 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 737 |
| 34 | Calgary International Airport |  | CA | 701 |
| 35 | Vitoria/Foronda Airport |  | ES | 701 |
| 36 | Amsterdam Airport Schiphol |  | NL | 696 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 691 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 683 |
| 40 | Scottsdale Airport |  | US | 683 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 627 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 435 | 21m | 244 km | 1,831.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 315 | 24m | 225 km | 1,222.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 308 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 291 | 1h 25m | 910 km | 4,566.5 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 289 | 1h 10m | 770 km | 3,839.1 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 237 | 26m | 275 km | 1,123.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 223 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 174 | 27m | 215 km | 644.4 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 164 | 44m | 241 km | 681.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 161 | 27m | 152 km | 420.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 149 | 18m | 144 km | 370.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 135 | 1h 17m | 961 km | 2,237.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NDU740 | NDU | Mesa Gateway Airport (KIWA) | Ak-Chin Regional Airport (KA39) | 2026-06-25 17:00 UTC | 2026-06-25 17:42 UTC | 41m |
| OEGTR | OEG | Eleftherios Venizelos International Airport (LGAV) | Innsbruck Airport (LOWI) | 2026-06-25 15:33 UTC | 2026-06-25 17:40 UTC | 2h 7m |
| N199BL |  | Johnston Regional Airport (KJNX) | Wayne Executive Jetport Airport (KGWW) | 2026-06-25 17:04 UTC | 2026-06-25 17:39 UTC | 35m |
| N115PJ |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-06-25 17:03 UTC | 2026-06-25 17:37 UTC | 33m |
| N786FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-25 16:51 UTC | 2026-06-25 17:36 UTC | 44m |
| DOC33 | DOC | Bergen Airport Flesland (ENBR) | Bergen Airport Flesland (ENBR) | 2026-06-25 17:07 UTC | 2026-06-25 17:36 UTC | 28m |
| MOAB08 | MOA | Hill Afb Airport (KHIF) | Lucin Airport (02UT) | 2026-06-25 16:01 UTC | 2026-06-25 17:34 UTC | 1h 33m |
| N808VS |  | Valdez Pioneer Field (PAVD) | Merle K (Mudhole) Smith Airport (PACV) | 2026-06-25 17:12 UTC | 2026-06-25 17:34 UTC | 22m |
| N849AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-06-25 17:09 UTC | 2026-06-25 17:32 UTC | 22m |
| DAL414 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-25 15:46 UTC | 2026-06-25 17:30 UTC | 1h 43m |
| N6489X |  | Minden-Tahoe Airport (KMEV) | Farias Wheel Airport (NV33) | 2026-06-25 17:16 UTC | 2026-06-25 17:29 UTC | 13m |
| N2250E |  | Dover Afb Airport (KDOV) | Dover Afb Airport (KDOV) | 2026-06-25 17:13 UTC | 2026-06-25 17:29 UTC | 16m |
| AXEL10 | AXE | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Castle Airport (KMER) | 2026-06-25 14:52 UTC | 2026-06-25 17:28 UTC | 2h 36m |
| N188HK |  | Hector International Airport (KFAR) | Hector International Airport (KFAR) | 2026-06-25 16:39 UTC | 2026-06-25 17:24 UTC | 45m |
| N302JG |  | London Biggin Hill Airport (EGKB) | Guernsey Airport (EGJB) | 2026-06-25 16:39 UTC | 2026-06-25 17:24 UTC | 44m |
| VULCN91 | VUL | Flysooner Field (OK50) | Double H Ranch Airport (OK40) | 2026-06-25 17:04 UTC | 2026-06-25 17:22 UTC | 17m |
| N2153N |  | Crystal Airport (KMIC) | St Cloud Regional Airport (KSTC) | 2026-06-25 17:03 UTC | 2026-06-25 17:22 UTC | 19m |
| CREEP31 | CRE | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-06-25 16:58 UTC | 2026-06-25 17:20 UTC | 22m |
| ANVIL71 | ANV | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-06-25 16:45 UTC | 2026-06-25 17:20 UTC | 35m |
| N995FG |  | Raleigh-Durham International Airport (KRDU) | Harnett Regional Jetport Airport (KHRJ) | 2026-06-25 16:38 UTC | 2026-06-25 17:20 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
