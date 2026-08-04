# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_11:54:12_UTC-green)

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

**Latest saved flight:** 2026-08-04 11:54:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 11:54:12 UTC

- **170,227** saved flights
- **55,464** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **170,227** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,052,377.0 tonnes** estimated CO2 emissions
- **118,978,379 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6777 |
| 2 | SkyWest Airlines | 6222 |
| 3 | EJA | 3376 |
| 4 | IndiGo | 2998 |
| 5 | Southwest Airlines | 2681 |
| 6 | American Airlines | 2680 |
| 7 | ENY | 2124 |
| 8 | Delta Air Lines | 2026 |
| 9 | LATAM Airlines | 1578 |
| 10 | Lufthansa | 1563 |
| 11 | AZU | 1497 |
| 12 | WIF | 1424 |
| 13 | Vueling | 1403 |
| 14 | LXJ | 1334 |
| 15 | AXM | 1175 |
| 16 | Swiss International | 1162 |
| 17 | easyJet | 1145 |
| 18 | Alaska Airlines | 1041 |
| 19 | EJU | 1041 |
| 20 | QLK | 1041 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 939 |
| 23 | Cathay Pacific | 911 |
| 24 | CXK | 899 |
| 25 | United Airlines | 896 |
| 26 | AEE | 891 |
| 27 | GLO | 890 |
| 28 | Air France | 875 |
| 29 | MXY | 868 |
| 30 | JetBlue | 854 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 146616 |
| 2 | 🇪🇸 ES | 10908 |
| 3 | 🇧🇷 BR | 9672 |
| 4 | 🇦🇺 AU | 9519 |
| 5 | 🇮🇳 IN | 9393 |
| 6 | 🇨🇦 CA | 9232 |
| 7 | 🇮🇹 IT | 8799 |
| 8 | 🇩🇪 DE | 8481 |
| 9 | 🇬🇧 GB | 7905 |
| 10 | 🇯🇵 JP | 6867 |
| 11 | 🇫🇷 FR | 6755 |
| 12 | 🇨🇴 CO | 6177 |
| 13 | 🇬🇷 GR | 4955 |
| 14 | 🇲🇽 MX | 4867 |
| 15 | 🇨🇭 CH | 4485 |
| 16 | 🇳🇴 NO | 4442 |
| 17 | 🇹🇷 TR | 4152 |
| 18 | 🇲🇾 MY | 3055 |
| 19 | 🇵🇱 PL | 2869 |
| 20 | 🇿🇦 ZA | 2759 |
| 21 | 🇹🇭 TH | 2482 |
| 22 | 🇳🇿 NZ | 2471 |
| 23 | 🇵🇭 PH | 2251 |
| 24 | 🇬🇹 GT | 2192 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1717 |
| 27 | 🇭🇷 HR | 1639 |
| 28 | 🇲🇪 ME | 1572 |
| 29 | 🇳🇱 NL | 1546 |
| 30 | 🇲🇴 MO | 1449 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3504 |
| 2 | Denver International Airport |  | US | 2820 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2107 |
| 5 | Indira Gandhi International Airport |  | IN | 2082 |
| 6 | Harry Reid International Airport |  | US | 2047 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1862 |
| 8 | Zurich Airport |  | CH | 1804 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1791 |
| 10 | La Aurora Airport |  | GT | 1691 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1568 |
| 12 | El Dorado International Airport |  | CO | 1546 |
| 13 | Chicago O'Hare International Airport |  | US | 1545 |
| 14 | Salt Lake City International Airport |  | US | 1528 |
| 15 | Frankfurt am Main International Airport |  | DE | 1524 |
| 16 | Macau International Airport |  | MO | 1449 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1401 |
| 18 | Congonhas Airport |  | BR | 1391 |
| 19 | Madrid Barajas International Airport |  | ES | 1334 |
| 20 | Capua Airport |  | IT | 1326 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1288 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1202 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1192 |
| 24 | Charlotte/Douglas International Airport |  | US | 1183 |
| 25 | Charles de Gaulle International Airport |  | FR | 1155 |
| 26 | Kuala Lumpur International Airport |  | MY | 1150 |
| 27 | Malpensa International Airport |  | IT | 1146 |
| 28 | Bengaluru International Airport |  | IN | 1117 |
| 29 | Ninoy Aquino International Airport |  | PH | 1059 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1057 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1050 |
| 32 | Barcelona International Airport |  | ES | 1008 |
| 33 | Daniel K Inouye International Airport |  | US | 988 |
| 34 | Seattle-Tacoma International Airport |  | US | 984 |
| 35 | Viracopos International Airport |  | BR | 967 |
| 36 | Calgary International Airport |  | CA | 962 |
| 37 | Reno/Tahoe International Airport |  | US | 953 |
| 38 | Tenerife Norte Airport |  | ES | 948 |
| 39 | Oslo Gardermoen Airport |  | NO | 945 |
| 40 | Scottsdale Airport |  | US | 936 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 875 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 621 | 21m | 244 km | 2,614.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 290 | 27m | 275 km | 1,374.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 252 | 44m | 241 km | 1,046.8 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 234 | 1h 47m | 1,423 km | 5,742.7 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 220 | 26m | 215 km | 814.8 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 201 | 50m | 556 km | 1,926.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 200 | 1h 15m | 961 km | 3,315.1 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 192 | 1h 38m | 1,156 km | 3,830.3 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 184 | 43m | 452 km | 1,434.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TONIC2 | TON | Nordholz Airport (ETMN) | Helgoland-Dune Airport (EDXH) | 2026-08-04 11:07 UTC | 2026-08-04 11:54 UTC | 46m |
| BHA253 | BHA | Tribhuvan International Airport (VNKT) | Tikapur Airport (VNTP) | 2026-08-04 10:27 UTC | 2026-08-04 11:30 UTC | 1h 3m |
| HK4384 |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-04 11:17 UTC | 2026-08-04 11:26 UTC | 8m |
| POLIB16 | POL | Ciampino Airport (LIRA) | Bari / Palese International Airport (LIBD) | 2026-08-04 10:37 UTC | 2026-08-04 11:26 UTC | 49m |
| MILAN78 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Valence-Chabeuil Airport (LFLU) | 2026-08-04 10:47 UTC | 2026-08-04 11:19 UTC | 32m |
| FJO71P | FJO | Eleftherios Venizelos International Airport (LGAV) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-04 09:01 UTC | 2026-08-04 11:16 UTC | 2h 14m |
| HYD144 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-08-04 10:23 UTC | 2026-08-04 11:16 UTC | 52m |
| EZY74HQ | easyJet | London Gatwick Airport (EGKK) | Kalamata Airport (LGKL) | 2026-08-04 08:00 UTC | 2026-08-04 11:13 UTC | 3h 12m |
| SEH5JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-08-04 10:44 UTC | 2026-08-04 11:10 UTC | 25m |
| AEZ2631 | AEZ | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-04 10:24 UTC | 2026-08-04 11:07 UTC | 43m |
| LLR513 | LLR | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-08-04 10:44 UTC | 2026-08-04 11:05 UTC | 21m |
| WUK9497 | WUK | London Luton Airport (EGGW) | Queen Alia International Airport (OJAI) | 2026-08-04 06:56 UTC | 2026-08-04 11:03 UTC | 4h 7m |
| SLG3 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Meadow Lake Airport (CYLJ) | 2026-08-04 10:31 UTC | 2026-08-04 11:03 UTC | 31m |
| WMT749 | WMT | Campia Turzii Air Base (LRCT) | Malpensa International Airport (LIMC) | 2026-08-04 09:17 UTC | 2026-08-04 10:59 UTC | 1h 41m |
| N624AL |  | Fernando Luis Ribas Dominicci Airport (TJIG) | PR07 (PR07) | 2026-08-04 10:29 UTC | 2026-08-04 10:56 UTC | 27m |
| OMLWD | OML | Zilina Airport (LZZI) | Zilina Airport (LZZI) | 2026-08-04 09:12 UTC | 2026-08-04 10:56 UTC | 1h 43m |
| SLJ101 | SLJ | Ciampino Airport (LIRA) | Dubrovnik Airport (LDDU) | 2026-08-04 10:08 UTC | 2026-08-04 10:55 UTC | 47m |
| DLA6YF | DLA | Munich International Airport (EDDM) | Malpensa International Airport (LIMC) | 2026-08-04 09:56 UTC | 2026-08-04 10:54 UTC | 57m |
| ZSTWF | ZST | O. R. Tambo International Airport (FAOR) | Middelburg Airport (FAMB) | 2026-08-04 10:06 UTC | 2026-08-04 10:51 UTC | 45m |
| SFR693 | SFR | Cape Town International Airport (FACT) | Rand Airport (FAGM) | 2026-08-04 09:11 UTC | 2026-08-04 10:51 UTC | 1h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
