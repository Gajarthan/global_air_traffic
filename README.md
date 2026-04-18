# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_09:39:30_UTC-green)

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

**Latest saved flight:** 2026-04-18 09:39:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 09:39:30 UTC

- **40,882** saved flights
- **17,343** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,882** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **492,232.7 tonnes** estimated CO2 emissions
- **28,535,227 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1712 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 1004 |
| 4 | EJA | 712 |
| 5 | American Airlines | 681 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 427 |
| 9 | Vueling | 410 |
| 10 | LATAM Airlines | 400 |
| 11 | Lufthansa | 391 |
| 12 | All Nippon Airways | 369 |
| 13 | AZU | 362 |
| 14 | Delta Air Lines | 348 |
| 15 | QLK | 341 |
| 16 | LXJ | 325 |
| 17 | WIF | 318 |
| 18 | Swiss International | 309 |
| 19 | Alaska Airlines | 277 |
| 20 | AEE | 273 |
| 21 | EJU | 268 |
| 22 | easyJet | 266 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 255 |
| 25 | Air France | 233 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | AXB | 211 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32302 |
| 2 | 🇮🇳 IN | 3069 |
| 3 | 🇪🇸 ES | 3012 |
| 4 | 🇦🇺 AU | 2904 |
| 5 | 🇧🇷 BR | 2411 |
| 6 | 🇯🇵 JP | 2251 |
| 7 | 🇮🇹 IT | 2129 |
| 8 | 🇩🇪 DE | 2043 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1657 |
| 12 | 🇫🇷 FR | 1563 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1233 |
| 15 | 🇨🇭 CH | 1116 |
| 16 | 🇲🇾 MY | 1037 |
| 17 | 🇳🇴 NO | 1011 |
| 18 | 🇿🇦 ZA | 845 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 750 |
| 21 | 🇹🇭 TH | 729 |
| 22 | 🇹🇷 TR | 708 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 672 |
| 25 | 🇵🇱 PL | 630 |
| 26 | 🇲🇦 MA | 501 |
| 27 | 🇳🇱 NL | 416 |
| 28 | 🇲🇪 ME | 413 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 378 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 769 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 678 |
| 5 | Indira Gandhi International Airport |  | IN | 661 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 612 |
| 7 | Harry Reid International Airport |  | US | 531 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 491 |
| 11 | Kuala Lumpur International Airport |  | MY | 407 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 391 |
| 16 | Macau International Airport |  | MO | 373 |
| 17 | Madrid Barajas International Airport |  | ES | 369 |
| 18 | Bengaluru International Airport |  | IN | 362 |
| 19 | Charlotte/Douglas International Airport |  | US | 358 |
| 20 | Tenerife Norte Airport |  | ES | 358 |
| 21 | Frankfurt am Main International Airport |  | DE | 356 |
| 22 | Congonhas Airport |  | BR | 353 |
| 23 | Ninoy Aquino International Airport |  | PH | 348 |
| 24 | Malpensa International Airport |  | IT | 330 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 306 |
| 28 | Charles de Gaulle International Airport |  | FR | 302 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 295 |
| 30 | Vitoria/Foronda Airport |  | ES | 285 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 281 |
| 33 | Reno/Tahoe International Airport |  | US | 280 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | O. R. Tambo International Airport |  | ZA | 272 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 271 |
| 37 | Barcelona International Airport |  | ES | 261 |
| 38 | Viracopos International Airport |  | BR | 248 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Seattle-Tacoma International Airport |  | US | 242 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 193 | 1h 7m | 706 km | 2,349.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 122 | 28m | 304 km | 639.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 118 | 1h 27m | 910 km | 1,851.7 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 109 | 21m | 244 km | 459.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 109 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 108 | 19m | 165 km | 307.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 96 | 26m | 275 km | 454.9 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 89 | 54m | 546 km | 837.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 84 | 44m | 452 km | 654.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 74 | 31m | 369 km | 471.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 66 | 20m | 250 km | 285.1 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 64 | 20m | 147 km | 162.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHNCJ | FHN | Brienne-le-Chateau Airport (LFFN) | Brienne-le-Chateau Airport (LFFN) | 2026-04-18 09:29 UTC | 2026-04-18 09:39 UTC | 10m |
| YLXTA | YLX | Adazi Airfield (EVAD) | Adazi Airfield (EVAD) | 2026-04-18 09:17 UTC | 2026-04-18 09:28 UTC | 10m |
| RYR442N | Ryanair | Bari / Palese International Airport (LIBD) | Bari / Palese International Airport (LIBD) | 2026-04-18 09:17 UTC | 2026-04-18 09:27 UTC | 10m |
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | LSMF (LSMF) | 2026-04-18 08:55 UTC | 2026-04-18 09:08 UTC | 12m |
| SAMU69 | SAM | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Lyon-Bron Airport (LFLY) | 2026-04-18 08:46 UTC | 2026-04-18 09:07 UTC | 21m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-18 08:52 UTC | 2026-04-18 09:04 UTC | 12m |
| RYR442N | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Bari / Palese International Airport (LIBD) | 2026-04-18 07:47 UTC | 2026-04-18 09:03 UTC | 1h 15m |
| OYPIF | OYP | Ringsted Airport (EKRS) | Ringsted Airport (EKRS) | 2026-04-18 08:46 UTC | 2026-04-18 08:55 UTC | 8m |
| EJU85EA | EJU | Bordeaux-Merignac (BA 106) Airport (LFBD) | Madeira Airport (LPMA) | 2026-04-18 06:03 UTC | 2026-04-18 08:53 UTC | 2h 50m |
| PHMSD | PHM | Stadtlohn-Vreden Airport (EDLS) | Stadtlohn-Vreden Airport (EDLS) | 2026-04-18 08:26 UTC | 2026-04-18 08:53 UTC | 26m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-18 08:38 UTC | 2026-04-18 08:51 UTC | 13m |
| GTROW | GTR | Gloucestershire Airport (EGBJ) | Ledbury Airport (EG34) | 2026-04-18 08:32 UTC | 2026-04-18 08:51 UTC | 18m |
| RYR3TT | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-18 07:16 UTC | 2026-04-18 08:47 UTC | 1h 30m |
| VOE1SA | VOE | Malaga Airport (LEMG) | Vitoria/Foronda Airport (LEVT) | 2026-04-18 07:45 UTC | 2026-04-18 08:44 UTC | 58m |
| FHNCJ | FHN | Brienne-le-Chateau Airport (LFFN) | Brienne-le-Chateau Airport (LFFN) | 2026-04-18 08:11 UTC | 2026-04-18 08:41 UTC | 29m |
| AXM429 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-18 08:18 UTC | 2026-04-18 08:40 UTC | 22m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-04-18 08:18 UTC | 2026-04-18 08:37 UTC | 19m |
| VOE8DL | VOE | Valencia Airport (LEVC) | La Morgal Airport (LEMR) | 2026-04-18 07:39 UTC | 2026-04-18 08:37 UTC | 58m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-18 08:09 UTC | 2026-04-18 08:36 UTC | 26m |
| AXB1035 | AXB | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-04-18 06:51 UTC | 2026-04-18 08:35 UTC | 1h 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
