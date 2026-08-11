# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_19:05:24_UTC-green)

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

**Latest saved flight:** 2026-08-11 19:05:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 19:05:24 UTC

- **187,679** saved flights
- **59,472** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **187,679** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,250,968.2 tonnes** estimated CO2 emissions
- **130,490,909 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7457 |
| 2 | SkyWest Airlines | 6816 |
| 3 | EJA | 3698 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2935 |
| 6 | American Airlines | 2916 |
| 7 | ENY | 2329 |
| 8 | Delta Air Lines | 2209 |
| 9 | LATAM Airlines | 1755 |
| 10 | AZU | 1690 |
| 11 | Lufthansa | 1645 |
| 12 | Vueling | 1554 |
| 13 | WIF | 1554 |
| 14 | LXJ | 1467 |
| 15 | easyJet | 1295 |
| 16 | Swiss International | 1281 |
| 17 | AXM | 1247 |
| 18 | EJU | 1162 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1118 |
| 22 | VIV | 1035 |
| 23 | GLO | 1008 |
| 24 | Air France | 977 |
| 25 | AEE | 968 |
| 26 | PGT | 964 |
| 27 | CXK | 963 |
| 28 | United Airlines | 953 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 934 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160078 |
| 2 | 🇪🇸 ES | 12098 |
| 3 | 🇧🇷 BR | 10778 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10266 |
| 6 | 🇨🇦 CA | 10245 |
| 7 | 🇮🇹 IT | 9730 |
| 8 | 🇩🇪 DE | 9293 |
| 9 | 🇬🇧 GB | 8733 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7515 |
| 12 | 🇨🇴 CO | 7108 |
| 13 | 🇬🇷 GR | 5510 |
| 14 | 🇲🇽 MX | 5345 |
| 15 | 🇨🇭 CH | 5028 |
| 16 | 🇹🇷 TR | 4972 |
| 17 | 🇳🇴 NO | 4831 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3113 |
| 21 | 🇹🇭 TH | 2895 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2390 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1909 |
| 27 | 🇭🇷 HR | 1903 |
| 28 | 🇲🇪 ME | 1681 |
| 29 | 🇳🇱 NL | 1676 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3890 |
| 2 | Denver International Airport |  | US | 3085 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2311 |
| 5 | Guaymaral Airport |  | CO | 2302 |
| 6 | Harry Reid International Airport |  | US | 2195 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1999 |
| 8 | Zurich Airport |  | CH | 1998 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1944 |
| 10 | La Aurora Airport |  | GT | 1837 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1703 |
| 12 | El Dorado International Airport |  | CO | 1684 |
| 13 | Salt Lake City International Airport |  | US | 1668 |
| 14 | Chicago O'Hare International Airport |  | US | 1655 |
| 15 | Frankfurt am Main International Airport |  | DE | 1613 |
| 16 | Congonhas Airport |  | BR | 1567 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1481 |
| 19 | Capua Airport |  | IT | 1463 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1458 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1395 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1343 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1292 |
| 25 | Charles de Gaulle International Airport |  | FR | 1283 |
| 26 | Charlotte/Douglas International Airport |  | US | 1261 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1173 |
| 30 | Ninoy Aquino International Airport |  | PH | 1169 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1148 |
| 32 | Barcelona International Airport |  | ES | 1120 |
| 33 | Viracopos International Airport |  | BR | 1082 |
| 34 | Seattle-Tacoma International Airport |  | US | 1078 |
| 35 | Reno/Tahoe International Airport |  | US | 1075 |
| 36 | Calgary International Airport |  | CA | 1064 |
| 37 | Daniel K Inouye International Airport |  | US | 1058 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1030 |
| 40 | Vitoria/Foronda Airport |  | ES | 1017 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 949 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 686 | 21m | 244 km | 2,888.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 438 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 315 | 27m | 275 km | 1,492.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 304 | 14m | 114 km | 596.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 276 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 229 | 1h 15m | 961 km | 3,795.8 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 221 | 24m | 218 km | 832.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N875DJ |  | Cape May County Airport (KWWD) | Woodbine Municipal Airport (KOBI) | 2026-08-11 18:44 UTC | 2026-08-11 19:05 UTC | 21m |
| CCM51WB | CCM | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | Auxerre-Branches Airport (LFLA) | 2026-08-11 17:41 UTC | 2026-08-11 19:05 UTC | 1h 23m |
| EJU48FH | EJU | Toulouse-Blagnac Airport (LFBO) | Torino / Aeritalia Airport (LIMA) | 2026-08-11 17:51 UTC | 2026-08-11 19:05 UTC | 1h 13m |
| EJU92VX | EJU | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Perouges - Meximieux Airport (LFHC) | 2026-08-11 17:39 UTC | 2026-08-11 19:05 UTC | 1h 25m |
| CAP3289 | CAP | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-08-11 18:09 UTC | 2026-08-11 18:59 UTC | 50m |
| SH141 |  | Florala Municipal Airport (K0J4) | South Alabama Regional At Bill Benton Field (K79J) | 2026-08-11 18:30 UTC | 2026-08-11 18:58 UTC | 28m |
| RYR7ME | Ryanair | Perugia / San Egidio Airport (LIRZ) | Palermo / Punta Raisi Airport (LICJ) | 2026-08-11 18:11 UTC | 2026-08-11 18:57 UTC | 46m |
| N828Y |  | Republic Airport (KFRG) | Bridgeport/Sikorsky Airport (KBDR) | 2026-08-11 17:47 UTC | 2026-08-11 18:57 UTC | 1h 9m |
| N900DF |  | Knox County Regional Airport (KRKD) | Matinicus Island Airport (35ME) | 2026-08-11 18:44 UTC | 2026-08-11 18:56 UTC | 12m |
| C6562 |  | San Francisco International Airport (KSFO) | San Francisco International Airport (KSFO) | 2026-08-11 17:57 UTC | 2026-08-11 18:53 UTC | 56m |
| N426MR |  | Laurence G Hanscom Field (KBED) | Boire Field (KASH) | 2026-08-11 18:17 UTC | 2026-08-11 18:49 UTC | 31m |
| MSR754 | EgyptAir | Madrid Barajas International Airport (LEMD) | HE42 (HE42) | 2026-08-11 14:54 UTC | 2026-08-11 18:48 UTC | 3h 53m |
| N709LA |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-11 18:35 UTC | 2026-08-11 18:45 UTC | 10m |
| FLE107 | FLE | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Vancouver International Airport (CYVR) | 2026-08-11 13:20 UTC | 2026-08-11 18:45 UTC | 5h 24m |
| N66MD |  | Rocky Mountain Metro Airport (KBJC) | Telluride Regional Airport (KTEX) | 2026-08-11 18:12 UTC | 2026-08-11 18:42 UTC | 29m |
| SYH4916 | SYH | Akron-Canton Regional Airport (KCAK) | Northeast Philadelphia Airport (KPNE) | 2026-08-11 16:22 UTC | 2026-08-11 18:41 UTC | 2h 18m |
| TKR183 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Christensen Field (8WA6) | 2026-08-11 17:46 UTC | 2026-08-11 18:40 UTC | 53m |
| RYR45KP | Ryanair | London Gatwick Airport (EGKK) | Dublin Airport (EIDW) | 2026-08-11 17:42 UTC | 2026-08-11 18:39 UTC | 57m |
| N280RH |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-08-11 18:30 UTC | 2026-08-11 18:37 UTC | 7m |
| ASI524 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-11 18:23 UTC | 2026-08-11 18:36 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
