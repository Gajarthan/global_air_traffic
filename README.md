# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_17:00:57_UTC-green)

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

**Latest saved flight:** 2026-05-19 17:00:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-19 17:00:57 UTC

- **88,165** saved flights
- **31,504** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **88,165** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,091,097.1 tonnes** estimated CO2 emissions
- **63,252,005 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3776 |
| 2 | SkyWest Airlines | 3268 |
| 3 | IndiGo | 1876 |
| 4 | EJA | 1668 |
| 5 | American Airlines | 1353 |
| 6 | Southwest Airlines | 1281 |
| 7 | Lufthansa | 1110 |
| 8 | ENY | 1093 |
| 9 | Delta Air Lines | 966 |
| 10 | Vueling | 842 |
| 11 | LATAM Airlines | 792 |
| 12 | AXM | 786 |
| 13 | WIF | 761 |
| 14 | AZU | 699 |
| 15 | Swiss International | 680 |
| 16 | All Nippon Airways | 669 |
| 17 | LXJ | 646 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 624 |
| 20 | easyJet | 580 |
| 21 | EJU | 568 |
| 22 | Cathay Pacific | 562 |
| 23 | AEE | 547 |
| 24 | VIV | 529 |
| 25 | Air France | 517 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 465 |
| 28 | AXB | 458 |
| 29 | MXY | 451 |
| 30 | AIQ | 431 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72363 |
| 2 | 🇪🇸 ES | 6256 |
| 3 | 🇮🇳 IN | 5877 |
| 4 | 🇦🇺 AU | 5504 |
| 5 | 🇩🇪 DE | 4912 |
| 6 | 🇮🇹 IT | 4890 |
| 7 | 🇧🇷 BR | 4838 |
| 8 | 🇨🇦 CA | 4411 |
| 9 | 🇯🇵 JP | 4344 |
| 10 | 🇬🇧 GB | 3757 |
| 11 | 🇫🇷 FR | 3528 |
| 12 | 🇨🇴 CO | 3007 |
| 13 | 🇲🇽 MX | 2741 |
| 14 | 🇬🇷 GR | 2557 |
| 15 | 🇳🇴 NO | 2447 |
| 16 | 🇨🇭 CH | 2327 |
| 17 | 🇲🇾 MY | 1973 |
| 18 | 🇿🇦 ZA | 1635 |
| 19 | 🇹🇷 TR | 1599 |
| 20 | 🇳🇿 NZ | 1523 |
| 21 | 🇹🇭 TH | 1518 |
| 22 | 🇵🇱 PL | 1468 |
| 23 | 🇰🇷 KR | 1365 |
| 24 | 🇵🇭 PH | 1357 |
| 25 | 🇬🇹 GT | 1327 |
| 26 | 🇲🇴 MO | 1020 |
| 27 | 🇲🇦 MA | 1019 |
| 28 | 🇲🇪 ME | 913 |
| 29 | 🇳🇱 NL | 896 |
| 30 | 🇭🇷 HR | 795 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1938 |
| 2 | Denver International Airport |  | US | 1475 |
| 3 | Tokyo International Airport |  | JP | 1449 |
| 4 | Indira Gandhi International Airport |  | IN | 1266 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1210 |
| 6 | Harry Reid International Airport |  | US | 1124 |
| 7 | Frankfurt am Main International Airport |  | DE | 1119 |
| 8 | Zurich Airport |  | CH | 1050 |
| 9 | Guaymaral Airport |  | CO | 1022 |
| 10 | Macau International Airport |  | MO | 1020 |
| 11 | La Aurora Airport |  | GT | 1008 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 975 |
| 13 | El Dorado International Airport |  | CO | 960 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 895 |
| 15 | Chicago O'Hare International Airport |  | US | 852 |
| 16 | Madrid Barajas International Airport |  | ES | 800 |
| 17 | Kuala Lumpur International Airport |  | MY | 783 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 756 |
| 19 | Capua Airport |  | IT | 745 |
| 20 | Salt Lake City International Airport |  | US | 735 |
| 21 | Malpensa International Airport |  | IT | 721 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 708 |
| 24 | Charles de Gaulle International Airport |  | FR | 687 |
| 25 | Charlotte/Douglas International Airport |  | US | 681 |
| 26 | Congonhas Airport |  | BR | 674 |
| 27 | Daniel K Inouye International Airport |  | US | 647 |
| 28 | Tenerife Norte Airport |  | ES | 646 |
| 29 | Ninoy Aquino International Airport |  | PH | 622 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 597 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 595 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 585 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 35 | Vitoria/Foronda Airport |  | ES | 564 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 554 |
| 37 | Don Mueang International Airport |  | TH | 552 |
| 38 | Amsterdam Airport Schiphol |  | NL | 548 |
| 39 | Calgary International Airport |  | CA | 524 |
| 40 | O. R. Tambo International Airport |  | ZA | 517 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 419 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 329 | 21m | 244 km | 1,385.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 228 | 14m | 114 km | 447.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 225 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 183 | 26m | 275 km | 867.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 129 | 27m | 215 km | 477.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 124 | 23m | 55 km | 117.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 122 | 20m | 250 km | 527.0 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 114 | 18m | 144 km | 283.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 113 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 106 | 1h 41m | 1,156 km | 2,114.7 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N717PK |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-19 15:56 UTC | 2026-05-19 17:00 UTC | 1h 4m |
| N221PG |  | Montgomery County Airpark (KGAI) | Lancaster Airport (KLNS) | 2026-05-19 16:23 UTC | 2026-05-19 16:57 UTC | 34m |
| WJA8912 | WJA | Calgary International Airport (CYYC) | Lethbridge (Mercer Field) (CMF3) | 2026-05-19 16:23 UTC | 2026-05-19 16:51 UTC | 27m |
| DILIA | DIL | Hamburg Airport (EDDH) | Antwerp International Airport (Deurne) (EBAW) | 2026-05-19 15:57 UTC | 2026-05-19 16:50 UTC | 53m |
| N375BL |  | Hinton Field (NC72) | Johnston Regional Airport (KJNX) | 2026-05-19 16:27 UTC | 2026-05-19 16:47 UTC | 19m |
| N45UD |  | Sommerset Strip (AL89) | Columbus Airport (KCSG) | 2026-05-19 16:23 UTC | 2026-05-19 16:45 UTC | 21m |
| ITY602 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | John F Kennedy International Airport (KJFK) | 2026-05-19 07:55 UTC | 2026-05-19 16:45 UTC | 8h 49m |
| N469ER |  | Lakefront Airport (KNEW) | Lakefront Airport (KNEW) | 2026-05-19 15:52 UTC | 2026-05-19 16:39 UTC | 47m |
| OTLDR | OTL | Gunnison-Crested Butte Regional Airport (KGUC) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-05-19 16:14 UTC | 2026-05-19 16:38 UTC | 23m |
| N5322A |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-05-19 16:03 UTC | 2026-05-19 16:34 UTC | 31m |
| N221NG |  | Phoenix Sky Harbor International Airport (KPHX) | Cottonwood Airport (KP52) | 2026-05-19 16:11 UTC | 2026-05-19 16:33 UTC | 21m |
| N301MT |  | Fort Lauderdale Executive Airport (KFXE) | Georgetown County Airport (KGGE) | 2026-05-19 15:22 UTC | 2026-05-19 16:33 UTC | 1h 10m |
| FFP91 | FFP | Sunray Airport (KX43) | Sunray Airport (KX43) | 2026-05-19 16:02 UTC | 2026-05-19 16:32 UTC | 29m |
| N353CT |  | Montgomery-Gibbs Executive Airport (KMYF) | San Bernardino International Airport (KSBD) | 2026-05-19 15:45 UTC | 2026-05-19 16:29 UTC | 44m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-19 15:10 UTC | 2026-05-19 16:26 UTC | 1h 16m |
| SRB502 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-05-19 14:47 UTC | 2026-05-19 16:26 UTC | 1h 38m |
| RIPPER1 | RIP | Chattanooga Sky Harbor Airport (K92F) | Grandfield Municipal Airport (K1O1) | 2026-05-19 15:59 UTC | 2026-05-19 16:26 UTC | 26m |
| VANDY70 | VAN | Tlc Airport (OK71) | 5TE8 (5TE8) | 2026-05-19 15:54 UTC | 2026-05-19 16:22 UTC | 27m |
| UPS768 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Dallas-Fort Worth International Airport (KDFW) | 2026-05-19 14:08 UTC | 2026-05-19 16:21 UTC | 2h 12m |
| REAPR05 | REA | Flying Tails Airport (SC05) | Sapelo Island Airport (08GA) | 2026-05-19 16:01 UTC | 2026-05-19 16:21 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
