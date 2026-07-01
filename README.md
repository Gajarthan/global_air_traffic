# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_13:10:36_UTC-green)

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

**Latest saved flight:** 2026-07-01 13:10:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-01 13:10:36 UTC

- **125,284** saved flights
- **42,832** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **125,284** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,512,731.9 tonnes** estimated CO2 emissions
- **87,694,605 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5105 |
| 2 | SkyWest Airlines | 4635 |
| 3 | EJA | 2448 |
| 4 | IndiGo | 2385 |
| 5 | American Airlines | 1934 |
| 6 | Southwest Airlines | 1877 |
| 7 | ENY | 1569 |
| 8 | Delta Air Lines | 1491 |
| 9 | Lufthansa | 1342 |
| 10 | LATAM Airlines | 1128 |
| 11 | Vueling | 1116 |
| 12 | WIF | 1107 |
| 13 | AZU | 1059 |
| 14 | AXM | 996 |
| 15 | LXJ | 969 |
| 16 | Swiss International | 876 |
| 17 | All Nippon Airways | 845 |
| 18 | Alaska Airlines | 820 |
| 19 | easyJet | 800 |
| 20 | QLK | 784 |
| 21 | EJU | 779 |
| 22 | Cathay Pacific | 695 |
| 23 | AEE | 692 |
| 24 | Air France | 685 |
| 25 | VIV | 683 |
| 26 | United Airlines | 669 |
| 27 | CXK | 667 |
| 28 | MXY | 653 |
| 29 | JetBlue | 641 |
| 30 | GLO | 630 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106853 |
| 2 | 🇪🇸 ES | 8391 |
| 3 | 🇮🇳 IN | 7477 |
| 4 | 🇦🇺 AU | 7320 |
| 5 | 🇧🇷 BR | 6977 |
| 6 | 🇩🇪 DE | 6628 |
| 7 | 🇮🇹 IT | 6613 |
| 8 | 🇨🇦 CA | 6580 |
| 9 | 🇬🇧 GB | 5536 |
| 10 | 🇯🇵 JP | 5506 |
| 11 | 🇫🇷 FR | 4961 |
| 12 | 🇨🇴 CO | 4034 |
| 13 | 🇲🇽 MX | 3633 |
| 14 | 🇬🇷 GR | 3581 |
| 15 | 🇳🇴 NO | 3437 |
| 16 | 🇨🇭 CH | 3198 |
| 17 | 🇹🇷 TR | 2634 |
| 18 | 🇲🇾 MY | 2576 |
| 19 | 🇿🇦 ZA | 2074 |
| 20 | 🇵🇱 PL | 2054 |
| 21 | 🇳🇿 NZ | 2025 |
| 22 | 🇹🇭 TH | 1969 |
| 23 | 🇰🇷 KR | 1946 |
| 24 | 🇵🇭 PH | 1778 |
| 25 | 🇬🇹 GT | 1733 |
| 26 | 🇲🇦 MA | 1346 |
| 27 | 🇲🇪 ME | 1244 |
| 28 | 🇳🇱 NL | 1183 |
| 29 | 🇲🇴 MO | 1181 |
| 30 | 🇭🇷 HR | 1082 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2621 |
| 2 | Denver International Airport |  | US | 2112 |
| 3 | Tokyo International Airport |  | JP | 1819 |
| 4 | Indira Gandhi International Airport |  | IN | 1644 |
| 5 | Harry Reid International Airport |  | US | 1567 |
| 6 | Guaymaral Airport |  | CO | 1522 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1503 |
| 8 | Zurich Airport |  | CH | 1387 |
| 9 | La Aurora Airport |  | GT | 1339 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1334 |
| 11 | Frankfurt am Main International Airport |  | DE | 1295 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1229 |
| 13 | Chicago O'Hare International Airport |  | US | 1210 |
| 14 | Macau International Airport |  | MO | 1181 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1064 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1041 |
| 19 | Madrid Barajas International Airport |  | ES | 1037 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1017 |
| 21 | Kuala Lumpur International Airport |  | MY | 1003 |
| 22 | Congonhas Airport |  | BR | 976 |
| 23 | Charlotte/Douglas International Airport |  | US | 944 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 920 |
| 25 | Charles de Gaulle International Airport |  | FR | 912 |
| 26 | Bengaluru International Airport |  | IN | 901 |
| 27 | Malpensa International Airport |  | IT | 863 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 833 |
| 29 | Ninoy Aquino International Airport |  | PH | 824 |
| 30 | Daniel K Inouye International Airport |  | US | 802 |
| 31 | Barcelona International Airport |  | ES | 787 |
| 32 | Tenerife Norte Airport |  | ES | 771 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 764 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 731 |
| 36 | Seattle-Tacoma International Airport |  | US | 724 |
| 37 | Vitoria/Foronda Airport |  | ES | 722 |
| 38 | Scottsdale Airport |  | US | 720 |
| 39 | Amsterdam Airport Schiphol |  | NL | 716 |
| 40 | Viracopos International Airport |  | BR | 712 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 634 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 458 | 21m | 244 km | 1,928.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 316 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 302 | 1h 10m | 770 km | 4,011.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 233 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 171 | 27m | 152 km | 446.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 161 | 1h 45m | 1,423 km | 3,951.2 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 143 | 1h 17m | 961 km | 2,370.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 140 | 30m | 49 km | 118.3 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 138 | 54m | 136 km | 323.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N767LA |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-07-01 12:54 UTC | 2026-07-01 13:10 UTC | 16m |
| EZY94MC | easyJet | London Gatwick Airport (EGKK) | Chania International Airport (LGSA) | 2026-07-01 09:47 UTC | 2026-07-01 13:04 UTC | 3h 16m |
| SYR515 | SYR | Damascus International Airport (OSDI) | Sirri Island Airport (OIBS) | 2026-07-01 10:42 UTC | 2026-07-01 13:01 UTC | 2h 18m |
| N600NM |  | Crystal Springs Ranch Airport (UT54) | K36U (K36U) | 2026-07-01 12:12 UTC | 2026-07-01 12:56 UTC | 44m |
| CCA107 | Air China | Beijing Capital International Airport (ZBAA) | Zhuhai Airport (ZGSD) | 2026-07-01 10:15 UTC | 2026-07-01 12:55 UTC | 2h 39m |
| DAL1054 | Delta Air Lines | Raleigh-Durham International Airport (KRDU) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-01 11:20 UTC | 2026-07-01 12:54 UTC | 1h 33m |
| FAYKA | FAY | Reims-Prunay Airport (LFQA) | Sarre Union Airport (LFQU) | 2026-07-01 11:59 UTC | 2026-07-01 12:49 UTC | 50m |
| SXS6NT | SXS | Birmingham International Airport (EGBB) | Cigli Airport (LTBL) | 2026-07-01 09:26 UTC | 2026-07-01 12:49 UTC | 3h 22m |
| EMB29 | EMB | Sitio Sao Jose Airport (SDZZ) | Usina de Jose Bonifacio Airport (SNHJ) | 2026-07-01 12:12 UTC | 2026-07-01 12:47 UTC | 35m |
| N245MA |  | Somerset Airport (KSMQ) | Lancaster Airport (KLNS) | 2026-07-01 11:55 UTC | 2026-07-01 12:40 UTC | 45m |
| TCUYD | TCU | Bursa Airport (LTBE) | Bursa Yenisehir Airport (LTBR) | 2026-07-01 12:25 UTC | 2026-07-01 12:38 UTC | 12m |
| CNS97 | CNS | Westchester County Airport (KHPN) | Ruby Airport (18ME) | 2026-07-01 11:29 UTC | 2026-07-01 12:37 UTC | 1h 8m |
| PYN04 | PYN | London Stansted Airport (EGSS) | Cork Airport (EICK) | 2026-07-01 10:59 UTC | 2026-07-01 12:37 UTC | 1h 37m |
| ECMMJ | ECM | Madrigalejo Del Monte Airport (LEJO) | Burgos Airport (LEBG) | 2026-07-01 11:52 UTC | 2026-07-01 12:31 UTC | 38m |
| N571SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-01 11:36 UTC | 2026-07-01 12:29 UTC | 52m |
| FAF4130 | FAF | Chalons-Vatry Air Base (LFOK) | Chatellerault Airport (LFCA) | 2026-07-01 10:38 UTC | 2026-07-01 12:28 UTC | 1h 50m |
| N5315T |  | Taunton Municipal/King Field (KTAN) | Fitchburg Municipal Airport (KFIT) | 2026-07-01 11:43 UTC | 2026-07-01 12:28 UTC | 45m |
| N445D |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-01 11:33 UTC | 2026-07-01 12:26 UTC | 52m |
| N1932K |  | Bay Minette Municipal Airport (K1R8) | Bhllc Airport (MS45) | 2026-07-01 11:59 UTC | 2026-07-01 12:25 UTC | 26m |
| N53402 |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-07-01 11:28 UTC | 2026-07-01 12:24 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
