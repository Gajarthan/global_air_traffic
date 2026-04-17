# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_20:47:09_UTC-green)

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

**Latest saved flight:** 2026-04-17 20:47:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 20:47:09 UTC

- **40,048** saved flights
- **17,129** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,048** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **481,948.1 tonnes** estimated CO2 emissions
- **27,939,020 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1685 |
| 2 | SkyWest Airlines | 1567 |
| 3 | IndiGo | 978 |
| 4 | EJA | 696 |
| 5 | American Airlines | 674 |
| 6 | Southwest Airlines | 561 |
| 7 | ENY | 516 |
| 8 | AXM | 413 |
| 9 | Vueling | 401 |
| 10 | LATAM Airlines | 396 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 356 |
| 13 | All Nippon Airways | 351 |
| 14 | Delta Air Lines | 341 |
| 15 | QLK | 327 |
| 16 | LXJ | 318 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 267 |
| 20 | AEE | 266 |
| 21 | easyJet | 264 |
| 22 | EJU | 261 |
| 23 | VIV | 256 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 227 |
| 26 | United Airlines | 221 |
| 27 | EDV | 215 |
| 28 | JetBlue | 213 |
| 29 | GLO | 208 |
| 30 | AIQ | 203 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 31738 |
| 2 | 🇮🇳 IN | 2981 |
| 3 | 🇪🇸 ES | 2973 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2376 |
| 6 | 🇯🇵 JP | 2131 |
| 7 | 🇮🇹 IT | 2096 |
| 8 | 🇩🇪 DE | 2016 |
| 9 | 🇨🇦 CA | 1974 |
| 10 | 🇨🇴 CO | 1935 |
| 11 | 🇬🇧 GB | 1638 |
| 12 | 🇫🇷 FR | 1531 |
| 13 | 🇲🇽 MX | 1265 |
| 14 | 🇬🇷 GR | 1201 |
| 15 | 🇨🇭 CH | 1099 |
| 16 | 🇳🇴 NO | 1005 |
| 17 | 🇲🇾 MY | 1003 |
| 18 | 🇿🇦 ZA | 827 |
| 19 | 🇳🇿 NZ | 813 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 716 |
| 22 | 🇹🇷 TR | 705 |
| 23 | 🇬🇹 GT | 680 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 494 |
| 27 | 🇳🇱 NL | 404 |
| 28 | 🇲🇪 ME | 401 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 935 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 679 |
| 4 | Denver International Airport |  | US | 666 |
| 5 | Indira Gandhi International Airport |  | IN | 641 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 598 |
| 7 | Harry Reid International Airport |  | US | 517 |
| 8 | Guaymaral Airport |  | CO | 515 |
| 9 | La Aurora Airport |  | GT | 500 |
| 10 | Zurich Airport |  | CH | 484 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 394 |
| 12 | Kuala Lumpur International Airport |  | MY | 394 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 393 |
| 14 | Chicago O'Hare International Airport |  | US | 390 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 364 |
| 17 | Madrid Barajas International Airport |  | ES | 361 |
| 18 | Charlotte/Douglas International Airport |  | US | 357 |
| 19 | Tenerife Norte Airport |  | ES | 356 |
| 20 | Frankfurt am Main International Airport |  | DE | 350 |
| 21 | Bengaluru International Airport |  | IN | 348 |
| 22 | Congonhas Airport |  | BR | 347 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 325 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 312 |
| 26 | Salt Lake City International Airport |  | US | 310 |
| 27 | Daniel K Inouye International Airport |  | US | 297 |
| 28 | Charles de Gaulle International Airport |  | FR | 294 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 277 |
| 31 | Vitoria/Foronda Airport |  | ES | 276 |
| 32 | Capua Airport |  | IT | 274 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 272 |
| 34 | Reno/Tahoe International Airport |  | US | 271 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Viracopos International Airport |  | BR | 245 |
| 39 | Calgary International Airport |  | CA | 240 |
| 40 | Don Mueang International Airport |  | TH | 240 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 159 | 14m | 114 km | 311.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 104 | 21m | 244 km | 437.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 100 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 63 | 52m | 556 km | 603.9 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 57 | 1h 53m | 1,304 km | 1,282.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 55 | 12m | 15 km | 14.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6269Q |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-04-17 20:02 UTC | 2026-04-17 20:47 UTC | 44m |
| N13358 |  | Pike County/Hatcher Field (KPBX) | Pike County/Hatcher Field (KPBX) | 2026-04-17 20:35 UTC | 2026-04-17 20:46 UTC | 10m |
| N363DA |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-04-17 20:41 UTC | 2026-04-17 20:41 UTC | 0m |
| N2237A |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-17 19:58 UTC | 2026-04-17 20:31 UTC | 33m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-17 20:06 UTC | 2026-04-17 20:26 UTC | 19m |
| PSJIM | PSJ | Sonhar Airport (SJSH) | Hercilio Luz International Airport (SBFL) | 2026-04-17 20:19 UTC | 2026-04-17 20:21 UTC | 2m |
| EJA129 | EJA | Philadelphia International Airport (KPHL) | Washington Dulles International Airport (KIAD) | 2026-04-17 19:44 UTC | 2026-04-17 20:18 UTC | 34m |
| N9454F |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-17 20:12 UTC | 2026-04-17 20:17 UTC | 4m |
| UAE9788 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-17 13:52 UTC | 2026-04-17 20:15 UTC | 6h 22m |
| N448AF |  | Yuba County Airport (KMYV) | Yuba County Airport (KMYV) | 2026-04-17 20:10 UTC | 2026-04-17 20:12 UTC | 1m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-17 19:56 UTC | 2026-04-17 20:12 UTC | 16m |
| SHWK422 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-04-17 18:31 UTC | 2026-04-17 20:12 UTC | 1h 41m |
| N752DW |  | Dayton Valley Airpark (KA34) | Silver Springs Airport (KSPZ) | 2026-04-17 19:57 UTC | 2026-04-17 20:11 UTC | 13m |
| RDHK705 | RDH | Aberdeen Field (31VA) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-17 20:00 UTC | 2026-04-17 20:10 UTC | 10m |
| CRN111 | CRN | Vancouver International Airport (CYVR) | Alert Bay Airport (CYAL) | 2026-04-17 19:27 UTC | 2026-04-17 20:10 UTC | 43m |
| N261AT |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-17 19:10 UTC | 2026-04-17 20:10 UTC | 59m |
| N403RW |  | Big Spring/Mc Mahon-Wrinkle Airport (KBPG) | Upton County Airport (KE48) | 2026-04-17 19:52 UTC | 2026-04-17 20:06 UTC | 14m |
| N46168 |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-17 19:39 UTC | 2026-04-17 20:06 UTC | 26m |
| N707SC |  | Midland International Air And Space Port Airport (KMAF) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-04-17 18:19 UTC | 2026-04-17 20:05 UTC | 1h 45m |
| N884BC |  | Naper Aero Club Airport (LL10) | Naper Aero Club Airport (LL10) | 2026-04-17 19:44 UTC | 2026-04-17 20:04 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
