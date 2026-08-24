# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_13:10:01_UTC-green)

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

**Latest saved flight:** 2026-08-24 13:10:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 13:10:01 UTC

- **231,788** saved flights
- **71,348** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,788** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,795,417.9 tonnes** estimated CO2 emissions
- **162,053,213 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9313 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3929 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3575 |
| 7 | Delta Air Lines | 2958 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2229 |
| 10 | AZU | 2150 |
| 11 | Vueling | 1981 |
| 12 | Lufthansa | 1891 |
| 13 | WIF | 1834 |
| 14 | LXJ | 1825 |
| 15 | easyJet | 1626 |
| 16 | Swiss International | 1552 |
| 17 | AXM | 1551 |
| 18 | EJU | 1485 |
| 19 | QLK | 1474 |
| 20 | United Airlines | 1471 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1385 |
| 23 | GLO | 1291 |
| 24 | WMT | 1280 |
| 25 | VIV | 1272 |
| 26 | PGT | 1267 |
| 27 | Air France | 1260 |
| 28 | Wizz Air | 1222 |
| 29 | AEE | 1155 |
| 30 | JetBlue | 1152 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192907 |
| 2 | 🇪🇸 ES | 14881 |
| 3 | 🇧🇷 BR | 13534 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12765 |
| 6 | 🇮🇹 IT | 12609 |
| 7 | 🇮🇳 IN | 12237 |
| 8 | 🇩🇪 DE | 11428 |
| 9 | 🇬🇧 GB | 10944 |
| 10 | 🇨🇴 CO | 9624 |
| 11 | 🇯🇵 JP | 9445 |
| 12 | 🇫🇷 FR | 9280 |
| 13 | 🇹🇷 TR | 6849 |
| 14 | 🇬🇷 GR | 6827 |
| 15 | 🇲🇽 MX | 6435 |
| 16 | 🇨🇭 CH | 6183 |
| 17 | 🇳🇴 NO | 5718 |
| 18 | 🇲🇾 MY | 4140 |
| 19 | 🇹🇭 TH | 4090 |
| 20 | 🇿🇦 ZA | 4053 |
| 21 | 🇵🇱 PL | 3850 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2905 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2668 |
| 27 | 🇲🇦 MA | 2354 |
| 28 | 🇲🇪 ME | 2130 |
| 29 | 🇳🇱 NL | 2081 |
| 30 | 🇮🇩 ID | 2014 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2830 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2656 |
| 6 | Harry Reid International Airport |  | US | 2494 |
| 7 | Zurich Airport |  | CH | 2423 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2331 |
| 10 | La Aurora Airport |  | GT | 2213 |
| 11 | El Dorado International Airport |  | CO | 2149 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1975 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1851 |
| 17 | Madrid Barajas International Airport |  | ES | 1820 |
| 18 | Capua Airport |  | IT | 1820 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1742 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1720 |
| 21 | Malpensa International Airport |  | IT | 1662 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1656 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1610 |
| 25 | Macau International Airport |  | MO | 1604 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1497 |
| 29 | Barcelona International Airport |  | ES | 1464 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1401 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1391 |
| 32 | Viracopos International Airport |  | BR | 1375 |
| 33 | Bengaluru International Airport |  | IN | 1369 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1337 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1299 |
| 39 | O. R. Tambo International Airport |  | ZA | 1259 |
| 40 | Vitoria/Foronda Airport |  | ES | 1257 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1077 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 846 | 21m | 244 km | 3,562.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 564 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 382 | 27m | 275 km | 1,810.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 358 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 358 | 1h 50m | 1,423 km | 8,785.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 337 | 44m | 241 km | 1,399.8 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 325 | 44m | 555 km | 3,112.0 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 306 | 24m | 218 km | 1,152.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 301 | 1h 38m | 1,156 km | 6,004.8 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 286 | 19m | 99 km | 489.9 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 281 | 27m | 215 km | 1,040.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 267 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 264 | 19m | 144 km | 656.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BLEED71 | BLE | Laughlin Afb Airport (KDLF) | Tularosa Airport (TA31) | 2026-08-24 12:59 UTC | 2026-08-24 13:10 UTC | 10m |
| N2215Y |  | Dekalb-Peachtree Airport (KPDK) | Flying G Ranch Airport (86GA) | 2026-08-24 12:37 UTC | 2026-08-24 13:09 UTC | 32m |
| N80790 |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-24 12:34 UTC | 2026-08-24 13:03 UTC | 28m |
| SAMU691 | SAM | Grenoble Le Versoud Airport (LFLG) | Lyon Brindas Airport (LFKL) | 2026-08-24 12:28 UTC | 2026-08-24 12:55 UTC | 26m |
| N234WL |  | K3C8 (K3C8) | Laguardia Airport (KLGA) | 2026-08-24 12:21 UTC | 2026-08-24 12:54 UTC | 33m |
| AIC4217 | Air India | Juhu Aerodrome (VAJJ) | Al Minhad Air Base (OMDM) | 2026-08-24 10:51 UTC | 2026-08-24 12:50 UTC | 1h 58m |
| N9993E |  | Pratermill Flight Park Airport (GA72) | Pratermill Flight Park Airport (GA72) | 2026-08-24 12:47 UTC | 2026-08-24 12:47 UTC | 0m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-24 12:11 UTC | 2026-08-24 12:47 UTC | 35m |
| N703CD |  | General Mariano Escobedo International Airport (MMMY) | Laredo International Airport (KLRD) | 2026-08-24 12:09 UTC | 2026-08-24 12:43 UTC | 33m |
| N125TN |  | George Bush Intcntl/Houston Airport (KIAH) | Austin-Bergstrom International Airport (KAUS) | 2026-08-24 12:17 UTC | 2026-08-24 12:42 UTC | 25m |
| TRF688 | TRF | North Texas Regional/Perrin Field (KGYI) | Nuggs Flying M Airport (TE68) | 2026-08-24 12:37 UTC | 2026-08-24 12:40 UTC | 2m |
| FTO382 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-24 12:07 UTC | 2026-08-24 12:37 UTC | 29m |
| VOLT14 | VOL | Ramstein Air Base (ETAR) | Saarlouis-Duren Airport (EDRJ) | 2026-08-24 12:15 UTC | 2026-08-24 12:36 UTC | 21m |
| HK5206G |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-24 12:09 UTC | 2026-08-24 12:36 UTC | 26m |
| M28B |  | Barth Airport (EDBH) | Barth Airport (EDBH) | 2026-08-24 12:23 UTC | 2026-08-24 12:36 UTC | 12m |
| HBVCP | HBV | Friedrichshafen Airport (EDNY) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-24 11:46 UTC | 2026-08-24 12:35 UTC | 49m |
| KMI261 | KMI | Abu Dhabi International Airport (OMAA) | Naypyidaw Airport (VYEL) | 2026-08-24 07:25 UTC | 2026-08-24 12:35 UTC | 5h 10m |
| N856FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-08-24 12:02 UTC | 2026-08-24 12:35 UTC | 33m |
| N5315T |  | Taunton Municipal/King Field (KTAN) | Cape Cod Gateway Airport (KHYA) | 2026-08-24 11:52 UTC | 2026-08-24 12:33 UTC | 41m |
| N821SS |  | Newark Liberty International Airport (KEWR) | Laguardia Airport (KLGA) | 2026-08-24 11:01 UTC | 2026-08-24 12:32 UTC | 1h 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
