# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_17:37:12_UTC-green)

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

**Latest saved flight:** 2026-04-03 17:37:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 17:37:12 UTC

- **13,847** saved flights
- **7,682** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,847** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **171,890.9 tonnes** estimated CO2 emissions
- **9,964,692 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 578 |
| 2 | Ryanair | 532 |
| 3 | IndiGo | 399 |
| 4 | EJA | 271 |
| 5 | American Airlines | 248 |
| 6 | Lufthansa | 208 |
| 7 | Southwest Airlines | 195 |
| 8 | ENY | 178 |
| 9 | Vueling | 150 |
| 10 | LATAM Airlines | 143 |
| 11 | AXM | 142 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 122 |
| 15 | Delta Air Lines | 107 |
| 16 | Swiss International | 107 |
| 17 | AZU | 104 |
| 18 | VIV | 100 |
| 19 | WIF | 97 |
| 20 | Japan Airlines | 89 |
| 21 | Alaska Airlines | 88 |
| 22 | AXB | 88 |
| 23 | easyJet | 87 |
| 24 | AEE | 85 |
| 25 | Cathay Pacific | 85 |
| 26 | United Airlines | 85 |
| 27 | EJU | 83 |
| 28 | EDV | 82 |
| 29 | GLO | 82 |
| 30 | BRC | 78 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10964 |
| 2 | 🇮🇳 IN | 1214 |
| 3 | 🇦🇺 AU | 1082 |
| 4 | 🇪🇸 ES | 1075 |
| 5 | 🇧🇷 BR | 803 |
| 6 | 🇩🇪 DE | 744 |
| 7 | 🇯🇵 JP | 727 |
| 8 | 🇨🇴 CO | 646 |
| 9 | 🇨🇦 CA | 636 |
| 10 | 🇮🇹 IT | 608 |
| 11 | 🇬🇧 GB | 537 |
| 12 | 🇫🇷 FR | 482 |
| 13 | 🇲🇽 MX | 481 |
| 14 | 🇬🇷 GR | 379 |
| 15 | 🇨🇭 CH | 364 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 291 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 257 |
| 22 | 🇬🇹 GT | 254 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 194 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇮🇩 ID | 166 |
| 27 | 🇲🇦 MA | 165 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 144 |
| 30 | 🇲🇪 ME | 144 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 331 |
| 2 | Indira Gandhi International Airport |  | IN | 256 |
| 3 | Tokyo International Airport |  | JP | 253 |
| 4 | Denver International Airport |  | US | 243 |
| 5 | El Dorado International Airport |  | CO | 229 |
| 6 | Frankfurt am Main International Airport |  | DE | 196 |
| 7 | Harry Reid International Airport |  | US | 186 |
| 8 | La Aurora Airport |  | GT | 176 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 175 |
| 10 | Zurich Airport |  | CH | 169 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Macau International Airport |  | MO | 157 |
| 13 | Guaymaral Airport |  | CO | 155 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 151 |
| 15 | Bengaluru International Airport |  | IN | 138 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 131 |
| 17 | Chicago O'Hare International Airport |  | US | 130 |
| 18 | Congonhas Airport |  | BR | 128 |
| 19 | Charlotte/Douglas International Airport |  | US | 124 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 121 |
| 21 | Ninoy Aquino International Airport |  | PH | 121 |
| 22 | Madrid Barajas International Airport |  | ES | 119 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Tenerife Norte Airport |  | ES | 112 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 109 |
| 26 | Vitoria/Foronda Airport |  | ES | 106 |
| 27 | Charles de Gaulle International Airport |  | FR | 103 |
| 28 | Salt Lake City International Airport |  | US | 103 |
| 29 | Reno/Tahoe International Airport |  | US | 101 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 101 |
| 31 | Daniel K Inouye International Airport |  | US | 99 |
| 32 | Malpensa International Airport |  | IT | 98 |
| 33 | Barcelona International Airport |  | ES | 95 |
| 34 | Pune Airport |  | IN | 94 |
| 35 | Austin-Bergstrom International Airport |  | US | 89 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 87 |
| 37 | Gimpo International Airport |  | KR | 86 |
| 38 | Seattle-Tacoma International Airport |  | US | 86 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 86 |
| 40 | Amsterdam Airport Schiphol |  | NL | 85 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 63 | 14m | 114 km | 123.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 42 | 1h 46m | 1,156 km | 837.9 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 35 | 22m | 99 km | 60.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 33 | 15m | 206 km | 117.3 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 33 | 26m | 152 km | 86.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 32 | 28m | 275 km | 151.6 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 30 | 53m | 556 km | 287.6 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 28 | 1h 55m | 1,304 km | 629.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 25 | 9m | - | - |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 24 | 1h 0m | 723 km | 299.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 19 | 30m | 213 km | 69.8 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 19 | 17m | 183 km | 59.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N57HR |  | Loxahatchee Airport (7FD6) | North Perry Airport (KHWO) | 2026-04-03 17:19 UTC | 2026-04-03 17:37 UTC | 17m |
| N70275 |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-04-03 16:45 UTC | 2026-04-03 17:24 UTC | 38m |
| N322MR |  | K5T6 (K5T6) | Andrews County Airport (KE11) | 2026-04-03 16:20 UTC | 2026-04-03 17:20 UTC | 1h 0m |
| REH050 | REH | Rogers Field (KO05) | Likely Airport (9CL3) | 2026-04-03 17:03 UTC | 2026-04-03 17:19 UTC | 16m |
| N2930X |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-04-03 15:52 UTC | 2026-04-03 17:15 UTC | 1h 23m |
| TOPCT26 | TOP | Offutt Afb Airport (KOFF) | Hunt Field (SD47) | 2026-04-03 16:26 UTC | 2026-04-03 17:14 UTC | 48m |
| MNL99 | MNL | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-04-03 16:33 UTC | 2026-04-03 17:10 UTC | 37m |
| N33DY |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-03 17:05 UTC | 2026-04-03 17:10 UTC | 4m |
| N110VU |  | Outlaw Field (KCKV) | Denney Airport (11TN) | 2026-04-03 16:59 UTC | 2026-04-03 17:09 UTC | 10m |
| N325PL |  | Statesville Regional Airport (KSVH) | Stag Air Park (7NC1) | 2026-04-03 15:05 UTC | 2026-04-03 17:00 UTC | 1h 54m |
| N881AC |  | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-03 16:44 UTC | 2026-04-03 16:59 UTC | 15m |
| DFEEL | DFE | Munich International Airport (EDDM) | Raron Airport (LSTA) | 2026-04-03 16:07 UTC | 2026-04-03 16:59 UTC | 51m |
| RYR9AH | Ryanair | Birmingham International Airport (EGBB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-03 15:08 UTC | 2026-04-03 16:58 UTC | 1h 49m |
| N76AW |  | Spokane International Airport (KGEG) | Quail Field (OG42) | 2026-04-03 15:38 UTC | 2026-04-03 16:57 UTC | 1h 18m |
| BRCAT04 | BRC | 81NM (81NM) | Skeen Ranch Airport (82NM) | 2026-04-03 16:32 UTC | 2026-04-03 16:54 UTC | 22m |
| TGARO | TGA | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-03 16:16 UTC | 2026-04-03 16:53 UTC | 36m |
| SLOW13 | SLO | 75OK (75OK) | Flying G Ranch Airport (3OK8) | 2026-04-03 16:24 UTC | 2026-04-03 16:51 UTC | 26m |
| RYR442N | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Bari / Palese International Airport (LIBD) | 2026-04-03 15:37 UTC | 2026-04-03 16:49 UTC | 1h 11m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-03 16:36 UTC | 2026-04-03 16:48 UTC | 11m |
| VADER82 | VAD | Smith-Stewart Field (79OH) | Albany Municipal Airport (KT23) | 2026-04-03 12:51 UTC | 2026-04-03 16:48 UTC | 3h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
