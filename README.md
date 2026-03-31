# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_23:47:44_UTC-green)

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

**Latest saved flight:** 2026-03-30 23:47:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 23:47:44 UTC

- **5,808** saved flights
- **3,924** unique routes
- **103** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **5,808** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **73,325.0 tonnes** estimated CO2 emissions
- **4,250,724 km** total distance flown
- **872 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 311 |
| 2 | Ryanair | 210 |
| 3 | IndiGo | 142 |
| 4 | EJA | 129 |
| 5 | American Airlines | 119 |
| 6 | Southwest Airlines | 97 |
| 7 | ENY | 93 |
| 8 | Lufthansa | 79 |
| 9 | LATAM Airlines | 67 |
| 10 | AXM | 59 |
| 11 | LXJ | 56 |
| 12 | Vueling | 55 |
| 13 | Delta Air Lines | 54 |
| 14 | United Airlines | 46 |
| 15 | Cathay Pacific | 45 |
| 16 | VIV | 45 |
| 17 | AZU | 43 |
| 18 | WIF | 43 |
| 19 | QLK | 40 |
| 20 | All Nippon Airways | 39 |
| 21 | EDV | 39 |
| 22 | Swiss International | 38 |
| 23 | Japan Airlines | 37 |
| 24 | Alaska Airlines | 35 |
| 25 | Avianca | 35 |
| 26 | AXB | 34 |
| 27 | MXY | 31 |
| 28 | VOE | 31 |
| 29 | EJU | 30 |
| 30 | GLO | 29 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5225 |
| 2 | 🇮🇳 IN | 424 |
| 3 | 🇪🇸 ES | 408 |
| 4 | 🇦🇺 AU | 353 |
| 5 | 🇧🇷 BR | 311 |
| 6 | 🇨🇴 CO | 282 |
| 7 | 🇮🇹 IT | 263 |
| 8 | 🇨🇦 CA | 258 |
| 9 | 🇯🇵 JP | 256 |
| 10 | 🇩🇪 DE | 242 |
| 11 | 🇲🇽 MX | 222 |
| 12 | 🇬🇧 GB | 184 |
| 13 | 🇫🇷 FR | 171 |
| 14 | 🇳🇴 NO | 143 |
| 15 | 🇲🇾 MY | 129 |
| 16 | 🇬🇹 GT | 128 |
| 17 | 🇨🇭 CH | 125 |
| 18 | 🇿🇦 ZA | 123 |
| 19 | 🇬🇷 GR | 117 |
| 20 | 🇵🇭 PH | 115 |
| 21 | 🇳🇿 NZ | 99 |
| 22 | 🇹🇷 TR | 92 |
| 23 | 🇲🇴 MO | 74 |
| 24 | 🇹🇭 TH | 73 |
| 25 | 🇲🇦 MA | 67 |
| 26 | 🇵🇱 PL | 65 |
| 27 | 🇧🇸 BS | 60 |
| 28 | 🇮🇩 ID | 58 |
| 29 | 🇰🇷 KR | 54 |
| 30 | 🇲🇪 ME | 50 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 162 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | El Dorado International Airport |  | CO | 102 |
| 4 | Indira Gandhi International Airport |  | IN | 97 |
| 5 | La Aurora Airport |  | GT | 88 |
| 6 | Tokyo International Airport |  | JP | 86 |
| 7 | Frankfurt am Main International Airport |  | DE | 80 |
| 8 | Chicago O'Hare International Airport |  | US | 75 |
| 9 | Macau International Airport |  | MO | 74 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 73 |
| 11 | Harry Reid International Airport |  | US | 71 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 13 | Zurich Airport |  | CH | 66 |
| 14 | Guaymaral Airport |  | CO | 65 |
| 15 | Tenerife Norte Airport |  | ES | 62 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 57 |
| 17 | Eleftherios Venizelos International Airport |  | GR | 54 |
| 18 | Reno/Tahoe International Airport |  | US | 53 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 52 |
| 20 | Ninoy Aquino International Airport |  | PH | 51 |
| 21 | Charlotte/Douglas International Airport |  | US | 50 |
| 22 | Madrid Barajas International Airport |  | ES | 48 |
| 23 | Salt Lake City International Airport |  | US | 48 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 48 |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 26 | Bengaluru International Airport |  | IN | 47 |
| 27 | Malpensa International Airport |  | IT | 46 |
| 28 | Miami International Airport |  | US | 46 |
| 29 | Kuala Lumpur International Airport |  | MY | 46 |
| 30 | Charles de Gaulle International Airport |  | FR | 45 |
| 31 | Congonhas Airport |  | BR | 45 |
| 32 | Centennial Airport |  | US | 43 |
| 33 | Seattle-Tacoma International Airport |  | US | 42 |
| 34 | O. R. Tambo International Airport |  | ZA | 42 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 41 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 37 | Los Angeles International Airport |  | US | 39 |
| 38 | Austin-Bergstrom International Airport |  | US | 39 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 39 |
| 40 | Vitoria/Foronda Airport |  | ES | 38 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 24 | 24m | 225 km | 93.1 t |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 18 | 1h 7m | 706 km | 219.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 18 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 17 | 26m | 99 km | 29.1 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 15 | 15m | 206 km | 53.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 15 | 1h 50m | 1,156 km | 299.2 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 15 | 1h 41m | 1,423 km | 368.1 t |
| 11 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 14 | 30m | 369 km | 89.1 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 14 | 21m | 165 km | 39.8 t |
| 13 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 14 | 4m | - | - |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 13 | 1h 25m | 910 km | 204.0 t |
| 16 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 12 | 28m | 304 km | 62.9 t |
| 19 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 12 | 29m | 275 km | 56.9 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 11 | 53m | 546 km | 103.6 t |
| 23 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 11 | 1h 10m | 770 km | 146.1 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 11 | 11m | 127 km | 24.1 t |
| 26 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 11 | 8h 6m | 38 km | 7.2 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 11 | 51m | 556 km | 105.4 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |
| 29 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 11 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 10 | 1h 47m | 1,290 km | 222.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY6266 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-03-30 10:59 UTC | 2026-03-30 23:47 UTC | 12h 48m |
| PXT795 | PXT | Monterey Bay Academy Airport (CA66) | Gnoss Field (KDVO) | 2026-03-30 23:15 UTC | 2026-03-30 23:42 UTC | 26m |
| N9542H |  | Cable Airport (KCCB) | Riverside Airport (KRAL) | 2026-03-30 23:06 UTC | 2026-03-30 23:39 UTC | 33m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-03-30 23:07 UTC | 2026-03-30 23:39 UTC | 31m |
| DSU90 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-03-30 22:52 UTC | 2026-03-30 23:29 UTC | 36m |
| N579WA |  | French Valley Airport (KF70) | Riverside Airport (KRAL) | 2026-03-30 23:17 UTC | 2026-03-30 23:28 UTC | 11m |
| LW11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-03-30 21:08 UTC | 2026-03-30 23:24 UTC | 2h 16m |
| KN42 |  | Norfolk Ns (Chambers Field) Airport (KNGU) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-03-30 22:08 UTC | 2026-03-30 23:18 UTC | 1h 10m |
| GRZLY39 | GRZ | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 23CN (23CN) | 2026-03-30 22:59 UTC | 2026-03-30 23:18 UTC | 19m |
| SCU59 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-03-30 23:14 UTC | 2026-03-30 23:15 UTC | 1m |
| N940PT |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-03-30 22:45 UTC | 2026-03-30 23:13 UTC | 28m |
| N951TG |  | Sarasota/Bradenton International Airport (KSRQ) | Peter O Knight Airport (KTPF) | 2026-03-30 22:49 UTC | 2026-03-30 23:09 UTC | 20m |
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 22:40 UTC | 2026-03-30 23:09 UTC | 29m |
| URSA31 | URS | Eielson Afb Airport (PAEI) | Ladd Army Air Field (PAFB) | 2026-03-30 21:41 UTC | 2026-03-30 23:06 UTC | 1h 24m |
| AXM6071 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-03-30 22:42 UTC | 2026-03-30 23:05 UTC | 23m |
| IGO930 | IndiGo | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-30 21:16 UTC | 2026-03-30 23:02 UTC | 1h 46m |
| N421RN |  | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-03-30 22:13 UTC | 2026-03-30 23:01 UTC | 47m |
| UAL345 | United Airlines | Washington Dulles International Airport (KIAD) | Kawaihapai Airfield (PHDH) | 2026-03-30 12:59 UTC | 2026-03-30 23:00 UTC | 10h 1m |
| RDHK705 | RDH | Aberdeen Field (31VA) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-03-30 22:51 UTC | 2026-03-30 23:00 UTC | 9m |
| LYI | LYI | Gold Coast Airport (YBCG) | Lismore Airport (YLIS) | 2026-03-30 22:26 UTC | 2026-03-30 22:59 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
