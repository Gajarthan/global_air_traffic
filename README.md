# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_07:45:45_UTC-green)

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

**Latest saved flight:** 2026-04-07 07:45:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 07:45:45 UTC

- **21,414** saved flights
- **10,607** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,414** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **267,801.5 tonnes** estimated CO2 emissions
- **15,524,725 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 886 |
| 3 | IndiGo | 597 |
| 4 | American Airlines | 411 |
| 5 | EJA | 404 |
| 6 | Southwest Airlines | 308 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 265 |
| 9 | Vueling | 227 |
| 10 | LATAM Airlines | 226 |
| 11 | AXM | 205 |
| 12 | Delta Air Lines | 189 |
| 13 | LXJ | 186 |
| 14 | All Nippon Airways | 182 |
| 15 | QLK | 179 |
| 16 | AZU | 169 |
| 17 | Swiss International | 158 |
| 18 | VIV | 157 |
| 19 | Alaska Airlines | 147 |
| 20 | easyJet | 143 |
| 21 | United Airlines | 143 |
| 22 | Japan Airlines | 140 |
| 23 | Avianca | 139 |
| 24 | EJU | 137 |
| 25 | AEE | 134 |
| 26 | WIF | 131 |
| 27 | EDV | 127 |
| 28 | AXB | 122 |
| 29 | Air France | 112 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16955 |
| 2 | 🇮🇳 IN | 1817 |
| 3 | 🇪🇸 ES | 1677 |
| 4 | 🇦🇺 AU | 1519 |
| 5 | 🇧🇷 BR | 1231 |
| 6 | 🇨🇴 CO | 1175 |
| 7 | 🇯🇵 JP | 1143 |
| 8 | 🇮🇹 IT | 1053 |
| 9 | 🇩🇪 DE | 1038 |
| 10 | 🇨🇦 CA | 960 |
| 11 | 🇬🇧 GB | 830 |
| 12 | 🇫🇷 FR | 773 |
| 13 | 🇲🇽 MX | 727 |
| 14 | 🇬🇷 GR | 597 |
| 15 | 🇨🇭 CH | 575 |
| 16 | 🇲🇾 MY | 481 |
| 17 | 🇿🇦 ZA | 468 |
| 18 | 🇬🇹 GT | 464 |
| 19 | 🇳🇴 NO | 443 |
| 20 | 🇳🇿 NZ | 440 |
| 21 | 🇹🇷 TR | 417 |
| 22 | 🇵🇭 PH | 406 |
| 23 | 🇰🇷 KR | 369 |
| 24 | 🇹🇭 TH | 318 |
| 25 | 🇵🇱 PL | 313 |
| 26 | 🇲🇦 MA | 260 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇮🇩 ID | 223 |
| 29 | 🇲🇪 ME | 222 |
| 30 | 🇳🇱 NL | 210 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Denver International Airport |  | US | 393 |
| 4 | Tokyo International Airport |  | JP | 391 |
| 5 | Indira Gandhi International Airport |  | IN | 373 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 284 |
| 8 | Harry Reid International Airport |  | US | 283 |
| 9 | Zurich Airport |  | CH | 260 |
| 10 | Frankfurt am Main International Airport |  | DE | 238 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 232 |
| 12 | Chicago O'Hare International Airport |  | US | 232 |
| 13 | Guaymaral Airport |  | CO | 230 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 229 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 216 |
| 16 | Charlotte/Douglas International Airport |  | US | 208 |
| 17 | Bengaluru International Airport |  | IN | 206 |
| 18 | Macau International Airport |  | MO | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 196 |
| 20 | Tenerife Norte Airport |  | ES | 193 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 191 |
| 22 | Ninoy Aquino International Airport |  | PH | 186 |
| 23 | Congonhas Airport |  | BR | 181 |
| 24 | Salt Lake City International Airport |  | US | 170 |
| 25 | Daniel K Inouye International Airport |  | US | 168 |
| 26 | Reno/Tahoe International Airport |  | US | 168 |
| 27 | Kuala Lumpur International Airport |  | MY | 168 |
| 28 | Malpensa International Airport |  | IT | 166 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 160 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 159 |
| 31 | Charles de Gaulle International Airport |  | FR | 155 |
| 32 | Miami International Airport |  | US | 153 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 146 |
| 35 | Vitoria/Foronda Airport |  | ES | 146 |
| 36 | O. R. Tambo International Airport |  | ZA | 144 |
| 37 | Pune Airport |  | IN | 142 |
| 38 | Barcelona International Airport |  | ES | 141 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 137 |
| 40 | Seattle-Tacoma International Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 98 | 1h 8m | 706 km | 1,193.2 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 73 | 28m | 304 km | 382.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 62 | 1h 27m | 910 km | 972.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 61 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 48 | 19m | 165 km | 136.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 47 | 1h 13m | 770 km | 624.4 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 45 | 23m | 252 km | 195.4 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 44 | 55m | 546 km | 414.3 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 40 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 40 | 20m | 250 km | 172.8 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 37 | 46m | 452 km | 288.4 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DRAGO64 | DRA | Pau Pyrenees Airport (LFBP) | Peyresourde Balestas Airport (LFIP) | 2026-04-07 07:23 UTC | 2026-04-07 07:45 UTC | 21m |
| DLA3PH | DLA | Frankfurt am Main International Airport (EDDF) | London City Airport (EGLC) | 2026-04-07 06:21 UTC | 2026-04-07 07:31 UTC | 1h 10m |
| CTM1105 | CTM | Villacoublay-Velizy (BA 107) Air Base (LFPV) | Limoges Airport (LFBL) | 2026-04-07 06:47 UTC | 2026-04-07 07:19 UTC | 31m |
| LOT52P | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Letnany Airport (LKLT) | 2026-04-07 06:13 UTC | 2026-04-07 07:15 UTC | 1h 2m |
| RYR5CN | Ryanair | Bari / Palese International Airport (LIBD) | Malpensa International Airport (LIMC) | 2026-04-07 05:57 UTC | 2026-04-07 07:15 UTC | 1h 18m |
| AM213 |  | Taree Airport (YTRE) | Bathurst Airport (YBTH) | 2026-04-07 06:40 UTC | 2026-04-07 07:15 UTC | 34m |
| BAW57K | British Airways | London Heathrow Airport (EGLL) | Vereeniging Airport (FAVV) | 2026-04-06 20:54 UTC | 2026-04-07 07:12 UTC | 10h 17m |
| AEE6400 | AEE | Eleftherios Venizelos International Airport (LGAV) | Limnos Airport (LGLM) | 2026-04-07 06:05 UTC | 2026-04-07 07:10 UTC | 1h 4m |
| WP4 |  | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-07 07:05 UTC | 2026-04-07 07:09 UTC | 4m |
| AIQ510 | AIQ | Don Mueang International Airport (VTBD) | Kluang Airport (WMAP) | 2026-04-07 05:15 UTC | 2026-04-07 07:07 UTC | 1h 52m |
| NAY4BX | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-07 06:47 UTC | 2026-04-07 06:59 UTC | 11m |
| HBFEM | HBF | LSMF (LSMF) | Meribel Airport (LFKX) | 2026-04-07 06:18 UTC | 2026-04-07 06:58 UTC | 39m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-07 06:35 UTC | 2026-04-07 06:57 UTC | 22m |
| SKYHWK2 | SKY | Nordholz Airport (ETMN) | Spangdahlem Air Base (ETAD) | 2026-04-07 06:19 UTC | 2026-04-07 06:57 UTC | 37m |
| RYR82SQ | Ryanair | Niederrhein Airport (EDLV) | Ifrane Airport (GMFI) | 2026-04-07 04:06 UTC | 2026-04-07 06:55 UTC | 2h 48m |
| AEE151 | AEE | Alexander the Great International Airport (LGKV) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-07 05:48 UTC | 2026-04-07 06:52 UTC | 1h 3m |
| EJU43CD | EJU | Berlin Brandenburg Airport (EDDB) | Niksic Airport (LYNK) | 2026-04-07 05:26 UTC | 2026-04-07 06:50 UTC | 1h 24m |
| TKJ5UH | TKJ | Samsun Carsamba Airport (LTFH) | Gaziemir Airport (LTBK) | 2026-04-07 00:09 UTC | 2026-04-07 06:50 UTC | 6h 41m |
| SOR400 | SOR | Quatro De Fevereiro Airport (FNLU) | Soyo Airport (FNSO) | 2026-04-07 06:09 UTC | 2026-04-07 06:49 UTC | 40m |
| AFR1212 | Air France | Charles de Gaulle International Airport (LFPG) | Linate Airport (LIML) | 2026-04-07 05:43 UTC | 2026-04-07 06:48 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
