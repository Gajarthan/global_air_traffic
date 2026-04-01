# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_04:05:16_UTC-green)

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

**Latest saved flight:** 2026-04-01 04:05:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 04:05:16 UTC

- **8,064** saved flights
- **5,069** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,064** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **98,699.9 tonnes** estimated CO2 emissions
- **5,721,735 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 389 |
| 2 | Ryanair | 293 |
| 3 | IndiGo | 210 |
| 4 | EJA | 173 |
| 5 | American Airlines | 153 |
| 6 | Southwest Airlines | 134 |
| 7 | ENY | 116 |
| 8 | Lufthansa | 115 |
| 9 | AXM | 86 |
| 10 | Vueling | 82 |
| 11 | LATAM Airlines | 81 |
| 12 | LXJ | 73 |
| 13 | Delta Air Lines | 70 |
| 14 | All Nippon Airways | 66 |
| 15 | QLK | 65 |
| 16 | VIV | 59 |
| 17 | WIF | 59 |
| 18 | AZU | 56 |
| 19 | Alaska Airlines | 55 |
| 20 | Swiss International | 55 |
| 21 | AXB | 54 |
| 22 | United Airlines | 54 |
| 23 | EDV | 53 |
| 24 | Japan Airlines | 52 |
| 25 | BRC | 49 |
| 26 | Cathay Pacific | 48 |
| 27 | Avianca | 46 |
| 28 | easyJet | 43 |
| 29 | EJU | 42 |
| 30 | ANZ | 40 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6994 |
| 2 | 🇮🇳 IN | 635 |
| 3 | 🇦🇺 AU | 608 |
| 4 | 🇪🇸 ES | 588 |
| 5 | 🇧🇷 BR | 398 |
| 6 | 🇨🇦 CA | 385 |
| 7 | 🇯🇵 JP | 384 |
| 8 | 🇩🇪 DE | 383 |
| 9 | 🇨🇴 CO | 380 |
| 10 | 🇮🇹 IT | 346 |
| 11 | 🇲🇽 MX | 302 |
| 12 | 🇬🇧 GB | 266 |
| 13 | 🇫🇷 FR | 228 |
| 14 | 🇳🇴 NO | 198 |
| 15 | 🇲🇾 MY | 192 |
| 16 | 🇳🇿 NZ | 182 |
| 17 | 🇬🇷 GR | 176 |
| 18 | 🇬🇹 GT | 171 |
| 19 | 🇨🇭 CH | 168 |
| 20 | 🇿🇦 ZA | 161 |
| 21 | 🇵🇭 PH | 146 |
| 22 | 🇹🇷 TR | 138 |
| 23 | 🇰🇷 KR | 103 |
| 24 | 🇮🇩 ID | 97 |
| 25 | 🇹🇭 TH | 96 |
| 26 | 🇲🇦 MA | 94 |
| 27 | 🇵🇱 PL | 94 |
| 28 | 🇲🇴 MO | 85 |
| 29 | 🇧🇸 BS | 75 |
| 30 | 🇲🇪 ME | 75 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 199 |
| 2 | Denver International Airport |  | US | 155 |
| 3 | Indira Gandhi International Airport |  | IN | 145 |
| 4 | Tokyo International Airport |  | JP | 138 |
| 5 | El Dorado International Airport |  | CO | 132 |
| 6 | Harry Reid International Airport |  | US | 120 |
| 7 | La Aurora Airport |  | GT | 120 |
| 8 | Frankfurt am Main International Airport |  | DE | 116 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 107 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 90 |
| 11 | Guaymaral Airport |  | CO | 90 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 88 |
| 13 | Zurich Airport |  | CH | 88 |
| 14 | Macau International Airport |  | MO | 85 |
| 15 | Chicago O'Hare International Airport |  | US | 84 |
| 16 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 17 | Reno/Tahoe International Airport |  | US | 77 |
| 18 | Tenerife Norte Airport |  | ES | 75 |
| 19 | Charlotte/Douglas International Airport |  | US | 71 |
| 20 | Kuala Lumpur International Airport |  | MY | 71 |
| 21 | Madrid Barajas International Airport |  | ES | 70 |
| 22 | Bengaluru International Airport |  | IN | 70 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 24 | Ninoy Aquino International Airport |  | PH | 66 |
| 25 | Daniel K Inouye International Airport |  | US | 64 |
| 26 | Salt Lake City International Airport |  | US | 64 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 28 | Malpensa International Airport |  | IT | 59 |
| 29 | Vitoria/Foronda Airport |  | ES | 59 |
| 30 | Seattle-Tacoma International Airport |  | US | 59 |
| 31 | Pune Airport |  | IN | 58 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 58 |
| 33 | Miami International Airport |  | US | 57 |
| 34 | Congonhas Airport |  | BR | 57 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 56 |
| 36 | Charles de Gaulle International Airport |  | FR | 53 |
| 37 | Centennial Airport |  | US | 53 |
| 38 | Austin-Bergstrom International Airport |  | US | 52 |
| 39 | Barcelona International Airport |  | ES | 51 |
| 40 | Vancouver International Airport |  | CA | 50 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 36 | 14m | 114 km | 70.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 35 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 31 | 1h 6m | 706 km | 377.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 31 | 24m | 225 km | 120.3 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 26 | 31m | - | - |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 25 | 1h 45m | 1,156 km | 498.7 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 23 | 23m | 99 km | 39.4 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 22 | 15m | 206 km | 78.2 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 22 | 29m | 304 km | 115.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 21 | 20m | 165 km | 59.7 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 19 | 1h 25m | 910 km | 298.2 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 17 | 53m | 546 km | 160.1 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 17 | 1h 10m | 770 km | 225.8 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 17 | 30m | 369 km | 108.2 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 15 | 1h 0m | 723 km | 187.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 15 | 11m | 127 km | 32.8 t |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 14 | 21m | - | - |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 13 | 13m | 99 km | 22.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YBW | YBW | Clifton Airport (YCFN) | Ballina Byron Gateway Airport (YBNA) | 2026-04-01 03:14 UTC | 2026-04-01 04:05 UTC | 51m |
| LS31 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-01 02:03 UTC | 2026-04-01 03:48 UTC | 1h 44m |
| N756TW |  | Bellingham International Airport (KBLI) | William R Fairchild International Airport (KCLM) | 2026-04-01 03:06 UTC | 2026-04-01 03:41 UTC | 34m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-01 03:27 UTC | 2026-04-01 03:38 UTC | 11m |
| ERU64 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | AZ86 (AZ86) | 2026-04-01 03:24 UTC | 2026-04-01 03:33 UTC | 8m |
| BATT02 | BAT | Davis Monthan Afb Airport (KDMA) | Kimball Farm Service Inc Airport (5XS2) | 2026-04-01 02:17 UTC | 2026-04-01 03:31 UTC | 1h 14m |
| AIH951 | AIH | G 417 Airport (RK34) | Macau International Airport (VMMC) | 2026-03-31 19:53 UTC | 2026-04-01 03:23 UTC | 7h 29m |
| GTI8158 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-31 16:15 UTC | 2026-04-01 03:21 UTC | 11h 5m |
| SWA2555 | Southwest Airlines | Harry Reid International Airport (KLAS) | Silver Springs Airport (KSPZ) | 2026-04-01 02:31 UTC | 2026-04-01 03:20 UTC | 49m |
| POL22 | POL | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-01 02:28 UTC | 2026-04-01 03:20 UTC | 52m |
| AXM1491 | AXM | Tan Son Nhat International Airport (VVTS) | Mersing Airport (WMAU) | 2026-04-01 01:58 UTC | 2026-04-01 03:18 UTC | 1h 20m |
| XTX123H | XTX | Badajoz Airport (LEBZ) | Salamanca Airport (LESA) | 2026-04-01 02:49 UTC | 2026-04-01 03:17 UTC | 27m |
| APG217 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-01 02:52 UTC | 2026-04-01 03:16 UTC | 24m |
| SLI2524 | SLI | Licenciado Benito Juarez International Airport (MMMX) | Minatitlan/Coatzacoalcos National Airport (MMMT) | 2026-04-01 02:24 UTC | 2026-04-01 03:12 UTC | 48m |
| AXM431 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-01 02:52 UTC | 2026-04-01 03:12 UTC | 20m |
| KLM888 | KLM Royal Dutch | Chek Lap Kok International Airport (VHHH) | Amsterdam Airport Schiphol (EHAM) | 2026-03-31 14:32 UTC | 2026-04-01 03:11 UTC | 12h 39m |
| ABB852 | ABB | Brussels Airport (EBBR) | Macau International Airport (VMMC) | 2026-03-31 15:34 UTC | 2026-04-01 03:09 UTC | 11h 35m |
| CWA929 | CWA | Viking Airport (CEE8) | Wetaskiwin Regional Airport (CEX3) | 2026-04-01 02:55 UTC | 2026-04-01 03:09 UTC | 13m |
| AIQ512 | AIQ | Don Mueang International Airport (VTBD) | Mersing Airport (WMAU) | 2026-04-01 01:25 UTC | 2026-04-01 03:08 UTC | 1h 43m |
| ANA375 | All Nippon Airways | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-04-01 02:01 UTC | 2026-04-01 03:06 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
