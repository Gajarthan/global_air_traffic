# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_16:11:15_UTC-green)

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

**Latest saved flight:** 2026-04-04 16:11:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 16:11:15 UTC

- **16,025** saved flights
- **8,551** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,025** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **198,561.6 tonnes** estimated CO2 emissions
- **11,510,816 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 679 |
| 2 | Ryanair | 646 |
| 3 | IndiGo | 468 |
| 4 | EJA | 305 |
| 5 | American Airlines | 285 |
| 6 | Lufthansa | 228 |
| 7 | Southwest Airlines | 228 |
| 8 | ENY | 200 |
| 9 | Vueling | 176 |
| 10 | LATAM Airlines | 171 |
| 11 | AXM | 159 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 135 |
| 15 | Delta Air Lines | 130 |
| 16 | Swiss International | 123 |
| 17 | AZU | 122 |
| 18 | VIV | 116 |
| 19 | EJU | 107 |
| 20 | Japan Airlines | 107 |
| 21 | Alaska Airlines | 104 |
| 22 | Avianca | 104 |
| 23 | WIF | 102 |
| 24 | AEE | 101 |
| 25 | AXB | 100 |
| 26 | United Airlines | 98 |
| 27 | easyJet | 97 |
| 28 | EDV | 94 |
| 29 | BRC | 92 |
| 30 | GLO | 92 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12579 |
| 2 | 🇮🇳 IN | 1426 |
| 3 | 🇪🇸 ES | 1303 |
| 4 | 🇦🇺 AU | 1207 |
| 5 | 🇧🇷 BR | 933 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 839 |
| 8 | 🇨🇴 CO | 812 |
| 9 | 🇮🇹 IT | 730 |
| 10 | 🇨🇦 CA | 705 |
| 11 | 🇬🇧 GB | 624 |
| 12 | 🇫🇷 FR | 588 |
| 13 | 🇲🇽 MX | 540 |
| 14 | 🇬🇷 GR | 447 |
| 15 | 🇨🇭 CH | 431 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 367 |
| 18 | 🇿🇦 ZA | 346 |
| 19 | 🇳🇴 NO | 337 |
| 20 | 🇵🇭 PH | 305 |
| 21 | 🇹🇷 TR | 295 |
| 22 | 🇰🇷 KR | 290 |
| 23 | 🇬🇹 GT | 284 |
| 24 | 🇹🇭 TH | 230 |
| 25 | 🇵🇱 PL | 230 |
| 26 | 🇲🇦 MA | 193 |
| 27 | 🇮🇩 ID | 177 |
| 28 | 🇧🇸 BS | 169 |
| 29 | 🇲🇪 ME | 167 |
| 30 | 🇲🇴 MO | 163 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 377 |
| 2 | El Dorado International Airport |  | CO | 306 |
| 3 | Tokyo International Airport |  | JP | 299 |
| 4 | Indira Gandhi International Airport |  | IN | 293 |
| 5 | Denver International Airport |  | US | 285 |
| 6 | Harry Reid International Airport |  | US | 215 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 210 |
| 8 | Frankfurt am Main International Airport |  | DE | 208 |
| 9 | La Aurora Airport |  | GT | 199 |
| 10 | Zurich Airport |  | CH | 195 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Guaymaral Airport |  | CO | 168 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 14 | Macau International Airport |  | MO | 163 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 158 |
| 16 | Bengaluru International Airport |  | IN | 155 |
| 17 | Chicago O'Hare International Airport |  | US | 150 |
| 18 | Charlotte/Douglas International Airport |  | US | 148 |
| 19 | Congonhas Airport |  | BR | 148 |
| 20 | Madrid Barajas International Airport |  | ES | 146 |
| 21 | Ninoy Aquino International Airport |  | PH | 140 |
| 22 | Tenerife Norte Airport |  | ES | 140 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 139 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 135 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 125 |
| 27 | Reno/Tahoe International Airport |  | US | 124 |
| 28 | Salt Lake City International Airport |  | US | 124 |
| 29 | Daniel K Inouye International Airport |  | US | 123 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 122 |
| 31 | Charles de Gaulle International Airport |  | FR | 120 |
| 32 | Vitoria/Foronda Airport |  | ES | 116 |
| 33 | Barcelona International Airport |  | ES | 113 |
| 34 | Pune Airport |  | IN | 108 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 107 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 106 |
| 37 | Austin-Bergstrom International Airport |  | US | 103 |
| 38 | Gimpo International Airport |  | KR | 101 |
| 39 | O. R. Tambo International Airport |  | ZA | 101 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 100 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 74 | 14m | 114 km | 145.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 64 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 49 | 1h 45m | 1,156 km | 977.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 40 | 26m | 152 km | 104.5 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 39 | 22m | 99 km | 66.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 37 | 28m | 275 km | 175.3 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 35 | 53m | 556 km | 335.5 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 33 | 1h 54m | 1,304 km | 742.4 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 28 | 13m | 99 km | 48.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 27 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 23 | 1h 20m | 961 km | 381.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N750AU |  | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-04-04 15:58 UTC | 2026-04-04 16:11 UTC | 13m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-04 15:47 UTC | 2026-04-04 16:04 UTC | 17m |
| N967SA |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Northeastern Regional Airport (KEDE) | 2026-04-04 15:29 UTC | 2026-04-04 16:03 UTC | 34m |
| N541LP |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-04 15:11 UTC | 2026-04-04 15:59 UTC | 48m |
| N8258N |  | Albert Whitted Airport (KSPG) | Lakeland Linder International Airport (KLAL) | 2026-04-04 15:14 UTC | 2026-04-04 15:58 UTC | 43m |
| N80842 |  | Daniel Field (KDNL) | Aiken Regional Airport (KAIK) | 2026-04-04 15:10 UTC | 2026-04-04 15:58 UTC | 47m |
| BPX251 | BPX | North Perry Airport (KHWO) | North Perry Airport (KHWO) | 2026-04-04 15:45 UTC | 2026-04-04 15:57 UTC | 12m |
| PNC0216 | PNC | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-04-04 15:18 UTC | 2026-04-04 15:51 UTC | 32m |
| VTE875 | VTE | Smyrna Airport (KMQY) | Long Meadow Airstrip (TN65) | 2026-04-04 15:35 UTC | 2026-04-04 15:49 UTC | 13m |
| N8236E |  | Spruce Creek Airport (7FL6) | Orlando Executive Airport (KORL) | 2026-04-04 15:16 UTC | 2026-04-04 15:48 UTC | 31m |
| N911RR |  | Tavernaero Park Airport (FA81) | Miami Executive Airport (KTMB) | 2026-04-04 15:28 UTC | 2026-04-04 15:43 UTC | 15m |
| N22952 |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-04-04 15:22 UTC | 2026-04-04 15:39 UTC | 17m |
| N65474 |  | Angel Fire Airport (KAXX) | Ohkay Owingeh Airport (KE14) | 2026-04-04 15:14 UTC | 2026-04-04 15:37 UTC | 22m |
| N32544 |  | Payson Airport (KPAN) | Cottonwood Airport (KP52) | 2026-04-04 15:18 UTC | 2026-04-04 15:36 UTC | 18m |
| N6026Y |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-04-04 15:24 UTC | 2026-04-04 15:35 UTC | 10m |
| TGPWO | TGP | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 15:13 UTC | 2026-04-04 15:34 UTC | 21m |
| N6338F |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-04-04 14:40 UTC | 2026-04-04 15:32 UTC | 52m |
| N483LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-04 14:32 UTC | 2026-04-04 15:31 UTC | 59m |
| N476LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-04 14:31 UTC | 2026-04-04 15:31 UTC | 1h 0m |
| N625SP |  | Ontario Municipal Airport (KONO) | Ontario Municipal Airport (KONO) | 2026-04-04 15:21 UTC | 2026-04-04 15:30 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
