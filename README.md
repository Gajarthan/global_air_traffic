# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_07:55:35_UTC-green)

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

**Latest saved flight:** 2026-06-07 07:55:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-07 07:55:35 UTC

- **105,052** saved flights
- **36,989** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,052** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,285,235.0 tonnes** estimated CO2 emissions
- **74,506,374 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4318 |
| 2 | SkyWest Airlines | 3961 |
| 3 | IndiGo | 2090 |
| 4 | EJA | 2009 |
| 5 | American Airlines | 1691 |
| 6 | Southwest Airlines | 1591 |
| 7 | ENY | 1320 |
| 8 | Delta Air Lines | 1244 |
| 9 | Lufthansa | 1203 |
| 10 | Vueling | 967 |
| 11 | LATAM Airlines | 929 |
| 12 | WIF | 914 |
| 13 | AXM | 901 |
| 14 | AZU | 841 |
| 15 | LXJ | 792 |
| 16 | Swiss International | 757 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 730 |
| 19 | QLK | 705 |
| 20 | easyJet | 683 |
| 21 | EJU | 661 |
| 22 | Cathay Pacific | 628 |
| 23 | AEE | 606 |
| 24 | VIV | 603 |
| 25 | Air France | 602 |
| 26 | United Airlines | 585 |
| 27 | MXY | 571 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 523 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88450 |
| 2 | 🇪🇸 ES | 7227 |
| 3 | 🇮🇳 IN | 6598 |
| 4 | 🇦🇺 AU | 6341 |
| 5 | 🇧🇷 BR | 5725 |
| 6 | 🇩🇪 DE | 5637 |
| 7 | 🇮🇹 IT | 5585 |
| 8 | 🇨🇦 CA | 5470 |
| 9 | 🇯🇵 JP | 4830 |
| 10 | 🇬🇧 GB | 4432 |
| 11 | 🇫🇷 FR | 4163 |
| 12 | 🇨🇴 CO | 3634 |
| 13 | 🇲🇽 MX | 3147 |
| 14 | 🇬🇷 GR | 2992 |
| 15 | 🇳🇴 NO | 2903 |
| 16 | 🇨🇭 CH | 2678 |
| 17 | 🇲🇾 MY | 2306 |
| 18 | 🇹🇷 TR | 2012 |
| 19 | 🇿🇦 ZA | 1808 |
| 20 | 🇳🇿 NZ | 1758 |
| 21 | 🇰🇷 KR | 1740 |
| 22 | 🇹🇭 TH | 1732 |
| 23 | 🇵🇱 PL | 1697 |
| 24 | 🇵🇭 PH | 1553 |
| 25 | 🇬🇹 GT | 1526 |
| 26 | 🇲🇦 MA | 1161 |
| 27 | 🇲🇴 MO | 1103 |
| 28 | 🇳🇱 NL | 1031 |
| 29 | 🇲🇪 ME | 1002 |
| 30 | 🇭🇷 HR | 916 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2285 |
| 2 | Denver International Airport |  | US | 1801 |
| 3 | Tokyo International Airport |  | JP | 1602 |
| 4 | Indira Gandhi International Airport |  | IN | 1433 |
| 5 | Harry Reid International Airport |  | US | 1346 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1331 |
| 7 | Guaymaral Airport |  | CO | 1323 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1187 |
| 10 | La Aurora Airport |  | GT | 1174 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1133 |
| 12 | El Dorado International Airport |  | CO | 1108 |
| 13 | Macau International Airport |  | MO | 1103 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1065 |
| 15 | Chicago O'Hare International Airport |  | US | 1058 |
| 16 | Madrid Barajas International Airport |  | ES | 918 |
| 17 | Kuala Lumpur International Airport |  | MY | 902 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 899 |
| 19 | Salt Lake City International Airport |  | US | 898 |
| 20 | Capua Airport |  | IT | 886 |
| 21 | Charlotte/Douglas International Airport |  | US | 816 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 807 |
| 23 | Charles de Gaulle International Airport |  | FR | 799 |
| 24 | Congonhas Airport |  | BR | 795 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 786 |
| 27 | Daniel K Inouye International Airport |  | US | 719 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 711 |
| 30 | Barcelona International Airport |  | ES | 689 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 678 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 674 |
| 34 | Amsterdam Airport Schiphol |  | NL | 639 |
| 35 | Don Mueang International Airport |  | TH | 634 |
| 36 | Vitoria/Foronda Airport |  | ES | 632 |
| 37 | Calgary International Airport |  | CA | 621 |
| 38 | Seattle-Tacoma International Airport |  | US | 612 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 604 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 601 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 546 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 387 | 21m | 244 km | 1,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 282 | 24m | 225 km | 1,094.0 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 258 | 1h 25m | 910 km | 4,048.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 257 | 28m | 304 km | 1,347.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 242 | 1h 10m | 770 km | 3,214.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 210 | 26m | 275 km | 995.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 136 | 18m | 144 km | 338.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGNEP | FGN | Sallanches Airport (LFHZ) | Megeve Airport (LFHM) | 2026-06-07 07:26 UTC | 2026-06-07 07:55 UTC | 28m |
| IMYAU | IMY | Bolzano Airport (LIPB) | Bolzano Airport (LIPB) | 2026-06-07 07:35 UTC | 2026-06-07 07:38 UTC | 2m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-06-07 07:18 UTC | 2026-06-07 07:33 UTC | 15m |
| ISR889 | ISR | Ben Gurion International Airport (LLBG) | Ordu–Giresun Airport (LTCB) | 2026-06-07 06:00 UTC | 2026-06-07 07:27 UTC | 1h 27m |
| AYT101 | AYT | Hatzor Air Base (LLHS) | Ein Yahav Airfield (LLEY) | 2026-06-07 07:09 UTC | 2026-06-07 07:26 UTC | 17m |
| QLK381D | QLK | Maryborough Airport (YMYB) | Brisbane International Airport (YBBN) | 2026-06-07 06:41 UTC | 2026-06-07 07:20 UTC | 38m |
| FHTEL | FHT | Paris-Le Bourget Airport (LFPB) | Zhuhai Airport (ZGSD) | 2026-06-06 20:04 UTC | 2026-06-07 07:11 UTC | 11h 6m |
| KLM1229 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Gothenburg-Landvetter Airport (ESGG) | 2026-06-07 05:57 UTC | 2026-06-07 07:10 UTC | 1h 13m |
| RYR18PG | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Ifrane Airport (GMFI) | 2026-06-07 04:31 UTC | 2026-06-07 07:07 UTC | 2h 35m |
| RJB302 | RJB | Nice-Cote d'Azur Airport (LFMN) | Trento / Mattarello Airport (LIDT) | 2026-06-07 06:27 UTC | 2026-06-07 07:06 UTC | 38m |
| APG223 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-06-07 06:35 UTC | 2026-06-07 07:01 UTC | 25m |
| FIN8RU | Finnair | Helsinki Vantaa Airport (EFHK) | Livno Brda Bosni Airport (LQLV) | 2026-06-07 04:26 UTC | 2026-06-07 06:58 UTC | 2h 31m |
| AXM6440 | AXM | Bentong Airport (WMAD) | Sungai Tiang Airport (WMAN) | 2026-06-07 06:35 UTC | 2026-06-07 06:56 UTC | 20m |
| 00000210 |  | Moi Air Base (HKRE) | Nairobi Wilson Airport (HKNW) | 2026-06-07 06:35 UTC | 2026-06-07 06:55 UTC | 19m |
| AIQ1030 | AIQ | Don Mueang International Airport (VTBD) | Sayaboury Airport (VLSB) | 2026-06-07 06:02 UTC | 2026-06-07 06:55 UTC | 52m |
| SAS2831 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Livno Brda Bosni Airport (LQLV) | 2026-06-07 05:09 UTC | 2026-06-07 06:54 UTC | 1h 44m |
| AXM397 | AXM | Kuala Lumpur International Airport (WMKK) | Kisaran Airport (WIML) | 2026-06-07 06:35 UTC | 2026-06-07 06:53 UTC | 18m |
| PGT2286 | PGT | Sabiha Gokcen International Airport (LTFJ) | Cardak Airport (LTAY) | 2026-06-07 06:16 UTC | 2026-06-07 06:53 UTC | 36m |
| AGV01 | AGV | Bex Airport (LSGB) | Bex Airport (LSGB) | 2026-06-07 06:52 UTC | 2026-06-07 06:52 UTC | 0m |
| SKY145 | SKY | Kobe Airport (RJBE) | Saga Airport (RJFS) | 2026-06-07 06:04 UTC | 2026-06-07 06:50 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
