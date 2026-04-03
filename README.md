# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_13:40:08_UTC-green)

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

**Latest saved flight:** 2026-04-03 13:40:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 13:40:08 UTC

- **13,285** saved flights
- **7,408** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,285** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **165,288.5 tonnes** estimated CO2 emissions
- **9,581,945 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 560 |
| 2 | Ryanair | 507 |
| 3 | IndiGo | 383 |
| 4 | EJA | 256 |
| 5 | American Airlines | 237 |
| 6 | Lufthansa | 205 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 142 |
| 10 | AXM | 139 |
| 11 | LATAM Airlines | 135 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 117 |
| 15 | Swiss International | 103 |
| 16 | Delta Air Lines | 102 |
| 17 | AZU | 99 |
| 18 | WIF | 97 |
| 19 | VIV | 96 |
| 20 | Japan Airlines | 88 |
| 21 | Alaska Airlines | 87 |
| 22 | AXB | 87 |
| 23 | Cathay Pacific | 85 |
| 24 | United Airlines | 84 |
| 25 | easyJet | 83 |
| 26 | EJU | 81 |
| 27 | EDV | 78 |
| 28 | AEE | 77 |
| 29 | ANZ | 72 |
| 30 | Avianca | 72 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10430 |
| 2 | 🇮🇳 IN | 1177 |
| 3 | 🇦🇺 AU | 1076 |
| 4 | 🇪🇸 ES | 1022 |
| 5 | 🇧🇷 BR | 745 |
| 6 | 🇯🇵 JP | 721 |
| 7 | 🇩🇪 DE | 721 |
| 8 | 🇨🇴 CO | 631 |
| 9 | 🇨🇦 CA | 610 |
| 10 | 🇮🇹 IT | 586 |
| 11 | 🇬🇧 GB | 508 |
| 12 | 🇲🇽 MX | 467 |
| 13 | 🇫🇷 FR | 461 |
| 14 | 🇬🇷 GR | 357 |
| 15 | 🇨🇭 CH | 348 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 313 |
| 18 | 🇳🇴 NO | 308 |
| 19 | 🇿🇦 ZA | 281 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 243 |
| 22 | 🇬🇹 GT | 238 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 187 |
| 25 | 🇹🇭 TH | 176 |
| 26 | 🇮🇩 ID | 166 |
| 27 | 🇲🇦 MA | 162 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇲🇪 ME | 140 |
| 30 | 🇳🇱 NL | 134 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 253 |
| 3 | Indira Gandhi International Airport |  | IN | 250 |
| 4 | Denver International Airport |  | US | 233 |
| 5 | El Dorado International Airport |  | CO | 222 |
| 6 | Frankfurt am Main International Airport |  | DE | 194 |
| 7 | Harry Reid International Airport |  | US | 182 |
| 8 | La Aurora Airport |  | GT | 165 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 164 |
| 10 | Zurich Airport |  | CH | 162 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Macau International Airport |  | MO | 157 |
| 13 | Guaymaral Airport |  | CO | 154 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Bengaluru International Airport |  | IN | 130 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 121 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 117 |
| 20 | Madrid Barajas International Airport |  | ES | 117 |
| 21 | Congonhas Airport |  | BR | 115 |
| 22 | Charlotte/Douglas International Airport |  | US | 114 |
| 23 | Kuala Lumpur International Airport |  | MY | 114 |
| 24 | Tenerife Norte Airport |  | ES | 108 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 107 |
| 26 | Vitoria/Foronda Airport |  | ES | 102 |
| 27 | Salt Lake City International Airport |  | US | 98 |
| 28 | Daniel K Inouye International Airport |  | US | 97 |
| 29 | Reno/Tahoe International Airport |  | US | 97 |
| 30 | Charles de Gaulle International Airport |  | FR | 97 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 97 |
| 32 | Malpensa International Airport |  | IT | 96 |
| 33 | Barcelona International Airport |  | ES | 93 |
| 34 | Pune Airport |  | IN | 91 |
| 35 | Gimpo International Airport |  | KR | 86 |
| 36 | Seattle-Tacoma International Airport |  | US | 86 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 38 | Austin-Bergstrom International Airport |  | US | 85 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 40 | Miami International Airport |  | US | 80 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 62 | 14m | 114 km | 121.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 41 | 1h 45m | 1,156 km | 817.9 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 34 | 22m | 99 km | 58.2 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 31 | 28m | 275 km | 146.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 19 | 20m | 250 km | 82.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N738CY |  | Stanton Municipal Airport (K63F) | 9TE3 (9TE3) | 2026-04-03 13:12 UTC | 2026-04-03 13:40 UTC | 27m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-03 13:14 UTC | 2026-04-03 13:32 UTC | 18m |
| DMFVG | DMF | Gunzenhausen-Reutberg Airport (EDMH) | Gunzenhausen-Reutberg Airport (EDMH) | 2026-04-03 13:05 UTC | 2026-04-03 13:30 UTC | 25m |
| JAL809 | Japan Airlines | Narita International Airport (RJAA) | Taipei Songshan Airport (RCSS) | 2026-04-03 10:24 UTC | 2026-04-03 13:30 UTC | 3h 5m |
| ROKT21 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Richton-Perry County Airport (KM59) | 2026-04-03 13:05 UTC | 2026-04-03 13:26 UTC | 20m |
| IBBFI | IBB | Reggio Calabria Airport (LICR) | Reggio Calabria Airport (LICR) | 2026-04-03 13:03 UTC | 2026-04-03 13:23 UTC | 19m |
| WIRE31 | WIR | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-04-03 12:53 UTC | 2026-04-03 13:22 UTC | 28m |
| N368BL |  | Springdale Municipal Airport (KASG) | Morrilton Airport (07AR) | 2026-04-03 12:53 UTC | 2026-04-03 13:11 UTC | 17m |
| NAY187J | NAY | Gran Canaria Airport (GCLP) | La Gomera Airport (GCGM) | 2026-04-03 12:42 UTC | 2026-04-03 13:11 UTC | 28m |
| VIV5030 | VIV | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-03 08:55 UTC | 2026-04-03 13:09 UTC | 4h 13m |
| FHTIL | FHT | Le Luc-Le Cannet Airport (LFMC) | Le Luc-Le Cannet Airport (LFMC) | 2026-04-03 13:06 UTC | 2026-04-03 13:09 UTC | 3m |
| ASP655 | ASP | Montréal / St-Hubert Airport (CYHU) | Montréal (Mirabel) Airport (CYMX) | 2026-04-03 12:53 UTC | 2026-04-03 13:08 UTC | 14m |
| PNC1VL | PNC | John Paul II International Airport Kraków-Balice Airport (EPKK) | Tripolis Airport (LGTP) | 2026-04-03 11:08 UTC | 2026-04-03 13:06 UTC | 1h 57m |
| BB054 |  | Pensacola International Airport (KPNS) | Collier/Pine Barren Airpark (FD89) | 2026-04-03 12:46 UTC | 2026-04-03 13:03 UTC | 16m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-04-03 12:42 UTC | 2026-04-03 13:02 UTC | 19m |
| VIV7332 | VIV | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-03 12:02 UTC | 2026-04-03 13:01 UTC | 59m |
| N370MD |  | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-04-03 12:49 UTC | 2026-04-03 13:01 UTC | 11m |
| CXK404 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-04-03 12:38 UTC | 2026-04-03 13:00 UTC | 22m |
| AUD91 | AUD | Orlando Sanford International Airport (KSFB) | Abaco I Walker C Airport (MYAW) | 2026-04-03 12:06 UTC | 2026-04-03 12:57 UTC | 50m |
| ERU414 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-04-03 12:34 UTC | 2026-04-03 12:55 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
