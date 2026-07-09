# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_14:02:10_UTC-green)

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

**Latest saved flight:** 2026-07-09 14:02:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 14:02:10 UTC

- **134,124** saved flights
- **45,389** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **134,124** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,614,374.4 tonnes** estimated CO2 emissions
- **93,586,920 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5451 |
| 2 | SkyWest Airlines | 4937 |
| 3 | EJA | 2624 |
| 4 | IndiGo | 2497 |
| 5 | American Airlines | 2092 |
| 6 | Southwest Airlines | 2011 |
| 7 | ENY | 1681 |
| 8 | Delta Air Lines | 1601 |
| 9 | Lufthansa | 1388 |
| 10 | LATAM Airlines | 1229 |
| 11 | Vueling | 1175 |
| 12 | WIF | 1171 |
| 13 | AZU | 1143 |
| 14 | LXJ | 1027 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 955 |
| 17 | All Nippon Airways | 878 |
| 18 | easyJet | 869 |
| 19 | Alaska Airlines | 851 |
| 20 | QLK | 841 |
| 21 | EJU | 824 |
| 22 | VIV | 739 |
| 23 | AEE | 729 |
| 24 | Air France | 721 |
| 25 | CXK | 721 |
| 26 | Cathay Pacific | 720 |
| 27 | United Airlines | 709 |
| 28 | JetBlue | 706 |
| 29 | MXY | 694 |
| 30 | GLO | 681 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 114874 |
| 2 | 🇪🇸 ES | 8904 |
| 3 | 🇮🇳 IN | 7831 |
| 4 | 🇦🇺 AU | 7766 |
| 5 | 🇧🇷 BR | 7548 |
| 6 | 🇨🇦 CA | 7073 |
| 7 | 🇩🇪 DE | 7007 |
| 8 | 🇮🇹 IT | 6974 |
| 9 | 🇬🇧 GB | 6035 |
| 10 | 🇯🇵 JP | 5755 |
| 11 | 🇫🇷 FR | 5333 |
| 12 | 🇨🇴 CO | 4197 |
| 13 | 🇲🇽 MX | 3897 |
| 14 | 🇬🇷 GR | 3837 |
| 15 | 🇳🇴 NO | 3646 |
| 16 | 🇨🇭 CH | 3479 |
| 17 | 🇹🇷 TR | 3046 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2221 |
| 20 | 🇿🇦 ZA | 2215 |
| 21 | 🇳🇿 NZ | 2103 |
| 22 | 🇹🇭 TH | 2062 |
| 23 | 🇰🇷 KR | 1984 |
| 24 | 🇵🇭 PH | 1850 |
| 25 | 🇬🇹 GT | 1816 |
| 26 | 🇲🇦 MA | 1425 |
| 27 | 🇲🇪 ME | 1337 |
| 28 | 🇳🇱 NL | 1258 |
| 29 | 🇭🇷 HR | 1195 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2789 |
| 2 | Denver International Airport |  | US | 2264 |
| 3 | Tokyo International Airport |  | JP | 1878 |
| 4 | Indira Gandhi International Airport |  | IN | 1730 |
| 5 | Harry Reid International Airport |  | US | 1666 |
| 6 | Guaymaral Airport |  | CO | 1637 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1575 |
| 8 | Zurich Airport |  | CH | 1495 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1422 |
| 10 | La Aurora Airport |  | GT | 1402 |
| 11 | Frankfurt am Main International Airport |  | DE | 1342 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1292 |
| 13 | Chicago O'Hare International Airport |  | US | 1278 |
| 14 | Salt Lake City International Airport |  | US | 1191 |
| 15 | El Dorado International Airport |  | CO | 1187 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1159 |
| 18 | Madrid Barajas International Airport |  | ES | 1097 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1096 |
| 20 | Capua Airport |  | IT | 1096 |
| 21 | Congonhas Airport |  | BR | 1067 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 975 |
| 25 | Charles de Gaulle International Airport |  | FR | 961 |
| 26 | Bengaluru International Airport |  | IN | 943 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 919 |
| 28 | Malpensa International Airport |  | IT | 885 |
| 29 | Ninoy Aquino International Airport |  | PH | 861 |
| 30 | Daniel K Inouye International Airport |  | US | 833 |
| 31 | Barcelona International Airport |  | ES | 826 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 818 |
| 33 | Tenerife Norte Airport |  | ES | 804 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 787 |
| 35 | Calgary International Airport |  | CA | 776 |
| 36 | Scottsdale Airport |  | US | 768 |
| 37 | Seattle-Tacoma International Airport |  | US | 767 |
| 38 | Viracopos International Airport |  | BR | 766 |
| 39 | Vitoria/Foronda Airport |  | ES | 759 |
| 40 | Amsterdam Airport Schiphol |  | NL | 755 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 689 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 485 | 21m | 244 km | 2,042.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 335 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 287 | 14m | 114 km | 562.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 244 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 187 | 26m | 215 km | 692.6 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 180 | 1h 46m | 1,423 km | 4,417.5 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 163 | 20m | 250 km | 704.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 155 | 1h 16m | 961 km | 2,569.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 153 | 1h 38m | 1,156 km | 3,052.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9610Q |  | San Marcos Regional Airport (KHYI) | San Marcos Regional Airport (KHYI) | 2026-07-09 13:44 UTC | 2026-07-09 14:02 UTC | 17m |
| N2438R |  | Warren County/John Lane Field (KI68) | Cincinnati West Airport (KI67) | 2026-07-09 13:37 UTC | 2026-07-09 13:57 UTC | 20m |
| N734WB |  | Lincoln County Regional Airport (KIPJ) | Lincoln County Regional Airport (KIPJ) | 2026-07-09 13:46 UTC | 2026-07-09 13:57 UTC | 11m |
| EVA659 | EVA Air | Ted Stevens Anchorage International Airport (PANC) | Taiwan Taoyuan International Airport (RCTP) | 2026-07-09 04:59 UTC | 2026-07-09 13:56 UTC | 8h 57m |
| N6097F |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-07-09 13:40 UTC | 2026-07-09 13:55 UTC | 14m |
| QTR4N | Qatar Airways | Larnaca International Airport (LCLK) | Al Khawr Airport (OTBK) | 2026-07-09 11:32 UTC | 2026-07-09 13:52 UTC | 2h 19m |
| HDB1 | HDB | Al Minhad Air Base (OMDM) | Al Minhad Air Base (OMDM) | 2026-07-09 13:30 UTC | 2026-07-09 13:50 UTC | 19m |
| N387LS |  | Spirit Of St Louis Airport (KSUS) | St Paul Downtown Holman Field (KSTP) | 2026-07-09 12:47 UTC | 2026-07-09 13:49 UTC | 1h 2m |
| HB2497 |  | L'alpe D'huez Airport (LFHU) | Puimoisson Airport (LFTP) | 2026-07-09 12:45 UTC | 2026-07-09 13:45 UTC | 1h 0m |
| CONGO64 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-07-09 13:09 UTC | 2026-07-09 13:44 UTC | 35m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-07-09 13:18 UTC | 2026-07-09 13:44 UTC | 26m |
| CGXXF | CGX | Macgregor Airport (CKF6) | Macgregor Airport (CKF6) | 2026-07-09 12:52 UTC | 2026-07-09 13:44 UTC | 51m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-07-09 06:30 UTC | 2026-07-09 13:42 UTC | 7h 12m |
| N588LA |  | Atlantic City International Airport (KACY) | Atlantic City International Airport (KACY) | 2026-07-09 13:25 UTC | 2026-07-09 13:42 UTC | 16m |
| N60BC |  | French Valley Airport (KF70) | Lake Tahoe Airport (KTVL) | 2026-07-09 12:46 UTC | 2026-07-09 13:42 UTC | 55m |
| WIF48D | WIF | Oslo Gardermoen Airport (ENGM) | Sandnessjoen Airport Stokka (ENST) | 2026-07-09 11:59 UTC | 2026-07-09 13:39 UTC | 1h 39m |
| GCFTO | GCF | Anisakan Airport (VYAS) | Anisakan Airport (VYAS) | 2026-07-09 09:18 UTC | 2026-07-09 13:39 UTC | 4h 20m |
| GSWOW | GSW | Wolverhampton Halfpenny Green Airport (EGBO) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-07-09 13:06 UTC | 2026-07-09 13:38 UTC | 32m |
| PSVTA | PSV | Campo de Marte Airport (SBMT) | Ubatuba Airport (SDUB) | 2026-07-09 13:14 UTC | 2026-07-09 13:38 UTC | 23m |
| N635KC |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-07-09 13:07 UTC | 2026-07-09 13:37 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
