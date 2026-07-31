# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_04:16:52_UTC-green)

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

**Latest saved flight:** 2026-07-31 04:16:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 04:16:52 UTC

- **161,872** saved flights
- **53,402** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **161,872** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,940,528.6 tonnes** estimated CO2 emissions
- **112,494,412 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6463 |
| 2 | SkyWest Airlines | 5910 |
| 3 | EJA | 3210 |
| 4 | IndiGo | 2833 |
| 5 | American Airlines | 2560 |
| 6 | Southwest Airlines | 2539 |
| 7 | ENY | 2018 |
| 8 | Delta Air Lines | 1923 |
| 9 | LATAM Airlines | 1523 |
| 10 | Lufthansa | 1520 |
| 11 | AZU | 1422 |
| 12 | WIF | 1366 |
| 13 | Vueling | 1339 |
| 14 | LXJ | 1261 |
| 15 | AXM | 1124 |
| 16 | Swiss International | 1112 |
| 17 | easyJet | 1057 |
| 18 | Alaska Airlines | 1006 |
| 19 | QLK | 999 |
| 20 | All Nippon Airways | 995 |
| 21 | EJU | 994 |
| 22 | VIV | 891 |
| 23 | CXK | 865 |
| 24 | United Airlines | 855 |
| 25 | Cathay Pacific | 850 |
| 26 | GLO | 849 |
| 27 | AEE | 846 |
| 28 | MXY | 840 |
| 29 | Air France | 837 |
| 30 | JetBlue | 827 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 139974 |
| 2 | 🇪🇸 ES | 10348 |
| 3 | 🇧🇷 BR | 9250 |
| 4 | 🇦🇺 AU | 9166 |
| 5 | 🇮🇳 IN | 8917 |
| 6 | 🇨🇦 CA | 8807 |
| 7 | 🇮🇹 IT | 8325 |
| 8 | 🇩🇪 DE | 8142 |
| 9 | 🇬🇧 GB | 7413 |
| 10 | 🇯🇵 JP | 6559 |
| 11 | 🇫🇷 FR | 6392 |
| 12 | 🇨🇴 CO | 5755 |
| 13 | 🇲🇽 MX | 4650 |
| 14 | 🇬🇷 GR | 4636 |
| 15 | 🇳🇴 NO | 4267 |
| 16 | 🇨🇭 CH | 4231 |
| 17 | 🇹🇷 TR | 3855 |
| 18 | 🇲🇾 MY | 2922 |
| 19 | 🇵🇱 PL | 2743 |
| 20 | 🇿🇦 ZA | 2601 |
| 21 | 🇳🇿 NZ | 2378 |
| 22 | 🇹🇭 TH | 2294 |
| 23 | 🇵🇭 PH | 2128 |
| 24 | 🇰🇷 KR | 2115 |
| 25 | 🇬🇹 GT | 2077 |
| 26 | 🇲🇦 MA | 1629 |
| 27 | 🇲🇪 ME | 1527 |
| 28 | 🇭🇷 HR | 1508 |
| 29 | 🇳🇱 NL | 1480 |
| 30 | 🇲🇴 MO | 1343 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3310 |
| 2 | Denver International Airport |  | US | 2694 |
| 3 | Tokyo International Airport |  | JP | 2070 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1984 |
| 6 | Harry Reid International Airport |  | US | 1967 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1785 |
| 8 | Zurich Airport |  | CH | 1721 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1701 |
| 10 | La Aurora Airport |  | GT | 1613 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1507 |
| 12 | El Dorado International Airport |  | CO | 1482 |
| 13 | Frankfurt am Main International Airport |  | DE | 1471 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1353 |
| 17 | Congonhas Airport |  | BR | 1345 |
| 18 | Macau International Airport |  | MO | 1343 |
| 19 | Madrid Barajas International Airport |  | ES | 1278 |
| 20 | Capua Airport |  | IT | 1271 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1238 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1156 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1148 |
| 24 | Charlotte/Douglas International Airport |  | US | 1140 |
| 25 | Kuala Lumpur International Airport |  | MY | 1114 |
| 26 | Charles de Gaulle International Airport |  | FR | 1104 |
| 27 | Malpensa International Airport |  | IT | 1068 |
| 28 | Bengaluru International Airport |  | IN | 1059 |
| 29 | Ninoy Aquino International Airport |  | PH | 999 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 991 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 983 |
| 32 | Barcelona International Airport |  | ES | 958 |
| 33 | Daniel K Inouye International Airport |  | US | 951 |
| 34 | Seattle-Tacoma International Airport |  | US | 941 |
| 35 | Calgary International Airport |  | CA | 927 |
| 36 | Viracopos International Airport |  | BR | 922 |
| 37 | Scottsdale Airport |  | US | 908 |
| 38 | Tenerife Norte Airport |  | ES | 907 |
| 39 | Oslo Gardermoen Airport |  | NO | 897 |
| 40 | Reno/Tahoe International Airport |  | US | 889 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 590 | 21m | 244 km | 2,484.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 385 | 24m | 225 km | 1,493.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 370 | 1h 9m | 770 km | 4,915.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 239 | 22m | 55 km | 227.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 238 | 19m | 165 km | 677.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 231 | 44m | 241 km | 959.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 198 | 30m | 49 km | 167.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 193 | 1h 15m | 961 km | 3,199.1 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 193 | 28m | 152 km | 504.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 181 | 1h 39m | 1,156 km | 3,610.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 180 | 1h 1m | 695 km | 2,157.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 178 | 44m | 452 km | 1,387.3 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 49m | 1,304 km | 3,892.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| A7GQC |  | Persian Gulf International Airport (OIBP) | Persian Gulf International Airport (OIBP) | 2026-07-31 03:53 UTC | 2026-07-31 04:16 UTC | 23m |
| HKC318 | HKC | VV01 (VV01) | Zhuhai Airport (ZGSD) | 2026-07-31 03:10 UTC | 2026-07-31 04:14 UTC | 1h 3m |
| CXK236 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-07-31 03:48 UTC | 2026-07-31 04:09 UTC | 20m |
| CPA2093 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-07-30 13:32 UTC | 2026-07-31 04:01 UTC | 14h 28m |
| HKE541 | HKE | Noi Bai International Airport (VVNB) | Zhuhai Airport (ZGSD) | 2026-07-31 02:50 UTC | 2026-07-31 03:58 UTC | 1h 7m |
| ASI469 | ASI | Phoenix Deer Valley Airport (KDVT) | 15AZ (15AZ) | 2026-07-31 02:44 UTC | 2026-07-31 03:56 UTC | 1h 11m |
| JAL4872 | Japan Airlines | Amakusa Airport (RJDA) | Iki Airport (RJDB) | 2026-07-31 03:42 UTC | 2026-07-31 03:56 UTC | 13m |
| JAL315 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-07-31 02:49 UTC | 2026-07-31 03:55 UTC | 1h 5m |
| MSR986 | EgyptAir | John F Kennedy International Airport (KJFK) | HE42 (HE42) | 2026-07-30 18:26 UTC | 2026-07-31 03:54 UTC | 9h 28m |
| THY6258 | Turkish Airlines | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-07-30 13:48 UTC | 2026-07-31 03:52 UTC | 14h 3m |
| N61842 |  | Lenawee County Airport (KADG) | II02 (II02) | 2026-07-31 01:59 UTC | 2026-07-31 03:49 UTC | 1h 49m |
| BLINR87 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-07-31 03:19 UTC | 2026-07-31 03:48 UTC | 28m |
| MSR969 | EgyptAir | Juhu Aerodrome (VAJJ) | Hulwan (HE15) | 2026-07-30 22:29 UTC | 2026-07-31 03:46 UTC | 5h 17m |
| A7GQC |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-07-31 02:21 UTC | 2026-07-31 03:43 UTC | 1h 21m |
| A7GQD |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-07-31 02:25 UTC | 2026-07-31 03:42 UTC | 1h 16m |
| 8L8 |  | Sydney Bankstown Airport (YSBK) | Oxley Station Airport (YOLY) | 2026-07-31 02:40 UTC | 2026-07-31 03:37 UTC | 57m |
| ASA69 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-07-31 02:21 UTC | 2026-07-31 03:36 UTC | 1h 15m |
| N567FL |  | Trenton Mercer Airport (KTTN) | Ocean City Municipal Airport (KOXB) | 2026-07-31 02:32 UTC | 2026-07-31 03:35 UTC | 1h 2m |
| CFH24 | CFH | Newcastle Airport (YWLM) | Kelvin Station Airport (YKEL) | 2026-07-31 03:00 UTC | 2026-07-31 03:31 UTC | 31m |
| QTR8905 | Qatar Airways | Chek Lap Kok International Airport (VHHH) | Tilin Airport (VYHN) | 2026-07-30 04:33 UTC | 2026-07-31 03:29 UTC | 22h 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
