# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_07:16:33_UTC-green)

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

**Latest saved flight:** 2026-04-05 07:16:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 07:16:33 UTC

- **17,396** saved flights
- **9,060** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,396** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **218,667.5 tonnes** estimated CO2 emissions
- **12,676,376 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 695 |
| 3 | IndiGo | 494 |
| 4 | EJA | 328 |
| 5 | American Airlines | 322 |
| 6 | Southwest Airlines | 247 |
| 7 | Lufthansa | 243 |
| 8 | ENY | 234 |
| 9 | Vueling | 194 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 170 |
| 12 | QLK | 151 |
| 13 | Delta Air Lines | 150 |
| 14 | All Nippon Airways | 149 |
| 15 | LXJ | 149 |
| 16 | AZU | 131 |
| 17 | VIV | 131 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 123 |
| 20 | United Airlines | 116 |
| 21 | Japan Airlines | 115 |
| 22 | Avianca | 113 |
| 23 | EJU | 109 |
| 24 | EDV | 108 |
| 25 | AEE | 107 |
| 26 | easyJet | 107 |
| 27 | AXB | 105 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | Cathay Pacific | 99 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13899 |
| 2 | 🇮🇳 IN | 1506 |
| 3 | 🇪🇸 ES | 1425 |
| 4 | 🇦🇺 AU | 1278 |
| 5 | 🇧🇷 BR | 1000 |
| 6 | 🇯🇵 JP | 918 |
| 7 | 🇨🇴 CO | 905 |
| 8 | 🇩🇪 DE | 885 |
| 9 | 🇮🇹 IT | 795 |
| 10 | 🇨🇦 CA | 780 |
| 11 | 🇬🇧 GB | 664 |
| 12 | 🇫🇷 FR | 612 |
| 13 | 🇲🇽 MX | 608 |
| 14 | 🇬🇷 GR | 468 |
| 15 | 🇨🇭 CH | 448 |
| 16 | 🇳🇿 NZ | 394 |
| 17 | 🇲🇾 MY | 390 |
| 18 | 🇿🇦 ZA | 358 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇬🇹 GT | 337 |
| 21 | 🇵🇭 PH | 336 |
| 22 | 🇹🇷 TR | 316 |
| 23 | 🇰🇷 KR | 308 |
| 24 | 🇹🇭 TH | 243 |
| 25 | 🇵🇱 PL | 239 |
| 26 | 🇲🇦 MA | 210 |
| 27 | 🇧🇸 BS | 191 |
| 28 | 🇮🇩 ID | 187 |
| 29 | 🇲🇴 MO | 183 |
| 30 | 🇲🇪 ME | 175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 419 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Denver International Airport |  | US | 327 |
| 4 | Tokyo International Airport |  | JP | 316 |
| 5 | Indira Gandhi International Airport |  | IN | 313 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 232 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 219 |
| 9 | Frankfurt am Main International Airport |  | DE | 217 |
| 10 | Zurich Airport |  | CH | 205 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 186 |
| 13 | Macau International Airport |  | MO | 183 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 168 |
| 18 | Charlotte/Douglas International Airport |  | US | 165 |
| 19 | Madrid Barajas International Airport |  | ES | 163 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 21 | Congonhas Airport |  | BR | 154 |
| 22 | Ninoy Aquino International Airport |  | PH | 153 |
| 23 | Tenerife Norte Airport |  | ES | 150 |
| 24 | Daniel K Inouye International Airport |  | US | 144 |
| 25 | Salt Lake City International Airport |  | US | 142 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 137 |
| 27 | Kuala Lumpur International Airport |  | MY | 136 |
| 28 | Reno/Tahoe International Airport |  | US | 135 |
| 29 | Malpensa International Airport |  | IT | 134 |
| 30 | Vitoria/Foronda Airport |  | ES | 130 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 123 |
| 34 | Barcelona International Airport |  | ES | 122 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | Seattle-Tacoma International Airport |  | US | 114 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 77 | 1h 8m | 706 km | 937.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 65 | 24m | 225 km | 252.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 60 | 29m | 304 km | 314.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 50 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 49 | 1h 27m | 910 km | 768.9 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 43 | 28m | 275 km | 203.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 39 | 19m | 165 km | 110.9 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 38 | 1h 11m | 770 km | 504.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 34 | 54m | 546 km | 320.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 30 | 46m | 452 km | 233.8 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 25 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 29 | 11m | 127 km | 63.5 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| STW135 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-04-05 04:28 UTC | 2026-04-05 07:16 UTC | 2h 48m |
| DLH491 | Lufthansa | Seattle-Tacoma International Airport (KSEA) | Reichelsheim Airport (EDFB) | 2026-04-04 21:29 UTC | 2026-04-05 07:09 UTC | 9h 40m |
| DLH4W | Lufthansa | Charlotte/Douglas International Airport (KCLT) | Dinkelsbuhl-Sinbronn Airport (EDND) | 2026-04-04 23:10 UTC | 2026-04-05 07:09 UTC | 7h 59m |
| DLH753 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Giebelstadt Airport (EDQG) | 2026-04-04 11:32 UTC | 2026-04-05 07:07 UTC | 19h 35m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-05 05:58 UTC | 2026-04-05 07:05 UTC | 1h 7m |
| CTN410 | CTN | Zagreb Airport (LDZA) | Frankfurt am Main International Airport (EDDF) | 2026-04-05 05:41 UTC | 2026-04-05 06:52 UTC | 1h 11m |
| FIN1AB | Finnair | Helsinki Vantaa Airport (EFHK) | Frankfurt am Main International Airport (EDDF) | 2026-04-05 04:37 UTC | 2026-04-05 06:51 UTC | 2h 13m |
| LT612 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-04-05 06:17 UTC | 2026-04-05 06:47 UTC | 30m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-04 19:57 UTC | 2026-04-05 06:45 UTC | 10h 48m |
| ANE30KP | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-04-05 05:56 UTC | 2026-04-05 06:33 UTC | 37m |
| RYR99SH | Ryanair | Palma De Mallorca Airport (LEPA) | Hamburg Airport (EDDH) | 2026-04-05 04:04 UTC | 2026-04-05 06:31 UTC | 2h 27m |
| IBS1651 | IBS | Madrid Barajas International Airport (LEMD) | Son Bonet Airport (LESB) | 2026-04-05 05:30 UTC | 2026-04-05 06:30 UTC | 1h 0m |
| VLG78JW | Vueling | Barcelona International Airport (LEBL) | Son Bonet Airport (LESB) | 2026-04-05 05:56 UTC | 2026-04-05 06:30 UTC | 33m |
| JAL375 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-05 05:13 UTC | 2026-04-05 06:25 UTC | 1h 12m |
| AXM5596 | AXM | Senai International Airport (WMKJ) | Sepulot Airport (WBKO) | 2026-04-05 04:28 UTC | 2026-04-05 06:22 UTC | 1h 53m |
| HBXDA | HBX | Megeve Airport (LFHM) | Raron Airport (LSTA) | 2026-04-05 06:17 UTC | 2026-04-05 06:18 UTC | 0m |
| ANE82BX | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-04-05 05:49 UTC | 2026-04-05 06:17 UTC | 28m |
| IBE05PY | Iberia | Madrid Barajas International Airport (LEMD) | Francisco de Sá Carneiro Airport (LPPR) | 2026-04-05 05:30 UTC | 2026-04-05 06:17 UTC | 47m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-04-05 05:02 UTC | 2026-04-05 06:16 UTC | 1h 14m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-04-05 05:39 UTC | 2026-04-05 06:16 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
