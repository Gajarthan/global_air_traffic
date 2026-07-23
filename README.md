# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_19:37:41_UTC-green)

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

**Latest saved flight:** 2026-07-23 19:37:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 19:37:41 UTC

- **146,338** saved flights
- **48,936** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **146,338** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,751,690.3 tonnes** estimated CO2 emissions
- **101,547,263 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5930 |
| 2 | SkyWest Airlines | 5358 |
| 3 | EJA | 2889 |
| 4 | IndiGo | 2645 |
| 5 | American Airlines | 2329 |
| 6 | Southwest Airlines | 2211 |
| 7 | ENY | 1819 |
| 8 | Delta Air Lines | 1735 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1348 |
| 11 | AZU | 1259 |
| 12 | WIF | 1244 |
| 13 | Vueling | 1243 |
| 14 | LXJ | 1129 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1034 |
| 17 | easyJet | 944 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 916 |
| 20 | QLK | 913 |
| 21 | EJU | 900 |
| 22 | VIV | 813 |
| 23 | CXK | 787 |
| 24 | AEE | 776 |
| 25 | JetBlue | 770 |
| 26 | Air France | 769 |
| 27 | MXY | 763 |
| 28 | United Airlines | 762 |
| 29 | Cathay Pacific | 758 |
| 30 | GLO | 754 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 126140 |
| 2 | 🇪🇸 ES | 9481 |
| 3 | 🇦🇺 AU | 8342 |
| 4 | 🇮🇳 IN | 8282 |
| 5 | 🇧🇷 BR | 8257 |
| 6 | 🇨🇦 CA | 7795 |
| 7 | 🇮🇹 IT | 7611 |
| 8 | 🇩🇪 DE | 7534 |
| 9 | 🇬🇧 GB | 6665 |
| 10 | 🇯🇵 JP | 6098 |
| 11 | 🇫🇷 FR | 5813 |
| 12 | 🇨🇴 CO | 4835 |
| 13 | 🇲🇽 MX | 4256 |
| 14 | 🇬🇷 GR | 4151 |
| 15 | 🇳🇴 NO | 3904 |
| 16 | 🇨🇭 CH | 3814 |
| 17 | 🇹🇷 TR | 3431 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2465 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2140 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1903 |
| 26 | 🇲🇦 MA | 1512 |
| 27 | 🇲🇪 ME | 1451 |
| 28 | 🇳🇱 NL | 1362 |
| 29 | 🇭🇷 HR | 1337 |
| 30 | 🇲🇴 MO | 1217 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3013 |
| 2 | Denver International Airport |  | US | 2452 |
| 3 | Tokyo International Airport |  | JP | 1960 |
| 4 | Indira Gandhi International Airport |  | IN | 1838 |
| 5 | Harry Reid International Airport |  | US | 1828 |
| 6 | Guaymaral Airport |  | CO | 1806 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1658 |
| 8 | Zurich Airport |  | CH | 1611 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1535 |
| 10 | La Aurora Airport |  | GT | 1474 |
| 11 | Frankfurt am Main International Airport |  | DE | 1401 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1376 |
| 13 | Chicago O'Hare International Airport |  | US | 1359 |
| 14 | Salt Lake City International Airport |  | US | 1320 |
| 15 | El Dorado International Airport |  | CO | 1310 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1268 |
| 17 | Macau International Airport |  | MO | 1217 |
| 18 | Capua Airport |  | IT | 1189 |
| 19 | Congonhas Airport |  | BR | 1178 |
| 20 | Madrid Barajas International Airport |  | ES | 1168 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1149 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1045 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1022 |
| 26 | Charles de Gaulle International Airport |  | FR | 1013 |
| 27 | Bengaluru International Airport |  | IN | 991 |
| 28 | Malpensa International Airport |  | IT | 945 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 892 |
| 31 | Barcelona International Airport |  | ES | 886 |
| 32 | Daniel K Inouye International Airport |  | US | 882 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 874 |
| 34 | Tenerife Norte Airport |  | ES | 839 |
| 35 | Seattle-Tacoma International Airport |  | US | 834 |
| 36 | Calgary International Airport |  | CA | 831 |
| 37 | Scottsdale Airport |  | US | 830 |
| 38 | Viracopos International Airport |  | BR | 829 |
| 39 | Amsterdam Airport Schiphol |  | NL | 822 |
| 40 | Oslo Gardermoen Airport |  | NO | 807 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 761 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 531 | 21m | 244 km | 2,235.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 355 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 264 | 27m | 275 km | 1,251.0 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 219 | 22m | 55 km | 208.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 196 | 1h 46m | 1,423 km | 4,810.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 196 | 44m | 241 km | 814.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 193 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 170 | 1h 16m | 961 km | 2,817.8 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FSION21 | FSI | Anacacho Ranch Airport (0XS7) | Anacacho Ranch Airport (0XS7) | 2026-07-23 19:20 UTC | 2026-07-23 19:37 UTC | 16m |
| UAV13 | UAV | Adelanto Airport (52CL) | Southern California Logistics Airport (KVCV) | 2026-07-23 19:11 UTC | 2026-07-23 19:28 UTC | 17m |
| N840ER |  | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-07-23 18:36 UTC | 2026-07-23 19:27 UTC | 50m |
| N918DB |  | Addison Airport (KADS) | Molair Airport (TX35) | 2026-07-23 19:03 UTC | 2026-07-23 19:25 UTC | 22m |
| KITE50 | KIT | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Bradshaw Army Airfield (PHSF) | 2026-07-23 18:16 UTC | 2026-07-23 19:18 UTC | 1h 2m |
| AIZ410 | AIZ | Batumi International Airport (UGSB) | Queen Alia International Airport (OJAI) | 2026-07-23 17:34 UTC | 2026-07-23 19:18 UTC | 1h 44m |
| N172VT |  | Franklin County State Airport (KFSO) | Franklin County State Airport (KFSO) | 2026-07-23 18:31 UTC | 2026-07-23 19:16 UTC | 44m |
| FAM3202 | FAM | Santa Lucia Air Force Base (MMSM) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-23 19:03 UTC | 2026-07-23 19:16 UTC | 12m |
| N3533Q |  | Brown Field Municipal Airport (KSDM) | Loma Madera Ranch Airport (25CA) | 2026-07-23 16:30 UTC | 2026-07-23 19:14 UTC | 2h 44m |
| N145FH |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-23 19:10 UTC | 2026-07-23 19:14 UTC | 3m |
| MTRX51 | MTR | Southport Airport (CYPG) | Mccreary Airport (CJR8) | 2026-07-23 18:52 UTC | 2026-07-23 19:14 UTC | 21m |
| N3262L |  | Schaumburg Regional Airport (K06C) | Schaumburg Regional Airport (K06C) | 2026-07-23 18:34 UTC | 2026-07-23 19:13 UTC | 38m |
| CXK146 | CXK | Morristown Municipal Airport (KMMU) | Lancaster Airport (KLNS) | 2026-07-23 18:14 UTC | 2026-07-23 19:11 UTC | 56m |
| ABD5013 | ABD | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-07-22 21:57 UTC | 2026-07-23 19:07 UTC | 21h 10m |
| EFY7836 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-07-23 18:38 UTC | 2026-07-23 19:06 UTC | 27m |
| PRCRV | PRC | Campo de Marte Airport (SBMT) | Ubatuba Airport (SDUB) | 2026-07-23 18:41 UTC | 2026-07-23 19:04 UTC | 23m |
| N62923 |  | Manistee County/Blacker Airport (KMBL) | Frankfort Dow Memorial Field (KFKS) | 2026-07-23 17:49 UTC | 2026-07-23 19:04 UTC | 1h 15m |
| N383TA |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-07-23 18:22 UTC | 2026-07-23 19:02 UTC | 40m |
| SNAKE1 | SNA | Dave Eby Field (4XA5) | 98OL (98OL) | 2026-07-23 18:34 UTC | 2026-07-23 19:01 UTC | 27m |
| N393CW |  | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-07-23 11:45 UTC | 2026-07-23 19:01 UTC | 7h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
