# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_13:05:11_UTC-green)

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

**Latest saved flight:** 2026-04-19 13:05:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 13:05:11 UTC

- **42,931** saved flights
- **17,948** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,931** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **517,207.5 tonnes** estimated CO2 emissions
- **29,983,046 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1805 |
| 2 | SkyWest Airlines | 1654 |
| 3 | IndiGo | 1061 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 444 |
| 9 | Vueling | 430 |
| 10 | Lufthansa | 426 |
| 11 | LATAM Airlines | 426 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 380 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 354 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 331 |
| 18 | WIF | 329 |
| 19 | AEE | 290 |
| 20 | Alaska Airlines | 290 |
| 21 | EJU | 282 |
| 22 | easyJet | 277 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 242 |
| 26 | United Airlines | 230 |
| 27 | AXB | 228 |
| 28 | JetBlue | 228 |
| 29 | GLO | 225 |
| 30 | AIQ | 221 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33709 |
| 2 | 🇮🇳 IN | 3258 |
| 3 | 🇪🇸 ES | 3155 |
| 4 | 🇦🇺 AU | 3025 |
| 5 | 🇧🇷 BR | 2564 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2241 |
| 8 | 🇩🇪 DE | 2177 |
| 9 | 🇨🇦 CA | 2086 |
| 10 | 🇨🇴 CO | 1976 |
| 11 | 🇬🇧 GB | 1748 |
| 12 | 🇫🇷 FR | 1655 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1321 |
| 15 | 🇨🇭 CH | 1192 |
| 16 | 🇲🇾 MY | 1086 |
| 17 | 🇳🇴 NO | 1050 |
| 18 | 🇿🇦 ZA | 899 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 777 |
| 22 | 🇹🇷 TR | 761 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 685 |
| 26 | 🇲🇦 MA | 536 |
| 27 | 🇲🇪 ME | 450 |
| 28 | 🇳🇱 NL | 441 |
| 29 | 🇮🇩 ID | 400 |
| 30 | 🇧🇸 BS | 398 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | Indira Gandhi International Airport |  | IN | 702 |
| 5 | El Dorado International Airport |  | CO | 692 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 656 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 518 |
| 11 | Kuala Lumpur International Airport |  | MY | 430 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 415 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 411 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 397 |
| 17 | Macau International Airport |  | MO | 394 |
| 18 | Madrid Barajas International Airport |  | ES | 383 |
| 19 | Bengaluru International Airport |  | IN | 383 |
| 20 | Tenerife Norte Airport |  | ES | 374 |
| 21 | Charlotte/Douglas International Airport |  | US | 371 |
| 22 | Ninoy Aquino International Airport |  | PH | 366 |
| 23 | Congonhas Airport |  | BR | 366 |
| 24 | Malpensa International Airport |  | IT | 352 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 322 |
| 28 | Daniel K Inouye International Airport |  | US | 319 |
| 29 | Charles de Gaulle International Airport |  | FR | 316 |
| 30 | Vitoria/Foronda Airport |  | ES | 300 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 299 |
| 32 | Reno/Tahoe International Airport |  | US | 294 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 289 |
| 35 | O. R. Tambo International Airport |  | ZA | 287 |
| 36 | Capua Airport |  | IT | 286 |
| 37 | Barcelona International Airport |  | ES | 276 |
| 38 | Don Mueang International Airport |  | TH | 264 |
| 39 | Viracopos International Airport |  | BR | 263 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 118 | 21m | 244 km | 496.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 116 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 69 | 20m | 147 km | 174.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 64 | 26m | 215 km | 237.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 60 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 30 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6694G |  | Ann Arbor Municipal Airport (KARB) | Lenawee County Airport (KADG) | 2026-04-19 12:39 UTC | 2026-04-19 13:05 UTC | 25m |
| BPX281 | BPX | North Perry Airport (KHWO) | Immokalee Regional Airport (KIMM) | 2026-04-19 12:05 UTC | 2026-04-19 12:59 UTC | 54m |
| N6665G |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-04-19 12:44 UTC | 2026-04-19 12:57 UTC | 13m |
| FJIRZ | FJI | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-04-19 12:24 UTC | 2026-04-19 12:52 UTC | 27m |
| GBILS | GBI | RAF Mona (EGOQ) | RAF Mona (EGOQ) | 2026-04-19 12:51 UTC | 2026-04-19 12:51 UTC | 0m |
| PTXHP | PTX | Sao Joao da Boa Vista Airport (SDJV) | Rachid Saliba Airport (SNRH) | 2026-04-19 12:33 UTC | 2026-04-19 12:50 UTC | 17m |
| ERU319 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-19 12:21 UTC | 2026-04-19 12:50 UTC | 28m |
| CCA1305 | Air China | Shenzhen Bao'an International Airport (ZGSZ) | Guangzhou Baiyun International Airport (ZGGG) | 2026-04-19 05:11 UTC | 2026-04-19 12:49 UTC | 7h 38m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-19 06:17 UTC | 2026-04-19 12:45 UTC | 6h 27m |
| PBD6544 | PBD | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-18 21:00 UTC | 2026-04-19 12:38 UTC | 15h 37m |
| FJO66L | FJO | Linate Airport (LIML) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-19 11:42 UTC | 2026-04-19 12:31 UTC | 49m |
| CMS329 | CMS | Larnaca International Airport (LCLK) | Zhuhai Airport (ZGSD) | 2026-04-18 20:48 UTC | 2026-04-19 12:24 UTC | 15h 35m |
| RYR98FC | Ryanair | Poznań-Ławica Airport (EPPO) | Dubrovnik Airport (LDDU) | 2026-04-19 10:45 UTC | 2026-04-19 12:23 UTC | 1h 38m |
| AIQ4352 | AIQ | Suvarnabhumi Airport (VTBS) | Khon Kaen Airport (VTUK) | 2026-04-19 11:44 UTC | 2026-04-19 12:23 UTC | 38m |
| GPTRK | GPT | City Airport Manchester (EGCB) | EGCA (EGCA) | 2026-04-19 11:58 UTC | 2026-04-19 12:20 UTC | 22m |
| EWG82U | EWG | Eleftherios Venizelos International Airport (LGAV) | Dusseldorf International Airport (EDDL) | 2026-04-19 09:19 UTC | 2026-04-19 12:17 UTC | 2h 58m |
| WMT4DW | WMT | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Paris-Orly Airport (LFPO) | 2026-04-19 10:29 UTC | 2026-04-19 12:16 UTC | 1h 47m |
| EWG4UY | EWG | Dusseldorf International Airport (EDDL) | Olbia / Costa Smeralda Airport (LIEO) | 2026-04-19 10:39 UTC | 2026-04-19 12:15 UTC | 1h 35m |
| PH1469 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-19 11:52 UTC | 2026-04-19 12:15 UTC | 22m |
| SWR8LZ | Swiss International | Zurich Airport (LSZH) | Malpensa International Airport (LIMC) | 2026-04-19 11:35 UTC | 2026-04-19 12:14 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
