# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_21:57:43_UTC-green)

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

**Latest saved flight:** 2026-08-03 21:57:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 21:57:43 UTC

- **169,476** saved flights
- **55,303** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **169,476** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,042,782.7 tonnes** estimated CO2 emissions
- **118,422,186 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6760 |
| 2 | SkyWest Airlines | 6203 |
| 3 | EJA | 3369 |
| 4 | IndiGo | 2981 |
| 5 | American Airlines | 2671 |
| 6 | Southwest Airlines | 2671 |
| 7 | ENY | 2112 |
| 8 | Delta Air Lines | 2020 |
| 9 | LATAM Airlines | 1570 |
| 10 | Lufthansa | 1557 |
| 11 | AZU | 1492 |
| 12 | WIF | 1419 |
| 13 | Vueling | 1398 |
| 14 | LXJ | 1332 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1158 |
| 17 | easyJet | 1139 |
| 18 | EJU | 1039 |
| 19 | Alaska Airlines | 1037 |
| 20 | QLK | 1029 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 935 |
| 23 | Cathay Pacific | 904 |
| 24 | CXK | 898 |
| 25 | United Airlines | 896 |
| 26 | GLO | 889 |
| 27 | AEE | 887 |
| 28 | Air France | 871 |
| 29 | MXY | 866 |
| 30 | JetBlue | 853 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 146177 |
| 2 | 🇪🇸 ES | 10868 |
| 3 | 🇧🇷 BR | 9640 |
| 4 | 🇦🇺 AU | 9411 |
| 5 | 🇮🇳 IN | 9337 |
| 6 | 🇨🇦 CA | 9194 |
| 7 | 🇮🇹 IT | 8749 |
| 8 | 🇩🇪 DE | 8444 |
| 9 | 🇬🇧 GB | 7875 |
| 10 | 🇯🇵 JP | 6789 |
| 11 | 🇫🇷 FR | 6714 |
| 12 | 🇨🇴 CO | 6156 |
| 13 | 🇬🇷 GR | 4923 |
| 14 | 🇲🇽 MX | 4855 |
| 15 | 🇨🇭 CH | 4461 |
| 16 | 🇳🇴 NO | 4426 |
| 17 | 🇹🇷 TR | 4114 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2859 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2459 |
| 22 | 🇳🇿 NZ | 2452 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2190 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1713 |
| 27 | 🇭🇷 HR | 1634 |
| 28 | 🇲🇪 ME | 1565 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1438 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3482 |
| 2 | Denver International Airport |  | US | 2817 |
| 3 | Tokyo International Airport |  | JP | 2133 |
| 4 | Guaymaral Airport |  | CO | 2107 |
| 5 | Indira Gandhi International Airport |  | IN | 2070 |
| 6 | Harry Reid International Airport |  | US | 2038 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1855 |
| 8 | Zurich Airport |  | CH | 1797 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1786 |
| 10 | La Aurora Airport |  | GT | 1690 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1564 |
| 12 | Chicago O'Hare International Airport |  | US | 1541 |
| 13 | El Dorado International Airport |  | CO | 1540 |
| 14 | Salt Lake City International Airport |  | US | 1524 |
| 15 | Frankfurt am Main International Airport |  | DE | 1517 |
| 16 | Macau International Airport |  | MO | 1438 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1399 |
| 18 | Congonhas Airport |  | BR | 1387 |
| 19 | Madrid Barajas International Airport |  | ES | 1333 |
| 20 | Capua Airport |  | IT | 1321 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1284 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1197 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1180 |
| 25 | Charles de Gaulle International Airport |  | FR | 1151 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1142 |
| 28 | Bengaluru International Airport |  | IN | 1108 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1052 |
| 30 | Ninoy Aquino International Airport |  | PH | 1051 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1048 |
| 32 | Barcelona International Airport |  | ES | 1005 |
| 33 | Daniel K Inouye International Airport |  | US | 985 |
| 34 | Seattle-Tacoma International Airport |  | US | 981 |
| 35 | Viracopos International Airport |  | BR | 963 |
| 36 | Calgary International Airport |  | CA | 958 |
| 37 | Reno/Tahoe International Airport |  | US | 950 |
| 38 | Tenerife Norte Airport |  | ES | 943 |
| 39 | Oslo Gardermoen Airport |  | NO | 941 |
| 40 | Scottsdale Airport |  | US | 936 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 875 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 618 | 21m | 244 km | 2,602.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 251 | 44m | 241 km | 1,042.6 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 233 | 1h 47m | 1,423 km | 5,718.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 202 | 19m | 144 km | 502.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 200 | 1h 15m | 961 km | 3,315.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 200 | 50m | 556 km | 1,917.2 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 190 | 1h 38m | 1,156 km | 3,790.4 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 183 | 8m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N831KX |  | Gastonia Municipal Airport (KAKH) | Gastonia Municipal Airport (KAKH) | 2026-08-03 21:37 UTC | 2026-08-03 21:57 UTC | 20m |
| N402DE |  | Eby Field (II74) | Eby Field (II74) | 2026-08-03 20:59 UTC | 2026-08-03 21:55 UTC | 55m |
| CXK154 | CXK | Butler County Regional/Hogan Field (KHAO) | Butler County Regional/Hogan Field (KHAO) | 2026-08-03 21:30 UTC | 2026-08-03 21:48 UTC | 18m |
| N327VA |  | Weller Airport (MI78) | KHLM (KHLM) | 2026-08-03 21:35 UTC | 2026-08-03 21:47 UTC | 12m |
| FLEDG41 | FLE | 2TX3 (2TX3) | Tularosa Airport (TA31) | 2026-08-03 21:29 UTC | 2026-08-03 21:45 UTC | 15m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-08-03 17:03 UTC | 2026-08-03 21:44 UTC | 4h 41m |
| N5217H |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-03 20:32 UTC | 2026-08-03 21:44 UTC | 1h 12m |
| ASA1075 | Alaska Airlines | Kapalua Airport (PHJH) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-08-03 21:21 UTC | 2026-08-03 21:43 UTC | 21m |
| LICHEN5 | LIC | Clear Creek Airport (2AK2) | Ladd Army Air Field (PAFB) | 2026-08-03 21:22 UTC | 2026-08-03 21:37 UTC | 14m |
| LUZON41 | LUZ | Tee Pee Creek Airport (8TE0) | Richie Rich Airport (8TE1) | 2026-08-03 21:11 UTC | 2026-08-03 21:37 UTC | 25m |
| N23HS |  | Chino Airport (KCNO) | Chino Airport (KCNO) | 2026-08-03 20:41 UTC | 2026-08-03 21:36 UTC | 55m |
| N4877J |  | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-08-03 21:14 UTC | 2026-08-03 21:34 UTC | 19m |
| N916J |  | Rancho Buena Vista Airport (TS94) | SN48 (SN48) | 2026-08-03 19:50 UTC | 2026-08-03 21:33 UTC | 1h 43m |
| N891SK |  | Delaurentis Airport (KOKH) | William R Fairchild International Airport (KCLM) | 2026-08-03 20:42 UTC | 2026-08-03 21:31 UTC | 49m |
| N82CX |  | Wild Billy Airport (OR29) | Portland-Hillsboro Airport (KHIO) | 2026-08-03 20:28 UTC | 2026-08-03 21:29 UTC | 1h 0m |
| N5102D |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-03 20:51 UTC | 2026-08-03 21:22 UTC | 30m |
| CWA921 | CWA | Edmonton International Airport (CYEG) | St. Paul Airport (CEW3) | 2026-08-03 21:00 UTC | 2026-08-03 21:22 UTC | 22m |
| SWA2238 | Southwest Airlines | Harry Reid International Airport (KLAS) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-08-03 15:43 UTC | 2026-08-03 21:21 UTC | 5h 37m |
| AZU4652 | AZU | Americana Airport (SDAI) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-08-03 20:41 UTC | 2026-08-03 21:21 UTC | 40m |
| SBI3746 | SBI | Antalya International Airport (LTAI) | Staroselye Airport (UUBK) | 2026-08-03 12:05 UTC | 2026-08-03 21:20 UTC | 9h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
