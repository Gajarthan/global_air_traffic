# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_16:58:43_UTC-green)

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

**Latest saved flight:** 2026-04-17 16:58:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 16:58:43 UTC

- **39,402** saved flights
- **16,889** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **39,402** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **475,259.4 tonnes** estimated CO2 emissions
- **27,551,271 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1660 |
| 2 | SkyWest Airlines | 1525 |
| 3 | IndiGo | 975 |
| 4 | EJA | 674 |
| 5 | American Airlines | 660 |
| 6 | Southwest Airlines | 548 |
| 7 | ENY | 505 |
| 8 | AXM | 413 |
| 9 | Vueling | 394 |
| 10 | LATAM Airlines | 392 |
| 11 | Lufthansa | 386 |
| 12 | All Nippon Airways | 351 |
| 13 | AZU | 348 |
| 14 | Delta Air Lines | 333 |
| 15 | QLK | 327 |
| 16 | WIF | 313 |
| 17 | LXJ | 311 |
| 18 | Swiss International | 300 |
| 19 | AEE | 262 |
| 20 | Alaska Airlines | 260 |
| 21 | easyJet | 259 |
| 22 | EJU | 256 |
| 23 | VIV | 248 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 224 |
| 26 | United Airlines | 214 |
| 27 | EDV | 213 |
| 28 | GLO | 206 |
| 29 | JetBlue | 203 |
| 30 | AIQ | 202 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30986 |
| 2 | 🇮🇳 IN | 2972 |
| 3 | 🇪🇸 ES | 2927 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2325 |
| 6 | 🇯🇵 JP | 2131 |
| 7 | 🇮🇹 IT | 2064 |
| 8 | 🇩🇪 DE | 2002 |
| 9 | 🇨🇦 CA | 1924 |
| 10 | 🇨🇴 CO | 1911 |
| 11 | 🇬🇧 GB | 1621 |
| 12 | 🇫🇷 FR | 1508 |
| 13 | 🇲🇽 MX | 1230 |
| 14 | 🇬🇷 GR | 1192 |
| 15 | 🇨🇭 CH | 1085 |
| 16 | 🇲🇾 MY | 1003 |
| 17 | 🇳🇴 NO | 996 |
| 18 | 🇿🇦 ZA | 823 |
| 19 | 🇳🇿 NZ | 811 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 715 |
| 22 | 🇹🇷 TR | 696 |
| 23 | 🇬🇹 GT | 671 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 618 |
| 26 | 🇲🇦 MA | 487 |
| 27 | 🇳🇱 NL | 402 |
| 28 | 🇲🇪 ME | 393 |
| 29 | 🇧🇸 BS | 384 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 911 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 672 |
| 4 | Denver International Airport |  | US | 653 |
| 5 | Indira Gandhi International Airport |  | IN | 639 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 591 |
| 7 | Harry Reid International Airport |  | US | 511 |
| 8 | Guaymaral Airport |  | CO | 502 |
| 9 | La Aurora Airport |  | GT | 493 |
| 10 | Zurich Airport |  | CH | 475 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 388 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 385 |
| 14 | Chicago O'Hare International Airport |  | US | 380 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 362 |
| 17 | Madrid Barajas International Airport |  | ES | 356 |
| 18 | Tenerife Norte Airport |  | ES | 354 |
| 19 | Charlotte/Douglas International Airport |  | US | 350 |
| 20 | Frankfurt am Main International Airport |  | DE | 350 |
| 21 | Bengaluru International Airport |  | IN | 346 |
| 22 | Congonhas Airport |  | BR | 343 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 319 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 304 |
| 26 | Salt Lake City International Airport |  | US | 300 |
| 27 | Daniel K Inouye International Airport |  | US | 291 |
| 28 | Charles de Gaulle International Airport |  | FR | 291 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 274 |
| 31 | Vitoria/Foronda Airport |  | ES | 269 |
| 32 | Capua Airport |  | IT | 266 |
| 33 | O. R. Tambo International Airport |  | ZA | 264 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 264 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 262 |
| 36 | Reno/Tahoe International Airport |  | US | 259 |
| 37 | Barcelona International Airport |  | ES | 254 |
| 38 | Viracopos International Airport |  | BR | 239 |
| 39 | Don Mueang International Airport |  | TH | 239 |
| 40 | Miami International Airport |  | US | 234 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 201 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 100 | 21m | 244 km | 421.1 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 98 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 91 | 26m | 275 km | 431.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 83 | 21m | 99 km | 142.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 62 | 52m | 556 km | 594.3 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 60 | 26m | 215 km | 222.2 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 60 | 16m | 162 km | 168.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 55 | 1h 20m | 961 km | 911.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N23AU |  | Danville Regional Airport (KDAN) | Danville Regional Airport (KDAN) | 2026-04-17 16:20 UTC | 2026-04-17 16:58 UTC | 38m |
| BURNY07 | BUR | Wichita Valley Airport (KF14) | Mc Neill Ranch Airport (6TE7) | 2026-04-17 16:35 UTC | 2026-04-17 16:58 UTC | 23m |
| N7669G |  | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-04-17 15:53 UTC | 2026-04-17 16:48 UTC | 55m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-17 16:32 UTC | 2026-04-17 16:44 UTC | 12m |
| N32AW |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-04-17 16:20 UTC | 2026-04-17 16:43 UTC | 23m |
| N2353V |  | Caldwell Executive Airport (KEUL) | Lanham Field (04ID) | 2026-04-17 16:23 UTC | 2026-04-17 16:35 UTC | 12m |
| KLM1479 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-17 14:42 UTC | 2026-04-17 16:35 UTC | 1h 52m |
| RTV2M | RTV | Vilar Da Luz Airport (LPVL) | Viseu Airport (LPVZ) | 2026-04-17 16:00 UTC | 2026-04-17 16:32 UTC | 31m |
| ERU944 | ERU | Daytona Beach International Airport (KDAB) | Skinners Wholesale Nursery Airport (16FD) | 2026-04-17 15:54 UTC | 2026-04-17 16:29 UTC | 35m |
| N132TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-17 16:04 UTC | 2026-04-17 16:27 UTC | 22m |
| N626LA |  | Hutchinson Regional Airport (KHUT) | Kinsley Municipal Airport (K33K) | 2026-04-17 16:06 UTC | 2026-04-17 16:26 UTC | 19m |
| TGJFC | TGJ | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-17 16:21 UTC | 2026-04-17 16:25 UTC | 3m |
| RPA4347 | Republic Airways | Toronto Pearson International Airport (CYYZ) | Old Rhinebeck Airport (NY94) | 2026-04-17 15:11 UTC | 2026-04-17 16:22 UTC | 1h 11m |
| RPA4552 | Republic Airways | Toronto Pearson International Airport (CYYZ) | New York Stewart International Airport (KSWF) | 2026-04-17 15:07 UTC | 2026-04-17 16:22 UTC | 1h 15m |
| N479LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-17 15:26 UTC | 2026-04-17 16:21 UTC | 54m |
| RPA4367 | Republic Airways | Philadelphia International Airport (KPHL) | Bulljump Airport (11MA) | 2026-04-17 15:10 UTC | 2026-04-17 16:20 UTC | 1h 10m |
| N60861 |  | Wright Army Air Field (Fort Stewart)/Midcoast Regional Airport (KLHW) | 9GA2 (9GA2) | 2026-04-17 16:07 UTC | 2026-04-17 16:19 UTC | 12m |
| G21277 |  | Brooks Field (8NC6) | Raleigh-Durham International Airport (KRDU) | 2026-04-17 15:58 UTC | 2026-04-17 16:19 UTC | 21m |
| N529NG |  | Erie Municipal Airport (KEIK) | Mesawood Airport (6CO2) | 2026-04-17 15:24 UTC | 2026-04-17 16:18 UTC | 54m |
| N79DH |  | Raleigh-Durham International Airport (KRDU) | Laguardia Airport (KLGA) | 2026-04-17 15:19 UTC | 2026-04-17 16:17 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
