# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_18:03:29_UTC-green)

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

**Latest saved flight:** 2026-08-24 18:03:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 18:03:29 UTC

- **232,785** saved flights
- **71,546** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,785** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,805,142.7 tonnes** estimated CO2 emissions
- **162,616,967 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9343 |
| 2 | SkyWest Airlines | 8232 |
| 3 | EJA | 4511 |
| 4 | IndiGo | 3940 |
| 5 | American Airlines | 3794 |
| 6 | Southwest Airlines | 3584 |
| 7 | Delta Air Lines | 2971 |
| 8 | ENY | 2833 |
| 9 | LATAM Airlines | 2238 |
| 10 | AZU | 2165 |
| 11 | Vueling | 1990 |
| 12 | Lufthansa | 1898 |
| 13 | WIF | 1850 |
| 14 | LXJ | 1833 |
| 15 | easyJet | 1630 |
| 16 | Swiss International | 1560 |
| 17 | AXM | 1551 |
| 18 | EJU | 1489 |
| 19 | United Airlines | 1476 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1398 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1297 |
| 24 | WMT | 1292 |
| 25 | VIV | 1276 |
| 26 | PGT | 1272 |
| 27 | Air France | 1266 |
| 28 | Wizz Air | 1229 |
| 29 | AEE | 1159 |
| 30 | JetBlue | 1158 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193779 |
| 2 | 🇪🇸 ES | 14949 |
| 3 | 🇧🇷 BR | 13596 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12812 |
| 6 | 🇮🇹 IT | 12667 |
| 7 | 🇮🇳 IN | 12275 |
| 8 | 🇩🇪 DE | 11474 |
| 9 | 🇬🇧 GB | 10981 |
| 10 | 🇨🇴 CO | 9722 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9321 |
| 13 | 🇹🇷 TR | 6890 |
| 14 | 🇬🇷 GR | 6852 |
| 15 | 🇲🇽 MX | 6460 |
| 16 | 🇨🇭 CH | 6210 |
| 17 | 🇳🇴 NO | 5759 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3878 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3185 |
| 24 | 🇬🇹 GT | 2923 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2679 |
| 27 | 🇲🇦 MA | 2365 |
| 28 | 🇲🇪 ME | 2146 |
| 29 | 🇳🇱 NL | 2086 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4838 |
| 2 | Denver International Airport |  | US | 3776 |
| 3 | Indira Gandhi International Airport |  | IN | 2840 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2669 |
| 6 | Harry Reid International Airport |  | US | 2501 |
| 7 | Zurich Airport |  | CH | 2431 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2376 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2339 |
| 10 | La Aurora Airport |  | GT | 2226 |
| 11 | El Dorado International Airport |  | CO | 2164 |
| 12 | Chicago O'Hare International Airport |  | US | 2103 |
| 13 | Salt Lake City International Airport |  | US | 2048 |
| 14 | Congonhas Airport |  | BR | 1984 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1962 |
| 16 | Frankfurt am Main International Airport |  | DE | 1859 |
| 17 | Capua Airport |  | IT | 1831 |
| 18 | Madrid Barajas International Airport |  | ES | 1829 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1751 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1725 |
| 21 | Malpensa International Airport |  | IT | 1670 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1619 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1534 |
| 27 | Charlotte/Douglas International Airport |  | US | 1509 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1471 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1419 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1405 |
| 32 | Viracopos International Airport |  | BR | 1384 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1365 |
| 35 | Seattle-Tacoma International Airport |  | US | 1364 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1319 |
| 38 | Oslo Gardermoen Airport |  | NO | 1305 |
| 39 | O. R. Tambo International Airport |  | ZA | 1265 |
| 40 | Vitoria/Foronda Airport |  | ES | 1263 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1083 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 849 | 21m | 244 km | 3,574.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 576 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 520 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 384 | 27m | 275 km | 1,819.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 338 | 44m | 241 km | 1,404.0 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 308 | 24m | 218 km | 1,160.4 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 304 | 1h 38m | 1,156 km | 6,064.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 269 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 265 | 19m | 144 km | 659.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 248 | 1h 50m | 1,304 km | 5,579.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EVIL01 | EVI | 75OK (75OK) | Anthony Municipal Airport (KANY) | 2026-08-24 17:14 UTC | 2026-08-24 18:03 UTC | 48m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-24 15:15 UTC | 2026-08-24 17:58 UTC | 2h 43m |
| FFT2045 | FFT | Harry Reid International Airport (KLAS) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-24 16:53 UTC | 2026-08-24 17:58 UTC | 1h 5m |
| GCGWE | GCG | Glasgow Prestwick Airport (EGPK) | Glasgow Prestwick Airport (EGPK) | 2026-08-24 17:41 UTC | 2026-08-24 17:52 UTC | 10m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 17:39 UTC | 2026-08-24 17:52 UTC | 13m |
| N221FL |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-08-24 16:44 UTC | 2026-08-24 17:52 UTC | 1h 8m |
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-08-24 17:36 UTC | 2026-08-24 17:46 UTC | 10m |
| N80214 |  | Blair Executive Airport (KBTA) | Lincoln Airport (KLNK) | 2026-08-24 17:14 UTC | 2026-08-24 17:46 UTC | 32m |
| PERRIS1 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-08-24 16:56 UTC | 2026-08-24 17:42 UTC | 46m |
| N94505 |  | Jirik Field (OL23) | Ragwing Acres Airport (2OK4) | 2026-08-24 17:10 UTC | 2026-08-24 17:42 UTC | 32m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-24 17:08 UTC | 2026-08-24 17:37 UTC | 28m |
| PGT350Z | PGT | Trabzon International Airport (LTCG) | Yalova Airport (LTBP) | 2026-08-24 16:21 UTC | 2026-08-24 17:36 UTC | 1h 14m |
| N18ZD |  | Cecil Ranch Airport (37CN) | 4Z Ranch Airport (30ID) | 2026-08-24 16:36 UTC | 2026-08-24 17:33 UTC | 56m |
| N207MH |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-24 17:14 UTC | 2026-08-24 17:31 UTC | 16m |
| N451DS |  | Preston Airport (KU10) | Preston Airport (KU10) | 2026-08-24 16:51 UTC | 2026-08-24 17:29 UTC | 38m |
| GRIM61 | GRI | Four Square Ranch Airport (3TA0) | Four Square Ranch Airport (3TA0) | 2026-08-24 17:12 UTC | 2026-08-24 17:29 UTC | 16m |
| GRIM62 | GRI | Pilots Landing Airport (81TE) | TA29 (TA29) | 2026-08-24 17:09 UTC | 2026-08-24 17:29 UTC | 19m |
| AXEL21 | AXE | Robert Gray Army Air Field (KGRK) | Judy Ranch Airport (OK39) | 2026-08-24 16:36 UTC | 2026-08-24 17:28 UTC | 51m |
| OHLCH | OHL | Helsinki Vantaa Airport (EFHK) | EFHF (EFHF) | 2026-08-24 17:00 UTC | 2026-08-24 17:25 UTC | 25m |
| N786TT |  | Chino Airport (KCNO) | Santa Fe Regional Airport (KSAF) | 2026-08-24 15:58 UTC | 2026-08-24 17:23 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
