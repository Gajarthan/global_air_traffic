# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_09:24:10_UTC-green)

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

**Latest saved flight:** 2026-07-06 09:24:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-06 09:24:10 UTC

- **130,749** saved flights
- **44,449** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **130,749** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,578,278.2 tonnes** estimated CO2 emissions
- **91,494,389 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5319 |
| 2 | SkyWest Airlines | 4842 |
| 3 | EJA | 2560 |
| 4 | IndiGo | 2450 |
| 5 | American Airlines | 2027 |
| 6 | Southwest Airlines | 1970 |
| 7 | ENY | 1644 |
| 8 | Delta Air Lines | 1571 |
| 9 | Lufthansa | 1369 |
| 10 | LATAM Airlines | 1196 |
| 11 | Vueling | 1155 |
| 12 | WIF | 1139 |
| 13 | AZU | 1113 |
| 14 | AXM | 1012 |
| 15 | LXJ | 1010 |
| 16 | Swiss International | 914 |
| 17 | All Nippon Airways | 863 |
| 18 | easyJet | 839 |
| 19 | Alaska Airlines | 838 |
| 20 | QLK | 820 |
| 21 | EJU | 809 |
| 22 | VIV | 723 |
| 23 | Cathay Pacific | 716 |
| 24 | Air France | 711 |
| 25 | AEE | 710 |
| 26 | CXK | 697 |
| 27 | United Airlines | 696 |
| 28 | JetBlue | 686 |
| 29 | MXY | 682 |
| 30 | GLO | 670 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 111953 |
| 2 | 🇪🇸 ES | 8711 |
| 3 | 🇮🇳 IN | 7685 |
| 4 | 🇦🇺 AU | 7567 |
| 5 | 🇧🇷 BR | 7362 |
| 6 | 🇨🇦 CA | 6898 |
| 7 | 🇩🇪 DE | 6858 |
| 8 | 🇮🇹 IT | 6828 |
| 9 | 🇬🇧 GB | 5823 |
| 10 | 🇯🇵 JP | 5653 |
| 11 | 🇫🇷 FR | 5198 |
| 12 | 🇨🇴 CO | 4102 |
| 13 | 🇲🇽 MX | 3818 |
| 14 | 🇬🇷 GR | 3733 |
| 15 | 🇳🇴 NO | 3541 |
| 16 | 🇨🇭 CH | 3357 |
| 17 | 🇹🇷 TR | 2894 |
| 18 | 🇲🇾 MY | 2623 |
| 19 | 🇿🇦 ZA | 2161 |
| 20 | 🇵🇱 PL | 2146 |
| 21 | 🇳🇿 NZ | 2082 |
| 22 | 🇹🇭 TH | 2031 |
| 23 | 🇰🇷 KR | 1966 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1779 |
| 26 | 🇲🇦 MA | 1395 |
| 27 | 🇲🇪 ME | 1295 |
| 28 | 🇳🇱 NL | 1229 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2732 |
| 2 | Denver International Airport |  | US | 2217 |
| 3 | Tokyo International Airport |  | JP | 1856 |
| 4 | Indira Gandhi International Airport |  | IN | 1695 |
| 5 | Harry Reid International Airport |  | US | 1627 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1542 |
| 8 | Zurich Airport |  | CH | 1441 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1393 |
| 10 | La Aurora Airport |  | GT | 1376 |
| 11 | Frankfurt am Main International Airport |  | DE | 1324 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1265 |
| 13 | Chicago O'Hare International Airport |  | US | 1257 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1163 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1113 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1073 |
| 19 | Madrid Barajas International Airport |  | ES | 1072 |
| 20 | Capua Airport |  | IT | 1070 |
| 21 | Congonhas Airport |  | BR | 1039 |
| 22 | Kuala Lumpur International Airport |  | MY | 1018 |
| 23 | Charlotte/Douglas International Airport |  | US | 974 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 952 |
| 25 | Charles de Gaulle International Airport |  | FR | 947 |
| 26 | Bengaluru International Airport |  | IN | 928 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 888 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 821 |
| 31 | Barcelona International Airport |  | ES | 810 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 796 |
| 33 | Tenerife Norte Airport |  | ES | 792 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 770 |
| 35 | Calgary International Airport |  | CA | 764 |
| 36 | Seattle-Tacoma International Airport |  | US | 756 |
| 37 | Viracopos International Airport |  | BR | 751 |
| 38 | Vitoria/Foronda Airport |  | ES | 750 |
| 39 | Scottsdale Airport |  | US | 747 |
| 40 | Amsterdam Airport Schiphol |  | NL | 743 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 474 | 21m | 244 km | 1,995.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 317 | 1h 10m | 770 km | 4,211.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 190 | 22m | 55 km | 180.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 183 | 44m | 241 km | 760.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 174 | 27m | 152 km | 454.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 171 | 1h 45m | 1,423 km | 4,196.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 160 | 18m | 144 km | 398.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 158 | 44m | 452 km | 1,231.4 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 157 | 30m | 49 km | 132.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| V622 |  | Wangen-Lachen Airport (LSPV) | Emmen Airport (LSME) | 2026-07-06 09:10 UTC | 2026-07-06 09:24 UTC | 13m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-07-06 09:10 UTC | 2026-07-06 09:23 UTC | 13m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-07-06 08:26 UTC | 2026-07-06 09:22 UTC | 56m |
| RAM809P | Royal Air Maroc | London Stansted Airport (EGSS) | Mohammed V International Airport (GMMN) | 2026-07-06 06:39 UTC | 2026-07-06 09:21 UTC | 2h 41m |
| DEEVC | DEE | Wilhelmshaven-Mariensiel Airport (EDWI) | Wilhelmshaven-Mariensiel Airport (EDWI) | 2026-07-06 08:45 UTC | 2026-07-06 09:16 UTC | 30m |
| NSZ3196 | NSZ | Copenhagen Kastrup Airport (EKCH) | Stockholm-Arlanda Airport (ESSA) | 2026-07-06 08:13 UTC | 2026-07-06 09:11 UTC | 58m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-06 06:37 UTC | 2026-07-06 09:02 UTC | 2h 25m |
| IGO6401 | IndiGo | Cochin International Airport (VOCI) | Bengaluru International Airport (VOBL) | 2026-07-06 08:25 UTC | 2026-07-06 09:00 UTC | 35m |
| WMT4078 | WMT | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Chania International Airport (LGSA) | 2026-07-06 07:27 UTC | 2026-07-06 08:58 UTC | 1h 31m |
| RYR7KW | Ryanair | Ciampino Airport (LIRA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-06 07:01 UTC | 2026-07-06 08:49 UTC | 1h 48m |
| RYR76RK | Ryanair | Dublin Airport (EIDW) | Los Martinez Del Puerto Airport (LEMP) | 2026-07-06 06:26 UTC | 2026-07-06 08:47 UTC | 2h 21m |
| APACHE2 | APA | Gilze Rijen Air Base (EHGR) | Volkel Air Base (EHVK) | 2026-07-06 07:40 UTC | 2026-07-06 08:43 UTC | 1h 2m |
| JSD67 | JSD | Budapest Ferenc Liszt International Airport (LHBP) | Livno Brda Bosni Airport (LQLV) | 2026-07-06 08:04 UTC | 2026-07-06 08:41 UTC | 36m |
| DAL2594 | Delta Air Lines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-05 23:40 UTC | 2026-07-06 08:39 UTC | 8h 59m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-07-06 07:41 UTC | 2026-07-06 08:36 UTC | 55m |
| AMU611 | AMU | Taiwan Taoyuan International Airport (RCTP) | Zhuhai Airport (ZGSD) | 2026-07-06 07:17 UTC | 2026-07-06 08:35 UTC | 1h 18m |
| SAS4773 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | LTGP (LTGP) | 2026-07-06 04:51 UTC | 2026-07-06 08:35 UTC | 3h 43m |
| EFC59A | EFC | Al Maktoum International Airport (OMDW) | Al Ain International Airport (OMAL) | 2026-07-06 08:15 UTC | 2026-07-06 08:34 UTC | 18m |
| AM313 |  | Melbourne Essendon Airport (YMEN) | Sale Airport (YSLT) | 2026-07-06 08:01 UTC | 2026-07-06 08:31 UTC | 30m |
| AFR34UP | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-07-06 07:14 UTC | 2026-07-06 08:30 UTC | 1h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
